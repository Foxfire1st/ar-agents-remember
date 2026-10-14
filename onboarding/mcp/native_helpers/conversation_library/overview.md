# Locked Native Conversation Library Helper Overview

## Governing Overview

[`mcp/overview.md`](../../overview.md)

## What This Area Is

This route supplies the repository-owned, dependency-pinned process boundary for Claude and Pi native conversation-library access. A shared JSON-lines protocol validates requests, correlates responses, reports runtime/helper versions, contains raw handler errors, and supplies signing and paging primitives. Two helper entries execute handshake, list, read, and resolve-resume-target through the declared Claude SDK and Pi `SessionManager` dependencies.

The Claude entry also enumerates each session's native `subagents/` directory, carries agent children in list rows, marks enumeration with `agentsEnumerated`, and routes optional `agentId` reads to native agent transcripts.

## Hot Path Summary

Read `src/protocol.ts` for the `ar-conversation-library-helper/v1` request/handshake boundary, correlated serve loop, version probing, signing, and paging. Read `src/claude.ts` and `src/pi.ts` for the per-harness operations; the Claude entry also owns project-directory candidates, sub-agent enumeration, and agent transcript parsing. `src/protocol.test.ts` contains version-reporting, request-shape, and fixed-error privacy cases. Their presence is not evidence that they were executed. `package.json` and `package-lock.json` define the repository's dependency resolution intent.

## Construction

The helper is a private ESM package declaring Node 20 or newer. Its exact direct runtime pins are `@anthropic-ai/claude-agent-sdk@0.3.207` and `@earendil-works/pi-coding-agent@0.80.7`; the lockfile records transitive resolution. TypeScript checking uses strict, no-emit compilation with exact optional-property and unchecked-index safety enabled.

| Path | Role |
| --- | --- |
| `package.json` | Private helper identity, scripts, engine, and exact direct dependency pins. |
| `package-lock.json` | Deterministic repository-owned transitive resolution. |
| `tsconfig.json` | Strict no-emit TypeScript contract checks. |
| `src/protocol.ts` | Versioned JSONL contract, serve loop, version probing, signing, and paging primitives. |
| `src/claude.ts` | Locked Claude SDK 0.3.207 list/read/resolve entry plus the sub-agent enumeration and agent transcript reads over the native `subagents/` layout. |
| `src/pi.ts` | Locked Pi SessionManager 0.80.7 list/read/resolve entry. |
| `src/protocol.test.ts` | Helper handshake, shape, and privacy regressions. |

The Python host starts one short-lived helper process per operation, using `node --import tsx` with this package as its working directory. It sends a handshake and the operation in the same process, then checks response framing and correlation. Missing prerequisites, timeout, malformed responses, and process failure produce errors rather than an invented result.

The parser admits handshake, list, read, and resolve-resume-target requests. It bounds each request at 1 MiB, requires an object and the protocol version, validates operation-specific fields, rejects keys outside the operation's allow-list, and reconstructs the typed request. Text fields must be non-empty; page limits must be positive safe integers. `agentId` is optional on read and is rejected on other operations.

Each entry probes its CLI with `--version`, takes the first semver token, and observes the declared dependency's version through the ESM resolver. A successfully parsed handshake reports observed runtime/helper versions and returns `ready`; expected versions are informational, not comparison predicates. Probing or dependency observation can still fail before that result is constructed. The Python capability gate performs a live helper list call after preflight; successful list execution, rather than version equality or dependency presence alone, selects its supported result.

The serve loop ignores blank lines. Each nonblank line receives one response: parse failures return `invalid-request` with request id `unknown`, admitted requests retain their request id, and handler failures map to the four typed error names. Untagged failures receive fixed raw-detail-withheld copy. Tagged failures retain the error name but also receive fixed copy here, because the helper's error constructor sets `helperError` without setting the `detail` property inspected by the response mapper.

### Native list, read, and resume resolution

Claude lists sessions with the requested project directory and `includeWorktrees: false`; Pi lists through `SessionManager.list` with the requested scope. Both sort by recency, offset-page the observed rows, and return SHA-256 signatures derived from their observable identity/modification data.

