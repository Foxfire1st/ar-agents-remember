# mcp/tests/test_worktree_status_terminal_next_tool.py

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

## Evidence

### Repo-Internal References

- The archive-ready branch names the accepted cleanup operation, its args bind to the real tool, and the branch is exercised for both cleanup verbs. [1]
- The wire envelope declares the three keys the projector writes; nothing rides as an extra. [2]
- The validator accepts roster members, accepts absence, and refuses an out-of-roster value. [3]
- The boundary case: a registered-but-non-public tool is refused on the worktree surface and accepted on the `task_doc` surface, which is what makes the rule per-surface. [4]
- The declarations and the membership validator the cases pin. [5]
- The advertised roster the validator enforces membership against. [6]
- The terminal-archive refusal producer that makes the protected state reachable. [7]
- The projector whose write this file protects. [8]
- The non-public name that must stay non-public on the worktree surface, and the registry row that still registers it. [9]

### Cross-Repo References

No cross-repository boundary is exercised; the fixture builds a local repository under `tmp_path`.
