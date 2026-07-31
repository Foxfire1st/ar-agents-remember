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

To improve quality when working on source code, the agent shall use `Ruff`, `Pyright`, `Radon`, `pytest`, `pytest-cov`, and CRAP-Calculator. For the `agents-remember` repo, install and run them from the source repository directory `agents-remember/`.

The installation has to be done by activating the project's virtual environment (`source .venv/bin/activate` on Linux and macOS, or `.venv\Scripts\activate` on Windows) and installing the MCP package with development extras from the source repository root:

```text
python -m pip install -e "mcp[dev]"
```

After activation, prefer the fixed source quality wrapper for full local checks:

```text
python -m agents_remember.code_quality.check
```

The wrapper runs `ruff check`, Pyright static type checking, Radon cyclomatic complexity and maintainability checks, `pytest` with coverage JSON, and CRAP-Calculator. Use the individual tool commands below for focused implementation checks.
CRAP threshold enforcement is part of the default wrapper. Every function with
a score at or above the configured threshold (30 by default) makes the wrapper
exit non-zero; no additional threshold-enforcement flag is required.

For implementation work, focused commands are iteration aids, not the final
test standard. A code implementation is not closeout-ready until the full
quality wrapper has been run from the source repository root and its result has
been recorded in the task notes or final response. Do not substitute a
model-chosen subset of checks for the project-owned suite. If the wrapper
cannot run, record the exact blocker and run the closest explicit equivalent:
Ruff, Pyright, Radon CC/MI, pytest with coverage JSON, and CRAP-Calculator.
Those focused diagnostics do not satisfy or bypass the repository commit gate.

When reporting implementation results, use
[`code-quality-report-template.md`](code-quality-report-template.md) as the
standard reporting shape. Include the actual tool findings: Ruff output,
Pyright output, pytest counts, coverage summary, Radon CC/MI pressure, CRAP threshold rows,
which findings are in touched files, which are inherited/out of scope, and the
decision for each in-scope issue. Do not summarize quality as only "tests
passed" when the tools emitted complexity, coverage, or threshold findings.

### Commit-Gate Enforcement

Wherever the wrapper runs it runs in full: Ruff, Pyright, the whole pytest
suite, and CRAP all fail the run; CRAP scores at or above 30 fail unless the
repository intentionally configures another threshold.

The local hooks are **tiered** (260731-EFA-L1). Both `.githooks/pre-commit` and
`.githooks/pre-push` are thin wrappers over `.githooks/_gate.sh`, which takes
the tier as its argument:

- **Local pre-commit — `fast` tier.** Certifies the **staged content** (parked
  with `git stash push --keep-index --include-untracked` under restore traps)
  with the generated-copy checks, Ruff, and Pyright. About 20 seconds. It does
  **not** run the wrapper. The tier is cheap on purpose: `--no-verify` is
  all-or-nothing, so a pre-commit expensive enough to be worth skipping costs
  Ruff and Pyright too.
- **Local pre-push — `full` tier.** Certifies the working tree with the
  generated-copy checks plus the whole wrapper, and blocks the push.
- **Workflow closeout** — `worktree_closeout_apply` runs the wrapper before
  creating a code commit and before any code, memory, ledger, contract, or
  applied-gate mutation, even when Git hooks are not configured. This applies to
  **any** repository whose checkout carries the wrapper, not only
  `agents-remember`; a checkout without it is reported as `wrapper-unavailable`
  in the closeout payload, which states that the commit was not quality-checked.
- **CI** — `.github/workflows/quality-checks.yml` runs the wrapper on **every
  branch push and every pull request** across a Python `3.11 / 3.12 / 3.13`
  matrix, alongside the `Dashboard frontend rail`. The branch ruleset on `main`
  requires all four. This is the non-bypassable backstop.
- **Release** — `.github/workflows/publish-mcp-to-pypi.yml` calls
  `quality-checks.yml` through `workflow_call` and declares `needs: [quality]`,
  so a tag pointing at a commit that never reached `main` is re-gated before
  anything is built or published.

Keep every gate calling the project-owned wrapper, not a hand-picked subset.
Enabling the local hooks (`./setup-hooks.sh`), the PR-gated landing flow, and
the release/tag/publish flow live in [`git-workflow.md`](git-workflow.md).

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

Pyright performs static type checking. It catches mismatches between typed public contracts and the values passed through controllers, adapters, tests, and response builders before runtime.

Common commands:

```text
python -m pyright --project .                              # Type-check the configured project scope.
python -m pyright --project . mcp/src/agents_remember      # Type-check package source paths.
python -m pyright --project . mcp/src/agents_remember/models mcp/tests/test_code_quality_check.py
```

