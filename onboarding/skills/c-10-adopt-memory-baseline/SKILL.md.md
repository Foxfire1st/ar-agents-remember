# skills/c-10-adopt-memory-baseline/SKILL.md

## Governing Overview

[overview.md](../../overview.md)

## Purpose

The authored baseline-adoption skill establishes the first Git-attributed memory-content baseline for existing external onboarding. It exposes drift and developer acceptance as trust decisions while separating committed content/history from the derived memory.md cache.

## Commentary

### Status, preview and explicit approval

The documented installed route uses memory_baseline_status before adoption and requires developer approval of the baseline decision. memory_baseline_adopt applies by default: dry_run=true is the preview, and omitting it is a real apply. The example with accept_drift=true is not blanket authorization to accept warnings; that flag belongs to an explicitly approved request. The instruction-only skill does not itself supply an adoption script or permission to run one.

### Attribution, not cache presence, proves adoption

The workflow resolves external context, runs MQC drift classification, and inspects reachable memory commits for Code-Commit attribution. Existing attribution yields already-adopted regardless of cache presence. The configured memory default branch receives one onboarding/system/docs content commit with a Code-Commit trailer; memory.md is computed afterward without another commit and is never committed as baseline content. A missing, stale or malformed cache is not evidence for or against adoption.

### Converted-tree validity cannot be waived

Actionable drift blocks unless the approved adoption request accepts it. Converted memory adds a non-waivable blocked-invalid condition: the knowledge validator must accept the tree before the first baseline is committed. accept_drift accepts stale anchors only, never validator violations. The converted-drift paragraph further states that a stale reference alone does not block; invariant currentness belongs to knowledge_read/knowledge_integrity_check. citation_fix handles moved-only anchors and curator re-authoring handles stale meaning; describing those operations does not authorize their execution.

### Reviewable states and refusal preservation

The source enumerates ready, blocked-drift, blocked-invalid, unavailable, already-adopted, adopted and would-adopt. Unreadable existing HEAD history waits rather than pretending adoption is absent. would-adopt requires staged-tree validation to pass; dry runs and refusals leave index, refs and files unchanged. adopted means the attributed content baseline committed and cache refresh was attempted, not a promise that every subsequent refresh succeeded.

### Refresh and inherited vocabulary boundaries

Adoption does not refresh onboarding; c-05 owns that maintenance. The old account’s already-ledgered state, command-line flags, existing-ledger test, delegation to c-09 and no-overwrite-memory.md assertion are retained as historical statements, not current adoption rules. In particular, cache state must not replace reachable attribution, and the current state name is already-adopted. Old package-service anchors remain archived evidence only; the skill text and its equal packaged copy are source-contract evidence, not implementation acceptance.

### Scoped inherited commentary and evidence

The following inherited account is retained for commentary, migration history, todos and evidence meaning. It is not wholesale re-certified. Its uses of “current”, “now”, dates, milestones, tool names, command examples, topology descriptions, implementation claims or verification stamps describe that inherited account only. The source-grounded account above and evidence table below own newly authored claims. Historical reference numbers are not converted reference identities: original reference identities remain historical, not freshly allocated identities for the current evidence. This retained body creates no role, task, permission, live-build or execution authority.

> **Inherited heading: c-10-adopt-memory-baseline/SKILL.md**
>
> **Inherited heading: Purpose**
>
> This skill documents the ergonomic adoption path for existing external-memory onboarding that predates `memory.md`. It tells agents how to inspect that onboarding, surface drift, and create the first ledgered baseline only after the developer has accepted the trust decision.
>
> **Inherited heading: Code Commentary**
>
> **Inherited heading: Logic**
>
> The skill routes users through `status` before `adopt`. The workflow resolves the code repository with `c-08-ar-coordination-context-resolver` skill using `--code-repository-name` or `--code-repository-root`, runs `c-02-memory-quality-control` skill drift classification with the reusable report under `c-08-ar-coordination-context-resolver` skill's resolved temp root by default, checks for an existing ledger, blocks actionable drift unless `--accept-drift` is present, and then delegates the actual external-memory bootstrap and `memory.md` creation to `c-09-git-worktree-manager` skill.
>
> **Inherited heading: Conventions**
>
> The output is state-oriented: `ready`, `blocked-drift`, `already-ledgered`, `adopted`, and `would-adopt` are the reviewable states. `--accept-drift` is not an automatic refresh; it records the developer's assertion that the current onboarding is factual enough to become the memory baseline.
>
> **Inherited heading: Invariants And Boundaries**
>
> `c-10-adopt-memory-baseline` skill may create the initial ledgered external-memory baseline through `c-09-git-worktree-manager` skill, but it must not overwrite an existing `memory.md` and must not update onboarding content. `c-05-create-or-update-onboarding-files` skill remains the refresh path for stale or incomplete onboarding.
>
> **Inherited heading: Todos**
>
> No current todo is recorded for the skill description itself. Future work should stay in the script and tests unless the user-facing workflow changes.
>
> **Inherited heading: Docs References**
>
> No external documentation is needed for this repository-local skill.
>
> No relevant external documentation found.
>
> **Inherited heading: Evidence**
>
> **Inherited heading: Repo-Internal References**
>
> The skill is the human-facing contract for the adoption script and its trust boundary.
>
> - The skill defines the adoption use case, uses `--code-repository-name`/`--code-repository-root` command examples, and makes `c-02-memory-quality-control` skill drift plus explicit acceptance the central trust boundary.
> - The package baseline service implements the documented states and delegates baseline creation to `c-09-git-worktree-manager` skill.
> - `c-10-adopt-memory-baseline` skill's drift run delegates report path resolution to `c-02-memory-quality-control` skill with the resolved `coordination_root` and `temp_root`.
>
> **Inherited heading: Cross-Repo References**
>
> No sibling repository evidence is needed for the skill itself.
>
> No meaningful cross-repo references found.

### Scoped inherited companion commentary

These are the old companion’s explanatory notes, retained as historical evidence descriptions rather than freshly validated targets. Original anchor objects, source paths, blobs, digests and locator values remain unchanged in input custody; they are not re-authored here.

> The skill defines the adoption use case, uses `--code-repository-name`/`--code-repository-root` command examples, and makes `c-02-memory-quality-control` skill drift plus explicit acceptance the central trust boundary.

> The package baseline service implements the documented states and delegates baseline creation to `c-09-git-worktree-manager` skill.

> `c-10-adopt-memory-baseline` skill's drift run delegates report path resolution to `c-02-memory-quality-control` skill with the resolved `coordination_root` and `temp_root`.

## Evidence

The following references support the source-contract commentary, not fresh runtime acceptance. Canonical authored source owns the contract; the inspected package copy is an equal distribution twin only. Root overview ownership context is onboarding/overview.md, especially its construction/ownership and retained naming-versus-reading doctrine. The description of a source contract is not runtime acceptance or permission to execute its operations.

- Existing-onboarding use case and explicit trust boundary [1]
- Status-first, apply-by-default preview and approval [2]
- External context, drift, attribution and validated content commit [3]
- Output states and no-change dry-run/refusal semantics [4]
- Converted reference drift versus invariant currentness [5]
- Cache exclusion, separate refresh and non-waivable validator [6]
