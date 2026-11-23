# mcp/tests/test_canvas_capsule_text.py

## Governing Overview

[governing route overview](overview.md)

## Purpose

The capability text's packaging: it is read from the installed package-data copy, its budget and wording are enforced at the read, and the installed copy is the generated copy of the canonical source.

## Code Commentary

- The installed copy is generated from the canonical source, so a hand-edited copy fails.
- The launch record names whether the baseline, an addition or a replacement was used.


The wording guard binds the side conversation to the environment. The installed instructions contain the `Message file:` cue for architect handovers. The assertions read the shipped instructions and establish the wording.

The package test pins the six authoring filenames, the self-contained explanation, the essay-first treatment and the planned variant. It counts 1,500 words in the shipped text. A separate test refuses 1,501 words.

## Evidence

- The case `test_the_installed_copy_is_the_generated_copy_of_the_canonical_source` protects this behaviour. [1]

- The launch record distinguishes the baseline, addition and replacement and records the 1,500-word cap. [2]
- The architect handover instruction requires the Message file cue. [3]
- The installed text contains the stage names and prescribed explanation wording and counts exactly 1,500 words. [4]
- The read refuses 1,501 words and checks missing and invalid wording cases. [5]
