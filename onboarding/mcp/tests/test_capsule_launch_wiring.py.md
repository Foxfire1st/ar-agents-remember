# mcp/tests/test_capsule_launch_wiring.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_capsule_launch_wiring.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-17T09:15+02:00 |
| lastVerifiedCommitHash | `7879f5b22c34a912f939e27868786818463c3b9c` |
| lastVerifiedCommitDate | 2026-09-19T20:18:09+02:00|
| reviewedWorkingCandidate | `ar/260915-caps-l11-ar` uncommitted source; base `a29a20c6eefea424a7e0321a54fcda2ed1b35098` |
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

**The acceptance test nobody had: the compiled capsule read out of a started session's own first
prompt.** The master built and individually proved every link of the capsule chain — the compiler (L2),
the admission/MCP surface (L4), the Codex instruction seam (L5), the eve carrier (L7) — and left the top
severed: **no production launch point supplied a capsule to a session**. Every green test hand-supplied
the intermediate value, which is exactly why no leaf's suite could see the gap. This module closes it in
the shape the master's standing rule requires (`notes/leaf-runbook.md`): a production path from producer
to consumer, with the artifact read from the **consumer's own side**.

`260915-CAPS-L15` added it — 14 cases and one lane row.

## Code Commentary

### Logic

**The acceptance pair (the reason the module exists).** Both cases drive a **production launch point**,
parse the runner argv token the launch point actually built back out of the base64 the child process
would exec, run the **real** runner preparation and the **real** adapter factory, and read the capsule
out of the `thread/start` request the session sent to the vendor boundary. The expected side is the
**compiler's own result** for the same seat, never a hand-built literal.

| Case | Launch point | Seat |
| --- | --- | --- |
| `test_a_task_attached_seat_reads_its_compiled_capsule_out_of_its_own_first_prompt` | the internal spawn primitive `dispatch_agent` calls | a leaf document + role `worker` |
| `test_a_free_agent_reads_its_compiled_capsule_out_of_its_own_first_prompt` | `POST /api/terminal/{session}`, the dashboard opener | role `bootstrap`, **no** task document |

**The production-chain pair (added in fix round 1, replacing a hand-supplied case).**
`test_a_production_eve_launch_runs_where_its_capsule_admits_and_the_consumer_accepts` takes the
**route's own** `TerminalSessionSpec` (cwd **and** env), asserts the cwd is the admitted worktree and
`AR_WORKSPACE_ROOT` equals it, then feeds exactly those captured values to `parse_runner_config` →
`_prepare_controlled_launch` → `launch_spec_binding` → `verify_capsule_binding` and requires a non-`None`
binding. `test_the_spawn_launch_agrees_with_its_capsule_about_the_workspace` exercises the runner's own
agreement check on the spawn side.

**Why the hand-supplied case was deleted rather than kept beside them.** Its value under test (the
launch workspace) was supplied by the test, which is precisely the evidence class the sealed finding
`L15R-2` was about — a green case that could not have failed if the wiring were absent. Keeping it would
have left a passing case measuring nothing. The two environment preconditions the route case declares
(`AR_EVE_NODE` pointed at a version-reporting fixture, plus a taught `orchestration.harnesses` row with a
program on PATH) are **disclosed in the case's own docstring** as documented operator surfaces, and the
values under test are not among them.

**The surrounding pins.** The rest of the module holds the parts that must stay true around the
delivery:

- `test_an_uncapsulable_role_refuses_by_name_before_any_host_effect` — HTTP 400 `capsule-unavailable`
  with the role named, and `host.ensured == []`.
- `test_the_mode_gate_names_capsule_legacy_and_refused_for_every_seat_class` — the one decision point,
  for every seat class.
- `test_the_legacy_launch_payload_is_byte_identical_to_the_pre_capsule_payload` — behaviour 6, measured
  as bytes rather than asserted as shape.
- `test_the_delivered_payload_carries_the_capsule_once_and_no_task_context` — the single-carrier bound
  (`D12`): exactly one `trustedInstructions` key, and the task context never enters argv. **L11 extends
  it with the argv bound itself**: the token the spawn actually receives is asserted
  `<= ARGV_TOKEN_BOUND_BYTES < MAX_ARGV_TOKEN_BYTES`, and a carrier padded past the kernel limit must
  be **refused by name** (measured size, bound, seat) with **no argv returned at all** — so no caller
  can spawn it. The seed is the failure the bound exists to catch rather than a value chosen to trip
  it.
