# mcp/tests/test_citation_document_transaction.py

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Actual citation-fixer document transaction and conflict isolation.

## Code Commentary

### Logic

Mixed accepted and declined claims publish only accepted edits and history. Preview binds the same complete-batch digest later published; two cells on one line keep original offsets. Concurrent document changes refuse that whole document while another batch can publish; replace failure and stale explicit snapshots preserve original bytes.

The `Scenario` fixture now carries a `stamp` field and a static `git(root, *args)` helper that raises on a non-zero exit, and `Scenario.card` writes a metadata table carrying `| lastVerifiedCommitHash | \`{self.stamp}\` |` above the citation header. The `scenario` fixture writes the VERIFIED tree first — `src/gone.py`/`unique` and `src/missing.py`/`another` held the anchors — git-inits and commits it, records the stamp, and only then deletes both files, so the mixed-claim transaction test still exercises an accepted edit alongside a claim declined by the continuity rule rather than by a missing source.

The file also carries a second, independent transaction: **migration**, driven through the real `migrate_onboarding_root` entry point over the same continuity authority. Its `Migration` fixture is a code tree plus a superseded three-column card (`Finding | Citations | Source Path`), with `source`/`stamp`/`card`/`migrate`/`row` helpers and a `build_migration` constructor. Three cases pin the reachable behaviour: a live cited file that no longer holds the anchor declines the row as `anchor_left_live_file` and the pointer is **not** moved; a gone cited file is refused far earlier as `source_unresolvable` (parametrized over a stamped and an unstamped card, i.e. both origin shapes) with the row's own evidence retained; and a deliberately-labelled **seam test** monkeypatches `migration.row_paths` to carry an unresolvable spelling through, reaching the two branches production cannot currently reach — an unproven origin declines as `anchor_continuity_unproven`, and a stamped kind-preserving relocation converts. That seam test's docstring states in its own words that production cannot reach those branches and that its value is **regression protection only**, so a green run must not be read as end-to-end coverage of a relocated file.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance. The migration seam test declares its own limitation at the point of use; keep that declaration when the test is edited.

### Invariants And Boundaries

CRLF and append-only history remain intact. Observed interleavings establish the fixer contract without claiming an operating-system compare-and-swap primitive. A declined claim in the mixed batch is declined under the continuity rule: the card names a stamp whose tree still held the anchor, while the current tree no longer does. The fixtures build provenance through Git, so no test asserts a semantic-similarity approval the fixer must not invent. **A green migration section is not end-to-end relocation coverage:** the only relocation refusal production reaches is `anchor_left_live_file`, because `row_paths`/`plan_row` refuse a gone source as `source_unresolvable` before placement; the continuity branches are pinned through a declared seam, not through the entry point.

### Todos

No file-local implementation change is requested by this reconciliation.

## Evidence

### Docs References

No Domain Documentation entries are configured in this memory root. These are repository-owned fixture and assertion contracts; no external library behavior is inferred.

No configured domain evidence applies to the file-local claims above.

### Repo-Internal References

The retained source anchors below support the fixture roles and assertion boundaries described above. They identify current behavior, not a request to restore historical test counts or percentage targets.

- Scenario fixture: code/onboarding roots, the recorded stamp. [1]
- One Git command per root, failing loudly on a non-zero exit. [2]
- A card writes its metadata stamp above the citation header. [3]
- The verified tree is committed and stamped before both cited files are deleted. [4]
- Mixed claims publish only the accepted edit and history. [5]
- Preview digest matches later publication and binds the complete batch. [6]
- Two prose source cells on one line keep their original offsets. [7]
- Observed conflict refuses the whole document and preserves other batches. [8]
- Atomic replace failure keeps the original document. [9]
- Crlf document bytes and history line endings survive. [10]
- Stale explicit snapshot refuses the actual scoped fixer. [11]
- The migration fixture: a code tree plus the superseded three-column card the transaction rewrites. [12]
- A live cited file that lost the anchor declines the row as `anchor_left_live_file` and the pointer is not moved. [13]
- A gone cited file is refused earlier as `source_unresolvable`, both stamped and unstamped, with the row's evidence retained. [14]
- A declared seam reaching the two production-unreachable continuity branches: unproven origin declines, stamped kind-preserving relocation converts. [15]

### Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

Fixture repositories and protocol doubles do not establish a live external integration.
