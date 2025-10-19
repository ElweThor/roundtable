#!/usr/bin/env python3
"""
translate_md_auto.py (KISS edition, no cache)

Usage:
  # Translate a single modified file (example used by the Action)
  python scripts/translate_md_auto.py docs/en/PRINCIPLES.md

  # Or translate everything (scan docs/)
  python scripts/translate_md_auto.py

Behaviour:
- Detects language from path: docs/<lang>/...
- Finds all language subdirs in ./docs/ (two-letter folders)
- For each target language != source, writes translated file preserving relative path
- Uses googletrans (4.0.0-rc1). Replace translator logic if prefer another provider.
"""

import os
import sys
from googletrans import Translator

BASE_DOCS = "docs"

def get_lang_dirs(base_dir=BASE_DOCS):
    langs = []
    if not os.path.isdir(base_dir):
        return langs
    for entry in os.listdir(base_dir):
        full = os.path.join(base_dir, entry)
        # consider only two-letter alphabetic directory names (en, it, fr, ru, ...)
        if os.path.isdir(full) and entry.isalpha() and len(entry) == 2:
            langs.append(entry)
    return sorted(langs)

def detect_src_lang_from_path(path):
    # expects paths like docs/en/whatever.md
    p = os.path.normpath(path).split(os.sep)
    if len(p) >= 2 and p[0] == BASE_DOCS and len(p[1]) == 2 and p[1].isalpha():
        return p[1]
    return None

def translate_file(src_path, src_lang, target_langs, base_dir=BASE_DOCS, translator=None):
    rel_path = os.path.relpath(src_path, os.path.join(base_dir, src_lang))
    with open(src_path, "r", encoding="utf-8") as f:
        text = f.read()

    for tgt in target_langs:
        tgt_dir = os.path.join(base_dir, tgt, os.path.dirname(rel_path))
        os.makedirs(tgt_dir, exist_ok=True)
        tgt_path = os.path.join(base_dir, tgt, rel_path)
        try:
            translated = translator.translate(text, src='auto', dest=tgt).text
            with open(tgt_path, "w", encoding="utf-8") as out:
                out.write(translated)
            print(f"Translated {src_path} → {tgt_path}")
        except Exception as e:
            print(f"ERROR translating {src_path} -> {tgt}: {e}")

def translate_all_in_dir(base_dir=BASE_DOCS):
    langs = get_lang_dirs(base_dir)
    if not langs:
        print(f"No language directories found in '{base_dir}'. Nothing to do.")
        return

    translator = Translator()
    for src_lang in langs:
        src_dir = os.path.join(base_dir, src_lang)
        target_langs = [l for l in langs if l != src_lang]
        for root, _, files in os.walk(src_dir):
            for fname in files:
                if not fname.lower().endswith(".md"):
                    continue
                src_path = os.path.join(root, fname)
                translate_file(src_path, src_lang, target_langs, base_dir, translator)

def translate_single_file(path):
    path = os.path.normpath(path)
    src_lang = detect_src_lang_from_path(path)
    langs = get_lang_dirs()
    if src_lang is None:
        print(f"Cannot detect source language from path '{path}'. Expected 'docs/<lang>/...'. Aborting.")
        return
    if src_lang not in langs:
        print(f"Source language '{src_lang}' not found among detected langs {langs}. Still proceeding (targets = detected langs \\ {{src}}).")
    target_langs = [l for l in langs if l != src_lang]
    if not target_langs:
        print("No target languages detected. Nothing to do.")
        return
    translator = Translator()
    translate_file(path, src_lang, target_langs, BASE_DOCS, translator)

if __name__ == "__main__":
    if len(sys.argv) == 1:
        # no args -> translate everything
        translate_all_in_dir(BASE_DOCS)
    else:
        # can accept 1..N args; translate each specified file (typical usage: single file)
        for arg in sys.argv[1:]:
            if os.path.isdir(arg):
                print(f"Arg is a directory; translating all in '{arg}'")
                translate_all_in_dir(arg)
            elif os.path.isfile(arg):
                translate_single_file(arg)
            else:
                print(f"Warning: path '{arg}' not found or not a file/dir; skipping.")
