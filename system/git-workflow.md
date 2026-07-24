# Git Workflow — PR-Gated `main`

Repo-local landing doctrine for `agents-remember`. Read this **before** committing,
pushing, opening a PR, or cutting a release. PR-gating and the spear branch are per-repo;
the coordinator only routes "read `git-workflow.md` when present."

---

## Spine

- **Spear branch = `main`.** `main` is **PR-gated — never push to it directly.** Every change
  reaches `main` through a GitHub PR that passes checks and is merged.
- Work branches are cut from the spear: **`feat/<slug>`** (features) or **`fix/<slug>`** (fixes).
- **Everything is worktree-backed** (chat _and_ task) so external memory stays consistent: memory
  parks on the worktree memory branch and lands on `main` via **C-11 carryover** _after_ the code PR
  merges.

---

## When you need an issue + PR

| Change kind                                        | Issue?                                                | PR to `main`?                      |
| -------------------------------------------------- | ----------------------------------------------------- | ---------------------------------- |
| `feat` / `fix` / `chore`                           | **`gh issue create`** (after agent + developer agree) | yes                                |
| pure research (read-only, no source/memory change) | no                                                    | no — maps to L-01's read-only exit |

---

## The landing flow

A job changes the checkout via these steps:

1. **`gh issue create`** for `feat`/`fix`/`chore` (skip for pure research).
2. Cut **`feat/<slug>`** | **`fix/<slug>`** from the spear (`main`).
3. **C-09 worktree on that branch — chat & task both** (task adds `task.md`; chat doesn't).
4. Work in the worktree; **memory parks on the worktree memory branch.**
5. **Commit gate (human + quality).** Nothing is committed before explicit developer commit
   approval (`c-12-closeout` worktree preview first). After approval, closeout runs the default
   strict project wrapper before any code, memory, ledger, contract, or applied-gate mutation.
6. **Push gate (human — one question).** After commit approval, a single "push?" approval hands the
   tail to the agent. Merge is **no longer its own gate** — only timing.
7. Agent owns the tail: **push the branch → `gh pr create` (target `main`) → checks green →
   `gh pr merge --delete-branch`.**
8. **C-09 closeout** + worktree/provider cleanup.
9. **C-11 carryover** of the parked memory to main-memory, run against the merged `main`. Carryover
   maps the ledger to the actual `main` HEAD — **including the PR merge commit** even when nothing
   else needs carrying — so the next worktree bases off the merged `main` without a manual
   reconciliation. Always run it after the merge (even the linear case where memory already
   fast-forwarded: carryover adds the missing merge-commit ledger row).

### Gates, in one line

`commit approval (human)` → `push approval (human, one question)` → agent owns `push → PR → checks
→ merge → cleanup → carryover → memory-main push`.

---

## Orchestrated Series (Super Integration Branch)

For developer-requested `l-01-agent-lifecycles` orchestrated work, the landing topology is accumulative rather
than one work branch straight to `main`:

- The orchestrator creates a **super integration branch** from PR-gated `main`.
- Every **master integration branch** bases from the current super branch, not from `main`.
- Every **leaf work branch** bases from its owning master integration branch.
- **C-11 is the universal integration mechanic** at every edge: leaf -> master, master -> super, and
  super -> main. Every edge carries memory so the ledger maps the accumulated code commits.
- The orchestrator dispatches managers by dependency order. Dependent masters start only after their
  dependencies are integrated into super; independent masters may run in parallel, with reconcile
  absorbing a moved super base.
- A completed master is integrated into super from an **orchestrator integration worktree** sourced at
  super, mirroring the leaf -> master worktree flow.
- The landing tail remains PR-gated: open the final super -> main PR, merge remotely, run C-11
  carry-over to main-memory so the ledger maps the actual main merge commit, then push memory.

The full orchestration doctrine lives in
`skills/l-01-agent-lifecycles/SKILL.md` and `skills/l-01-agent-lifecycles/roles/orchestrator.md`.

---

## PR merge: prefer a merge commit over squash

- **Default: merge commit** (`gh pr merge --delete-branch`). It preserves the branch's distinct
  commits on `main` — important when a PR bundles several self-contained changes (each with its own
  onboarding + ledger mapping), so history stays bisectable and traceable.
- **Squash** (`--squash`) is for messy WIP branches full of "fix typo" commits where the individual
  history has no value. Do not squash a bundle of distinct features just to get a single line.
- Never `--rebase`-merge onto `main` in a way that rewrites already-pushed history.

---

## Commit and push quality gates

Every repository-owned quality gate runs the same default project wrapper.
Ruff, Pyright, the full pytest suite, and CRAP all fail the run; every CRAP
score at or above the configured threshold (30 by default) is mandatory failure.

- **Local pre-commit** — `.githooks/pre-commit` runs the wrapper before an
  ordinary local commit.
- **Workflow closeout** — `worktree_closeout_apply` runs the wrapper before its
  code commit and before any code, memory, ledger, contract, or applied-gate
  mutation, even when local hooks are not configured.
- **Local pre-push** — `.githooks/pre-push` repeats the same wrapper and blocks
  the push. **Enable the hooks once per clone** with `./setup-hooks.sh` (which
  sets `git config core.hooksPath .githooks` after `pip install -e "mcp[dev]"`);
  `git push --no-verify` bypasses the local push hook intentionally, not CI.
- **CI** — `.github/workflows/quality-checks.yml` runs on every push and PR to `main` across a
  Python `3.11 / 3.12 / 3.13` matrix. This is the non-bypassable backstop.

Keep every gate calling the project-owned wrapper, not a hand-picked subset. See
[`tools.md`](tools.md) for the quality wrapper itself.

---

## Release And Changelog Convention

This repo has **no `CHANGELOG.md`**. The release history and user-facing release notes live in
**GitHub Releases** — that is the canonical changelog, and what the README's "read the release notes
before upgrading" line points at. Do not introduce a `CHANGELOG.md`.

### Tag scheme

- **`mcp-vX.Y.Z`** is the canonical release tag. Pushing it triggers
  [`publish-mcp-to-pypi.yml`](agents-remember/.github/workflows/publish-mcp-to-pypi.yml)
  (`on: push: tags: mcp-v*`), which builds the wheel/sdist and publishes `agents-remember-mcp` to
  PyPI. Attach the GitHub Release to this `mcp-vX.Y.Z` tag.
- A bare `vX.Y.Z` scheme exists only on the older `v0.9.0` Release. Use `mcp-v*` going forward.

### Version bump locations (keep in sync)

A release bumps the version string in exactly three places; they must match:

1. `mcp/pyproject.toml` — `version`
2. `mcp/src/agents_remember/mcp/__init__.py` — `SERVER_VERSION` fallback
3. `README.md` — the Status section line

`SERVER_VERSION` and `pyproject` `version` must stay equal so installed server payloads (`ping`,
`server_info`) report the same version PyPI installs. `mcp/tests/test_tools.py::test_ping_payload`
asserts `payload["version"] == SERVER_VERSION` **dynamically** — it is not a bump location; it
validates the bump automatically (it must stay dynamic, never re-pinned to a literal).

### Release commit subject

Use `Release MCP X.Y.Z: <one-line summary>` (version-first), matching existing release-commit history.

### End-to-end release flow (PR-gated)

1. On a `feat/`|`fix/` branch in the worktree, bump the four version locations, run the full quality
   wrapper, and close out the change (code, onboarding, ledger) per `C-12-closeout`.
2. **Land it on `main` via PR** (the landing flow above) — `main` is PR-gated, so a release reaches
   `main` through the merged PR, not a direct push.
3. **Tag the merged commit:** push the `mcp-vX.Y.Z` tag pointing at the merge commit on `main`;
   confirm `publish-mcp-to-pypi.yml` succeeded and the version resolves on PyPI (PyPI's JSON metadata
   can show a release ~30s before the files are installable; `uv`/`uvx` may need `--refresh`).
4. Create the GitHub Release on the `mcp-vX.Y.Z` tag (format below). The publish workflow does **not**
   create the Release; that step is manual.

### GitHub Release format

House style observed across `v0.7.0`–`v0.9.0`:

- a **thematic title** that names the headline change, not a version-only title
  (e.g. "Worktree management & Git Versioned Memory")
- a Markdown body shaped as:

```markdown
## Agents Remember X.Y.Z

<1–2 sentence summary of the release theme>

### Highlights

- <bullet>
- <bullet>

### <Themed section, e.g. "Onboarding And Memory">

- <sub-bullets>
```

Create it with the web UI (repo → Releases → Draft a new release → choose the `mcp-vX.Y.Z` tag) or
the `gh` CLI; use `--draft` first to review before publishing:

```text
gh release create mcp-vX.Y.Z --target main --title "<thematic title>" --notes-file <notes.md> --draft
```
