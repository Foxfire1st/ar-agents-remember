# mcp/src/agents_remember/mcp/tools/dispatch_brief.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | mcp/src/agents_remember/mcp/tools/dispatch_brief.py |
| doc_type | file-level-onboarding |
| lastUpdated | 2026-07-31T15:31+02:00 |
| lastVerifiedCommitHash | `f3115ce8603f83b7b5cbd82aa402f66ec1d8a29d`|
| lastVerifiedCommitDate | 2026-07-31T19:28:50+02:00|
| governingOverview | mcp/src/agents_remember/mcp/tools/overview.md |

## Governing Overview

Governing overview: mcp/src/agents_remember/mcp/tools/overview.md

## Purpose

The dispatch-brief half of the inbox path: the readiness gate a `dispatch-brief` must pass before a
durable row exists, and the assignment clocks that start once it does. Not a tool itself — it is
shared by `operator_inbox.py`.

## Code Commentary

### Logic

**`HostedDelivery`** (added 260731-EFA-L2) is the delivery bundle: `enabled` — the caller's request
to push into the recipient's live hosted session at all — plus the collaborators the push runs
through (`catalog`, `host`, `paster`, `readiness`, `gate`). Each collaborator is optional so
production takes the real one and tests inject a double. Two shared values name the two ordinary
cases: `HOSTED_DELIVERY` (deliver, real collaborators) and `NO_HOSTED_DELIVERY` (record the entry
durably and stop).

**`require_dispatch_target(config, *, message_kind, agent_id, delivery, host)`** returns the exact
ready target or refuses **before** the durable row is created. It is a no-op for any kind other than
`DISPATCH_BRIEF_KIND`. Otherwise it raises `ValueError` when there is no catalog, when `agent_id` is
absent or `delivery.enabled` is false, and — after running `delivery.readiness or _readiness` — when
the observed status is not `ready`, when there is no entry, or when the entry's id is not the exact
`agent_id` asked for. Exact-session and fail-closed: a brief is never queued against a session that
was not proved ready under its own id.

**`start_dispatch_expectations(config, entry, target)`** starts the assignment clocks from the one
durable row's `createdAt` and id: a `briefed-by` row always, plus a `turn-report-by` row when the
target carries a binding leaf key. `store.find_by_source(entry.id, kind=...)` makes it idempotent —
an already-started clock is skipped rather than duplicated. Each row is written as an
`Expectation(kind, source_id, subject=ExpectationSubject(agent_id, lifecycle_id, leaf_key,
seat_role), note)` alongside `row_id`, `now` and `sla_seconds` (260731-EFA-L2; the identity fields
used to be six separate keyword arguments on `write_expectation_row`).

`fulfill_dispatch_expectation` closes the `briefed-by` clock; `expectation_store` /
`expectation_sla_seconds` are the shared accessors the inbox module reuses.

### Invariants And Boundaries

- The readiness check must stay **before** the durable row. Refusing after the row exists would
  leave an undeliverable brief in the inbox.
- Identity is exact: `observed.entry.id != agent_id` is a refusal, not a near-match.
- Expectation writing is idempotent by `(source_id, kind)`.
- Delivery mechanics live in `serving/`; this module gates and clocks, it does not paste.

## Docs References

No relevant documentation was configured in the resolved source registry; repository source is the
direct evidence.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The inbox builders that pass `HostedDelivery` and call these helpers. | [operator_inbox.py](agents-remember/mcp/src/agents_remember/mcp/tools/operator_inbox.py) |
| `Expectation` / `ExpectationSubject` and `write_expectation_row`. | [controlplane/expectation_rows.py](agents-remember/mcp/src/agents_remember/controlplane/expectation_rows.py) |
| The readiness predicate the gate runs. | [serving/hosted_readiness.py](agents-remember/mcp/src/agents_remember/serving/hosted_readiness.py) |
| `DISPATCH_BRIEF_KIND`, `DispatchBriefGate`, `fulfill_briefed_expectation`. | [serving/dispatch_brief.py](agents-remember/mcp/src/agents_remember/serving/dispatch_brief.py) |

## Cross-Repo References

No meaningful cross-repo references.

## Update History

- 2026-07-31T15:31+02:00 — 260731-EFA-L2 curator: added `HostedDelivery` (+ `HOSTED_DELIVERY` /
  `NO_HOSTED_DELIVERY`), which `require_dispatch_target` now takes in place of the separate
  `deliver_to_hosted` / `catalog` / `readiness` arguments; expectation rows are now written as
  `Expectation` + `ExpectationSubject` values. Replaced the placeholder body (Purpose, Logic and
  References had been one repeated sentence) with the module's actual gate, clock and refusal
  behaviour, read from the current source. Verification metadata pinned until closeout stamps the L2
  code commit.

- 2026-07-12T14:20:00+02:00 — 260712-TRH-L4 curator refresh: final candidate onboarding; exact-session dispatch and serialized-writer/lock-free-reader concurrency recorded.
