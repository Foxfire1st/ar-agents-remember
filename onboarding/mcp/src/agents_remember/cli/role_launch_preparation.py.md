# mcp/src/agents_remember/cli/role_launch_preparation.py

## Governing Overview

[overview](../../../overview.md)

## Purpose

Resolve launch defaults, workspace, scoped readers, instructions and handover before native creation.

## Code Commentary

`prepare_role_handover` accepts an optional `step_up` reason, selects defaults from current task, receipt, and decision facts, and validates the resulting provider, model, mode, and features against the host catalog (including the native Antigravity refusal) before workspace or enclosure creation. Ordinary roles without an alternative continue using their own choices.

`_role_defaults` delegates settings projection to `role_launch_defaults` while retaining the host role read. `_compile_handover` delegates instruction composition through `_compose_compact_instructions`, which resolves `durable_composition_corpus_root(cache_root=coordination_root / ".cache" / "skill-corpus")`, calls `compose_launch_instructions(..., compact_links=True, corpus_root=durable_root)` to freeze detail bytes under symlink-confined `<stem>.details/<source_path>` and compose user append/`<overwrite>` notes, and emits JSON-quoted `Link roots: skill="..."` (plus `, detail="..."` via `nested_detail_root` when `detailReferences` is non-empty). `_assembled_brief` compacts `capsule.shared_block` with `compact_skill_uri_links` and passes `BriefParts` (including `link_roots`) to `role_brief_message.brief_prompt`.

Canonical task JSON and rendered copy metadata (`_prepare_task_document_files`, `_task_document_copy_lists`), `missingCopies` disclosure, request-scoped report/scratch custody (`_prepare_role_folders`), exact parent and `leafSeats` peer routing, taskless scope, and grant-aware revival remain separate contracts. A leaf of a master that no sprint commands gets `leafSeats` peer arguments and a manager return address without a `sprint_document_ref`; `sprint_document_ref` appears only when the selection has a sprint. For every launch, `_compile_handover` writes full `ownerRelation` and `developerQuestions` into `.handover.json` alongside compact structured `host.developerQuestionRoute` (`{"mode": "parent", "agentId": started_by.agent_id}` when parented, `{"mode": "own-chat"}` when parentless) for the slim wire projection. A source-bound handover is not code/memory acceptance or live-host proof.

- Launch-aware AR guidance (`_ar_tool_server_usage`, `_brief_servers`) follows the launch's actual exclusion record rather than a universal `exclusion_applied=False`: a known AR server on Claude receives record-backed `providerOptions` MCP exclusion and omits `_AR_OTHER_SERVER_CHOICE`, while unknown/indeterminate acceptance and other harnesses retain conditional choice wording.
- Condensed `_AR_TOOL_SERVER_USAGE_HEAD`, `BRIEFS_SENTENCES`, and `_AR_TOOL_SERVER_USAGE_TAIL` direct `read_ar_files` with a `files` list of repository-relative path strings, native file tools for saved briefs (`briefs/<path>.md`, with `INDEX.md` in source brief folders and no index in `briefs/_task/`) and source/card files, `arMcpContext.readerArguments.shared`, and stopping on missing `task_context` schema support.
- Compiled `roleTools.usage` distinguishes host acceptance from product holding (permission prompts, unfinished starts, and unwritable turns are held and drained in order without granting permission bypass) and states that chat text answers only a waiting caller while other handovers go via `role_message`.

The preparer assembles a launch: it resolves the selection, writes the task-document copies and folder set, compiles the handover object, and calls `role_brief_message.brief_prompt` to compose the first message and complete handover content. It publishes neither handover file (`role_launch_routes` calls `role_handover_publication.publish_handover_files` before sending) and sends nothing.

`role_report_preparation.role_report_path` owns the request-qualified report path and settles the request's handover locator at the canonical report folder before writing the report folder or frozen details, refusing a colliding or retargeted alias before content exists.

