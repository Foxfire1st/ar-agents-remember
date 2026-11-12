# mcp/tests/test_memory_quality_source_files.py

## Governing Overview

[Tests overview](overview.md)

## Purpose

Exercise source-file behavior through the public synchronous memory-quality controller using isolated code and converted-memory fixture repositories.

## Code Commentary

The uncited fixture family covers ignored build output, a large tracked binary, a file link, explicit skipped-file reasons, both `pathRules` exclusion directories and a population above 100,000 files. These shapes must not cause a whole-run size or count failure.

The cited family distinguishes readable ignored, binary and excluded files from unreadable large files and links. Readable fixtures are checked both before and after content mutation. Ignored and binary sources retain a separate reason; excluded sources have no remark. Directory links and embedded Git links have named unavailable observations instead of aborting the synchronous call.

The fixture constructs real Git repositories and calls the controller. Its scenario grouping preserves each assertion while sharing the collected test-case budget; it is not whole-repository or performance certification.

## Evidence

- Fixture checks call the public controller in sync mode. [1]
- The uncited family preserves reported shapes, listing reasons and the large file population. [2]
- Readable content changes produce a stale-content observation while retaining source-note policy. [3]
