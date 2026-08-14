# Coding Tools & Repo Notes

---

## Code Discovery And Analysis

- Onboarding
- CGC
- Grepai

Note: `C-04-retrieval-strategy-router` documents the usage of these context retrieval tools.

---

## Dependency Code Library

Instead of looking up library and dependency code online for this project, use `opensrc` in the shell:

### List cached sources

```text
opensrc list          # human-readable
opensrc list --json   # JSON output
```

### Fetch source code

```text
opensrc fetch zod                                         # npm-package
opensrc fetch pypi:requests crates:serde vercel/next.js   # PyPi
opensrc fetch https://github.com/anomalyco/opentui        # GitHub
```

### Cache Location

```text
~/.opensrc/repos/<host>/<owner>/<repo>/<version>/
```

---

## Code Quality

Agents Remember acceptance runs only through the pinned Dagger Ubuntu graph. Direct host `pytest`,
Vitest, Playwright, and `python -m agents_remember.code_quality.check` invocations must refuse; they
are neither diagnostics nor fallback evidence. Deterministic non-test host checks may be used for
fast feedback.

The lifecycle owns the two accepted invocations:

- leaf closeout: `dagger call quality ... --mode=targeted --diff-base=<recorded leaf base>` exactly
  once, before the leaf commit;
- master integration: `dagger call quality ... --mode=full --diff-base=<recorded super base>`
  exactly once, before integrating the master into super.

Leaf integration, series/master closeout, ordinary push, pull-request validation, tag, and publish
do not rerun acceptance. Use `dagger call quality --help` for the live source/bundle/base/mode/cap
argument contract; do not reconstruct omitted arguments from memory. The graph receives the exact
candidate plus a separate Git ancestry bundle and must not mount the live coordination root,
credentials, or container socket.

The targeted graph covers changed files, reverse-import closure, the derived test subset,
coverage/CRAP over changed production modules, changed-lines coverage, and the configured file-size
rail. The full graph covers the repository suite. A missing graph, missing mandatory diff base,
invalid Dagger attestation, absent self-owned wrapper, or non-zero result refuses with no host or
direct-Docker fallback. An explicit lifecycle memory cap is passed to the graph's inner wrapper;
otherwise the container runtime owns RAM and swap.

Every completed lifecycle acceptance run atomically replaces the enclosure's
`reports/test-results.md` and exports `clean-quality-results.json` as the authoritative result.
Content-addressed retry proof may be consumed only inside an attested Dagger run. An exact accepted
tree may reuse its pytest proof; source, configuration, selected-suite, runtime, environment, or
artifact drift forces the ordinary Dagger selection, and inconclusive coverage deltas fail closed
to the graph's full pytest selection. `AR_QUALITY_NO_RETRY=1` disables proof reuse inside Dagger.

When reporting implementation results, use
[`code-quality-report-template.md`](code-quality-report-template.md) as the
standard reporting shape. Include the actual tool findings: Ruff output,
Pyright output, pytest counts, coverage summary, Radon CC/MI pressure, CRAP threshold rows,
which findings are in touched files, which are inherited/out of scope, and the
decision for each in-scope issue. Do not summarize quality as only "tests
passed" when the tools emitted complexity, coverage, or threshold findings.

### Commit-Gate Enforcement

The local fast and targeted hook tiers run deterministic non-test checks only: generated-copy
checks, Ruff, formatting, Pyright, dashboard code generation, lint, and typecheck. The manual full
hook tier refuses and points to Dagger. Pull requests always run the deterministic non-test GitHub
check; ordinary branch pushes do not launch a duplicate workflow. The tag-only publish workflow
requires the tagged commit to be reachable from `origin/main`, then builds and publishes without
rerunning acceptance.

`worktree_closeout_apply` stages the exact leaf candidate and owns the single targeted Dagger run.
Leaf integration reuses its certified commit. `worktree_integrate` on a master owns the single full
Dagger run. The Agents Remember self repository treats removal of its acceptance wrapper as a
refusal, not `wrapper-unavailable`.

---

### Ruff

Ruff handles Python linting, import sorting, and formatting. The active rules are defined in `pyproject.toml`.

Common commands:

```text
python -m ruff check .              # Lint all Python files from the source repo root.
python -m ruff check --fix --diff . # Preview Ruff's safe automatic fixes without writing.
python -m ruff check --fix .        # Apply Ruff's safe automatic fixes after reviewing --diff.
python -m ruff format .             # Format all Python files from the source repo root.
python -m ruff format --diff .      # Preview formatting changes without writing.
python -m ruff check path/to/file.py
python -m ruff format path/to/file.py
```

Ruff only fixes issues it considers safe to fix automatically. Everything else requires a manual code change.

