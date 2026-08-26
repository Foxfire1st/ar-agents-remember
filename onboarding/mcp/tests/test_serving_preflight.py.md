# mcp/tests/test_serving_preflight.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_serving_preflight.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T14:19+02:00 |
| lastVerifiedCommitHash | `ae8c47ce897b04380ebcb80f750d77ed4dc9f37d` |
| lastVerifiedCommitDate | 2026-08-26T08:10:26+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Forcing suite for the served-build preflight (`tasks/serving_preflight.py`, 260815-DAG-L15-R4):
the version-floor semantics, the two refusal legs (missing model fields; non-editable pre-floor
wheel), the editable/source-tree pass, and — from the gate-repair round — every branch of the real
`_is_editable_install` detection so the container-installed editable build cannot leave those
branches dark.

## Code Commentary

### Logic

`ServingFloorTests` pins the floor semantics (`_below_floor`): proven pre-floor releases
(`3.0.0rc7`, `2.9.0`) are below; the floor and newer (`3.0.0rc8`, `rc9`, `3.0.0`, `3.1.0`) are not;
dev/post/local builds and unparseable versions are **not provably stale** and pass (so CI editable
installs and dev builds are unaffected). The refusal legs are tested directly:
`require_serving_topology_schema` raises `TopologyServingBuildError` with upgrade guidance when
`TaskDocument.model_fields` lacks the topology fields (mocked empty) and when a mocked non-editable
dist reports `3.0.0rc7`; it passes with no installed distribution, with an editable install, and
with a real non-editable build at/above the floor.

`EditableInstallDetectionTests` (gate-repair, RAIL 2) drives the REAL `_is_editable_install` with a
`_FakeDist` stand-in over real temp filesystem shapes: egg-info inside the source root (containment
True), editable `direct_url.json` True, non-editable direct_url False, `dir_info`-not-a-dict
fallthrough, invalid JSON fallthrough, `read_text` OSError fallthrough, `__editable__*.pth` marker
True, None metadata dir, metadata path that is a file, `_path_is_within` True/False, and a real
non-editable pre-floor distribution reaching the version-floor raise through the real function.
Every branch of `_is_editable_install`, `_path_is_within`, `_below_floor`, `_installed_distribution`
(found + `PackageNotFoundError`), and the two `require_serving_topology_schema` refusal legs is
executed (RAIL 2/RAIL 3 coverage).

### Invariants And Boundaries

- The suite never runs the real installed distribution check against a live environment in a way
  that could pass for the wrong reason: the pre-floor wheel is always mocked/faked, never installed.
- The editable-detection tests use real temp filesystem shapes (no mocking of the function itself),
  so the source-tree egg-info containment behavior is proven, not assumed.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The floor and pass/refuse semantics under test. | `ServingFloorTests` | mcp/tests/test_serving_preflight.py:26-105 |
| The branch matrix over the real editable-detection and refusal legs. | `EditableInstallDetectionTests` | mcp/tests/test_serving_preflight.py:106-238 |
| The module under test. | `require_serving_topology_schema`; `_is_editable_install`; `_below_floor` | mcp/src/agents_remember/tasks/serving_preflight.py:58-103; mcp/src/agents_remember/tasks/serving_preflight.py:113-149; mcp/src/agents_remember/tasks/serving_preflight.py:207-218 |

## Cross-Repo References

No cross-repo boundary applies to this forcing suite.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## 260815-DAG Master Full-Gate Repair

`EditableInstallDetectionTests` gained `test_callable_read_text_is_invoked_with_the_metadata_filename`,
pinning that `_is_editable_install` invokes the injected `read_text` callable with the exact
metadata filename (`direct_url.json`). No other editable-detection branches changed.

## 260821-DAGQC-L2 Observable-Failure Matrix

The suite now forces distribution discovery, metadata iteration, path stat, direct-url read, and
version-read failures through the typed chained refusal boundary. It also proves one version
snapshot per check, the real editable-install adapter path, and that programmer errors outside the
declared environment failure families still escape.

## Update History

- 2026-08-26T10:44:52+02:00 — No content impact: the distribution-version case now uses the shared fake-distribution adapter; serving-preflight failure translation and one-snapshot behavior are unchanged.

- 2026-08-24T14:19+02:00 — 260821-DAGQC-L2: expanded serving-preflight coverage to the explicit read/stat/iteration/version boundary and single-snapshot semantics. Verification metadata remains pinned until architect-owned closeout.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: added the callable read_text
  filename-invocation regression to the editable-install detection branch matrix. Verified at
  code commit e5cb139f.

- 2026-08-20T21:30+02:00 — Created for 260815-DAG-L15-R4: the served-build preflight forcing suite
  (floor semantics, both refusal legs, editable/source pass), extended in the gate-repair round with
  the `EditableInstallDetectionTests` branch matrix over the real `_is_editable_install`.
  Verified at code commit de3a0fd9.
