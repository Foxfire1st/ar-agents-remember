# mcp/tests/test_post_integration_cleanup_guidance.py

| Field | Value |
| --- | --- |
| verificationStatus | working-candidate |

The body describes the uncommitted LCA L9 working candidate. The commit fields identify the latest real commit touching this source file; they do not claim that the candidate is committed or accepted.

## Governing Overview

[Nearest governing route overview](overview.md)

## Purpose

Pin finalization guidance for a landed task, the still-working checkpoint phase, and cache-independent external-memory completion.

## Code Commentary

### Logic

The minimal internal-memory contract tests phase, operation, tool, contract args, required args, and explanatory summary. A landed but unfinalized task must offer lifecycle_finalize_task rather than a cleanup decision/retry. The vocabulary case keeps the retired cleanup choices absent and finalize present. A checkpointed series stays worktree-started and continues work.

The external-memory case creates real temporary code and memory repositories. Missing, malformed, or stale cache text leaves carryover completion and finalization guidance valid when the accepted outputs are landed. An unlanded memory commit, nonexistent accepted code commit, or missing memory repository must still make the completion proof false.

### Conventions

Module-level tests use the small constructed contract where only projection is at issue and real Git where ancestry is the subject. The external-memory case is no longer accurately described as repository-free.

### Invariants And Boundaries

- Assert structured phase/tool/args, not summary text alone.
- Finalization owns reclamation and a checkpoint remains open.
- Cache contents cannot decide carryover completion.
- Actual missing or unlanded output identities still refuse completion.
- **A step's reason travels with the step.** The coherence-route case asserts the summary carries why
  `validate` must run now, because a step named without its reason is the step the next operator skips —
  which is the defect (D-25) the case exists for.

### Todos

No new file-local follow-up is identified by this source reconciliation.

## Evidence

### Docs References

No domain-documentation source is configured for this slice. The behavior described here is established by current repository source and the authorized LCA L9 change, rather than an invented external reference.

### Repo-Internal References

These current source spans identify the implementation owners and the specific assertions supporting the file's behavior. A test definition is evidence of its assertions, not an execution or certification receipt.

- Finalization and retired cleanup-vocabulary assertions. [1]
- External completion depends on landed commits, never cache text. [2]
- Checkpoint guidance remains still-working. [3]
- Production completion and post-integration guidance owner. [4]

### Cross-Repo References

The operation and fixture boundaries described here are defined by same-repository contracts and Git helpers. No separate cross-repository document is used as evidence for this card.

## KS-R23@v1 The Validate Step Is Named Before Its Window Closes

`260915-KS-L23` item 18's first half (D-25). The guidance chain used to move straight from
closeout-completed to integration, and nothing anywhere named `curator_coherence validate` — while
`lifecycle_finalize_task`'s automatic cleanup collects the enclosure root that the standalone validate
addresses, so a leaf following the tool's own hints finalized and could never re-prove the authority it
had published. Three module-level cases now drive `lifecycle_guidance` over a leaf external-memory
contract:

- `test_a_published_coherence_authority_puts_validate_before_integration` (`:191-222`) — with the
  contract's canonical authority present, the move out of `closeout_status == "completed"` is
  `nextTool == "curator_coherence"` with `action == "validate"`, the exact canonical `caller` payload
  (`{"role": "curator", "task_document_ref": {"repository": "repo", "path": "leaf/leaf.json"}}`), and a
  summary carrying the reason. `nextOperation` stays `request_integration_decision`: the validation is
  the precondition of that decision, not a replacement for it. Red if the branch reverts to
  `worktree_integrate` (the D-25 defect) or names the step without the reason that forces it.
- `test_a_leaf_that_has_not_published_is_still_told_to_integrate` (`:225-234`) — red if the
  published-authority condition is dropped and every leaf is routed to a tool that would refuse.
- `test_a_series_contract_is_never_routed_to_the_coherence_route` (`:237-249`) — red if the leaf-only
  applicability guard is lost.

`_external_memory_leaf` (`:154-188`) builds the contract those cases drive — external memory, a memory
worktree, a completed closeout — and writes the canonical authority where `curator_coherence_paths`
resolves it, which is what makes the first case's condition real rather than mocked.
