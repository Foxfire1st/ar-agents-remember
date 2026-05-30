# Coding Tools & Repo Notes

---

## Code Discovery And Analysis

- Onboarding
- CGC
- Grepai

Note: `C-04-retrieval-strategy-router` documents the usage of these context retrieval tools.

---

## Code Quality

To improve quality when working on source code, the agent shall use `Ruff`, `Pyright`, `Radon`, `pytest`, `pytest-cov`, and CRAP-Calculator. For the `agents-remember-md` repo, install and run them from the source repository directory `agents-remember-md/`.

The installation has to be done by activating the project's virtual environment (`source .venv/bin/activate` on Linux and macOS, or `.venv\Scripts\activate` on Windows) and installing the MCP package with development extras from the source repository root:

```text
python -m pip install -e "mcp[dev]"
```

After activation, prefer the fixed source quality wrapper for full local checks:

```text
python -m agents_remember.code_quality.check
```

The wrapper runs `ruff check`, Pyright static type checking, Radon cyclomatic complexity and maintainability checks, `pytest` with coverage JSON, and CRAP-Calculator. Use the individual tool commands below for focused implementation checks.
CRAP threshold findings are report-only by default so existing refactor targets
do not make the remembered suite unusable. Add `--fail-on-crap-threshold` only
when intentionally gating a cleanup or refactor branch.

For implementation work, focused commands are iteration aids, not the final
test standard. A code implementation is not closeout-ready until the full
quality wrapper has been run from the source repository root and its result has
been recorded in the task notes or final response. Do not substitute a
model-chosen subset of checks for the project-owned suite. If the wrapper
cannot run, record the exact blocker and run the closest explicit equivalent:
Ruff, Pyright, Radon CC/MI, pytest with coverage JSON, and CRAP-Calculator.

When reporting implementation results, use
[`code-quality-report-template.md`](code-quality-report-template.md) as the
standard reporting shape. Include the actual tool findings: Ruff output,
Pyright output, pytest counts, coverage summary, Radon CC/MI pressure, CRAP threshold rows,
which findings are in touched files, which are inherited/out of scope, and the
decision for each in-scope issue. Do not summarize quality as only "tests
passed" when the tools emitted report-only findings.

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

## Release And Changelog Convention

This repo has no `CHANGELOG.md`. The release history and user-facing release
notes live in **GitHub Releases** — that is the canonical changelog, and it is
what the README's "read the release notes before upgrading" line points at. Do
not introduce a `CHANGELOG.md`; keep release notes as GitHub Releases.

### Tag scheme

- `mcp-vX.Y.Z` is the canonical release tag. Pushing it triggers
  [`publish-mcp-to-pypi.yml`](agents-remember-md/.github/workflows/publish-mcp-to-pypi.yml)
  (`on: push: tags: mcp-v*`), which builds the wheel/sdist and publishes
  `agents-remember-mcp` to PyPI. Attach the GitHub Release to this `mcp-vX.Y.Z`
  tag.
- A bare `vX.Y.Z` scheme exists only on the older `v0.9.0` Release. Do not start
  new releases on it; use `mcp-v*` going forward.

### Version bump locations (keep in sync)

A release bumps the version string in exactly four places; they must match:

1. `mcp/pyproject.toml` — `version`
2. `mcp/src/agents_remember/mcp/__init__.py` — `SERVER_VERSION`
3. `README.md` — the Status section line
4. `mcp/tests/test_tools.py` — the `payload["version"]` assertion in `test_ping_payload`

`SERVER_VERSION` and `pyproject` `version` must stay equal so installed server
payloads (`ping`, `server_info`) report the same version PyPI installs.

### Release commit subject

Use `Release MCP X.Y.Z: <one-line summary>` (version-first), matching the
existing release-commit history.

### End-to-end release flow

1. bump the four version locations, run the full quality wrapper, and close out
   the change (code, onboarding, ledger) per `C-12-closeout`
2. push the `mcp-vX.Y.Z` tag; confirm `publish-mcp-to-pypi.yml` succeeded and the
   version resolves on PyPI (note: PyPI's JSON metadata can show a release ~30s
   before the files are installable; `uv`/`uvx` may need `--refresh`)
3. create the GitHub Release on the `mcp-vX.Y.Z` tag (see format below)

The publish workflow does **not** create the GitHub Release; that step is
manual.

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

Create it with the web UI (repo → Releases → Draft a new release → choose the
`mcp-vX.Y.Z` tag) or the `gh` CLI; use `--draft` first to review before
publishing:

```text
gh release create mcp-vX.Y.Z --target main --title "<thematic title>" --notes-file <notes.md> --draft
```
