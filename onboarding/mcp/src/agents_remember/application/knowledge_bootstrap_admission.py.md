# mcp/src/agents_remember/application/knowledge_bootstrap_admission.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/knowledge_bootstrap_admission.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-24T09:20+02:00 |
| lastVerifiedCommitHash | `8b0254263c6998b1d4814b2e97c1bd231d39350f` |
| lastVerifiedCommitDate | 2026-09-29T15:00:35+02:00|
| governingOverview | `mcp/src/agents_remember/application/overview.md` |

## Governing Overview

[application route overview](overview.md)

## Purpose

**The taskless admission: a real knowledge write derived from authority that exists for a repository
with no task (ICR-R29@v1).** The only admission the write plane had was a leaf enclosure contract,
which is correct for a task's own ingest and wrong for a repository's *first* knowledge — a repository
that by definition has no task, no leaf and no enclosure yet. `BOOTSTRAP-HANDOVER.md` line 11 refuses
minting a contract to satisfy that shape and a second write path is the parallel-store defect, so this
module is the third option: **a second admission, derived from an authority that really exists.**

That authority is the product's own setup authority:

- the MCP runtime settings document (`McpRuntimeConfig`) — the same document
  `initialize_memory` reads — declares which repositories exist, where their checkouts are and where
  their external memory root is; a repository it does not list is refused by name, exactly as the
  memory initializer refuses it;
- the coordination resolver, invoked with **no enclosure selector**, is the owner of "which memory
  layer does this repository's ordinary read select" — so the bootstrap publishes where ordinary
  readers resolve rather than to a second convention that agrees today;
- the two real Git checkouts supply the **exact source inputs**: the code line's commit and the memory
  line's commit, read at admission time rather than asserted by a caller.

**Every way out is a named state, and none of them is a fallback.** A repository that is not declared,
a memory layer that cannot be resolved, a coordination root that does not exist, a code root that is
not a Git checkout, a memory root that is not the one the ordinary read route selects, an enclosure
somehow in scope, an unreadable revision: each is a `BootstrapRefusal` (`:118-129`) carrying a stable
`code`, the fact that produced it and the `next_action` that re-observes it. There is deliberately no
branch that borrows another repository's memory root, another branch's commit or another dataset's
namespace — the packet's "no silent fallback to another repository, branch or dataset" is a property
of the control flow rather than a promise in a docstring.

## Code Commentary

### Logic

**`admit_bootstrap_context` is one ordered chain, and the order is the order the facts depend on**
(`:175-214`). The repository entry, then the coordination root, then the code checkout, then the memory
layer the ordinary read route resolves, then the equality of that layer with the one the setup document
declares, then the two exact revisions. Each step delegates to its own helper — `_coordination_root_refusal`
(`:217-234`), `_code_checkout_refusal` (`:237-258`), `_resolved_context` (`:261-291`),
`_context_admission` (`:294-348`) — and no step is skipped because a later one might have answered.

**The resolver is called with an empty selector, and that is the whole point** (`:261-291`). A bootstrap
is a repository-scoped act; an enclosure selector would make the effective memory root *this task's*
memory worktree — a line about to be cleaned up — rather than the repository's memory layer. Anything
the resolver cannot answer becomes a named refusal carrying the resolver's own sentence rather than a
path this module guessed.

**The declaration/resolution pair is carried, not collapsed** (`:294-348`). `declared` is what the
settings document says the memory root is and `context.memory_root` is what the ordinary read route
resolved; the two are compared, and an inequality is `memory_line_moved` naming both paths, because a
reader has to be able to *see* the equality rather than trust it. The same helper refuses
`enclosure_in_scope` when the resolved context carries a contract path, with the reason stated: a
bootstrap must not publish onto a line that is about to be cleaned up.

