# mcp/src/agents_remember/kernel/memory_ledger.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/kernel/memory_ledger.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-15T01:02 |
| lastVerifiedCommitHash | `67b21aeb66df96a971a33ae431a13992f2528b45` |
| lastVerifiedCommitDate | 2026-09-15T06:37:48+02:00|
| governingOverview | `../../../overview.md` |

## Governing Overview

[Nearest governing overview](../../../overview.md)

Working candidate verification: source inspected at 2026-09-15T01:02 UTC against the uncommitted L9 candidate.
The commit fields identify the latest real commit touching this source; they do not identify a future commit for the working changes.

## Purpose

Defines the consumer memory-ledger representation: schema and row types, structural parsing,
validation, canonical serialization, and current-versus-historical row lookup. It does not derive
Git authority from those serialized rows.

## Code Commentary

### Logic

The format is a fenced JSON metadata block followed by a two-column `Code commit` / `Memory commit`
table. `parse_ledger_text_unvalidated` checks structure, schema, repository name, and sort-order
metadata without enforcing current-header agreement. Nonempty tables still require all revision
metadata. `parse_ledger_text` additionally calls `validate_ledger`.

An empty derived ledger is valid. It has no mapping rows and may leave revision metadata empty;
validation refuses an empty ledger that nevertheless claims a current code or memory mapping.
For nonempty rows, the first pair must agree with the current header and ordering remains
`newest-first`.

`prepend_mapping` returns a representation with the new pair and updated current header.
`find_mapping` selects the first matching code row; `contains_mapping` asks whether an exact pair
occurs anywhere in the data. Repeated code commits can therefore represent ordered memory states
without collapsing their history.

`write_ledger` serializes only the explicitly supplied representation. It creates no commit and
performs no staging or ref move. Runtime refresh uses `memory_cache.refresh_memory_cache` to derive
and materialize current data. `LEDGER_RELATIVE_PATH` owns the filename; `MEMORY_CACHE_EXCLUDE` is the
exact root-cache exclusion consumed by Git staging/status helpers, including ignored or unreadable
legacy cache files. The former projection-module reexport is no longer a reader contract.

### Conventions

The parser uses a narrow standard-library grammar. Representation helpers and lookup ordering are
data semantics; callers must not treat a successful parse or matching row as permission for Git
work. Runtime derivation and best-effort cache writing have their separate kernel owner.

### Invariants And Boundaries

- Empty data must not claim a current mapping; nonempty data must retain its required metadata.
- The current header matches the first row when validated.
- Current lookup and historical containment are distinct and do not impose global code-key uniqueness.
- Writing a representation does not stage or commit it.
- A cached table is disposable; only committed attribution supplies runtime mappings.

### Todos

No new implementation or live-state operation is authorized by this documentation pass.

## Docs References

No Domain Documentation source is configured for this repository. No external domain documents
were available through the configured registry to consult; the current claims are grounded in the
working source and package-local evidence below. The registry is discovery input, not a citation.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured external domain-documentation evidence. | — | — |

## Repo-Internal References

These repository-relative targets and exact ranges were checked against the L9 working source.
Source declarations and test assertions are distinguished from execution and acceptance evidence.

| Finding | Citations | Source Path |
| --- | --- | --- |
| Format constants, row types, and the exact cache-exclusion expression. | L24-L24; L27-L27; L30-L33; L36-L45 | [mcp/src/agents_remember/kernel/memory_ledger.py](mcp/src/agents_remember/kernel/memory_ledger.py) |
| Structural parsing and validation distinguish empty and nonempty representations. | L68-L132; L149-L158; L173-L184 | [mcp/src/agents_remember/kernel/memory_ledger.py](mcp/src/agents_remember/kernel/memory_ledger.py) |
| Serialization and data lookup stay independent from Git publication. | L187-L212; L229-L236; L239-L250; L253-L255; L258-L266 | [mcp/src/agents_remember/kernel/memory_ledger.py](mcp/src/agents_remember/kernel/memory_ledger.py) |
| The runtime cache owner derives data rather than trusting a serialized table. | L22-L41; L65-L91 | [mcp/src/agents_remember/kernel/memory_cache.py](mcp/src/agents_remember/kernel/memory_cache.py) |

## Cross-Repo References

The code/memory or fixture-repository boundaries above are established by package-local source.
No additional configured external or sibling-repository evidence is claimed.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No additional configured cross-repository evidence. | — | — |

## Update History

