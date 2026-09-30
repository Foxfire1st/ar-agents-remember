# mcp/src/agents_remember/worktrees/knowledge_gate.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/knowledge_gate.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T20:09:38+02:00 |
| lastVerifiedCommitHash | `c052b2593b85d9baf425cc1d5c46f384b13fc9ea`|
| lastVerifiedCommitDate | 2026-09-30T21:09:40+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[worktrees route overview](overview.md)

## Purpose

**The mandatory invariant gate at the worktree layer's routes (MIK-R09).** Every route that commits or lands memory
asks the gate before it moves anything. The gate ranks above this layer and is reached through
`services.KnowledgeGatePort`; this module decides whether it applies, with marker probes that read no knowledge,
refuses a converted route whose port is unbound, and owns the closeout's own write: the memory commit that publishes a
leaf sets `closed: true` in its history file (MIK-R07 rule 7, MIK-R09 rule 3). It also keeps a direct landing's
closing across calls in per-generation receipts until that generation is decided.

## Code Commentary

### Logic

- **Applicability (rule 6).** `converted_memory(repository, *treeishes)` is true when any named side holds
  `knowledge/layout.json` (through `has_layout_marker`); a side Git cannot read raises `GateProbeError`, never
  "unconverted". The probes per route:
  - `leaf_memory_converted(contract)`: the leaf memory worktree's marker file, else the official memory line's tip
    (the closeout's own writes);
  - `_leaf_gate_applies`: the candidate tree and the official line; an unreadable probe or an invalid branch cell is a
    refusal (`True`, reason);
  - `checkout_memory_converted(repository)`: a direct landing's working tree or `HEAD`, before anything is captured;
  - the landing request's memory commit and bases (`landing_gate_refusal`).

  Where no side holds the marker every function returns `None` (or `False`) after the probe, and the route behaves
  exactly as before this master.
- **No bypass (rule 5).** `GATE_UNBOUND`: a converted route with no bound `knowledge_gate` is refused ("converted
  memory is never committed or landed ungated"). No function takes a flag that skips the gate.
- **`parent_memory_tip(contract)`** is the tip of `memory_source_branch`, the validator's base for a leaf, so every
  record the leaf made is new (the L27 carry).
- **`leaf_gate_refusal(contract, *, code_tree, memory_tree)`** is the closeout validator's gate: probe, port, then
  the tip (a failed or timed-out read is a named refusal, "cannot read the parent memory line"), then
  `port.leaf_refusal`.
- **`direct_gate_verdict`** probes the candidate tree and `HEAD`, then asks `port.direct_verdict`.
- **`landing_gate_refusal(request)`** probes the landed memory commit and its bases, then runs the validator through
  `memory_commit_refusal` (with `leaf_publication` for a leaf's recorded landing) **and** `port.landing_refusal`, and
  joins the named refusals.
- **`prepared_closeout_refusal(contract)`** (ruling 14:38:47 gap 3): the certified (prepared) closeout binds its memory
  commit to the curator-attested candidate, so it cannot set `closed: true`; on converted memory it refuses with
  `PREPARED_CLOSEOUT_UNCLOSABLE` (`prepared-closeout-knowledge-history-unclosable`), naming why and that the leaf
  should close out through the worktree closeout commit. Unconverted memory gets `None`.
- **`close_owner_history(memory_root, owner)`** sets `closed: true` in `knowledge/history/<owner>.json`, creating the
  file with no rows when absent; the rows are never rewritten and the file stays canonical; a file that does not parse
  is left for the validator to name. It returns a `HistoryClosing(path, previous)` whose `restore()` puts the previous
  bytes back (or removes a file it created).
- **A direct landing's closing outlives the call (review R1 F3; R2-2 and R2-5; R3-1).**
  - `keep_direct_closing(contract, closing, fingerprint)` writes a receipt at
    `<worktree_group>/reports/direct-landing-history-closings/<sha256(fingerprint)[:32]>.json`
    (`direct_closing_receipt`): the path, the previous bytes (base64), the SHA-256 of the closed bytes and
    `closedBlob`, computed by `git hash-object` in the memory repository (`_closed_blob`: the repository's own object
    format and filters, R3-1). An existing receipt of the same generation is never overwritten; each generation has
    its own (N12). A Git failure raises `ClosingReceiptError`.
  - `forget_direct_closing` drops only the failing call's own receipt.
  - `settle_direct_closing(contract, *, current, state)` decides each receipt on its own: the current generation's is
    kept while `in-flight`, forgotten once `landed`, restored once `cancelled`; any other generation's was never
    accepted by the journal and is restored, unless the memory line's `HEAD` already holds the closed blob (`_landed`).
    A restore happens only while the file's bytes still equal the closed bytes, so a later edit is never overwritten
    (`_restore_receipt`, N04).
  - `require_readable_closings` and `_receipts` raise `ClosingReceiptError` for an unreadable or malformed receipt,
    naming the file and how to clear it (`_unreadable`: find the leaf history file that is closed although no memory
    commit closed it, reopen it by hand if its landing did not land, delete the receipt and retry); a `HEAD` probe Git
    cannot answer raises the same.

### Conventions

- Imports only the worktree layer's own modules and `services`; the gate itself is never imported here.
- Receipts are JSON (`direct-landing-history-closing/v1`) written with `atomic_write_text`.

### Invariants And Boundaries

- **On unconverted memory every route behaves exactly as before the gate.** Candidate invariant (not ingested).
  Realized by the probes above, which read one file's existence and tree entries and nothing else; proved by
  `test_an_unconverted_leaf_is_not_gated_at_any_route` (every helper returns `None` with no services bound;
  `count-objects` and `status` unchanged) and by `unconverted.sh` (base `904e804b` against this build on the real
  unconverted memory: worklist `null`, memory commit tree `20ccf39a…`, the same record-landing payload including an
  unreadable memory commit, the same direct-landing preview and object count).
- **A probe Git cannot answer is never unconverted memory.** Proved by
  `test_a_marker_probe_git_cannot_answer_is_never_unconverted_memory`.
- **A closing is undone whenever its landing does not land, and never overwrites a later edit.** Proved by the F3,
  N04, N05, N12, R2-5 and R3-1 tests in `test_knowledge_gate_routes.py`.

### Todos

- Review R3 residuals, accepted: after a generation completes through operation-control recovery (which never
  settles), its receipt stays until the next apply or cancel on that series, then is forgotten as landed; a Git failure
  inside `_landed` during a cancel's settle surfaces only after the cancellation is published, and a repeated cancel
  settles again.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is `MIK-R09@v2` and `09_mandatory-invariant-closeout-gate.json`,
outside the repositories.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module docstring: applicability, no bypass, the closing and its receipts. | "A probe Git cannot answer refuses; an unreadable" | mcp/src/agents_remember/worktrees/knowledge_gate.py:1-28 |
| The unbound refusal and the marker probe. | `GATE_UNBOUND`; `GateProbeError`; `converted_memory` | mcp/src/agents_remember/worktrees/knowledge_gate.py:89-105 |
| The parent tip and the leaf probes. | `parent_memory_tip`; `leaf_memory_converted`; `_leaf_gate_applies` | mcp/src/agents_remember/worktrees/knowledge_gate.py:112-148 |
| The prepared path fails closed on converted memory. | `PREPARED_CLOSEOUT_UNCLOSABLE`; `prepared_closeout_refusal` | mcp/src/agents_remember/worktrees/knowledge_gate.py:151-173 |
| The closeout validator's gate. | `leaf_gate_refusal` | mcp/src/agents_remember/worktrees/knowledge_gate.py:176-196 |
| Direct landing's probe and verdict. | `checkout_memory_converted`; `direct_gate_verdict` | mcp/src/agents_remember/worktrees/knowledge_gate.py:199-227 |
| A landing: the validator through the route entry point, plus the port. | `landing_gate_refusal` | mcp/src/agents_remember/worktrees/knowledge_gate.py:230-260 |
| The closeout's own write and its restore. | `HistoryClosing`; `close_owner_history` | mcp/src/agents_remember/worktrees/knowledge_gate.py:263-300 |
| Per-generation receipts, the blob in the repository's own format. | `ClosingReceiptError`; `direct_closing_receipt`; `_closed_blob`; `keep_direct_closing`; `forget_direct_closing` | mcp/src/agents_remember/worktrees/knowledge_gate.py:308-392 |
| Settling each receipt; an unreadable one refuses by name. | `settle_direct_closing`; `require_readable_closings`; `_receipts`; `_unreadable`; `_landed`; `_restore_receipt` | mcp/src/agents_remember/worktrees/knowledge_gate.py:395-497 |
| Unconverted memory is not gated at any route. | `test_an_unconverted_leaf_is_not_gated_at_any_route` | mcp/tests/test_knowledge_closeout_gate.py:993-1026 |

## Cross-Repo References

No meaningful cross-repo references found: the module probes the leaf's memory repository and writes receipts under
the worktree group.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-30T20:09:38+02:00 — 260928-MIK-L09 curator (staged change set on `ar/260928-mik-l09`, code base `904e804b07a598d5d6c66f06b7e67ddab64d9b8e`; review R1 changes-required, fix round, R2 pass-with-notes, round, R3 pass with R3-1 and R3-2 fixed): created this card for the new file MIK-R09 adds, recording gap 3 (the prepared path fails closed) and gap 1 (not wired here; carried to L37) of 14:38:47, review R1 F2, F3, F6 and F9 (16:07:55), R2-2 and R2-5 (17:59:48) and R3-1 (19:16:07, the hash-object backstop). The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