**The two revisions are read, never accepted** (`:392-423`). `_source_revisions` runs
`rev-parse --verify HEAD^{commit}` in the code checkout and in the memory root, and a checkout that
cannot answer is a refusal naming it — `code_revision_unavailable` or `memory_revision_unavailable` —
never a silently empty revision. The docstring states why: an admission with no commit would make the
snapshot and candidate references meaningless while still looking admitted.

**The retry scope is a function of the repository alone** (`:154-162`). `bootstrap_scope` returns
`knowledge-bootstrap:<repo_id>`, deliberately independent of the commit the code line has advanced to,
or a resumed run would mint a second set of identities for knowledge it already holds. The scope is
joined with the entry's own id to form the allocation-journal key, so a repository's bootstrap and any
leaf of that repository never alias each other.

**Staging lives in one derived place** (`:165-172`, `:76-79`).
`BOOTSTRAP_STAGING_DIRECTORY` is a constant rather than a caller argument, and
`bootstrap_staging_root(context, repo_id)` derives the path from the resolved context's own
`temp_root`, so the writer, the resume path and the cleanup owner name one directory by construction.

**The branch is a hint, not an identity** (`:380-389`). `_current_branch` answers the checkout's own
symbolic ref, or `""` for a detached HEAD; the operation then reads `HEAD` and, failing that, the
admitted base commit, and reports which of the three it used.

### Conventions

The module imports the write-admission value, the published-dataset path owner, the coordination
resolver, the shipped Git runner and the contract reader. It writes nothing, opens no database and
computes no digest.

### Invariants And Boundaries

- No caller can assert an admission: `admit_bootstrap_context(config, repo_id)` is the only producer.
- **Two refusals are defence in depth and no case exercises either.** `enclosure_in_scope` cannot be
  reached through this API (the resolver is called with an empty `EnclosureSelector`), and neither can
  `memory_line_moved`: this call passes the coordination root the settings document declares, so the
  memory layer the resolver derives is the one the document declares. The verifier measured the second
  one — mutating that condition to `if False:` left all nineteen cases passing — and re-ran the
  construction proof for both, so they are recorded here as guards that defend a future change of the
  selector or the authority document, **not** as refusals a case reaches.
- The resolver is called with an empty `EnclosureSelector`; a resolved contract path is
  `enclosure_in_scope`.
- The declared memory root and the resolved one are compared, and the pair is reported.
- Both revisions are read from the real checkouts; an unreadable revision is a refusal, never `""`.
- Every refusal carries a stable code, the fact that produced it and the route that re-observes it.
- No branch falls back to another repository, branch or dataset.
- `AdmissionProvenance.reference` is `<config_path>#repositories.<repo_id>`, so the admission can be
  re-opened rather than trusted.

### Todos

None recorded.

## Docs References