- `test_every_production_launch_request_site_is_wired_or_declares_its_legacy_chain` — walks every
  `TerminalLaunchRequest(` construction in `mcp/src/agents_remember/**` with `ast` and fails naming the
  file, the line and the two admissible dispositions; it also fails when the **set** of sites changes,
  so a fourth launch point cannot appear without a decision.
- `test_the_declared_legacy_reopen_names_why_it_cannot_carry_a_capsule` — the one declared exclusion.
- The free agent's two cases: the named absence, and an identity that moves with the seat (a different
  workspace gives a different semantic digest).
- `test_the_registered_capsule_operation_resolves_a_repository_through_its_schema` (`D13`) —
  `{"contract_path","task_path","role"} ⊆ required` and `"contract_path" ∈ properties`, so the declared
  schema losing the field the resolution depends on fails it.
- `test_a_refused_stage_refuses_again_in_the_same_process` (`D20`) — a first refusing call followed by a
  second in the same process must refuse identically and by name, never pass.

**Falsifiability, measured by the builder and re-measured by the reviewer.** Eight seeds each break
their named case and none survives: the reconciliation removed (route and spawn), the selection not
following, the wiring removed at the spawn site, a fourth `TerminalLaunchRequest(` site, the mode gate
reverted, `D13`'s repository resolution reverted, `D20`'s fail-open restored, and the duplication seed.
Seed `S1`/`S3` (which mutate production modules in place) are also why the builder recorded the one red
run it saw: a suite reading a concurrently-seeded worktree reported the acceptance case failing with
`KeyError: 'developerInstructions'`. Re-run with nothing else touching the tree: **0 failed**, twice
observed. The lesson is in `E5` — never run the mutation probe against a tree a suite is reading.

The 52 skips in the full suite are the named environment guards (including L16's
`eve_runtime/node_modules` guard); no skip is presented as a pass.

### Conventions

- The two boundary doubles are module-local and deliberately thin: `RecordingTransport` records what the
  session sent to the vendor boundary; `_FakeHost` doubles the tmux process boundary so no real process
  is started.
- The lane row is `unit-regression` in `mcp/tests/test-evidence-lanes.toml` (D9's invariant — the
  fail-closed loader still names exactly the six historical D9 modules), and the module's three
  governed-artifact **consumer rows** are the reason `evidence-lifecycle.toml`'s byte pin was re-derived
  a third time at this leaf's tip (populations unchanged at 4 contracts / 51 artifacts).
- The expected side of every acceptance assertion is the compiler's own result; a hand-built literal is
  the defect class this module exists to prevent.

### Invariants And Boundaries

- **A production path from producer to consumer, read at the consumer's side.** A case that
  hand-supplies the value under test does not belong in this module; that is `L15R-2`'s evidence class
  and it was deleted.
- **The enumeration case is the guard against a silent fourth launch point.** A new
  `TerminalLaunchRequest(` construction must either carry `capsule=capsule` or declare
  `legacy_launch_capsule(...)` with a reason.
- **The legacy payload is pinned as bytes**, not as a key set, so an unconditional capsule key breaks
  the case rather than slipping through.
- **This module starts no real process and calls no vendor.** The vendor boundary is recorded, not
  executed; the live system-block read is `E8`'s evidence, not this module's.
- **A named skip is not a pass.** The environment guards report "skipped" with a reason; nothing here
  asserts over a skipped path.

### Todos

None. The module is a test population; its coverage limits are the leaf's declared ones rather than
technical debt here:

- **No case exercises a real vendor model turn** — the capsule's arrival at the consumer's own boundary
  is what is measured, and a real provider call is not part of any requirement.
- **A shipped-row eve seat through the dashboard route is not covered** because it is impossible today
  (the route does not set `session_backend`), which is defect-class and owned by **L17**; the route case
  therefore teaches a registry row, exactly as the leaf's disclosure says.

## Docs References

