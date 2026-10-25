# mcp/src/agents_remember/memory_quality/knowledge_validator/rules_reference_anchors.py

## Governing Overview

[memory_quality route overview](../overview.md)

## Purpose

**MIK-R198 rule 5 as a registered validator rule: every code and test reference anchor must hold at the exact paired code tree.** An anchor must name the blob of its source path in that tree and resolve there to its recorded content identity. Nothing less publishes: there is no inherited baseline, no stale-content exemption and no count allowance, and a content-current anchor whose blob moved still refuses, because the blob is what binds the claim to the bytes it was written against. Importing the module registers the rule, so every commit, landing and quality route runs it.

## Code Commentary

### Logic

- `check_reference_anchors(context)` returns without a finding when the validation carries no code tree; there is then nothing to judge and no pass to claim. Otherwise it walks `observations_of(context.parsed.sidecars, code)` and yields one `Finding` per non-current observation, at the observation's sidecar and its `references.N.targets.I` field.
- The message names the state, the reason, the pair measured (`measured at <code label> for <candidate label>`) and what the anchor must name, and ends by naming the rule so a refusal is attributable without the reader opening the registry.
- The rule reuses the product's own traversal and resolution (`reference_anchors.observations_of`, the same `located`/`git_blob_id`/`content_identity`/`blob_lines` pieces the census and the fixer run) rather than a parallel scanner, so the guard, the census and the fixer cannot disagree about one anchor.
- Registration carries rule 7's two reporting dispositions. `merge_reports=True` makes each finding a report at a sync merge, where `merge_reports_at` holds and `merge_report_note` appends the sentence naming the next route that refuses it — a merge can create the state from two valid sides and it is repaired only after the merge exists. `writer_reports=True` lets authoring report the debt instead of refusing, so a leaf can break an anchor and repair it before closeout, while no publication route may treat it as a report.

### Conventions

- The message is built once, in `_message`, so both the refusing and the reporting route describe the same two facts in the same words.
- The rule id (`R198.1-reference-anchor`) is declared in `reference_anchors` beside the census that classifies the same anchors, and imported here rather than repeated.

### Invariants And Boundaries

- **Only a current anchor is skipped.** Every other state refuses at a commit or landing route, whatever its repair class; the census's mechanical/judgment split is a repair schedule, not a severity.
- **A blob match alone is not enough.** The recorded content identity must also hold at that blob, and a content match with a moved blob still refuses.
- **The reporting dispositions are the registry's, not this module's own flag.** Writer reporting is a repair affordance and merge reporting is a route reason; neither is publication permission.

### Todos

None recorded.

## Evidence

- The module states rule 5's obligation and the two reporting dispositions it registers. [1]
- The message names the observation's state, its reason and the measured pair. [2]
- The one check: no code tree, no finding; otherwise one finding per non-current anchor. [3]
- Whether this route reports rather than refuses is the registry's merge disposition. [4]
- Each non-current observation becomes a finding at its sidecar and its own target field. [5]
- The observations the check walks are the census module's, over sidecars this route already parsed. [6]
- A reporting route appends the sentence naming what refuses it next. [7]
- The rule id is the census module's own identifier. [8]
- Registration: the rule id, its rule caption, the check, and both dispositions. [9]
- Writer reporting is granted at registration. [10]
- Merge reporting is granted at registration. [11]
- The anchor debt reports at a sync merge, refuses every publication, and is a writer-reported rule. [12]
- A stale anchor refuses the pair the publication routes judge, and repairing that anchor alone clears it. [13]
- A blob-only move refuses a leaf publication even when the located bytes are identical. [14]
- A matching blob with the wrong recorded content refuses. [15]
