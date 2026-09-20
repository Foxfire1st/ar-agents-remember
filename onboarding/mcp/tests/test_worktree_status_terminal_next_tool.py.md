# mcp/tests/test_worktree_status_terminal_next_tool.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_worktree_status_terminal_next_tool.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-13T11:43+02:00 |
| lastVerifiedCommitHash | `7ca3ac48914a562bb90b5fe04d6c17b5a3f51d80` |
| lastVerifiedCommitDate | 2026-09-20T02:00:33+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

`test_worktree_status_terminal_next_tool.py` (260831-LOCR-L32) pins the worktree surface's advertised
next move: the `terminal-archive-ready` branch of `worktree_status` must name a **registered public**
tool, and the wire envelope must actually declare the keys the projector writes. It is the executor
for an invariant that previously had none, and it is the first coverage of the `terminal-archive-ready`
branch at all — that branch had **zero** cases before this leaf.

The cases are integration-lane members (`mcp/tests/test-evidence-lanes.toml`) and are registered as
consumers in three `mcp/tests/evidence-lifecycle.toml` rows.

## Code Commentary

### Logic

Two producers reach the protected field, and the module proves both.

`_terminal_archive_ready_status` reaches the real state rather than faking it: it drafts a leaf
contract, `publish_test_enclosure`s it, calls
`terminal_enclosure_archive.terminal_archive_required_result(..., dry_run=False)` to publish the
archive and receipt, then `shutil.rmtree`s the worktree group — which is the deletion step of the
production cleanup, and what leaves the locator `terminal-archived` with the archive proof still
durable. It then calls the real `worktree_status_payload`. The `rmtree` is not a shortcut; it is the
state transition under test.

**`test_archive_ready_status_names_the_accepted_cleanup_operation`** is parametrized over
`worktree_cleanup` (`TerminalWorktreeCleanupArguments(teardown_providers=True)`) and
`worktree_abandon` (`TerminalWorktreeAbandonArguments(force=False)`). It asserts
`state == status == "terminal-archive-ready"`, `nextTool == operation`, `nextAction == operation`,
and that `nextArgs` equals `{"contract_path": <path>, "dry_run": False, **arguments.model_dump(mode="json")}`.
It then calls `inspect.signature(payload_builder).bind(None, **next_args)`: the emitted mapping must
bind to the *real* tool signature, so an extra key or a missing required one raises `TypeError`.
That is what makes the emitted `nextArgs` provably actionable rather than merely shaped right.

**`test_worktree_status_declares_the_next_move_keys`** asserts
`TOOL_RESPONSE_MODELS["worktree_status"] is WorktreeStatusResponse` and that `nextAction`,
`nextTool` and `nextArgs` are all in `WorktreeStatusResponse.model_fields` — i.e. that nothing rides
as an undeclared extra on the flexible envelope.

**`test_next_tool_must_name_a_registered_public_tool`** drives the validator in both directions:
`worktree_cleanup`, `worktree_abandon`, `worktree_status` and `task_doc` are in `PUBLIC_TOOLS` and
validate; an absent key yields `nextTool is None`; and `not_a_tool` raises `ValidationError`
mentioning `not in PUBLIC_TOOLS`.

**`test_the_worktree_surface_refuses_a_registered_but_non_public_tool`** is the boundary case that
makes the rule per-surface: `session_retire` is in `TOOL_RESPONSE_MODELS` and absent from
`PUBLIC_TOOLS`, the worktree standard refuses it, and the same value validates on the `task_doc`
surface (`TaskDocResponse.model_validate(...).nextTool == "session_retire"`).

### Conventions

- The module's docstring carries the whole producer survey behind the invariant (union of 20
  `nextTool` values traced to their producers) and the per-surface rule. That prose is the argument
  for the assertion set, so it is not redundant with this card.
- Deletion happens through production code paths (`terminal_archive_required_result`,
  `shutil.rmtree`) rather than mock state, so the case cannot drift from the state machine.

### Invariants And Boundaries

- **The invariant is per surface, and that is deliberate.** The worktree surface's next move must name
  a registered **public** tool, because those values are advertised guidance an agent acts on. The
  `task_doc` surface may name a non-public tool. Widening `PUBLIC_TOOLS` to admit `session_retire`
  would be the wrong fix; so would moving the invariant onto a shared envelope.
- **`normalize_closeout_input` and `worktree closeout` are not outliers.** They are
  `CloseoutCorrectedCall.tool` — a different field, not `nextTool` — so they are outside this
  invariant.
- Do not weaken the `inspect.signature(...).bind(...)` check to a key-set comparison: binding against
  the real builder is what proves the emitted args are exactly what the named tool accepts.
- `pytestmark = pytest.mark.usefixtures("worktree_services")` selects real worktree services; the
  cases are integration-lane, not hermetic units.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The archive-ready branch names the accepted cleanup operation, its args bind to the real tool, and the branch is exercised for both cleanup verbs. | `test_archive_ready_status_names_the_accepted_cleanup_operation` | mcp/tests/test_worktree_status_terminal_next_tool.py:192-219 |
