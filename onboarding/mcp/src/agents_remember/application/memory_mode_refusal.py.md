# mcp/src/agents_remember/application/memory_mode_refusal.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/memory_mode_refusal.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T14:25+02:00 |
| lastVerifiedCommitHash | `ea9cf0abeab4fe88961bda10b4f54d30266a9634` |
| lastVerifiedCommitDate | 2026-09-17T23:56:19+02:00|
| reviewedWorkingCandidate | `ar/260915-caps-l12`; code candidate landed as `b281bcd68261866be306cc80a48241921b6dd0d2` |
| governingOverview | `../../../overview.md` |

## Governing Overview

[MCP package overview](../../../overview.md)

## Purpose

How a removed-memory-mode refusal is published **to the operator at a tool boundary**. The kernel
contract reader is the right place to decide that a document recording `internal` must not be read; it
is the wrong place to stop, because it sits several frames below the tool that answers the developer.
This module is the one reporter every such boundary uses, so the removal reads identically wherever it
surfaces and a new boundary cannot invent another spelling of it.

## Code Commentary

### Logic

The problem this module exists to solve is a type-hierarchy accident with an operational consequence.
`MemoryModeUnsupportedError` subclasses `ValueError`, and several tool boundaries read a contract inside
a broad `except (ContractError, OSError, UnicodeError, ValueError)` clause — because a document that is
not a contract at all is one of their *ordinary* outcomes. So without a typed clause ahead of the
generic one, a contract recording the removed mode reaches the operator as "unreadable or invalid":
true, useless, and missing the three facts that matter — which value is recorded, what is supported, and
how to get out.

The module publishes those facts in the two shapes the boundaries actually need.
`memory_mode_refusal_evidence` builds the removal facts inside the public failure-evidence `observed`
mapping, so they travel in the established evidence envelope rather than as a parallel payload shape;
it sets `observed.state` to `REMOVED_MODE_EVIDENCE_STATE` (`"removed-mode"`) as the marker that says
"this failure evidence is a removal refusal". `memory_mode_refusal_payload` returns the same facts as
top-level keys — `status`, `summary`, `detail`, `requested`, `supported`, `remedies`, `nextAction`
(`developer-decision`), `developerDecisionRequired`, `decisionSurface`, and `artifact` when one exists —
for a boundary that owns its whole payload.

`removed_memory_mode_fields_from_evidence` is the inverse direction, and it exists because one boundary
assembles the status payload while another projects it, so the projection sometimes holds the *evidence*
rather than the exception. It returns `None` when the mapping is not a removal refusal, which is what
makes it safe to call on any read failure. Its notable discipline: the `detail` text is **rebuilt** from
the vocabulary via `memory_mode_refusal_message` rather than carried inside the evidence, so the refusal
has exactly one source of truth and a hand-built evidence block cannot invent a different sentence. The
marker constant is written and read through the same name, so the two directions cannot drift apart.

Seven operator surfaces consume the reporter, each catching `MemoryModeUnsupportedError` **ahead of** its
generic clause: `worktree_status` (two sites), `configured_contract_admission` (two sites),
`direct_landing`, `task_unstarted_evidence`, and `worktrees/modules/start`. Each of the seven is
independently load-bearing for at least one published path — the fix-verification round falsified the
classification and the seventh surface by seeding them, and named failing cases caught both.

### Conventions

The module is `application`-rank rather than a kernel helper because it is a *presentation* concern: the
refusal is decided in the kernel, and how a tool boundary reports it belongs above the kernel. It
imports the vocabulary message from `kernel.memory_mode` and the typed error from `errors`, so it adds
no new vocabulary of its own — the only declaration here is the evidence-state marker.

Public names are listed in `__all__`, and the three functions answer different consumers rather than
being convenience aliases: evidence for the evidence envelope, payload for a boundary-owned payload,
and the inverse reconstruction for a projecting boundary.

### Invariants And Boundaries

**A removal refusal is never published as generic unreadability.** Every boundary that can meet one
catches the typed error before its broad clause; the operator receives `status =
memory-mode-unsupported` with the requested value, the supported set, the exact artifact and the
remedies.

**One text, one source.** The operator sentence is constructed only in
`memory_mode_refusal_message`. Neither this module nor any boundary spells it out inline, and the
evidence-reconstruction path rebuilds it rather than trusting a carried copy.

**The refusal never claims a different failure.** A removed-mode answer must not be reported as a lost
publication or as an unreadable document; that negative claim is asserted by its own case, because the
generic-clause bug's observable symptom was exactly that misreporting.