Pyright is part of the full quality wrapper and should not be scoped out of that wrapper. If the whole-repo baseline reports inherited errors, record the exact count and representative files, then fix in-scope errors in touched files before closeout.

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

Pytest runs the existing `unittest` tests and provides better test selection, failure output, fixtures, and coverage integration for new tests.

Common commands:

```text
python -m pytest mcp/tests -q
python -m pytest mcp/tests/test_crap_calculator.py -q
python -m pytest mcp/tests --cov=mcp/src/agents_remember --cov-report=json:coverage.json --cov-report=term
```

Use focused pytest runs during implementation. Use coverage JSON when CRAP-Calculator needs risk scoring.

---

### CRAP-Calculator

CRAP-Calculator combines Radon function-level cyclomatic complexity with Coverage.py JSON line coverage. It reports function-level CRAP scores and derives a per-file rollup from those function scores.

Recommended flow:

```text
python -m agents_remember.code_quality.check
python -m agents_remember.code_quality.check --coverage-json coverage.json
python -m agents_remember.code_quality.crap_calculator mcp/src/agents_remember --coverage-json coverage.json --project-root . --format json
```

Use CRAP-Calculator for refactor scouting. It is more useful than raw complexity alone because it highlights complex functions with weak test coverage.
The standalone calculator may be used for focused diagnosis, but the default
wrapper is the repository gate: any score at or above 30 fails it.
The plain wrapper command uses a temporary coverage JSON file. Use
`--coverage-json coverage.json` only when the JSON artifact should be reused by
the standalone CRAP-Calculator command.

---

### Quality Working Rules

- Run quality tools from the source repository root, not from the coordinator root.
- Scope checks to touched files or directories first. Use whole-repo checks when the task changes shared behavior, module layout, imports, or public contracts.
- Use the full quality wrapper before implementation closeout. Focused Ruff,
  Pyright, Radon, or pytest runs may prove local edits during development, but they do
  not replace the project-owned full suite for final validation.
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
- Record the full quality wrapper result and any focused Ruff/Radon/test
  commands in the final answer or task notes when code was changed.

---

### Refactoring And Onboarding Reuse

- Do not discard onboarding just because a source file was renamed, split, or moved.
- When a refactor preserves behavior, move or rename the matching onboarding content and update the path/hash metadata instead of deleting it and generating a blank replacement.
- When behavior changes while files are renamed, split, merged, or deleted, check whether existing behavior moved from one source location to another. Reuse the still-accurate fine print in the new target onboarding and update only the parts that changed.
- Treat onboarding deletion as the last option. It is appropriate only when the documented behavior is gone and no safe target remains for the preserved knowledge.
- During refactor closeout, make the source move and the onboarding move visible together so reviewers can see which behavior was preserved, which behavior changed, and which metadata was refreshed.

---

## Browser Tooling For Frontend Work

Frontend and dashboard work hinges on the agent having the right browser tool for the job.
This workstation is WSL2 **with WSLg** (`DISPLAY=:0`, Wayland active), a full Linux Google
Chrome at `/usr/bin/google-chrome`, and Playwright Chromium builds cached under
`~/.cache/ms-playwright`. Three distinct browser routes exist; they are not interchangeable.

### Route 1 — Playwright (default for agent-driven verification)

The agent's own browser. Use for dashboard verification, e2e flows, screenshots, console/network
inspection — anything where the agent must *drive and observe* a page. The dashboard repo already
carries Playwright configs (`dashboard/playwright*.config.ts`); the `playwright-cli` skill covers
ad-hoc driving outside the test suites. Headful runs render through WSLg as a visible window (with
the WSL border), so the developer can watch; headless works the same without the window.
Deterministic, scriptable, available to every spawned CLI seat — no setup required.

Two Playwright frontends are wired into the workspace and split by interaction shape:

- **`playwright-cli` skill** — scripted runs, screenshots, and the dashboard e2e suites. Full
  Playwright API via Bash; no standing context cost.
- **Playwright MCP (`@playwright/mcp`)** — long, exploratory sessions with many small
  interactive steps (click → look → click). One persistent browser session across the whole
  conversation, typed tools, accessibility-tree snapshots. Registered for both harnesses via
  `.codex/mcp-playwright.sh` (referenced from `Projects/.mcp.json` for Claude and
  `.codex/config.toml` for Codex); artifacts land in `Projects/.playwright-mcp/`.

Rule: many small interactive steps → MCP; scripted runs and test suites → CLI skill.

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