- 2026-09-15 — Preserved the following dated pre-takeover review notes from the parent working tree. They describe that earlier candidate; current behavior is documented above. Exact original files and patches are retained in the master cutover report.

- 2026-09-14T23:55+02:00 — 260913-LCA completed-master review follow-up (same uncommitted change
  set, `ar/260913_ledger-commit-attribution`, base `bb65a207`): anchor repoint only, no claim change.
  The ledger projection grew above its import block, so this card's citation of the re-export site
  moved: `worktrees/ledger_projection.LEDGER_RELATIVE_PATH` 44-63 → 47-66. The range was read back at
  its current position and still covers the `kernel/memory_ledger` import and the re-export comment.
  Verification metadata remains closeout-owned; no acceptance claim and no verification stamp
  advanced.

- 2026-09-15T01:02 UTC — Replaced the immediate-ledger-commit durability rule with consumer serialization semantics; documented valid empty derived ledgers, retained nonempty validation, and the shared root-cache exclusion constant. Earlier R12 entries describe the former committed-table design. Working candidate verified by source inspection; commit metadata records real committed history only.


- 2026-09-14T19:00+02:00 — 260913-LCA-L12 curator (residue citation pass): re-derived the source
  range of 2 claim(s) whose anchor no longer sat in its cited range and normalised 3 further
  range(s) from their anchors against the frozen source snapshot (`agents-remember memory-citations
  --fix --document`). 1 further claim(s) were declined because the solution they name no longer
  exists in the code tree, so their wording needs a reading curator; they are recorded in the pass
  report. No claim wording was changed to fit an anchor; every rewritten range was read back at its
  current position. Verification metadata remains closeout-owned.
- 2026-09-14T17:20+02:00 — 260913-LCA-L3 (uncommitted change set on `ar/260913-lca-l3-ar`, base
  `7317108b`): `LEDGER_RELATIVE_PATH = "memory.md"` is now declared here, beside the schema, the row
  type and the parser, instead of in `worktrees/ledger_projection.py`. The reason is recorded in
  `Purpose`, `Logic` and a new invariant: the path is a property of the ledger format, and a
  kernel-level migration that reads the same table (`kernel/memory_backfill.ledger_rows_at`) must not
  import a feature package to learn a filename. The projection imports and re-exports it, so every
  caller that already names it from `worktrees.ledger_projection` is unchanged. Every citation in this
  card was re-derived against the grown file — `write_ledger` 216-238 → 222-244 (the ruling paragraph
  it anchors is unchanged), `parse_ledger_text` 52-104 → `parse_ledger_text`/`parse_ledger_text_unvalidated`/`validate_ledger`
  at 58-63 / 66-125 / 168-177, `validate_ledger` 162-171 → 168-177, `ledger_to_text` 174-199 →
  180-205, `prepend_mapping` 241-252 → 247-258, `find_mapping` 255-257 → 261-263, `contains_mapping`
  260-268 → 266-274, the module-shape row 17-41 → 17-47, and
  `require_integrated_ledger_mapping` 229-282 → 274-359. Verification metadata remains
  closeout-owned; no acceptance claim and no verification stamp advanced.
- 2026-09-11T23:05:00+00:00: Curator citation reconciliation: `ledger_to_text`, `prepend_mapping`, `validate_ledger` repointed to mcp/src/agents_remember/kernel/memory_ledger.py:162-171, mcp/src/agents_remember/kernel/memory_ledger.py:174-199, mcp/src/agents_remember/kernel/memory_ledger.py:241-252. No content impact: mechanical anchor-range projection against citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged.
- 2026-09-11T22:39:01+00:00: Generated citation repair: `find_mapping`; `contains_mapping` repointed to mcp/src/agents_remember/kernel/memory_ledger.py:255-257; mcp/src/agents_remember/kernel/memory_ledger.py:260-268. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-11T22:39:01+00:00: Generated citation repair: "def write_ledger(path: Path" repointed to mcp/src/agents_remember/kernel/memory_ledger.py:216-216. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-11T22:39:01+00:00: Generated citation repair: `write_ledger` repointed to mcp/src/agents_remember/kernel/memory_ledger.py:216-238. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-11T22:39:01+00:00: Generated citation repair: `write_ledger` repointed to mcp/src/agents_remember/kernel/memory_ledger.py:216-238. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-10T07:41:10+00:00: Generated citation repair: "existing_mapping = find_mapping(ledger" repointed to mcp/src/agents_remember/worktrees/modules/closeout_external.py:64-64. No content impact: mechanical anchor-range projection bound to citation source snapshot 794cfaf55738c596793ad49b95a946add84e2c03f1bf6499e2f00c6b84bd85ba; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-08-26T14:32+02:00 — Corrected the ledger contract after the IAS activation regression:
  repeated code commits are valid newest-first memory-state history; `find_mapping` owns current
  authority and `contains_mapping` owns exact historical-edge proof. Removed the unrequested
  global uniqueness rule. Verification remains closeout-owned.
