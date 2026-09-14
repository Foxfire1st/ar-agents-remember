# mcp/src/agents_remember/kernel/memory_ledger.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/kernel/memory_ledger.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-09-14T17:20+02:00 |
| lastVerifiedCommitHash | `270704b86116728a64ada83ee258a0e7726206b4` |
| lastVerifiedCommitDate | 2026-09-14T18:18:08+02:00|
| governingOverview      | `../../../overview.md`                     |

## Governing Overview

[mcp/overview.md](../../../overview.md)

## Purpose

`memory_ledger.py` parses, validates, writes, and updates the external-memory
`memory.md` ledger that maps code commits to memory-content commits. It also declares **where** that
ledger lives: `LEDGER_RELATIVE_PATH = "memory.md"`
cit:([`LEDGER_RELATIVE_PATH`], mcp/src/agents_remember/kernel/memory_ledger.py:25-25) sits beside the schema, the row type and the
parser because the path is a property of the ledger format rather than of any one reader.

## Code Commentary

### Logic

The module reads a fenced JSON metadata block plus the first `Code commit |
Memory commit` table, validates that the newest table row matches the metadata,
serializes the canonical ledger format, prepends new mappings, finds existing
mappings, and creates an initial ledger.

`find_mapping` returns the first—and therefore current—row for a code commit. `contains_mapping`
answers the different historical question: whether one exact code/memory edge exists anywhere in
the immutable row history.

`LEDGER_RELATIVE_PATH` is a declared constant and not a default buried in one reader, and the
placement is the point: a kernel-level migration that reads the same table must not import a feature
package to learn a filename. `worktrees/ledger_projection.py` imports it from here and re-exports it
cit:([`LEDGER_RELATIVE_PATH`], mcp/src/agents_remember/worktrees/ledger_projection.py:44-63), so the callers that already name
it from the projection keep working unchanged, while the kernel's own reader of the tracked table
(`kernel/memory_backfill.ledger_rows_at`) takes it as its `relative` default without importing
`worktrees` at all.

### 260731-EFA-L5 R12: `write_ledger` is a plain whole-file write, and that was decided, not missed

cit:([`write_ledger`], mcp/src/agents_remember/kernel/memory_ledger.py:216-238) is two statements — `mkdir(parents=True, exist_ok=True)`
then `path.write_text(...)`. It got no lock, no temp-and-rename and no `fsync` in the leaf that gave
all six control-plane JSONL stores exactly those things, and L5 records why in the function's own
docstring cit:([`write_ledger`], mcp/src/agents_remember/kernel/memory_ledger.py:216-238) rather than leaving the omission to be re-litigated. The ruling is **degraded,
not unrecoverable**, and it rests on two properties of the callers, both of which are checkable:

- **Every call commits within two statements.** Six call sites across five modules —
  `worktrees/modules/closeout.py` L539, `worktrees/modules/integrate.py` L254-L257,
  `worktrees/modules/start.py` L1128, `memory/carryover.py` L759-L762 **and** L849, and
  `memory/baseline.py` L153 — are each followed immediately by
  `require_git(<memory root>, ["add", "memory.md"])` and then `commit_if_dirty(...)`. So the durable
  authority for a mapping is the git object, not the working-tree file: a torn or truncated
  `memory.md` costs the uncommitted delta and nothing else, and `git checkout -- memory.md` restores
  it. (The docstring says "five callers … `carryover.py` (twice)", which is five modules and six
  calls; both readings are in the text, and the count that matters is that all six commit.)
- **No second long-lived process writes it.** `write_ledger` does not appear anywhere under
  `observer/` or `serving/`. The dashboard reads the ledger — `observer/snapshots.py` L42 imports
  `LedgerError`, `LedgerRow` and `load_ledger` from this module, and no writer — so there is nothing
  to serialize against and a lock here would guard nothing. (The docstring's parenthetical says
  snapshots.py "imports `load_ledger` and nothing else"; it imports three names. The claim that
  matters — that none of them writes — holds.)

**One caller-reach claim in the docstring is not exact, and the card records the accurate version.**
It says all five are "reached only through MCP tool registrations". Three of them are also reachable
from a script: `worktrees/modules/cli.py` registers `start`, `closeout` and `integrate` subcommands
(`build_parser`, `main`), and `worktrees/git_worktree_manager.py` L194-L195 is
`if __name__ == "__main__": raise SystemExit(main())`. That is a short-lived process, it commits on
the same two-statement path, and it changes nothing about the ruling — but it does mean the second
bullet's premise is "no concurrent *daemon* writes this", not "only the MCP process ever writes
this".

**What would falsify the ruling**, stated so a later reader can check it rather than trust it: a
`write_ledger` caller that does not `git add` + commit in the same function, or one reached from a
process that runs concurrently with another writer (a serving route, a projection tick, a
supervisor sweep). Either one makes a truncated ledger lose history rather than a delta, and the
ledger then belongs on the `ar-durable-store/1.0` contract in `controlplane/durable_store.py` like
the six JSONL logs.

### Conventions

The parser deliberately uses the standard library and a small markdown/table
grammar rather than pulling in a general markdown or YAML dependency. The ledger's path is exported
as one module constant rather than passed around as a literal, so a reader, a writer and a migration
agree on `memory.md` by construction.

### Invariants And Boundaries