**Reporting only.** Nothing here writes, migrates or repairs state. The module turns an already-decided
refusal into operator-facing facts.

## Docs References

No Domain Documentation entries are configured in this memory root. These are repository-owned
transport-shape and evidence-envelope contracts, not external library behaviour.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain evidence applies to the file-local claims above. | N/A | N/A |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The reporter exists because the typed refusal subclasses `ValueError` and would otherwise be caught as generic unreadability. | `MemoryModeUnsupportedError` | mcp/src/agents_remember/errors.py:566-614 |
| The evidence-state marker distinguishes a removal refusal from any other read failure. | `REMOVED_MODE_EVIDENCE_STATE` | mcp/src/agents_remember/application/memory_mode_refusal.py:23-23 |
| The removal facts travel in the established public failure-evidence envelope. | `memory_mode_refusal_evidence` | mcp/src/agents_remember/application/memory_mode_refusal.py:27-41 |
| The same facts are available as a boundary-owned payload, with the artifact when one exists. | `memory_mode_refusal_payload` | mcp/src/agents_remember/application/memory_mode_refusal.py:44-63 |
| The inverse direction rebuilds the operator fields and returns `None` for a non-removal failure. | `removed_memory_mode_fields_from_evidence` | mcp/src/agents_remember/application/memory_mode_refusal.py:66-104 |
| The reconstruction rebuilds the refusal text from the vocabulary rather than trusting a carried copy. | `memory_mode_refusal_message` | mcp/src/agents_remember/kernel/memory_mode.py:78-86 |
| Surface 1 of 7 catches the typed refusal ahead of its generic clause. | `except MemoryModeUnsupportedError` | mcp/src/agents_remember/application/worktree_status.py:98 |
| Surface 2 publishes the refusal through the reporter rather than the generic failure path. | `memory_mode_refusal_evidence` | mcp/src/agents_remember/application/worktree_status.py:410-425 |
| Surfaces 3 and 4 classify a configured contract's removal on both admission paths. | `configured_contract_reread_refusal` | mcp/src/agents_remember/application/lifecycle/configured_contract_admission.py:374-388 |
| Surface 5 carries the refusal into the direct-landing answer. | "except MemoryModeUnsupportedError" | mcp/src/agents_remember/application/lifecycle/direct_landing.py:226-226 |
| Surface 6 reports the removal as its own fact in the unstarted-evidence answer. | "except MemoryModeUnsupportedError" | mcp/src/agents_remember/application/task_docs/task_unstarted_evidence.py:276-276 |
| Surface 7 keeps the worktree-start payload typed instead of falling through to the generic clause. | "except MemoryModeUnsupportedError" | mcp/src/agents_remember/worktrees/modules/start.py:151-151 |

## Cross-Repo References

No cross-repository implementation evidence is required for these local reporting-shape claims.

| Finding | Anchor | Source |
| --- | --- | --- |

## Update History


- 2026-09-16T14:25+02:00 — 260915-CAPS-L12 curator (closeout-gate follow-up): the two verification fields above, which this card's creation entry left un-advanced, were populated on the closeout gate's refusal — `external-memory closeout requires onboarding verification metadata before memory commit`. They follow the canonical file-level model (`file-level-onboarding-workflow.md` § Metadata Rules: "use the latest commit that touched the source file once the content has been verified") and now read hash `b281bcd68261866be306cc80a48241921b6dd0d2`, date `2026-09-16T14:24:58+02:00` — the `[260915-CAPS-L12]` code commit that actually contains this source file, matching the value closeout's own `refresh_onboarding_metadata_for_context` writes for every required card. An earlier revision of this entry named the pre-commit base `c1dbebf8`, which does not contain this file; that value was replaced rather than retained, and no earlier history entry was rewritten. The creation entry's sentence that no stamp was advanced is superseded here, added rather than edited because `Update History` is append-only. Closeout re-stamps both fields authoritatively at the real commit.
- 2026-09-16T14:05+02:00 — 260915-CAPS-L12 curator: **created the missing sidecar**. This module is the
  round-2 repair for `L12R-1`, which established that the typed refusal never reached the operator on
  four contract-report surfaces because it subclasses `ValueError`. Recorded the two publish shapes, the
  inverse reconstruction and its one-text discipline, the evidence-state marker, and the seven consuming
  boundaries with the typed clause ahead of each generic catch. Verification metadata remains
  closeout-owned: the source is uncommitted, so no stamp was advanced and no commit hash was invented.