- 2026-08-22T10:39+02:00 — 260821-CLIVE-L1 candidate-11 curation rebind: refreshed formatter-moved source coordinates against accepted tree `4241908c`; where applicable, replaced a deleted coordinator anchor with the sole current owner. Verification metadata remains pinned until governed closeout.
- 2026-08-17T12:30+02:00 — 260815-DAG-L5: added `find_unique_mapping` for one-to-one code mapping with duplicate-authority refusal. Verification remains closeout-owned.

- 2026-08-12T15:19+02:00 — L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges; verification provenance remains closeout-owned.

- 2026-08-08T17:18+02:00 — No content impact: 260731-EFA-L9 moved the ledger reader (`observer/snapshots.py` → `serving/projections/snapshots.py`); the documented behavior is unchanged and the reader-path citation was re-pointed. Body re-verified current. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-04T18:29+02:00 — 260731-EFA-L6 S18-B17 curator: repaired the four malformed rows and two
  superseded prose cites. `parse_ledger_text` bound to 52-104; closeout/integration rows bound to
  their import blocks plus the exact conditional/unconditional mapping-rewrite spans (`find_mapping`
  at closeout.py:698-710, `prepend_mapping` at integrate.py:253-258). The durable-store row: the
  verbatim deployment-fact paragraph the L5 entry cites is gone from the frozen 446-line file, but
  the module docstring (1-25) still carries both predicates — the unconditional per-log mutex +
  `flock` and the shared-local-POSIX-filesystem deployment requirement — so the claim stands,
  anchored on "ar-durable-store/1.0" at 1-25; not a Tier-3 remainder. Also extended
  `prepend_mapping`'s row range to its true end (218-231) and converted the two `(L…)` history
  prose cites to cit forms. No claim wording changed.

- 2026-08-01T20:15+02:00 — 260731-EFA-L5 curator (correction pass): **the `durable_store.py` row
  pointed at the wrong docstring.** It cited "contract front matter L1-L116; the deployment-fact
  paragraph L190-L198". Neither range holds. `durable_store.py` grew 598 → 699 lines mid-pass: the
  module docstring now runs **L1-L147**, so L1-L116 stops 31 lines short and cuts off the
  read-policy sections the row's claim depends on; and L190-L198 is not the deployment-fact
  paragraph at all — it lands on `SUPPORTED_SCHEMA_MAJOR`, `ProcessRole` and the error classes. The
  deployment-fact text ("only one process writes this file" is a deployment fact, not a structural
  one, and a store whose durability rests on one is precisely what this leaf was called in to
  repair) is at **L237-L243**, inside `StoreOwnership`'s class docstring, where it explains why that
  dataclass has no `serialized` field. Replaced both with symbol-name citations and no ranges, as
  this leaf's test cards do, because a number that was wrong within the hour is worse than no
  number. The row's claim is unchanged and was re-read at the new location. The four citations into
  this module's own source were re-read and are correct: L17-L41 (`LEDGER_SCHEMA` L17, `LedgerRow`
  L23, "def parse_ledger_text(text: str) -> MemoryLedger:" L29, "class LedgerError(AgentsRememberError):" L40), "def parse_ledger_text(text: str) -> MemoryLedger:" L51-L104 cit:(["def parse_ledger_text(text: str) -> MemoryLedger:"], mcp/src/agents_remember/kernel/memory_ledger.py:58-58),
  `validate_ledger` L147 / `ledger_to_text` L159 / `prepend_mapping` L218, and `write_ledger`
  L193-L215 cit:(["def write_ledger(path: Path"], mcp/src/agents_remember/kernel/memory_ledger.py:222-222). Nothing on this card asserts a measured figure.

