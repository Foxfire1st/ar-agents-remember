# skills/l-01-agent-lifecycles/roles/bootstrap.md

[overview](overview.md)

## Purpose and authority

Bootstrap uses read_ar_files for source and card locations and bounded file-rule text. The Bootstrap tool boundary still admits only the named setup and read routes.


Bootstrap is the free-agent first-hour setup/report seat for one repository, not a general maintenance or leaf transaction role: it is started from the dashboard, has no parent and needs none, because the user made the one call (`role_start(role="bootstrap", request_id=<UUID>)`) from their own chat and nothing dispatches it. `operations/bootstrap.md` owns its ordered procedure, and the current source orders those two pages explicitly: where they disagree, the prohibitions in the role page's **Boundaries** win, because no step orders this seat to write onboarding or knowledge or to run a citation fixer. Setup mutations use their existing owning surfaces with preview/read-back and developer decisions; native reads and checked helpers grant no extra authority. It authors no onboarding or knowledge, moves no branch and creates no worktree, and it organises no knowledge authoring: it reports the foundation state it read and tells the user to start the Architect. Its five permitted mutation surfaces are `runtime_install`, `memory_init`, `memory_baseline_status`, `memory_baseline_adopt` and `user_settings_init` (one-write limit; preserve existing). `role_message` is forbidden and not in Bootstrap's tool list: a question for the developer is written in its own chat and ends the turn. Its current reader surface names `context_packet`, `server_info` and `read_ar_files`: card discovery through `read_ar_files` and opening the returned files with native tools are distinct steps. Its Reference index links `../templates/bootstrap-report.md`, `reference/bootstrap/foundation-state.md#read-the-state`, `reference/knowledge/commands.md`, `reference/knowledge/use.md#read-the-source-that-owns-a-setting` and `reference/sandbox-actors.md`. The negative list explicitly retains `retire_child`; a supported public tool is not automatically a Bootstrap power.

Its sole durable output is written at `taskReportPath` (exact path on line 1, no second post), following `templates/bootstrap-report.md` and `reference/bootstrap/foundation-state.md#read-the-state` for resolved setup and foundation-state report fields. Missing inputs/capabilities and instruction/system contradictions are reported honestly; no alternate mode or artifact migration substitutes for a refused step.

## Message/file transport

Bootstrap messages no one, so the shared wake-up and file-payload transport rule has no sending duty here: its one durable artifact is its report file, and a developer question is its own reply. The canonical source and the packaged copy the tool server serves share this contract.

Bootstrap sends no role_message; developer questions are its own reply and end the turn. Its report is its one durable artifact and names its own path.



- Bootstrap reads through `context_packet`, `server_info` and `read_ar_files`, and is forbidden `retire_child` and the other lifecycle tools beyond its setup surfaces. [2]



- Bootstrap sends no role messages: it writes a developer question in its own reply and ends the turn. Its one report states its exact path on the first line, and it reads and reports the foundation state without authoring knowledge. [1]