Claude enumerates sub-agents before paging. Its list signature includes agent ids and transcript modification times; each row carries `agents`, and the response carries `agentsEnumerated: true`, including for an empty catalog. Project directories use `CLAUDE_CONFIG_DIR` or the user's `.claude` directory. The local slug function replaces non-alphanumerics with `-`; long slugs take the first 200 characters and append a base36 absolute Java-style hash of the original scope. A distinct realpath adds another project-directory candidate. The source describes this rule as SDK-replicated; this inspection verifies the local algorithm, not equivalence to installed SDK internals.

Enumeration uses the first candidate whose `subagents/` directory can be read. It recognizes `agent-<id>.jsonl`, records transcript modification time, and reads optional `agent-<id>.meta.json` fields. Unreadable metadata leaves the agent-id row intact. Invalid JSON or a null/non-object metadata value raises `helper-failed`; invalid optional fields are omitted. Directory-read failures advance to another candidate and can ultimately yield an empty agent list.

Ordinary Claude reads call `getSessionMessages`; agent reads open the native transcript under the candidate project directories. Agent transcript parsing skips blank lines and rejects invalid JSON, null/non-object records, or missing string `type`/`uuid` fields. Tagged parse failures propagate; file-read failures try another candidate. Absent or empty agent transcripts and absent, unreadable, or empty ordinary Claude conversations return `stale-identity`.

Pi finds the requested session id in a fresh scope list, opens the resulting session file, and reads `getBranch()`. A missing id or empty branch returns `stale-identity`; other SDK/open failures pass through the generic handler failure boundary. Neither entry calls append, branch-switch, or mutation APIs. This establishes the helper's read-only API usage, without independently proving dependency internals.

Both reads window the full native sequence by 1-based ordinal, return the full sequence's item count, and sign identity/count/tail information. Claude maps message or transcript records; Pi maps branch entries by native entry type.

Claude resume resolution looks up session information in the requested directory. Pi re-lists the scope, finds the session file, opens it, and returns its file and header-derived working directory. The removed Python ports no longer reject IDs or mint product resume targets. The retained Node handlers return their scope-bound session information only; Claude sub-agent transcripts have no native resume target. The standing resume intent requires identity re-proof, but expectedIdentityDigest is not compared by these TypeScript handlers. Native existence lookup is not a helper digest re-proof, and no deleted Python comparison or resume-orchestration guarantee is current.

## Invariants And Boundaries

Repository package and lock data remain the standing dependency authority. Cache, OpenSrc, global-module, `NODE_PATH`, and `npx` fallback discovery are forbidden by this overview's intent. The host selects the repository entry and package working directory, and the observer uses standard ESM resolution; those facts alone do not prove that ambient resolution is impossible in every installation.

Locked dependency presence must not promote a capability. The retained Node helper/protocol only declares its own read/normalization behavior; removed Python serving/conversation gates and open orchestration are not current integration owners. Observed versions remain informational evidence, not a live product capability.

The caller's authorized scope must not be widened to another checkout's history. Claude explicitly excludes worktrees from SDK listing. Sub-agent access uses the supplied scope's plain and realpath-derived project directories.

Unknown request fields and fields belonging to another operation cannot cross the parsed helper seam. Optional `agentId` preserves ordinary read callers' request shape; the Claude handler consumes it, while the Pi handler does not route agent transcripts.

The standing privacy intent is that raw process error detail never crosses the public boundary. Raw handler exception text and unsuccessful-process stderr are not public authority. The shared handler mapper supplies fixed copy for the errors constructed by these entries. This does not restore a deleted Python spawn-error boundary or certify external process/dependency behavior; only the retained Node mapper and actual handler usage support current helper claims.

Sub-agent identity remains evidence-bound. Unreadable metadata permits an agent-id-only row; malformed metadata fails closed. `agentsEnumerated` distinguishes an enumerating helper from one that supplies no enumeration marker over an empty catalog. It does not prove that every candidate directory was readable.

| Nearby Thing | Belongs Instead In |
| --- | --- |
| Removed normalized Python conversation/page/control DTOs | No current owner: serving/conversation is deleted; retained Node helper data is not a replacement product DTO/port. |
| Removed Python active-session/projector/library integration | No current owner; the retained Node helper does not restore these deleted routes. |
| npm cache, OpenSrc, global module, `NODE_PATH`, or `npx` resolution | Nowhere; these are explicitly forbidden. |