No configured Domain Documentation source applies; `BOOTSTRAP-HANDOVER.md` is the process authority
this admission implements, and it is a task-tree document rather than a configured domain source.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external documentation is required for the taskless bootstrap admission. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| **The module's own statement of why the enclosure shape is wrong here and what the third option is.** | "a second admission"; "derived from an authority that really exists"; "line 11" | mcp/src/agents_remember/application/knowledge_bootstrap_admission.py:1-40 |
| The published surface: the staging constant, the four values, the resolver and the two derivers. | `__all__` | mcp/src/agents_remember/application/knowledge_bootstrap_admission.py:66-74 |
| The one staging directory name, a constant so the cleanup owner and the writer name one place. | `BOOTSTRAP_STAGING_DIRECTORY` | mcp/src/agents_remember/application/knowledge_bootstrap_admission.py:79-79 |
| The retry-scope prefix that keeps a repository's bootstrap and a task's knowledge two operations. | `_SCOPE_PREFIX` | mcp/src/agents_remember/application/knowledge_bootstrap_admission.py:85-85 |
| **The authority a taskless bootstrap was admitted under, with the declared/resolved memory-root pair carried rather than collapsed.** | `BootstrapAuthority`; `authority_entry` | mcp/src/agents_remember/application/knowledge_bootstrap_admission.py:88-115 |
| The authority reference in one stable spelling, for a report or a progress record. | `source`; "repositories" | mcp/src/agents_remember/application/knowledge_bootstrap_admission.py:111-115 |
| **Why a repository could not be admitted, and the route that re-observes the condition.** | `BootstrapRefusal`; `next_action` | mcp/src/agents_remember/application/knowledge_bootstrap_admission.py:118-129 |
| One admitted bootstrap: the authority, the admission, the destination and the staging root. | `AdmittedKnowledgeBootstrap`; `destination_path` | mcp/src/agents_remember/application/knowledge_bootstrap_admission.py:132-151 |
| **The retry scope as a function of the repository alone, so a resume asks the same question.** | `bootstrap_scope` | mcp/src/agents_remember/application/knowledge_bootstrap_admission.py:154-162 |
| The staging root derived from the resolved context's own temp root. | `bootstrap_staging_root` | mcp/src/agents_remember/application/knowledge_bootstrap_admission.py:165-172 |
| **The ordered chain, where no step is skipped because a later one might have answered.** | `admit_bootstrap_context` | mcp/src/agents_remember/application/knowledge_bootstrap_admission.py:175-214 |
| Why an absent coordination root is refused rather than created by Git. | `_coordination_root_refusal`; "coordination_root_unavailable" | mcp/src/agents_remember/application/knowledge_bootstrap_admission.py:217-234 |
| Why a declared code root that is not a Git checkout cannot supply exact source inputs. | `_code_checkout_refusal`; "code_checkout_is_not_a_git_checkout" | mcp/src/agents_remember/application/knowledge_bootstrap_admission.py:237-258 |
| **The resolver called with no enclosure selector, and the refusal that keeps a guessed path out.** | `_resolved_context`; `EnclosureSelector`; "memory_layer_not_resolved" | mcp/src/agents_remember/application/knowledge_bootstrap_admission.py:261-291 |
| **The equality check between the declared and the resolved memory root, and the enclosure refusal.** | `_context_admission`; "memory_line_moved"; "enclosure_in_scope" | mcp/src/agents_remember/application/knowledge_bootstrap_admission.py:294-348 |
| **The write admission this context confers, with provenance naming the settings entry.** | `_admission`; `AdmissionProvenance` | mcp/src/agents_remember/application/knowledge_bootstrap_admission.py:351-377 |
| The branch as a hint about which line to read, never an identity input. | `_current_branch` | mcp/src/agents_remember/application/knowledge_bootstrap_admission.py:380-389 |
| **The two exact revisions read from the real checkouts, and the refusals when a checkout cannot answer.** | `_source_revisions`; "code_revision_unavailable"; "memory_revision_unavailable" | mcp/src/agents_remember/application/knowledge_bootstrap_admission.py:392-423 |
| The one commit id a checkout answers, or nothing. | `_revision` | mcp/src/agents_remember/application/knowledge_bootstrap_admission.py:426-431 |
| The value this module produces, and the two kinds it declares. | `KnowledgeWriteAdmission`; `BOOTSTRAP_ADMISSION_KIND` | mcp/src/agents_remember/application/knowledge_write_admission.py:60-60; mcp/src/agents_remember/application/knowledge_write_admission.py:79-131 |
| **The destination owner resolved through the ordinary read route, so writer and reader cannot disagree.** | `published_dataset_path` | mcp/src/agents_remember/application/published_intent.py:239-255 |
| The resolver and the selector type the empty selector is an instance of. | `resolve_coordination_context`; `CoordinationHints`; `EnclosureSelector` | mcp/src/agents_remember/kernel/coordination_context_resolver.py:134-147; mcp/src/agents_remember/kernel/coordination_context_resolver.py:30-30; mcp/src/agents_remember/kernel/coordination_context_resolver.py:36-36 |
| The context whose `temp_root` the staging root is derived from, and the request the resolver takes. | `CoordinationContext`; `temp_root`; `CoordinationRequest` | mcp/src/agents_remember/kernel/coordination_context/models.py:188-216; mcp/src/agents_remember/kernel/coordination_context/models.py:158-164 |
| **The settings document and repository entry that are the authority here.** | `McpRuntimeConfig`; `RepositoryScope`; `allowed_repo_ids` | mcp/src/agents_remember/kernel/primitives/runtime_config.py:80-86; mcp/src/agents_remember/kernel/primitives/runtime_config.py:128-156 |
| The shipped Git runner every revision read goes through. | `run_git` | mcp/src/agents_remember/kernel/git_command.py:150-214 |
| The contract reader the resolver is given, which answers an empty selector with no contract. | `WorktreeContractReader` | mcp/src/agents_remember/worktrees/modules/contract_reader.py:27-115 |
| The memory initializer this module's authority document is shared with (since MIK-R24 it also writes `knowledge/layout.json` for a brand-new root, and never for an existing one). | `initialize_memory` | mcp/src/agents_remember/kernel/memory_init.py:216-317 |

