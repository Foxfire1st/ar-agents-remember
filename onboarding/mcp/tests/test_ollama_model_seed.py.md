# test_ollama_model_seed.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/tests/test_ollama_model_seed.py`      |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-01T00:00+02:00                     |
| lastVerifiedCommitHash | `f3115ce8603f83b7b5cbd82aa402f66ec1d8a29d`                |
| lastVerifiedCommitDate | 2026-07-31T19:28:50+02:00|
| governingOverview      | `../overview.md`                              |

## Governing Overview

[overview.md](../overview.md)

## Purpose

`test_ollama_model_seed.py` verifies the worktree Ollama model seeding path
that avoids a per-worktree network re-pull (~274 MB) by copying the model from
the already-running workspace Ollama via a local tar pipe. It protects: the
tar-pipe shell command shape, the no-source/same-container guard, the
successful-seed-skips-pull short-circuit, the failed-seed-falls-back-to-pull
fallback, and the no-source-pulls-without-seeding path.

## Code Commentary

### Logic

A `_embedder(seed_from=...)` helper builds a minimal embedder dict with
`containerName="ar-grepai-ollama-wt"` and `model="nomic-embed-text"`.

`SeedFromSourceTests` covers `_seed_ollama_model_from_source`:

- `test_returns_none_without_source`: `seed_from=None` → `None`.
- `test_returns_none_when_source_equals_target`: same container name → `None`.
- `test_streams_model_via_tar_pipe`: mocks `docker_command` and `run_command`,
  asserts the composed shell command is `sh -c "<docker> exec <source> tar -C
  /root/.ollama -cf - models | <docker> exec -i <target> tar -C /root/.ollama
  -xf -"`.

`EnsureModelTests` covers `docker_ensure_ollama_model`:

- `test_present_model_neither_seeds_nor_pulls`: model already present → `alreadyPresent=True`, `run_command` never called.
- `test_successful_seed_skips_pull`: seed succeeds, model becomes present after seed → `seededFrom` present, `pull` absent, `run_command` called once.
- `test_failed_seed_falls_back_to_pull`: seed fails (returncode=1), then pull succeeds → `pull` in result, `run_command` called twice.
- `test_no_source_pulls_without_seeding`: no `seedFromContainer` → `seedAttempt=None`, pull runs, `run_command` called once.

All tests use `unittest.mock` to patch module-level functions; no Docker or network access is needed.

### Conventions

Tests mock at the module level via `mock.patch.object(embedder_module, ...)`.
The `_seed_ollama_model_from_source` private helper is imported directly for
targeted unit coverage.

### Invariants And Boundaries

The tests protect: the tar-pipe direction (source → target, not target →
source); the `_seed_ollama_model_from_source` returns `None` not a failed dict
when no source is configured (callers skip the seed path entirely);
`docker_ensure_ollama_model` never calls pull when seed succeeds and the model
is subsequently listed.

## Docs References

No external documentation is needed for these standard-library unit tests.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The embedder module under test. | `_seed_ollama_model_from_source`, `docker_ensure_ollama_model` | mcp/src/agents_remember/providers/grepai/lifecycle/embedder.py:74-105; mcp/src/agents_remember/providers/grepai/lifecycle/embedder.py:108-134 |

## Cross-Repo References

No sibling repository evidence is needed for these tests.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-08-02T20:45:43+02:00 — L6 W2-B02 curator: anchored 1 repository-internal embedder reference for the seed and ensure-model paths; final scoped result 0 (checker-clean).

- 2026-07-31T16:35+02:00 — No content impact: the only change to
  `mcp/tests/test_ollama_model_seed.py` since the L2 base commit is the whole-tree `ruff format`
  pass in `00e8379`, which re-wrapped 3 line(s) with no token change whatsoever. Checked by
  parsing both revisions and comparing the abstract syntax trees (identical) and the comment
  tokens (identical), so no symbol, signature, default, decorator, control-flow branch, docstring,
  or assertion this card describes has moved, and every claim this card makes about its own source
  still holds.

- 2026-06-01T00:00+02:00 — Created onboarding for the new Ollama model seed tests.
