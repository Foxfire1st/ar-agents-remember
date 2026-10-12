# mcp/src/agents_remember/models/knowledge/review_final_output_receipt.py

## Governing Overview
[models route overview](../overview.md)

## Purpose
Defines exact final-output receipts for tree-bound comparisons while decoding the historical receipt format separately.

## Code Commentary
FinalOutputReceipt binds the recorded code and knowledge trees and their comparison digest. The v2 verdict is two-valued (`bound`/`moved`): `unmeasured` belongs to the v1 generation record only, and no product path writes it into a v2 receipt. `delivered_memory_content_commit` and `delivered_memory_tree_id` are required, and `code_match`/`memory_match` are measured matches against the reviewed input. `tree_match_state` and `tree_output_verdict` compare the actually supplied identities; an unread half is not matching. LegacyFinalOutputReceipt retains the historical code/logical-dataset shape and its validator functions without reopening that dataset. The removed _code_clause/_knowledge_clause helpers are not current rendering owners. A receipt is data about exact compared outputs, never leaf or Git acceptance.

### Invariants And Boundaries

- **`bound` is the only value that claims coverage, and it requires a measured match on every channel the
  generation actually selected.** This is the module's load-bearing invariant; the validator enforces it,
  so no writer can produce a coverage claim the channels do not support.
- **No authored prose.** Every field is an owner-produced fact; the one sentence is derived. A reader
  comparing two receipts compares identities, not wording.
- **A carried identity is never a recomputed one (v1 `LegacyFinalOutputReceipt` only).** `binding_digest` and `manifest_digest` are copied from
  the published record; a digest this vocabulary derived from a field set of its own would be a second
  identity to trust. v2 `FinalOutputReceipt` carries neither field — it carries `comparison` and `comparison_digest` instead.
- **The v1 `LegacyFinalOutputReceipt` typed absence is a value, not a gap.** `not-comparable`, `not-recorded`, `not-selected` and
  `unusable` all mean something specific and are never left to be inferred from `None`.
- **Boundary: this module is the vocabulary only.** It reads nothing, writes nothing and resolves nothing;
  a consumer that wants a receipt from the store calls the application owner. That boundary is why the
  validator can be a pure function of the record's own fields.

## Evidence
### Repo-Internal References

- The one verdict rule and why it has three values (v1 legacy). [36]
- The single verdict expression both the writer and the validator call, so they cannot disagree (v1 `final_output_verdict`; v2 calls `tree_output_verdict`). [37]
- The validator that refuses a record whose verdicts do not follow from the identities it carries (v1 `_the_receipt_agrees_with_itself`; v2 validates tree binding in `_validate_tree_binding`). [38]

- `FinalOutputReceipt` owns the current boundary described above. [19]
- `tree_comparison_digest` owns the current boundary described above. [20]
- `tree_output_verdict` owns the current boundary described above. [21]
- `LegacyFinalOutputReceipt` owns the current boundary described above. [22]

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Cross-Repo References

No cross-repository behavior is implemented in this file. The historical v1 `LegacyFinalOutputReceipt` declares path fields
(`task_root`, `contract_path`, `published_knowledge_path`) are recorded as the owner produced them; the
relocation boundary that follows from a recorded absolute path is stated on
`application/review_final_output_receipt.py` and is the same one ICR-R12/R13 own for the generation
record.

No meaningful cross-repo references found.

- The version and selection-rule literals, carried as fields so the answer travels with the record. [23]
- **In v1 `LegacyFinalOutputReceipt`, the two phases are separate measurements and the historical published dataset can move between them.** [24]
- **The v1 dataset channel's `not-comparable` means one side cannot be compared; this historical state does not make that receipt `moved`.** [25]
- The v1 legacy dataset publication-location states, in the resolving route's vocabulary. [26]
- The code channel's comparison: delivered tree against reviewed candidate tree. [28]
- **The v1 legacy knowledge channel is `not-comparable` when one side is not a dataset and never claims a match without comparison.** [29]
- The record itself: the generation's identities, the delivered commits and trees, the published identity, the two match verdicts and the one state. [31]
- **The one sentence the record publishes, derived from its own fields, one clause per verdict.** [33]
- The shared shapes this vocabulary reuses rather than re-declaring. [34]
- The historical v1 `SnapshotIdentity` the published dataset channel carried when its dataset was read. [35]
