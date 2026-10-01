# mcp/tests/test_parked_external_await_separation.py

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

## Evidence

### Docs References

No external Domain Documentation source is configured; the separation obligation is repository-owned
and its evidence is the cited source.

No configured external domain source governs this guard.

### Repo-Internal References

The guard module and the relay-side owners it protects are the load-bearing same-repository evidence.
These ranges record current source, not a recorded test execution.

- The guard fixes the exact parked identifiers whose presence would mean the parked design was adopted. [1]
- The parked `waiting` kind is absent from the expectation model and cannot be validated into a row. [2]
- No wait-registration tool is advertised and no wait/recheck/check-descriptor machinery ships. [3]
- The relay's expectation kind is the Literal that must not gain a parked value. [4]
- The parked row payload is rejected at model validation, not merely omitted from a set. [5]
- The dispatch-surface kind set is the second definition the guard requires to stay parked-free. [6]
- The advertised public capability set is what the no-wait-registration assertion inspects. [7]

### Cross-Repo References

The parked design lives in another task tree; this card asserts only that the runtime package carries
none of its mechanism. No live external system or sibling repository is read here.

No separate cross-repository authority is established by this guard.