No neighboring workspace repository is read or updated by the inspected helper entries. Third-party dependency behavior is not established by package names alone.

## Maintenance Guidance

Read this overview, the package/lock cards, and the protocol card before changing helper selection or framing. The package declares `npm run typecheck` and `npm test`. The standing guidance also calls for Python foundation verification of topology and forbidden resolution strings, and installed-runtime verification on machines with the harnesses. Those are maintenance intentions, not execution or acceptance evidence from this inspection.

There is no child overview in the assigned route. The helper entries and shared protocol form one bounded package; keep that construction together rather than fragmenting the protocol boundary into a redundant `src/` overview. This describes architectural intent, not an accepted whole-corpus coherence result.

## Non-Operative Metadata

The following route, coverage, and historical verification metadata is preserved. It does not establish current lifecycle state, executed checks, installed capability, or acceptance. No lifecycle authority was supplied within the assigned evidence scope.

| Field | Value |
| --- | --- |
| sourceRoute | `mcp/native_helpers/conversation_library/` |
| onboardingRoute | `mcp/native_helpers/conversation_library/overview.md` |
| parentOverview | [`mcp/overview.md`](../../overview.md) |

### Load-Bearing Files

| File | Role | Why It Matters | Onboarding |
| --- | --- | --- | --- |
| `src/protocol.ts` | protocol/privacy/execution boundary | Establishes exact framing, versions, shape, raw-error containment, and the shared serve/probe/sign/page primitives. | covered |
| `src/claude.ts` | claude operations | Scope-exact SDK list/read/resolve with typed stale-identity posture, plus sub-agent enumeration and agent transcript reads over the native `subagents/` layout. | covered |
| `src/pi.ts` | pi operations | Read-only SessionManager list/branch-read/session-file resolution with typed stale-identity posture. | covered |
| `package.json` | dependency authority | Names the only allowed direct helper versions and verification commands. | covered |
| `package-lock.json` | resolution authority | Prevents ambient runtime dependency selection. | covered |
| `src/protocol.test.ts` | regression proof | Exercises exact versions, operation key sets, and hostile secret/path error examples. | covered |
| `tsconfig.json` | static contract | Makes strict no-emit checking part of the package gate. | covered |

### File-Level Onboarding Map

| Source File | Onboarding File | Status | Reason |
| --- | --- | --- | --- |
| `package.json` | [`package.json.md`](package.json.md) | covered | Direct version and script authority. |
| `package-lock.json` | [`package-lock.json.md`](package-lock.json.md) | covered | Deterministic transitive dependency authority. |
| `tsconfig.json` | [`tsconfig.json.md`](tsconfig.json.md) | covered | Strict compiler contract. |
| `src/protocol.ts` | [`src/protocol.ts.md`](src/protocol.ts.md) | covered | Versioned request/privacy boundary plus execution primitives. |
| `src/claude.ts` | [`src/claude.ts.md`](src/claude.ts.md) | covered | Locked Claude SDK operation entry. |
| `src/pi.ts` | [`src/pi.ts.md`](src/pi.ts.md) | covered | Locked Pi SessionManager operation entry. |
| `src/protocol.test.ts` | [`src/protocol.test.ts.md`](src/protocol.test.ts.md) | covered | Exact helper regression matrix. |

Historical verification statement, preserved without renewing its claim:

- Installed Pi 0.80.7 list/read/resolve passed through the production helper seam (the
  installed-runtime gate).

## Evidence

- The helper suite contains exact pin assertions, informational-version handshake cases, malformed/wrong-version and cross-operation request cases, and a hostile secret/path corpus; it does not contain a request-byte-bound case. [2]
- Package identity, engine, scripts, direct pins, lock root, and strict compiler configuration are declared locally. [4]
- Claude implements list, sub-agent directory candidates, metadata handling, transcript parsing, ordinal reads, and native session-info resolution. [5]
- Pi implements scope listing, session-id lookup, branch reads, typed missing/empty failures, record mapping, and file/header resolution. [6]

- The helper protocol declares exact helper pins, the 1 MiB bound, operation field validation, fixed handler-error copy, and shared serve/probe/sign/page primitives; handshake versions are informational and blank lines are skipped. [1]
