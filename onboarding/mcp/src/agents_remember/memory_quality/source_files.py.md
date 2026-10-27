# mcp/src/agents_remember/memory_quality/source_files.py

## Governing Overview

[Memory-quality overview](overview.md)

## Purpose

Supply the source view for one synchronous memory-quality check. Git lists tracked and non-ignored untracked files; a citation can still read a file outside that listing.

## Code Commentary

`QualitySourceFiles` retains only cited file bodies for the lifetime of the check. Its report inspects uncited bodies one at a time and reports the listed, indexed and skipped counts. No file-count limit refuses the check.

Reads are bounded at 4 MiB and reject symbolic links in every path component, paths outside the repository and nonregular files. The descriptor walk also prevents following a link substituted after the preliminary path check. A file that cannot be read yields a precise unavailable reason; an absent file remains distinct.

Readable ignored and binary citations retain content verification. Their reasons appear as separate source notes. Onboarding `pathRules` do not enter this reader: an excluded readable file is checked without a policy remark. The Git listing excludes ignored paths, while the citation reader can read them; these are separate responsibilities.

There is no persistent source index. Per-check path, cited-content and reason state expires with the reader.

## Evidence

- The read bound is 4 MiB. [1]
- The reader's Git file set and bounded cited-byte cache are local to one instance. [2]
- The report names skipped files without retaining uncited bodies. [3]
- Readable ignored and binary files retain their bytes with separate notes. [4]
- Path validation rejects links before Git classification, and descriptor opens refuse following links. [5]
- Git classification failures become named unavailability. [6]
