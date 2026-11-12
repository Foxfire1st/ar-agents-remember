# mcp/src/agents_remember/application/review_supplemental_evidence.py

## Governing Overview

[overview.md](overview.md)

## Purpose

Byte receipts for evidence admitted from outside the four comparison trees: resolves one source through the task that owns it, binds the exact bytes examined, and refuses a source that escapes the task's admitted roots.

## Code Commentary

`admit_supplemental` confines the path to the task’s `requirements/` and `notes/` roots, plus the leaf’s exact own JSON and Markdown task-document names, and refuses a symlinked component; the read is a real `stream.read(limit + 1)` admission, so an over-cap source refuses with its measured sentinel byte count and no digest rather than being stat-ed and then read whole. `capture_supplemental` records the canonical source, producer/authority where recorded, digest, read state and capture identity, and says the receipt is supplemental.
`reread_supplemental` answers a successor receipt with the new bytes or an unavailable result; the earlier receipt keeps its digest, so a changed or lost document is never carried under the old identity.

The task root is never admitted wholesale and `DEVELOPER-DIRECTION.md` stays excluded. A root-level document reread checks its recorded producer leaf before re-admitting the stem. `packet_version_stale` also checks the requirements manifest: an old packet’s unchanged bytes do not hide that the registered version moved on.

## Evidence

- A supplemental source is resolved inside the task's own admitted roots. 
- A capture binds the bytes examined and states that it is supplemental. [2]
- A later read answers a successor receipt and never rewrites the earlier one. [3]

- The current implementation adds leaf-bound document reread and manifest-version staleness; the earlier successor-receipt identity account remains valid. [4]

- Retired at the fifth freeze d59c3493: mcp/src/agents_remember/application/review_supplemental_evidence.py::admit_supplemental - the bytes it recorded now occur 4 times in the file, so no single home can be named and it is not given to the likelier one. Retired means the anchor no longer stands, not that the cited subject was deleted.