`SPLIT_WORK_DIRECTION` defines the split-work rule (parallel own-assignment helpers from the start with no cap, another role through `role_start`, named serial exceptions, single writer of stage records, helper verification, and reporting how work was split or why not). It stands once in the static immutable prefix before `ar_tools`, `shared_block`, and the compiled capsule, while `started_from`, `first_read`, and `Link roots:` follow after the capsule under `## Launch Context`.

Leaf revival (`_verify_leaf_revival_scope`, `_revival_contract_path`, `_recorded_leaf_scope`) recomputes the canonical task/contract pair before comparing the saved receipt: a current readable direct grant binds the exact leaf to the master series contract, an ungranted leaf retains its canonical enclosure, and unreadable grant evidence refuses without fallback.

`_task_document_read_metadata` tells launched roles to read the rendered task document with native file tools, use `task_doc` first, and never parse rendered copies back. When `shared_block` is present and already carries the `refused-write.md` ladder and `"never keep a blanket ban on writing it by hand"`, `_task_document_read_metadata` conditionally omits the duplicate recovery ladder from `first_read`; when `shared_block` is absent or lacks those phrases, it retains the full `refused-write.md` recovery clause so no witnessed launch loses the rule.

`ROLE_START_OPERATIONS` binds `bootstrap` alongside the other seven roles to its capsule operation. Taskless assignments (architect, investigator, bootstrap) live in `cli.role_launch_assignments`, with `investigator_assignment` selecting parent-first-message vs developer-request wording from `started_by`. Enclosure preparation (`_leaf_contract_path`, `_resolve_workspace`, `_ensure_leaf_enclosure`) lives in `cli/role_launch_workspace.py`.

## Evidence

- Frozen implementation of `_ar_mcp_context` supporting leaf and configured-project reader arguments. [2]
- The `_resolve_workspace` implementation lives in its extracted owner `cli/role_launch_workspace.py`. [3]
- Independent views read fresh metadata, Start reads metadata then its selected pair, and explicit Refresh renews discovery. [5]
- Launch validation rejects unoffered selections; an unoffered model refuses before the workspace resolver is called. [6]
- Changed/missing saved scope refuses with both pairs, no bridge/write/enclosure creation. [7]
- Leaf revival compares current grant-sensitive canonical task/contract scope before bridge use. [9]
- Defaults extraction preserves host-role lookup. [12]
- The capsule operation each launcher role is compiled from, including the free agent. [15]
- The assignment the bootstrap seat carries, which names no task. [16]

- The shared preparer resolves launch choices before workspace preparation, then compiles the bound task readers and handover. [1]

- The parented handover values: `ownerRelation` from `_owner_relation` (with verified `owning_architect_id` direct skeletons), `developerQuestions` from `_developer_questions`, and compact structured `host.developerQuestionRoute` (`parent` vs `own-chat`). [4]
- An Investigator's assignment comes from `investigator_assignment` with the actual starting parent: a parented start takes its concern from the parent's first message, a parentless start asks the developer. [8]

- `_compile_handover` compiles instructions, names canonical task and copied documents, records starter and leaf peers through bound role addresses, and populates `host.developerQuestionRoute`. [10]

- Selection validation and the native Antigravity refusal run before workspace and enclosure preparation. [11]

- `_compose_compact_instructions` resolves the durable corpus root, calls `compose_launch_instructions(..., compact_links=True)`, emits JSON-quoted `Link roots:`, and includes the instruction digest in the immutable message binding. [13]

- Compact nested detail composition and user-note precedence delegate to `compose_launch_instructions` and `_write_nested_detail_artifacts`. [14]

- `_task_document_read_metadata` names `task_doc` first and conditionally deduplicates the `refused-write.md` ladder only when `shared_block` already carries it. [17]
- `_assembled_brief` compacts `shared_block` `skill://` URIs via `compact_skill_uri_links` and passes `link_roots` and condensed `_AR_TOOL_SERVER_USAGE*` into `BriefParts`. [21]
