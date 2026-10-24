# mcp/tests/test_mik_r196_l188_preparation_order.py

## Governing Overview

[MCP tests overview](overview.md)

## Purpose

The cold first run crossing its own gate, and a refused one telling the whole truth (L188-B01, L188-B05,
L188-B06). Three operations are protected: the scaffold predicate is what the surviving runtime installer
actually creates in both delivery modes, so a genuinely absent configured root reaches the host stage; selection
and request binding are settled before any stage writes, an execution that already answers the request is not
prepared twice, and a cold preparation runs under the dispatch lock; and a failed stage carries every completed
stage, their paths and the host state it left behind through the refusal the start path answers with.

The installer, the authority writer and the product's host reader run for real. Only the provisioner and the
bridge reads are replaced at their owners, so no test touches a live host.

## Code Commentary

### Logic

- **The retained scaffold (L188-B01).** `test_the_installed_scaffold_is_what_the_cold_path_accepts` runs over the
  `legacy` and `capsule` modes: stage `scaffold` is `created` with the mode as its delivery, `docs/` and `tasks/`
  exist, no coordination-root `skills/` copy is made, and `AGENTS.md` exists only in legacy mode — the instruction
  target capsule mode withholds is not part of the predicate.
  `test_the_cold_path_crosses_the_scaffold_gate_to_the_host_stage` reads the four stages in order (`scaffold`,
  `host-authority`, `host`, `host-verify`), the authority stage's path as the MCP settings file, the written block's
  five keys, the recorded roots, a block the build loads back, and no user settings file (MIK-R137).
- **Convergence and reconciliation (L188-B05).** `test_a_same_request_retry_converges_without_rewriting_anything`
  repeats the preparation and reads `present`, `present`, `provisioned`, `running` with unchanged configuration
  bytes and the same recalled report. `test_an_existing_receipt_is_reconciled_without_a_second_preparation` and
  `test_preparation_is_skipped_only_for_an_existing_receipt` make the receipt the only reason to skip preparation.
  `test_a_request_with_a_binding_but_no_receipt_is_not_prepared_again` treats the message-binding file as proof the
  request prepared, so a stale queued retry reconciles instead of scaffolding a cold root twice.
- **Order before effect (L188-B05).** `test_an_invalid_document_reference_is_refused_before_any_effect` and
  `test_an_archived_request_id_is_refused_before_any_effect` answer 409 with no `docs/`, no `tasks/`, no
  `paseoRuntime` and no user settings file. `test_cold_preparation_runs_under_the_dispatch_lock` holds the lock
  with one thread and asserts a second start is refused as busy, with one preparation and one call recorded.
  `test_a_queued_same_request_refreshes_admission_before_preparing` shows the waiting request seeing the binding
  published while it waited, so the root is prepared once and both answers are identical.
- **A refused stage (L188-B06).** `test_a_provision_failure_carries_the_completed_stages_and_the_retained_daemon`
  names `host-provision-failed`, the completed stages, their paths, the retained daemon action, the provisioner
  change count and the same-request retry instruction, and recalls the failed report on the same context.
  `test_a_plugin_load_failure_carries_the_running_daemon` names `host-plugin-not-loaded` at `host-verify` with the
  loaded and installed digests. `test_an_unreadable_authority_file_is_a_named_host_authority_failure` keeps the
  file's bytes and names the scaffold that completed before it. `test_an_unknown_delivery_mode_is_an_install_refusal`
  refuses at `scaffold` and writes nothing. `test_the_root_configuration_refusal_is_kept_and_writes_nothing` keeps
  the upgrade-required detail and installs no partial root.

### Conventions

`_workspace_config` writes the MCP authority file of a workspace whose coordination root is absent;
`_stub_host` replaces `provision_for_install`, `bridge_call`, `read_loaded_stamp`, `installed_plugin_path` and
`tree_digest` with named answers, and `_select_mode` sets `AR_EXPERIMENT=role-capsules` or removes it. The `cold`
fixture is parameterised over the two modes and asserts the root is genuinely absent before the run.

### Invariants And Boundaries

- A cold run reaches the host stage only through the scaffold predicate the installer satisfies in its own mode.
- The MCP settings file is the host authority; the developer's user settings file never receives a block.
- A retry that already has a receipt or a binding never prepares the root a second time, and two cold starts never
  prepare side by side.
- A refused stage reports the stages it completed and the host state it left; no failure is reported as success.
- These cases prove preparation order on test-owned roots; they claim no live host, launch or acceptance.

## Evidence

- The installed scaffold satisfies the cold path's predicate in both delivery modes, with no skills copy.
- The cold path crosses the gate to the host stage and writes a block this build loads back as a usable host.
- A same-request retry converges with unchanged bytes, and only a receipt or a binding skips preparation.
- A refused document reference, an archived request id and an unknown mode all stop before any effect.
- A queued same request sees the published binding and prepares the root once.
- A provision, plugin-load or authority-read failure names its stage, carries the completed stages and reports the
  retained daemon state.