## Cross-Repo References

No cross-repository behavior is implemented in this file: it resolves exactly one repository's own
context and reads only that repository's two checkouts. The resolved settings' `crossRepo.allow` is
empty, so nothing here names, reads or writes another repository.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-29T14:21:42+02:00 — 260928-MIK-L24 curator (uncommitted change set on `ar/260928-mik-l24`, code base `cd3e943d740b490d391722389af0a6bca0ccf93e` plus the working-tree delta and untracked files): **Reopened claim re-read (MIK-R24).** `initialize_memory` changed: it now writes the layout marker for a brand-new root only. The row naming it as the shared initializer still holds; it was reworded to say so, and its range (`216-317`) is the function's real extent. This folds in the fixer projection of this pass. No claim about this card's own source changed.
- 2026-09-29T12:03:26+00:00: Generated citation repair: `published_dataset_path` repointed to mcp/src/agents_remember/application/published_intent.py:239-255. No content impact: mechanical anchor-range projection bound to citation source snapshot 75677f16e5ed8ed01a37a3496ecf058f05e2f85f804720849cd36afc05309a98; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-24T10:20+02:00 — 260921-ICR-L29 curator, **fix-round bytes** (uncommitted change set on
  `ar/260921-icr-l29-ar`, base `0d7910f9d646161c414ed6543453536a3c749d49`; gate `verify-l29-round2.md`,
  first line `pass-with-findings`): **the two construction-proved guards are now named as such.** This
  module is byte-identical to the round-1 candidate, so no sentence about its behaviour needed
  correcting; what the round-1 verification established is a *coverage* fact that belongs on the card:
  neither `enclosure_in_scope` nor `memory_line_moved` is exercised by a case, the second one measured by
  mutating its condition and watching all nineteen cases still pass, and both were construction-proved
  by the verifier. Recording that prevents a later reader from treating either as a reached refusal.
  **No verification stamp was advanced** — the candidate is uncommitted and the governed closeout owns
  the real code and memory commits.

- 2026-09-24T09:20+02:00 — 260921-ICR-L29 curator (uncommitted change set on `ar/260921-icr-l29-ar`,
  base `0d7910f9d646161c414ed6543453536a3c749d49`): created this one-to-one card for the module
  `ICR-R29@v1` introduced as **the taskless admission**. The stamp basis is the leaf's base commit,
  because the module is untracked there. What a reader must not lose is that this is authority rather
  than a flag: the repository entry is read from the settings document, the memory layer from the
  ordinary read route's own resolution with **no enclosure selector**, and both revisions from the real
  checkouts — nothing on this path accepts "is this a bootstrap?" as input. The second is that every
  failure is a named refusal with a re-observing route, so no branch falls back to another repository,
  branch or dataset. No verification stamp beyond the leaf's base is advanced: the candidate is
  uncommitted and the governed closeout owns the real commit.
