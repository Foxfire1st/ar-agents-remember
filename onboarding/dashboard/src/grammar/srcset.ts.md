# dashboard/src/grammar/srcset.ts

## Governing Overview

[overview](overview.md)

## Purpose

Parses HTML source-set candidates before document media admission.

## Code Commentary

URL collection preserves embedded commas and distinguishes trailing separator commas. Descriptor collection tracks descriptor, parentheses and after-descriptor states. Invalid or conflicting width, density or future-height descriptors discard their candidate. Parsing resumes after its delimiter; an unclosed parentheses state consumes the remaining input.

## Relationships

DocumentMarkdown applies its media policy to each returned candidate. This parser makes no fetch or address-admission decision.

## Evidence

- Parses HTML source-set candidates before document media admission. [1]
