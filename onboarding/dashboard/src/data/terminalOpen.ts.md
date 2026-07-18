# dashboard/src/data/terminalOpen.ts

| Field                  | Value                                  |
| ---------------------- | -------------------------------------- |
| repository             | agents-remember                        |
| path                   | `dashboard/src/data/terminalOpen.ts`   |
| doc_type               | `file-level-onboarding`                |
| lastUpdated            | 2026-07-18T15:22+02:00                 |
| lastVerifiedCommitHash | `31f58834f86c0d98e26b0896e099a2403a8729ee`                                     |
| lastVerifiedCommitDate |                                        2026-07-18T15:41:39+02:00|
| governingOverview      | `overview.md`                          |

## Governing Overview

[data overview](overview.md)

## Purpose

This module is the sole browser-side authority for opening raw terminals and hosted harness
sessions. It owns the one `POST /api/terminal/{id}` transport, converts every response into a
discriminated `TerminalOpenResult`, validates the exact request/server identity, and exposes only
server-returned row facts to callers. A request is never enough to authorize a local running row.

## Code Commentary

### Logic

- `OpenTerminalOptions`, `OpenedTerminalSession`, and `TerminalOpenResult` separate caller proposals,
  accepted server facts, and five failure classes: `network`, `http`, `protocol`, `harness`, and
  `missing-response`.
- `openTerminalSession` sends the one browser open POST, reads the body once as text, distinguishes
  unreadable/empty/malformed bodies from non-OK responses, and retains response status/body evidence
  for callers that need the established hosted-launch outcome grammar.
- `classifyAcceptedOpen` requires a JSON object with the exact caller-minted session id, request kind,
  and harness identity. A raw-terminal response may omit or explicitly null `harness` and
  `controlState`; any non-null harness/control claim is a protocol contradiction, including an empty
  harness string.
- Only an accepted response with label and `status: "running"` produces `OpenedTerminalSession`.
  Lifecycle, leaf, seat-role, control, and resolved model/effort facts come from that response rather
  than from the request proposal.
- `terminalOpenFailureMessage` provides stable visible copy while preserving the structured failure
  class for tests and higher-level policy.

### Conventions

Protocol parsing happens before row construction. Success and failure remain a discriminated union;
callers branch on `outcome` instead of coercing transport state to boolean truthiness.

### Invariants And Boundaries

- There is one production browser opener. `data/terminal.ts` re-exports it, `data/sessions.ts` gates
  store mutation on it, and `data/launchFlow.ts` delegates hosted launch to it.
- Network, HTTP, protocol, harness, or missing-response failure authorizes no upsert, activation,
  focus, catalog broadcast, readiness wait, context delivery, or submit.
- The accepted server row/id is the only materialization identity. Exact id/kind/harness agreement
  prevents a response for one entity from creating another.
- Raw terminals cannot claim harness control. This is an authority/identity guard, not compatibility
  handling or a speculative fallback.
- Development scenarios simulate an accepted server response through the explicit `/dev/bench`
  fetch injector. Production never selects a local-success path, retry, poll, or reload fallback.

### Todos

No task-independent technical debt was identified during MX-FIX-2 review.

## Docs References

No Domain Documentation source is configured for this repository. The direct source, producer,
callers, and reviewed regression tests are the current evidence.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant domain documentation was found for this file. | Source discovery checked | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The result union and exact accepted-response identity checks. | L16-L54; L76-L199 | [terminalOpen.ts](terminalOpen.ts) |
| The sole POST plus network, body, HTTP, and harness-failure classification. | L201-L300 | [terminalOpen.ts](terminalOpen.ts) |
| The compatibility import surface re-exports this authority instead of owning a second opener. | L320-L337 | [terminal.ts](terminal.ts) |
| The session store mutates and broadcasts only after `outcome: opened`. | L598-L621 | [sessions.ts](sessions.ts) |
| Hosted launch delegates to this opener while preserving its established response grammar. | L189-L225 | [launchFlow.ts](launchFlow.ts) |
| Direct parser and caller regressions cover accepted identity and every failure family. | L343-L537 | [terminal.test.ts](terminal.test.ts) |

## Cross-Repo References

The module implements a repository-local browser/server contract and imports no adjacent-repository
authority.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No applicable cross-repository source was found. | Import and task-boundary review | — |

## Update History

- 2026-07-18T15:22+02:00 — Created for FEUI MX-FIX-2 after same-reviewer Round 2 PASS: recorded the
  sole discriminated opener, five failure classes, exact raw/harness response identity, server-row
  materialization authority, stable visible failure copy, and explicit dev-only HTTP simulation.
  Verification metadata remains blank until closeout creates and stamps the code commit.