- **The ledger's path is declared with the ledger's format.** `LEDGER_RELATIVE_PATH` lives here
  beside `LEDGER_SCHEMA` and `LedgerRow`; `worktrees/ledger_projection.py` re-exports it through its
  import so existing callers keep working, and no second declaration may appear.
- `sortOrder` must remain `newest-first`.
- The first table row must match `lastVerifiedCodeCommit` and
  `lastMemoryContentCommit`.
- `prepend_mapping()` requires both commits and updates metadata and rows
  together.
- Repeated code commits are valid. They record later external-memory states—such as settings-only
  changes—for unchanged code while preserving the older mapping as audit history.
- Row order carries authority: the newest matching row is current. Global code-key uniqueness must
  not be inferred by readers.
- Exact-edge checks use `contains_mapping`; current-state checks use `find_mapping`.
- **A `write_ledger` call must be followed by `git add memory.md` + commit in the same function.**
  That is not a style rule; it is the whole reason this file is allowed to do an unguarded
  whole-file write while the control-plane stores may not. A caller that writes and defers the
  commit converts "lose the uncommitted delta" into "lose the mapping history".

### Todos

- `parse_ledger_rows()` is a Phase 06 complexity hotspot candidate.

## Docs References

No external documentation is needed for this repository-local ledger format.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external documentation is needed for the local ledger parser. | n/a | n/a |

## Repo-Internal References

Same-repository source is the direct evidence for the external-memory ledger
format.

| Finding | Anchor | Source |
| --- | --- | --- |
| The module defines the canonical ledger schema, row and ledger dataclasses, and validation error type (a subclass of "class LedgerError(AgentsRememberError):"). | "class LedgerError(AgentsRememberError):" | mcp/src/agents_remember/kernel/memory_ledger.py:17-47 |
| The declared location of the ledger, moved here from `worktrees/ledger_projection.py` so a kernel-level reader of the same table needs no feature-package import. | `LEDGER_RELATIVE_PATH` | mcp/src/agents_remember/kernel/memory_ledger.py:25-25 |
| `parse_ledger_text()` requires the fenced JSON metadata block, required metadata fields, supported schema, and a valid mapping table; the unvalidated structural parse and the validator it delegates to are beside it. | `parse_ledger_text`; `parse_ledger_text_unvalidated`; `validate_ledger` | mcp/src/agents_remember/kernel/memory_ledger.py:58-63; mcp/src/agents_remember/kernel/memory_ledger.py:66-125; mcp/src/agents_remember/kernel/memory_ledger.py:168-177 |
| `validate_ledger()`, `ledger_to_text()`, and `prepend_mapping()` keep metadata and newest-first rows synchronized. | `validate_ledger`; `ledger_to_text`; `prepend_mapping` | mcp/src/agents_remember/kernel/memory_ledger.py:168-177; mcp/src/agents_remember/kernel/memory_ledger.py:180-205; mcp/src/agents_remember/kernel/memory_ledger.py:247-258 |
| `find_mapping()` resolves current newest-first authority, while `contains_mapping()` proves one exact historical edge without imposing global code-key uniqueness. | `find_mapping`; `contains_mapping` | mcp/src/agents_remember/kernel/memory_ledger.py:261-263; mcp/src/agents_remember/kernel/memory_ledger.py:266-274 |
| `write_ledger()` is an unguarded whole-file write, and its docstring carries the 260731-EFA-L5 R12 ruling that made that a decision: the durable copy is the git object every caller commits two statements later. | `write_ledger` | mcp/src/agents_remember/kernel/memory_ledger.py:222-244 |
| The contract this file was measured against and deliberately left off — what an unconditional per-log lock buys, and why a store whose durability rests on a deployment fact is the defect L5 was called in to repair. | "contract for control-plane JSONL stores" | mcp/src/agents_remember/controlplane/durable_store.py:1-1 |

## Cross-Repo References

The ledger records code and memory commits across the source repository and its
external memory repository, but the implementation contract is local to this
file and the `c-09-git-worktree-manager` skill worktree manager.

| Finding | Anchor | Source |
| --- | --- | --- |
| Journaled worktree closeout's sole external-phase owner imports these ledger helpers, then rewrites the code-to-memory mapping only when it actually changed. | "existing_mapping = find_mapping(ledger" | mcp/src/agents_remember/worktrees/modules/closeout_external.py:64-64 |
| The irreversible integration transaction loads the exact named-ref ledger and requires its existing code-to-memory row to match the accepted content commit before moving protected refs. | `require_integrated_ledger_mapping` | mcp/src/agents_remember/worktrees/integration/integration_ref_transaction.py:274-359 |

## Update History
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
  L23, "def parse_ledger_text(text: str) -> MemoryLedger:" L29, "class LedgerError(AgentsRememberError):" L40), "def parse_ledger_text(text: str) -> MemoryLedger:" L51-L104 cit:(["def parse_ledger_text(text: str) -> MemoryLedger:"], mcp/src/agents_remember/kernel/memory_ledger.py:52-52),
  `validate_ledger` L147 / `ledger_to_text` L159 / `prepend_mapping` L218, and `write_ledger`
  L193-L215 cit:(["def write_ledger(path: Path"], mcp/src/agents_remember/kernel/memory_ledger.py:193-193). Nothing on this card asserts a measured figure.

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
  `ledger_to_text` cit:([`ledger_to_text`], mcp/src/agents_remember/kernel/memory_ledger.py:159-184), and `L193-L204` began at `def write_ledger` and stopped 5 lines short of
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
