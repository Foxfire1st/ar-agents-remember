# mcp/src/agents_remember/mcp/registration/gates.py

| Field                  | Value                                                    |
| ---------------------- | -------------------------------------------------------- |
| repository             | agents-remember                                           |
| path                   | `mcp/src/agents_remember/mcp/registration/gates.py`       |
| doc_type               | `file-level-onboarding`                                   |
| lastUpdated            | 2026-07-31T15:31+02:00                                    |
| lastVerifiedCommitHash | `7c56c11d651972515723b4090b8174087eb5236f`                |
| lastVerifiedCommitDate | 2026-08-07T20:50:27+02:00|
| governingOverview      | `overview.md`                                             |

## Governing Overview

[registration route overview](overview.md)

## 260731-EFA-L8 Change

The tool-registration functions gained bare-`*` keyword-only signatures (the 19
PLR0917 fixes across `mcp/registration/*.py`); the rule stays enabled and call sites
already pass keywords. Registered tools are unchanged.

## Purpose

`register_gate_tools(server, config)` declares the three public gate tools: `lifecycle_gate`,
`gate_decide`, `gate_list`. The retired split helpers (`lifecycle_block`, `gate_create`,
`gate_wait`, `gate_response_wait`) are **not** registered; their payload builders remain
lower-level internals.

## Code Commentary

### Logic

`lifecycle_gate` is the single agent-facing gate junction: it creates the durable typed gate, blocks
the active lifecycle with the developer-facing ask, and waits for the developer decision or a
gate-specific response — all in one call. The body packs into `GateRaise(kind, anchor, request,
ask)`, where `anchor` is `GateAnchor(lifecycle_id, enclosure, repo_id)` and `request` is
`GateRequest(packet, required_decision, evidence_refs)` — the same three pieces the record layer
stores. `kind` is the dashboard junction (plan-approval, worktree-intent, closeout-approval, …);
`ask.kind` is the answer shape (decision, question, conflict).

The `wait` argument becomes `GateWait(block=wait, timeout_seconds=None)`. The explicit `None` is
load-bearing: a non-blocking raise has nothing to time out, so it must not inherit `GateWait`'s
blocking default. `wait=false` is reserved for delegated seam kinds (master-handover-approval under
a delegating policy; any other kind blocks) and additionally requires `enclosure=<master task name>`
— the address the integration enforcement matches the gate by. The call returns the gateId, the
raiser carries it in the handover packet, and the delegated decider resolves it by id via
`gate_decide(deciding_role=...)`.

**`gate_decide` is where an attribution decision is made in this layer, not forwarded from the
caller.** A plain decision sends `GateVerdict(by="model", via="cli")`; supplying `deciding_role`
switches `via` to `"orchestration"` and sends `by=""` for the server to fill from the active
lifecycle/session, after which the decision is checked against the configured gate policy. The
agent cannot self-attribute a developer decision because `by` is never taken from an argument.
Decisions are append-only — a new snapshot, never an overwrite — over `approve` | `reject` |
`request-revision` | `cancel`.

`gate_list(lifecycle_id=None)` defaults to the ACTIVE (ambient) lifecycle, so an agent can poll its
own raised gate without handling lifecycle ids; with no ambient lifecycle it lists the workspace
gates. Read-only.

### Invariants And Boundaries

- Never accept `decided_by` from the caller. The `by`/`via` pair is fixed here.
- `wait=false` must keep passing `timeout_seconds=None`.
- Gate creation, expiry of older open gates, policy checks and the wait loop live in
  `mcp/tools/gates.py`; the durable gate substrate lives in `controlplane/`.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| `GateRaise`, `GateWait`, and the create/block/wait junction. | `GateRaise`; `GateWait`; `lifecycle_gate_tool` | mcp/src/agents_remember/application/gate_tools.py:188-203; mcp/src/agents_remember/application/gate_tools.py:216-228; mcp/src/agents_remember/application/gate_tools.py:384-454 |
| `GateAnchor`, `GateRequest`, `GateVerdict`. | `GateAnchor`; `GateRequest`; `GateVerdict` | mcp/src/agents_remember/controlplane/records.py:128-136; mcp/src/agents_remember/controlplane/records.py:139-146; mcp/src/agents_remember/controlplane/records.py:149-163 |
| The configured delegation policy checked on a role-attributed decision. | `decision_role_for_gate` | mcp/src/agents_remember/controlplane/gate_policy.py:154-159 |
| Both attribution paths and the `wait=false` timeout proved through a live server. | `RegistrationWiringTests` | mcp/tests/test_mcp_registration_wiring.py:61-1307 |

## Update History
- 2026-08-07T08:19Z — 260731-EFA-L8 curator: recorded the bare-`*` keyword-only signature remediation (PLR0917). Verification metadata stays pinned until closeout stamps the code commit.

- 2026-08-02T16:44:03+02:00 — W1-B07 curator: repaired 4 repository-reference citations (4/4 anchored and sourced; scoped citation check clean).

- 2026-07-31T15:31+02:00 — 260731-EFA-L2 curator: created with the package. The three gate
  declarations moved out of `server.py`; `lifecycle_gate` now packs `GateRaise` + `GateWait` and
  `gate_decide` packs `GateVerdict`, keeping the fixed model/cli vs orchestration attribution in the
  declaration. Verification metadata pinned to the pre-change commit until closeout stamps the L2
  code commit.
