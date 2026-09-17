# mcp/tests/test_parked_external_await_separation.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_parked_external_await_separation.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-10T10:06:31+02:00 |
| lastVerifiedCommitHash | `420669c459aab3650cdaa5b3e5271e71d7d94c0e` |
| lastVerifiedCommitDate | 2026-09-17T10:54:08+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp tests overview](overview.md)

## Purpose

Separation guards keeping the parked open-turn external-await design out of the ended-turn completion
relay. The module asserts that the parked `waiting` expectation kind stays unparseable and that no
wait-registration tool or wait/recheck/check-descriptor machinery ships in the runtime package. It
adds no production behavior: it is a regression fence over an existing separation, not relay
behavior evidence.

## Code Commentary

### Logic

`test_parked_waiting_expectation_kind_is_not_accepted` proves the parked kind is absent from
`get_args(ExpectationKind)` and from `KNOWN_EXPECTATION_KINDS`, and that
`ExpectationRow.model_validate` raises `ValidationError` for a well-formed row payload carrying
`kind="waiting"`. No parked wait row can therefore enter the relay as a completion fallback.

`test_shipped_runtime_exposes_no_parked_await_mechanism` proves `register_wait` is not advertised in
`PUBLIC_TOOLS`, then scans every shipped `.py` under the package root for the parked identifiers
held by `PARKED_MECHANISM_IDENTIFIERS` (`register_wait`, `external_await`, `resurface_by`,
`recheck_cadence`/`recheckCadenceSeconds`, `check_descriptor`/`CheckDescriptor`,
`last_checked_at`/`lastCheckedAt`, `last_exit_class`/`lastExitClass`, `waiting expectation`) and
requires the offender list to be empty.

### Conventions

- The scan names exact parked identifiers rather than generic vocabulary; "wait" and "script" are
  deliberately excluded because they occur legitimately across the relay and the wider runtime.
- The scan boundary is the shipped package root only, so `mcp/tests` itself is outside it.
- Assertions and docstrings state the technical boundary only; they carry no task, leaf,
  requirement, or report identifier.

### Invariants And Boundaries

- The relay's trigger stays canonical terminal truth after a subordinate provider turn ends; the
  parked open-turn external-await design remains a separate, parked decision space.
- A green run proves the parked mechanism is absent today. It does not authorize adopting that
  design, and it does not make the absence itself a relay behavior guarantee.
- An open-turn external-condition capability requires its own requirement and approval gate; this
  card records separation, not a permanent prohibition on any future approved capability.

### Todos

No additional implementation scope is opened by this memory reconciliation.

## Docs References

No external Domain Documentation source is configured; the separation obligation is repository-owned
and its evidence is the cited source.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured external domain source governs this guard. | N/A | N/A |

## Repo-Internal References

The guard module and the relay-side owners it protects are the load-bearing same-repository evidence.
These ranges record current source, not a recorded test execution.

| Finding | Anchor | Source |
| --- | --- | --- |
| The guard fixes the exact parked identifiers whose presence would mean the parked design was adopted. | `PARKED_MECHANISM_IDENTIFIERS` | mcp/tests/test_parked_external_await_separation.py:34-47 |
| The parked `waiting` kind is absent from the expectation model and cannot be validated into a row. | `test_parked_waiting_expectation_kind_is_not_accepted` | mcp/tests/test_parked_external_await_separation.py:64-70 |
| No wait-registration tool is advertised and no wait/recheck/check-descriptor machinery ships. | `test_shipped_runtime_exposes_no_parked_await_mechanism` | mcp/tests/test_parked_external_await_separation.py:72-82 |
| The relay's expectation kind is the Literal that must not gain a parked value. | `ExpectationKind` | mcp/src/agents_remember/controlplane/expectation_rows.py:47-47 |
| The parked row payload is rejected at model validation, not merely omitted from a set. | `ExpectationRow` | mcp/src/agents_remember/controlplane/expectation_rows.py:49-55 |
| The dispatch-surface kind set is the second definition the guard requires to stay parked-free. | `KNOWN_EXPECTATION_KINDS` | mcp/src/agents_remember/kernel/_agentic_settings_core.py:127-127 |
| The advertised public capability set is what the no-wait-registration assertion inspects. | `PUBLIC_TOOLS` | mcp/src/agents_remember/models/tools/public_roster.py:22-85 |

## Cross-Repo References

The parked design lives in another task tree; this card asserts only that the runtime package carries
none of its mechanism. No live external system or sibling repository is read here.

| Finding | Anchor | Source |
| --- | --- | --- |
| No separate cross-repository authority is established by this guard. | N/A | N/A |

## Update History
- 2026-09-17T06:49:47+00:00: Generated citation repair: `ExpectationKind` repointed to mcp/src/agents_remember/controlplane/expectation_rows.py:47-47. No content impact: mechanical anchor-range projection bound to citation source snapshot 3fa9290dfd218ae31f16951129eb57f6acdf1a92ecb95026b64d55227e9f1ad6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T06:49:47+00:00: Generated citation repair: `KNOWN_EXPECTATION_KINDS` repointed to mcp/src/agents_remember/kernel/_agentic_settings_core.py:127-127. No content impact: mechanical anchor-range projection bound to citation source snapshot 3fa9290dfd218ae31f16951129eb57f6acdf1a92ecb95026b64d55227e9f1ad6; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-10T10:06:31+02:00 — 260831-LOCR-L25 curator: created this card for the new separation-guard module delivered by the leaf's candidate (base `6096941f41204c9a7d6ccb2b29f6b2e862ed56b4`). It records the parked-mechanism absence boundary and the exact current source ranges without claiming execution, acceptance, or a future commit stamp; verification metadata remains closeout-owned.
