# Coding Tools & Repo Notes

---

## Code Discovery And Analysis

- Onboarding
- CGC
- Grepai

Note: `C-04-retrieval-strategy-router` documents the usage of these context retrieval tools.

---

## Code Quality

To improve quality when working on source code, the agent shall use `Ruff`, `Radon`, `pytest`, `pytest-cov`, and CRAP-Calculator. For the `agents-remember-md` repo, install and run them from the source repository directory `agents-remember-md/`.

The installation has to be done by activating the project's virtual environment (`source .venv/bin/activate` on Linux and macOS, or `.venv\Scripts\activate` on Windows) and installing the repository requirements from `requirements.txt`. After activation, prefer the fixed source quality wrapper for full local checks:

```text
python -m agents_remember.code_quality.check
```

The wrapper runs `ruff check`, Radon cyclomatic complexity and maintainability checks, `pytest` with coverage JSON, and CRAP-Calculator. Use the individual tool commands below for focused implementation checks.
CRAP threshold findings are report-only by default so existing refactor targets
do not make the remembered suite unusable. Add `--fail-on-crap-threshold` only
when intentionally gating a cleanup or refactor branch.

For implementation work, focused commands are iteration aids, not the final
test standard. A code implementation is not closeout-ready until the full
quality wrapper has been run from the source repository root and its result has
been recorded in the task notes or final response. Do not substitute a
model-chosen subset of checks for the project-owned suite. If the wrapper
cannot run, record the exact blocker and run the closest explicit equivalent:
Ruff, Radon CC/MI, pytest with coverage JSON, and CRAP-Calculator.

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
  Radon, or pytest runs may prove local edits during development, but they do
  not replace the project-owned full suite for final validation.
- Before refactoring complex Python, capture a baseline with Ruff, Radon, and the relevant tests. After the change, compare against that baseline.
- Do not fix unrelated Ruff or Radon findings during a narrow task unless the developer approves the cleanup scope.
- Before applying `ruff check --fix` or `ruff format`, run the corresponding `--diff` command first and inspect the proposed changes.
- Treat `Radon` as a map of risk, not a scoring game. Do not split code into tiny helpers just to lower complexity; split by responsibility and purpose.
- When touching a function above the repository complexity target, either reduce the complexity locally or tell the developer why the function should remain as-is for now.
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
