# mcp/src/agents_remember/memory_quality/legacy_cards.py

## Governing Overview

[Memory-quality overview](overview.md)

## Purpose

Detect old-format onboarding cards for the first attributed baseline of a converted memory tree. This detector belongs to baseline status/adoption, not the ordinary knowledge validator.

## Code Commentary

A table row counts only when its first cell, with whitespace and backticks stripped, is one of the three metadata stamp keys. A prose mention in another cell does not count. The other sign is the level-two Update History heading. Fenced text is read as authored, so quoting old card structure still carries it into a fresh baseline.

Enumeration returns sorted memory-relative Markdown paths under onboarding, including cards inside dot directories. It applies the shared generated-cache predicate to root-relative paths. Missing onboarding yields an empty list. The scanner skips reads that raise `OSError`. Invalid UTF-8 raises `UnicodeDecodeError` through the direct baseline call. The baseline owner gives existing attributed adoption precedence and refuses listed old-format cards before first adoption regardless of drift acceptance.

## Evidence

- Legacy signs are metadata-key first cells or the Update History heading; later-cell prose mentions do not count. [1]
- Discovery scans sorted onboarding Markdown, including dot-directory cards. It skips I/O read errors. Invalid UTF-8 raises a decoding error. [2]


- First adoption refuses the listed cards without allowing accept_drift to lift that refusal. [3]