No Domain Documentation source is configured in the resolved source registry for this pass.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The acceptance case for a task-attached seat: the spawn primitive's own argv, the real runner and factory, and the capsule read from the session's own `thread/start`. | `test_a_task_attached_seat_reads_its_compiled_capsule_out_of_its_own_first_prompt` | mcp/tests/test_capsule_launch_wiring.py:486-530 |
| The acceptance case for a free agent with no task document, through the production dashboard route. | `test_a_free_agent_reads_its_compiled_capsule_out_of_its_own_first_prompt` | mcp/tests/test_capsule_launch_wiring.py:532-577 |
| The negative case: an un-compilable role refuses by name before any host effect. | `test_an_uncapsulable_role_refuses_by_name_before_any_host_effect` | mcp/tests/test_capsule_launch_wiring.py:579-615 |
| The one decision point, for every seat class. | `test_the_mode_gate_names_capsule_legacy_and_refused_for_every_seat_class` | mcp/tests/test_capsule_launch_wiring.py:617-659 |
| Behaviour 6 measured as bytes: the capsule-free payload is identical to the pre-capsule one. | `test_the_legacy_launch_payload_is_byte_identical_to_the_pre_capsule_payload` | mcp/tests/test_capsule_launch_wiring.py:661-712 |
| The single-carrier bound: exactly one `trustedInstructions` key, and no task context in argv. **L11 extends this case with D12's argv bound** — the delivered token is asserted under `ARGV_TOKEN_BOUND_BYTES` and a padded carrier is refused by name, with no argv returned. | `test_the_delivered_payload_carries_the_capsule_once_and_no_task_context`; `ARGV_TOKEN_BOUND_BYTES` | mcp/tests/test_capsule_launch_wiring.py:714-803 |
| The enumeration case: every production launch site is wired or declares its legacy chain, and the site set cannot change silently. | `test_every_production_launch_request_site_is_wired_or_declares_its_legacy_chain` | mcp/tests/test_capsule_launch_wiring.py:805-845 |
| The one declared legacy exclusion, named with its reason. | `test_the_declared_legacy_reopen_names_why_it_cannot_carry_a_capsule` | mcp/tests/test_capsule_launch_wiring.py:847-916 |
| The production-chain eve case: the route's own cwd and env, then the consumer's own gate, then the workspace agreement. | `test_a_production_eve_launch_runs_where_its_capsule_admits_and_the_consumer_accepts` | mcp/tests/test_capsule_launch_wiring.py:816-872 |
| The spawn side's agreement with its own capsule about the workspace. | `test_the_spawn_launch_agrees_with_its_capsule_about_the_workspace` | mcp/tests/test_capsule_launch_wiring.py:874-918 |
| D13: the registered MCP operation resolves a repository through its declared schema, and a schema losing the field fails the case. | `test_the_registered_capsule_operation_resolves_a_repository_through_its_schema` | mcp/tests/test_capsule_launch_wiring.py:1020-1070 |
| The free agent's named absence, and the identity that moves with the seat. | `test_the_free_agent_admission_names_its_absent_task_plane`; `test_the_free_agent_capsule_identity_moves_with_the_seat` | mcp/tests/test_capsule_launch_wiring.py:964-988; mcp/tests/test_capsule_launch_wiring.py:990-1018 |
| D20: a refused stage refuses again in the same process, never passing. | `test_a_refused_stage_refuses_again_in_the_same_process` | mcp/tests/test_capsule_launch_wiring.py:1072-1104 |
| The two boundary doubles: the vendor-process recorder and the tmux host. | `RecordingTransport`; `_FakeHost` | mcp/tests/test_capsule_launch_wiring.py:133-277; mcp/tests/test_capsule_launch_wiring.py:279-478 |
| The lane row D9's fail-closed loader requires for every new test module. | "mcp/tests/test_capsule_launch_wiring.py" | mcp/tests/test-evidence-lanes.toml:22-22 |
| The three governed-artifact consumer rows this module added, which re-derived the catalog's byte pin at this leaf's tip without changing the populations. | `consumers` | mcp/tests/evidence-lifecycle.toml:38-38; mcp/tests/evidence-lifecycle.toml:58-58; mcp/tests/evidence-lifecycle.toml:77-77; mcp/tests/evidence-lifecycle.toml:88-88; mcp/tests/evidence-lifecycle.toml:92-92 |
| The pin is a byte contract at one tip and re-derives again for whoever changes the catalog last. | `LIFECYCLE_CATALOG_SHA256`; `LIFECYCLE_ARTIFACT_COUNT` | mcp/tests/test_dependency_ownership_ast_helpers.py:46-46; mcp/tests/test_dependency_ownership_ast_helpers.py:45-45 |
| The launch points this module drives, and the modules whose wiring it pins. | `spawn_agent_session_tool`; `_open_terminal_response`; `resolve_launch_capsule`; `compile_launch_capsule` | mcp/src/agents_remember/application/terminal_tools.py:822-931; mcp/src/agents_remember/serving/_app_terminal_routes.py:239-334; mcp/src/agents_remember/serving/launch_capsule.py:275-314; mcp/src/agents_remember/application/role_capsules/launch.py:273-295 |
| **Superseded evidence pointer, kept for the record** — `L15`'s round-1 production-chain transcript no longer exists at this path (`citation_source_vanished`; the enclosing `notes/reports/` tree holds only the master's own artifacts, and L15's evidence directory was never carried into this memory repo). The **live** equivalent claimed by the module is `test_a_production_eve_launch_runs_where_its_capsule_admits_and_the_consumer_accepts` below, plus `test_the_spawn_launch_agrees_with_its_capsule_about_the_workspace`. Do not re-cite the deleted file. | `test_a_production_eve_launch_runs_where_its_capsule_admits_and_the_consumer_accepts` | mcp/tests/test_capsule_launch_wiring.py:860-916 |

