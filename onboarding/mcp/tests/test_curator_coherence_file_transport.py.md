# mcp/tests/test_curator_coherence_file_transport.py

## Governing Overview

[Owning route overview](overview.md)

## Purpose

Guards the candidate-file/status transport and file-sourced publication while preserving exact publication checks.

## Code Commentary

Prepare cases require the written candidate set, counts, digest and locations rather than inline candidate/identity material. File and inline publication produce equivalent authority; changed preparation inputs refuse publication. The maximum-count test validates both collection maxima directly and compares the short-ASCII fixture's serialization size with the file-byte cap. It does not acquire that fixture through the file reader or stimulate supplementary-character expansion. Separate resource/type cases retain their own tested scopes; collection-count validation is not an all-legal-width acquisition proof. Supplying either list both inline and by file, even explicitly empty, refuses. Status/validate retain state and counts. Evidence is against hermetic fixture authorities, not this leaf’s production acceptance.

## Evidence

No Domain Documentation sources are configured; the evidence below is repository implementation or test assertions, not a new execution attestation.

- Prepare writes the complete set and bounded answer. [1]
- File and inline publication authority equivalence is asserted. [2]
- Maximum collection counts pass direct entry validation; the short-ASCII fixture serialization is below the file-byte cap, without exercising acquisition or supplementary width. [3]
- An explicit empty inline collection is still duplicate sourcing. [4]
