# mcp/tests/test_harness_launch.py

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Harness-specific launch vocabulary and exact model identity.

## Code Commentary

### Logic

Pi accepts only the full provider-qualified catalog key. Effective launch refuses a different model. Applying native knobs preserves fixed argv/environment and rejects duplicate selector authority; a parameterized harness population carries the selected model and effort through each native vocabulary.

`_knob_values` is the extraction helper that defines what "carried into its own launch vocabulary"
means, and 260915-CAPS-L6 extended it to collect **`knobs.env`** beside `knobs.argv` and
`knobs.session_config.values()`. The reason is eve: its model and reasoning effort are compiled
application values with no argv vocabulary, so its selection rides the launch environment the adapter
composes (`eve_launch_knobs` returns `argv=()` with the model/effort in `env`). Without the env
carrier the parametrized case failed for `eve`; extending the helper was preferred over weakening the
assertion or excluding `eve` from the parametrization. The parametrization is over
`sorted(BUILTIN_PROTOCOL_HARNESSES)` — the registry `create_harness_protocol_adapter` itself consults
— so it now covers four harnesses.

### Conventions

This card describes the retained source at the leaf's uncommitted candidate over IAS `d3610903`.
Historical entries below record earlier test populations; they do not require restoring removed cases.
Source inspection is memory preparation and does not claim a test run or acceptance.

A carrier added to `LaunchKnobs` must be reflected in `_knob_values`, or the contract silently stops
covering that carrier for every harness at once.

### Invariants And Boundaries

Catalog identity owns selection; an ambiguous model suffix is not a substitute. These cases do not start vendor processes or prove every historical catalog-validation edge.

The population is a registry parametrization, not a list: adding a fifth harness to
`BUILTIN_PROTOCOL_HARNESSES` holds it to the contract without an edit here, and excluding one would
defeat the contract this file exists to assert. The test asserts the shared contract rather than any
harness's own flag spelling.

### Todos

No file-local implementation change is requested by this reconciliation.

## Evidence

### Docs References

No Domain Documentation entries are configured in this memory root. These are repository-owned fixture and assertion contracts; no external library behavior is inferred.

No configured domain evidence applies to the file-local claims above.

### Repo-Internal References

The retained source anchors below support the fixture roles and assertion boundaries described above. They identify current behavior, not a request to restore historical test counts or percentage targets.

- Pi requires the exact provider qualified catalog key. [1]
- Effective launch still refuses a genuinely different model. [2]
- Apply launch knobs preserves fixed argv and refuses duplicate authority. [3]
- Every harness carries a clean selection into its own launch vocabulary. [4]
- The extraction helper enumerates every carrier, including the launch environment added for eve. [5]
- eve is the environment-only harness whose addition forced the carrier extension. [6]
- The two environment names eve's selection rides on are module constants rather than inline strings, which is what makes the carrier assertable. [7]
- The registry the parametrization drives is the one the adapter factory consults. [8]

### Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

Fixture repositories and protocol doubles do not establish a live external integration.