## Cross-Repo References

The vendor boundary this module records is the installed Codex app-server's thread-open request shape;
the fixture it is pinned against lives in this repository.

| Finding | Anchor | Source |
| --- | --- | --- |
| The recorded vendor boundary is the thread-open request, and the capsule travels the instruction field it declares. | `developerInstructions` | mcp/src/agents_remember/serving/capsule_delivery.py:44-52 |

## Update History
- 2026-09-18T13:36:47+00:00: Generated citation repair: "mcp/tests/test_capsule_launch_wiring.py" repointed to mcp/tests/test-evidence-lanes.toml:23-23. No content impact: mechanical anchor-range projection bound to citation source snapshot 468e47519c1a75ea8349538fbc4903207afc60f299e5295d1631f1f15f11a5ef; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_capsule_launch_wiring.py" repointed to mcp/tests/test-evidence-lanes.toml:22-22. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T20:42:17+00:00: Generated citation repair: "mcp/tests/test_capsule_launch_wiring.py" repointed to mcp/tests/test-evidence-lanes.toml:20-20. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-17T15:56+02:00 — 260915-CAPS-L11 curator (**final-verification leaf**): recorded the candidate's **D12 extension of the acceptance case** and re-anchored every range in this card against the working source. The delivered token is now asserted under `ARGV_TOKEN_BOUND_BYTES` (129024) with a padded carrier refused **by name and with no argv returned** — the bound checked where the encoded bytes first exist, so an over-bound launch is refused before any spawn rather than surfacing as an invisible `E2BIG`. Re-anchoring follows the candidate's insertion: the acceptance pair 483-526→**486-530** and 529-574→**532-577**; the pins 577-607→**579-615**, 615-657→**617-659**, 659-710→**661-712**, 712-759→**714-803**, 761-801→**805-845**, 803-814→**847-858**, 816-872→**860-916**, 874-918→**918-962**, 919-944/945-968→**964-988**/**990-1018**, 975-1022→**1020-1070**, 1028-1059→**1072-1104**, and the doubles 131-270/277-476→**133-277**/**279-478**. Three citations repaired beyond a range shift: the lane row pointed at `test-evidence-lanes.toml:19-19` (now **23-23**), the `consumers` rows pointed at lines that no longer hold the anchor (now **38-38 / 58-58 / 77-77**, the pin constant at `test_dependency_ownership_ast_helpers.py:46`), and the `L15 FIX ROUND 1 — E8` transcript is **`citation_source_vanished`** — that path does not exist in either tree, so the row was replaced with a pointer to the live case that now claims it and an explicit "do not re-cite the deleted file", rather than left asserting evidence a reader cannot open. The L15 curator's original entry below is preserved as the dated record it is.

- 2026-09-17T09:15+02:00 — 260915-CAPS-L15 curator: **created this card** (the census reported it
  missing, `integrity.missing_onboarding`). Records the module as the acceptance test the master lacked:
  a production path from producer to consumer with the artifact read out of each started session's own
  first prompt, for a task-attached seat and for a free agent; the production-chain pair added in fix
  round 1 and **why the hand-supplied case was deleted rather than kept beside them** (`L15R-2`'s
  evidence class — a case that could not have failed if the wiring were absent); the enumeration guard
  against a silent fourth launch point; the byte-level legacy payload pin; the single-carrier bound; the
  `D13` and `D20` pins; and the two coverage limits that belong to the leaf's disclosure rather than to
  this module (no real vendor turn; the shipped-row eve route case is `L17`'s). Verification metadata
  pins the leaf's base `15fa0e2c`; the candidate is deliberately uncommitted, so the governed closeout
  stamps the real code commit and no hash or fingerprint was invented here.
