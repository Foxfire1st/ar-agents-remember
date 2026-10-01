# mcp/src/agents_remember/application/knowledge_bootstrap_admission.py

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

## Evidence

### Docs References

No configured Domain Documentation source applies; `BOOTSTRAP-HANDOVER.md` is the process authority
this admission implements, and it is a task-tree document rather than a configured domain source.

No external documentation is required for the taskless bootstrap admission.

### Repo-Internal References

- **The module's own statement of why the enclosure shape is wrong here and what the third option is.** [1]
- The published surface: the staging constant, the four values, the resolver and the two derivers. [2]
- The one staging directory name, a constant so the cleanup owner and the writer name one place. [3]
- The retry-scope prefix that keeps a repository's bootstrap and a task's knowledge two operations. [4]
- **The authority a taskless bootstrap was admitted under, with the declared/resolved memory-root pair carried rather than collapsed.** [5]
- The authority reference in one stable spelling, for a report or a progress record. [6]
- **Why a repository could not be admitted, and the route that re-observes the condition.** [7]
- One admitted bootstrap: the authority, the admission, the destination and the staging root. [8]
- **The retry scope as a function of the repository alone, so a resume asks the same question.** [9]
- The staging root derived from the resolved context's own temp root. [10]
- **The ordered chain, where no step is skipped because a later one might have answered.** [11]
- Why an absent coordination root is refused rather than created by Git. [12]
- Why a declared code root that is not a Git checkout cannot supply exact source inputs. [13]
- **The resolver called with no enclosure selector, and the refusal that keeps a guessed path out.** [14]
- **The equality check between the declared and the resolved memory root, and the enclosure refusal.** [15]
- **The write admission this context confers, with provenance naming the settings entry.** [16]
- The branch as a hint about which line to read, never an identity input. [17]
- **The two exact revisions read from the real checkouts, and the refusals when a checkout cannot answer.** [18]
- The one commit id a checkout answers, or nothing. [19]
- The value this module produces, and the two kinds it declares. [20]
- **The destination owner resolved through the ordinary read route, so writer and reader cannot disagree.** [21]
- The resolver and the selector type the empty selector is an instance of. [22]
- The context whose `temp_root` the staging root is derived from, and the request the resolver takes. [23]
- **The settings document and repository entry that are the authority here.** [24]
- The shipped Git runner every revision read goes through. [25]
- The contract reader the resolver is given, which answers an empty selector with no contract. [26]
- The memory initializer this module's authority document is shared with (since MIK-R24 it also writes `knowledge/layout.json` for a brand-new root, and never for an existing one). [27]

### Cross-Repo References

No cross-repository behavior is implemented in this file: it resolves exactly one repository's own
context and reads only that repository's two checkouts. The resolved settings' `crossRepo.allow` is
empty, so nothing here names, reads or writes another repository.

No meaningful cross-repo references found.
