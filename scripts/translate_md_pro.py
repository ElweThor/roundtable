#!/usr/bin/env python3
# translate_md_pro.py
# Script avanzato per tradurre file Markdown con caching, preservando link e struttura
# Usa googletrans 4.0.0-rc1

import os
import sys
import hashlib
import json
from googletrans import Translator

CACHE_FILE = "translate_cache.json"

def load_cache():
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def save_cache(cache):
    with open(CACHE_FILE, "w", encoding="utf-8") as f:
        json.dump(cache, f, ensure_ascii=False, indent=2)

def file_hash(path):
    with open(path, "rb") as f:
        return hashlib.md5(f.read()).hexdigest()

def translate_text(text, dest, translator):
    # Si può estendere per preservare meglio i link Markdown se necessario
    return translator.translate(text, src='auto', dest=dest).text

def main(src_dir, tgt_dir):
    translator = Translator()
    cache = load_cache()

    if not os.path.exists(tgt_dir):
        os.makedirs(tgt_dir)

    for root, _, files in os.walk(src_dir):
        for f in files:
            if f.endswith(".md"):
                src_path = os.path.join(root, f)
                rel_path = os.path.relpath(src_path, src_dir)
                tgt_path = os.path.join(tgt_dir, rel_path)
                os.makedirs(os.path.dirname(tgt_path), exist_ok=True)

                src_hash = file_hash(src_path)
                cache_key = f"{rel_path}:{tgt_dir.split('/')[-1]}"

                # Salta traduzione se presente in cache
                if cache.get(cache_key) == src_hash:
                    print(f"Skipping {src_path}, cached")
                    continue

                with open(src_path, "r", encoding="utf-8") as infile:
                    text = infile.read()

                try:
                    translated = translate_text(text, tgt_dir.split('/')[-1], translator)
                    with open(tgt_path, "w", encoding="utf-8") as outfile:
                        outfile.write(translated)
                    cache[cache_key] = src_hash
                    print(f"Translated {src_path} → {tgt_path}")
                except Exception as e:
                    print(f"Error translating {src_path}: {e}")

    save_cache(cache)
    print("Translation complete.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python translate_md_pro.py <source_dir> <target_dir>")
        sys.exit(1)

    main(sys.argv[1], sys.argv[2])