For more information on ruff usage use the official documentation: [Ruff Documentation](https://docs.astral.sh/ruff/) or check `context7` mcp if available for code examples and usage patterns.

---

### Pyright

Pyright performs static type checking. It catches mismatches between typed public contracts and the values passed through application entry points, adapters, tests, and response builders before runtime.

Common commands:

```text
python -m pyright --project .                              # Type-check the configured project scope.
python -m pyright --project . mcp/src/agents_remember      # Type-check package source paths.
python -m pyright --project . mcp/src/agents_remember/models mcp/tests/test_code_quality_check.py
```

Pyright is part of both Dagger acceptance modes and must not be scoped out of them. Deterministic
host Pyright remains permitted for fast feedback.

---

### Radon

Radon reports cyclomatic complexity and maintainability pressure for Python refactoring work. The project configuration lives in `pyproject.toml` under `[tool.radon]`.

Whole-repo commands:

```text
python -m radon cc . -s -a --total-average -n B --order SCORE
python -m radon mi . -s -n B
```

Scoped commands:

```text
python -m radon cc runtime/path/to/file.py -s -a --total-average -n B --order SCORE
python -m radon mi runtime/path/to/file.py -s -n B
```

For more information on radon usage use the official documentation: [Radon Documentation](https://radon.readthedocs.io/en/latest/) or check `context7` mcp if available for code examples and usage patterns.

---

### Pytest And Coverage

Pytest and Coverage.py execute only inside the nonce-attested Dagger graph. Direct host pytest
refuses before collection. Leaf closeout derives the targeted selection; master integration runs
the full selection. Do not hand-pick a host subset for diagnosis or acceptance.

---

### CRAP-Calculator

CRAP-Calculator combines Radon function-level cyclomatic complexity with Coverage.py JSON line coverage. It reports function-level CRAP scores and derives a per-file rollup from those function scores.

The Dagger graph runs CRAP-Calculator against the coverage artifact produced by its own pytest
selection. The repository threshold is enforced inside both acceptance modes; no host wrapper or
standalone calculator result can replace that gate. Exported CRAP rows may be inspected for
refactor scouting after the run.

---

### Quality Working Rules

- Run quality tools from the source repository root, not from the coordinator root.
- Use deterministic non-test host checks such as Ruff, formatting, Pyright, Radon, dashboard
  codegen, lint, and typecheck for implementation feedback. Do not run host test suites or the
  direct wrapper.
- Do not start an extra Dagger acceptance run during implementation. Leaf closeout owns targeted
  acceptance once; master integration owns full acceptance once. A failed boundary is repaired and
  retried through that same lifecycle operation.
- Before refactoring complex Python, capture a baseline with Ruff, Pyright, Radon, and the relevant tests. After the change, compare against that baseline.
- Do not fix unrelated Ruff or Radon findings during a narrow task unless the developer approves the cleanup scope.
- Before applying `ruff check --fix` or `ruff format`, run the corresponding `--diff` command first and inspect the proposed changes.
- Treat `Radon` as a map of risk, not a scoring game. Do not split code into tiny helpers just to lower complexity; split by responsibility and purpose.
- When touching a function above the repository complexity target, either reduce the complexity locally or tell the developer why the function should remain as-is for now.
- For Radon or CRAP-Calculator complexity findings in files touched by the current task, ignoring the finding is not an option. Report every in-scope violation with a concrete fix suggestion so the developer can approve that fix or give alternate direction.
- Preserve existing script/function contracts unless the developer explicitly approves a contract change.
- Prefer facade refactors: keep the current entrypoint stable, move the implementation behind it, and prove behavior with focused tests.
- If a change worsens complexity or maintainability in touched code, call that out explicitly and explain why it is acceptable or what follow-up is needed.
- Do not add defensive wrappers, fallbacks, or compatibility layers just to satisfy tools. Defensive code needs a concrete reason.
- Record the lifecycle-owned Dagger result and any deterministic Ruff/Pyright/Radon feedback in the
  final answer or task notes when code was changed.

---

### Refactoring And Onboarding Reuse

- Do not discard onboarding just because a source file was renamed, split, or moved.
- When a refactor preserves behavior, move or rename the matching onboarding content and update the path/hash metadata instead of deleting it and generating a blank replacement.
- When behavior changes while files are renamed, split, merged, or deleted, check whether existing behavior moved from one source location to another. Reuse the still-accurate fine print in the new target onboarding and update only the parts that changed.
- Treat onboarding deletion as the last option. It is appropriate only when the documented behavior is gone and no safe target remains for the preserved knowledge.
- During refactor closeout, make the source move and the onboarding move visible together so reviewers can see which behavior was preserved, which behavior changed, and which metadata was refreshed.

---

## Dashboard Checks

The host-side deterministic hook and PR check may run these from `dashboard/`:

```text
npm run lint         # eslint .
npm run typecheck    # tsc -b
```

Vitest, Playwright, coverage, and performance suites are test-capable and run only inside the
nonce-attested Dagger acceptance graph. Do not invoke `npx vitest`, `npx playwright`, `npm run
test*`, `npm run e2e`, or `npm run perf:cockpit` from a host seat. Leaf closeout and master
integration own the accepted Dagger invocations described above.

**Never type-check the dashboard with `tsc --noEmit`.** It exits 0 without checking
anything. `dashboard/tsconfig.json` is solution-style — `"files": []`, no `include`, and
three `references` (`tsconfig.app.json`, `tsconfig.node.json`, `tsconfig.driver.json`) —
and `--noEmit` does not follow project references, so it compiles an empty file list and
reports success. Only `tsc -b` (which `npm run typecheck` and `npm run build` both use)
walks the referenced projects.

This was measured, not inferred: a change that `tsc --noEmit` passed produced **11 errors**
under `tsc -b`. The vacuous form is the conventional one to reach for, which is exactly why
it is worth knowing here.

---

## Browser Tooling For Frontend Work

Frontend and dashboard work hinges on the agent having the right browser tool for the job.
This workstation is WSL2 **with WSLg** (`DISPLAY=:0`, Wayland active), a full Linux Google
Chrome at `/usr/bin/google-chrome`, and Playwright Chromium builds cached under
`~/.cache/ms-playwright`. Three distinct browser routes exist; they are not interchangeable.

### Route 1 — Playwright (agent-driven inspection, not repository tests)

The agent's own browser. Use for dashboard verification, e2e flows, screenshots, console/network
inspection — anything where the agent must *drive and observe* a page. Repository Playwright test
configs (`dashboard/playwright*.config.ts`) are Dagger-only; an interactive browser tool does not
authorize `playwright test` on the host. The `playwright-cli` skill covers ad-hoc driving outside
those suites. Headful runs render through WSLg as a visible window (with
the WSL border), so the developer can watch; headless works the same without the window.
Deterministic, scriptable, available to every spawned CLI seat — no setup required.

Two Playwright frontends are wired into the workspace and split by interaction shape:

- **`playwright-cli` skill** — ad-hoc scripted browser driving and screenshots. It is not the
  repository's test executor; the dashboard e2e suites remain Dagger-owned.
- **Playwright MCP (`@playwright/mcp`)** — long, exploratory sessions with many small
  interactive steps (click → look → click). One persistent browser session across the whole
  conversation, typed tools, accessibility-tree snapshots. Registered for both harnesses via
  `.codex/mcp-playwright.sh` (referenced from `Projects/.mcp.json` for Claude and
  `.codex/config.toml` for Codex); artifacts land in `Projects/.playwright-mcp/`.

Rule: many small interactive steps → MCP; ad-hoc scripted inspection → CLI skill; repository test
suites → lifecycle-owned Dagger only.

### Route 2 — Windows Chrome via WSL interop (show the developer something)

WSL can launch Windows binaries: `cmd.exe /c start <url>`, `wslview <url>`, or `xdg-open` (wslu)
pop a tab in the **Windows-side** Chrome. This is **one-way launch only** — there is no control
channel back, so the agent cannot click, type, read the console, or move the mouse in that tab.
Right tool for exactly one job: opening a URL for the human to look at.

### Route 3 — Claude in Chrome extension (not usable on this workstation)

The extension gives a Claude Code session bidirectional control of the developer's personal
browser (login state included). Auth-wise our seats qualify (subscription `/login`), but the
extension ↔ native-messaging-host ↔ CLI pairing cannot cross the WSL/Windows boundary — Chrome
integration is officially unsupported in WSL. A Linux Chrome inside WSL could in principle host
the whole stack on one side, but that is untested/unsupported; do not build workflows on it.

### Rule of thumb

- Agent must verify or interact with a page → **Playwright** (headful via WSLg when the developer wants to watch).
- Developer just needs to see a URL → **interop tab-launch** into Windows Chrome.
- Personal-browser state (logins) needed programmatically → not available on WSL; on native
  Windows/macOS/Linux the extension route or a Chrome DevTools MCP would cover it. Agent SDK /
  API-key sessions never get the extension — MCP (Playwright MCP, Chrome DevTools MCP) is the
  sanctioned programmatic route there.

---

## Release And Changelog Convention

Moved to [`git-workflow.md`](git-workflow.md): the `mcp-vX.Y.Z` tag scheme (→ PyPI publish), the four
version-bump locations that must stay in sync, the `Release MCP X.Y.Z: …` commit subject, the
PR-gated end-to-end release flow (land via PR, then tag the merged commit), and the GitHub Release
format. This repo keeps release notes in **GitHub Releases**, not a `CHANGELOG.md`.