- 2026-08-01T13:20+02:00 — 260731-EFA-L5 curator: the only source change here is a 20-line docstring
  on `write_ledger`, and it is a **ruling**, not a description — so the card now records the ruling,
  the evidence for it, and what would overturn it. Verified all six call sites myself rather than
  taking the docstring's word: `closeout.py` L539, `integrate.py` L254-L257, `start.py` L1128,
  `carryover.py` L759-L762 and L849, `baseline.py` L153 — each followed by
  `require_git(..., ["add", "memory.md"])` and `commit_if_dirty(...)` in the next two statements, so
  the durable authority is the git object and a truncated `memory.md` costs the uncommitted delta.
  Confirmed no writer under `observer/` or `serving/`; `serving/projections/snapshots.py` L42 imports
  `LedgerError`, `LedgerRow` and `load_ledger` and never `write_ledger`. Added the caller obligation
  as an invariant, because it is the property the whole exemption rests on.
  **Two docstring imprecisions carried into the card as the accurate version, and reported.**
  (1) It says snapshots.py "imports `load_ledger` and nothing else" — it imports three names; the
  load-bearing half (no writer) is true. (2) It says all five callers "are reached only through MCP
  tool registrations" — `worktrees/modules/cli.py` registers `start`/`closeout`/`integrate`
  subcommands and `worktrees/git_worktree_manager.py` L194-L195 (`if __name__ == "__main__": raise
  SystemExit(main())`) makes them runnable as a script. That is a short-lived process on the same
  commit-immediately path, so the ruling stands; the premise is "no concurrent daemon writes this",
  not "only the MCP process ever writes this".
  **Citations repaired.** The docstring inserts 20 lines at L194, so `prepend_mapping` moved:
  `L142-L179; L193-L204` → `validate_ledger` **L147-L156**, `ledger_to_text` **L159-L184**,
  `prepend_mapping` **L218-L229**. Note the old range was already defective in the shape the L4
  audit found — `L142-L179` began at `_is_separator_row` and stopped 5 lines short of the end of
  `ledger_to_text` cit:([`ledger_to_text`], mcp/src/agents_remember/kernel/memory_ledger.py:180-205), and `L193-L204` began at `def write_ledger` and stopped 5 lines short of
  the end of `prepend_mapping`; both symbols the claim names are now fully inside their ranges.
  Added a row for `write_ledger` itself and one for the contract it was measured against.
  Verification metadata pinned until closeout stamps the L5 code commit.

- 2026-07-31T17:20+02:00 — 260731-EFA-L2 curator: repaired the cross-repo citation that broke when
  the worktree manager was split into `worktrees/modules/`. `git_worktree_manager.py` is now a
  195-line pure re-export facade with no ledger call in it at all, so the old `L18-L24; L923-L929;
  L1071-L1078` pointed past the end of the file. Split the row in two and repointed to the real
  call sites, both read back: `modules/closeout.py` L9-L14 (import) + L523-L534 (direct-closeout
  mapping update, which now skips the rewrite when `find_mapping` already matches) and
  `modules/integrate.py` L10-L15 (import) + L251-L257 (integration mapping prepend). Claim text
  rewritten to name the two modules and the conditional-vs-unconditional difference.

- 2026-07-31T16:35+02:00 — No content impact: the only change to
  `mcp/src/agents_remember/kernel/memory_ledger.py` since the L2 base commit is the whole-tree
  `ruff format` pass in `00e8379`, which re-wrapped 1 line(s) with no token change whatsoever.
  Checked by parsing both revisions and comparing the abstract syntax trees (identical) and the
  comment tokens (identical), so no symbol, signature, default, decorator, control-flow branch,
  docstring, or assertion this card describes has moved, and every claim this card makes about its
  own source still holds.

- 2026-07-31T00:00+02:00 — 260731-EFA-L2 attestation: this file was touched ONLY by the
  whole-tree `ruff format` pass (commit `00e8379`) — line reflow, no behaviour, contract,
  structure or responsibility change. The sidecar was re-read against the current source and
  every claim in it still holds, so it was deliberately not rewritten. Verification metadata
  pinned until closeout stamps the L2 commit.

- 2026-05-31T12:30+02:00 — Removed `find_ledger_anchor_commit()` (and its `subprocess` use) from Logic and references; `LedgerError` now subclasses `AgentsRememberError` (1.0.0 review remediation).

- 2026-05-29T18:35+02:00: Extracted `_ledger_rows_from` (inner row loop) from `parse_ledger_rows` to reduce complexity; behavior-preserving (commit `e3dab63`).

- 2026-05-23T22:37+02:00: Created during quality-pass closeout after direct-closeout preview found the changed file lacked sidecar onboarding.
