# dashboard/src/data/terminalOpen.ts

| Field                  | Value                                  |
| ---------------------- | -------------------------------------- |
| repository             | agents-remember                        |
| path                   | `dashboard/src/data/terminalOpen.ts`   |
| doc_type               | `file-level-onboarding`                |
| lastUpdated            | 2026-07-18T15:22+02:00                 |
| lastVerifiedCommitHash | `d9a1eb82849baea6c0b86735e772a932f4bbdc7c`                                     |
| lastVerifiedCommitDate |                                        2026-08-12T00:45:15+02:00|
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

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant domain documentation was found for this file. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The result union and exact accepted-response identity checks. | "export type TerminalOpenResult =" | dashboard/src/data/terminalOpen.ts:41-41 |
| The sole POST plus network, body, HTTP, and harness-failure classification. | "export async function openTerminalSession" | dashboard/src/data/terminalOpen.ts:350-350 |
| The compatibility import surface re-exports this authority instead of owning a second opener. | "from \"./terminalOpen\"" | dashboard/src/data/terminal.ts:385-385 |
| The session store mutates and broadcasts only after `outcome: opened`. | "sessionStore.getState().upsert(result.session" | dashboard/src/data/sessions.ts:800-800 |
| Hosted launch delegates to this opener while preserving its established response grammar. | "export async function openHostedSession" | dashboard/src/data/launchFlow.ts:248-248 |
| Direct parser and caller regressions cover accepted identity and every failure family. | "POSTs raw metadata and accepts the exact server-owned row" | dashboard/src/data/terminal.test.ts:356-392 |

## Cross-Repo References

The module implements a repository-local browser/server contract and imports no adjacent-repository
authority.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-08-11T19:58+02:00 — Aligned the current data-contract card for `terminalOpen.ts` with task-document identity, qualified seat state, and terminal projections represented by this source.
- 2026-08-07T08:19Z — 260731-EFA-L8 curator: reviewed this sidecar against the frontend-rail change set (strict-target lint remediation: complexity, max-lines-per-function, react-hooks, jsx-a11y, and import-cycle fixes). No content impact: behavior-preserving refactor; the file's responsibilities and the claims in this card remain current. Verification metadata stays pinned until closeout stamps the code commit.
- 2026-08-03T02:57+02:00 — W3-B03 curator: curated 6 table citations for terminal-open result, route, store, hosted-session, and raw-metadata behavior; fixer-generated ranges verified.

- 2026-07-18T15:22+02:00 — Created for FEUI MX-FIX-2 after same-reviewer Round 2 PASS: recorded the
  sole discriminated opener, five failure classes, exact raw/harness response identity, server-row
  materialization authority, stable visible failure copy, and explicit dev-only HTTP simulation.
  Verification metadata remains blank until closeout creates and stamps the code commit.