| The wire envelope declares the three keys the projector writes; nothing rides as an extra. | `test_worktree_status_declares_the_next_move_keys` | mcp/tests/test_worktree_status_terminal_next_tool.py:230-236 |
| The validator accepts roster members, accepts absence, and refuses an out-of-roster value. | `test_next_tool_must_name_a_registered_public_tool` | mcp/tests/test_worktree_status_terminal_next_tool.py:231-244 |
| The boundary case: a registered-but-non-public tool is refused on the worktree surface and accepted on the `task_doc` surface, which is what makes the rule per-surface. | `test_the_worktree_surface_refuses_a_registered_but_non_public_tool` | mcp/tests/test_worktree_status_terminal_next_tool.py:247-278 |
| The declarations and the membership validator the cases pin. | "# The next-move triple, declared here so the worktree surface's guidance is part of"; "def _require_registered_public_next_tool" | mcp/src/agents_remember/models/worktree.py:352-352; mcp/src/agents_remember/models/worktree.py:385-385 |
| The advertised roster the validator enforces membership against. | `PUBLIC_TOOLS` | mcp/src/agents_remember/models/tools/public_roster.py:22-85 |
| The terminal-archive refusal producer that makes the protected state reachable. | `terminal_archive_required_result` | mcp/src/agents_remember/worktrees/integration/terminal_enclosure_archive.py:86-150 |
| The projector whose write this file protects. | `_project_terminal_contract_status` | mcp/src/agents_remember/application/worktree_status.py:463-505 |
| The non-public name that must stay non-public on the worktree surface, and the registry row that still registers it. | "\"session_retire\","; "\"session_retire\": SessionRetireResponse," | mcp/src/agents_remember/models/tools/tool_registry.py:134-134; mcp/src/agents_remember/models/tools/tool_registry.py:158-158; mcp/src/agents_remember/models/tools/tool_registry.py:140-140; mcp/src/agents_remember/models/tools/tool_registry.py:164-164; mcp/src/agents_remember/models/tools/tool_registry.py:147-147; mcp/src/agents_remember/models/tools/tool_registry.py:171-171 |

## Cross-Repo References

No cross-repository boundary is exercised; the fixture builds a local repository under `tmp_path`.

## Update History
- 2026-09-20T01:00+02:00 — 260915-KS citation residue clearance (uncommitted change set on memory base `66b2ae8adebea11bc2300d2d51822f321a128657`): cleared the 2 enforced citation rows this card carried (citation_anchor_absent_from_range): both cited ranges were hand-read against mcp/src/agents_remember/models/worktree.py and already held the anchor their claim names — the next-move-triple comment at worktree.py:352-352 and `def _require_registered_public_next_tool` at worktree.py:385-385 — so no range was changed; every claim wording, anchor and every other range is unchanged, and no verification stamp was advanced.
- 2026-09-20T00:31+02:00 — 260915-KS-L30 curator (uncommitted change set on `ar/260915-ks-l30-ar`, base `7dcec036094768c5f50e571fb45e59a27ae78efc`): **mechanical citation-range projection** against this leaf's candidate. The checklist reported 2 row(s) whose cited range no longer holds its anchor although the construct is present in the cited file; each range was widened to the lines that carry it — `# The next-move triple, declared here so the worktree surface's guidance is part of`; `def _require_registered_public_next_tool`. No claim wording, anchor or citation was added, removed or re-worded, and no range was deleted: the new range is the checklist's own resolved extent for that anchor on this candidate. No verification stamp was advanced.
- 2026-09-18T19:51:00+02:00 — 260915-KS-L23 residue clearance, seat B (uncommitted change set on `ar/260915-ks-l23`, memory base `59eab7a0`): **cleared the one enforced `citation_anchor_absent_from_range` row in this document.** The pinned-declarations row's next-move-triple cell cited `models/worktree.py:323-323`, which is `code_quality_gate`; widened to `323-330` so the range reaches the comment that declares the triple. The validator cell at `355-364` and the claim are unchanged. No claim was re-worded, no anchor or range was dropped to silence a row, and no verification stamp advanced: the candidate is uncommitted and the governed closeout owns the real code and memory commits.
- 2026-09-17T20:42:17+00:00: Generated citation repair: `test_worktree_status_declares_the_next_move_keys` repointed to mcp/tests/test_worktree_status_terminal_next_tool.py:230-236. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T20:42:17+00:00: Generated citation repair: `_project_terminal_contract_status` repointed to mcp/src/agents_remember/application/worktree_status.py:463-505. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-13T14:32+02:00 — Curator citation repoint after the contract-scoped atomic-series activation re-keying shrank `models/worktree.py`: the next-move triple comment now resolves at `models/worktree.py:322-322` and `_require_registered_public_next_tool` at `models/worktree.py:355-364`, so the declarations/validator row was rebound. Claim wording unchanged.
- 2026-09-13T09:43+00:00 -- 260831-LOCR-L34 curator citation review: every claim this card carries was re-read against its cited range in the code worktree; anchors were rebound to the exact literal bytes at the cited location, ranges stale by a line shift were repaired, and claims the generated projection left unsupported were re-cited or re-worded. No verification stamp advanced.
- 2026-09-12T22:55+02:00 — 260831-LOCR-L32 curator: created the card for the new integration-lane
  module. Recorded that it is the first and only coverage of the `terminal-archive-ready` branch, that
  it reaches that state through real production calls, that it pins the three declarations plus the
  membership validator in both directions, and that the boundary case is what makes the invariant
  per-surface (`task_doc` may name the registered-but-non-public `session_retire`; the worktree
  surface must not, and `PUBLIC_TOOLS` must not be widened to allow it). Verification metadata
  remains closeout-owned; no acceptance claim.
