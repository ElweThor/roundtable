#!/usr/bin/env python3
# translate_md.py
# Script minimale per tradurre file Markdown da una cartella sorgente a una target
# Usa googletrans 4.0.0-rc1

import os
import sys
from googletrans import Translator

if len(sys.argv) != 3:
    print("Usage: python translate_md.py <source_dir> <target_dir>")
    sys.exit(1)

src_dir = sys.argv[1]
tgt_dir = sys.argv[2]

translator = Translator()

if not os.path.exists(tgt_dir):
    os.makedirs(tgt_dir)

for root, _, files in os.walk(src_dir):
    for f in files:
        if f.endswith(".md"):
            src_path = os.path.join(root, f)
            rel_path = os.path.relpath(src_path, src_dir)
            tgt_path = os.path.join(tgt_dir, rel_path)
            os.makedirs(os.path.dirname(tgt_path), exist_ok=True)
            
            with open(src_path, "r", encoding="utf-8") as infile:
                text = infile.read()
            
            try:
                translated = translator.translate(text, src='auto', dest=tgt_dir.split('/')[-1])
                with open(tgt_path, "w", encoding="utf-8") as outfile:
                    outfile.write(translated.text)
                print(f"Translated {src_path} → {tgt_path}")
            except Exception as e:
                print(f"Error translating {src_path}: {e}")
