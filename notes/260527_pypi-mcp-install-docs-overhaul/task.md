# Task: PyPI MCP Install And User Documentation Overhaul

**Status:** inProgress
**Repo:** agents-remember-md
**Type:** Docs | Config | Skill
**Created:** 2026-05-27T12:27
**Execution Mode:** current checkout until implementation approval; no C-09 worktree requested yet

---

## Objective

Validate the PyPI-based Agents Remember MCP installation path end to end, then rewrite the user-facing installation and workflow documentation from the perspective of a first-time, non-hardcore user who expects to ask their model to use Agents Remember rather than manually drive tool calls.

The documentation overhaul must stand on proven workflow integrity: chat mode, light tasks, and worktree-backed tasks need to be checked before the manual promises those paths are frictionless.

---

## Request And Framing

### Surface Request

Create a new standalone light task for the PyPI MCP install and documentation overhaul, with a workflow-integrity section before documentation update work.

### Deeper Objective

Make Agents Remember feel installable and usable by someone who has never seen the repo, is comfortable vibe-coding with an agent, and may trip over missing operational details such as restarting the code harness after MCP registration.

### Highest-Leverage Framing

Treat the manual as a guided first-run product experience, not an internal reference dump. The normal path should be: install the PyPI MCP package, register it in the harness, restart/reload the harness, ask the model to install/scaffold/use Agents Remember, and only consult manual tool-call reference when troubleshooting.

---

## Requirements

- Create this as a new standalone task, not an add-on to the existing harness MCP compatibility docs plan.
- Start with workflow integrity before documentation edits.
- Investigate the real PyPI install path from a project folder, including MCP installation, harness registration, restart/reload expectations, runtime scaffold install, skills install, provider setup, memory initialization, and existing-memory adoption from a Git repo.
- Document the software requirements needed to run the MCP, including required Python/package tooling, Git, optional provider/runtime dependencies, harness capabilities, and platform caveats.
- Use Codex as the executable harness target for first-pass MCP registration and workflow validation.
- Fully validate both GrepAI and CodeGraphContext provider setup with integration tests that cover the relevant success and failure cases before provider docs are rewritten.
- Validate whether chat mode can start work and complete through closeout.
- Validate whether light-task workflow still gives a clear durable plan and approval gate under the MCP-first install model.
- Validate whether worktree-backed tasks create independent provider/runtime state instead of accidentally watching global provider roots.
- Validate whether worktree start copies or maps existing memory correctly.
- Validate whether worktree cleanup removes worktree provider state as part of cleanup when such state exists.
- Document chat mode, light task, and worktree workflows as user-facing paths.
- Make the primary user instruction model: once MCP is running, ask the model to use Agents Remember tools and skills.
- Keep manual MCP tool calls documented for troubleshooting and advanced operator use, but do not make them the happy-path interaction style.
- Explicitly document harness restart/reload after adding or changing the MCP server.
- Keep provider setup instructions practical: what the user asks the agent to do, what visible success looks like, and where to look when setup fails.
- Distinguish bootstrapping a brand-new memory root from adopting/installing existing memory from Git, covering both external memory repos and repo-local `ar-memory/`.
- Record every defect found during workflow validation in `findings.md` inside this task folder, including repro, expected behavior, actual behavior, impact, status, fix owner/path, and retest result.
- Follow the sequence: test workflows end to end first, record all issues in `findings.md`, fix defects separately, retest, then write the documentation from the passing behavior.
- Preserve approval gates: implementation approval is separate from commit/closeout approval.
- Update source docs, installed runtime skill guidance, and onboarding only after implementation approval.

---

## Assumptions

- The published package is `agents-remember-mcp` and exposes `agents-remember-mcp` plus `python -m agents_remember.mcp` entrypoints.
- The current source MCP tool surface includes install, memory, provider, worktree, closeout, baseline, carryover, and benchmark tools, but the installed PyPI package must be verified rather than assumed.
- Some harnesses may hide newly registered MCP tools until the harness process or agent session is restarted.
- The best documentation will give users copyable prompts to give their model, plus separate operator/tool-call references for debugging.

---

## Invariants And Non-Goals

- Do not document unverified workflow behavior as the happy path.
- Do not make users manually call MCP tools in the main path when the intended behavior is asking the model to use tools.
- Do not hide manual tool calls entirely; they remain necessary for troubleshooting.
- Do not conflate runtime installation, memory initialization, onboarding bootstrap, provider setup, and task closeout.
- Do not redesign the MCP server or provider architecture unless workflow-integrity validation proves a blocking defect.
- Do not edit documentation before the integrity plan is approved.

---

## Evidence Plan

- Source evidence: inspect MCP package metadata, entrypoints, settings examples, runtime install code, skills install code, provider lifecycle code, memory init/adoption code, worktree code, and current docs.
- Package evidence: install the PyPI package in a clean temporary environment and verify entrypoints, tool list, import paths, package data, and version.
- Requirements evidence: verify the actual software prerequisites for the MCP happy path and optional provider paths rather than copying assumptions from old docs.
- Runtime evidence: use isolated temporary workspace folders for first-run install, runtime scaffold, skills install, provider setup, memory initialization, existing-memory adoption, chat/direct closeout, light task, and worktree lifecycle tests, but execute the Agents Remember workflow operations through real MCP tool calls.
- Harness evidence: verify Codex registration and restart/reload behavior concretely, then use a fresh Codex agent session registered to the PyPI-installed MCP server as the authority for workflow validation.
- Provider evidence: add integration tests for GrepAI and CodeGraphContext setup/status/watch cases, using isolated settings and runtime roots where possible.
- Defect evidence: keep `findings.md` as the task-local defect log throughout validation, fixing, and retesting.
- Documentation evidence: verify links, examples, command snippets, and task-flow wording after rewrite.

---

## Validation Method Contract

The workflow-integrity pass must validate the published package as users run it:

- Install `agents-remember-mcp` from PyPI into a clean virtual environment outside the source checkout.
- Register that venv's `agents-remember-mcp` executable as a Codex MCP server for an isolated test workspace.
- Start a fresh Codex agent session with that MCP server loaded.
- Prove the child session is using the isolated PyPI server by recording `server_info.configPath`, `server_info.workspaceRoot`, and the server executable/config used to launch it.
- Execute Agents Remember workflow operations only by asking that agent to use MCP tools.
- Treat direct imports such as `agents_remember.mcp.tools.*_payload`, provider setup Python APIs, local source modules, or repo-local test helpers as invalid for workflow-integrity evidence.
- Treat the source checkout as inspection-only during validation; it must not be on the MCP server `PYTHONPATH`, and the MCP server must not be launched from the checkout.
- Treat CLI commands as setup/inspection only: package install, Codex MCP registration, temp fixture creation, Git fixture setup, and post-run filesystem/Git verification are allowed; Agents Remember workflow behavior is not proven unless it came from MCP tool calls.
- Capture evidence from the harness run: child Codex prompt, MCP server config path, `server_info` output from the child session, MCP tool results, and any transcript/event output showing the tool path.
- The active workspace MCP server can be used only for the real `agents-remember-md` task context. It does not validate the isolated PyPI install unless the isolated server is the registered server for that run.

Pass 01 is invalid as workflow-integrity proof because it used direct package/API calls for most workflow checks. It remains only a package smoke and mistake-analysis artifact.

---

## Follow-Up Task Series

- [Provider Workflow Compatibility For Worktrees And Benchmarks](/home/mohamedreadone/Projects/ar-coordination/tasks/agents-remember-md/260527_pypi-mcp-install-docs-overhaul/task-provider-workflow-compatibility.md) covers the provider-runtime defect family before provider docs are rewritten. It owns provider instance namespacing, Docker ownership verification, worktree and benchmark provider isolation, safe cleanup, and copying/seeding existing provider data with rewritten target paths/base URLs so expensive re-indexing is not the default workflow.

---

## Implementation Steps

### S1 - Workflow Integrity Baseline

- [x] Prove or classify the current install and workflow behavior through real MCP tool calls before documentation edits.
  - [x] Verify and record software requirements for the base MCP path: Python version, package installer choices, Git, supported shells/OS assumptions, harness MCP support, and restart/reload needs.
  - [x] Verify and record optional software requirements for provider paths, especially Docker/Compose, provider images, local ports, and any model/embedder dependencies.
  - [x] Verify the PyPI package install in a clean temporary environment, including entrypoints and `server_info` via the MCP tool.
  - [x] Verify the starting-from-project-folder path with Codex: create an isolated project folder, register the PyPI MCP server, start a fresh Codex session, and confirm tools are visible by calling `server_info`.
  - [x] Verify runtime scaffold installation through MCP and confirm package-owned files land in `ar-coordination` without overwriting user-owned data.
  - [ ] Verify skills installation through MCP for both tree and flat harness skill layouts, including what the user must restart or reload. Pass 02 covered tree layout plus fresh Codex skill visibility; flat layout remains pending.
  - [ ] Build integration tests for GrepAI provider setup/status/watch success and failure cases using MCP tool calls or a harness-run test harness; direct provider APIs do not satisfy this item.
  - [ ] Build integration tests for CodeGraphContext provider setup/status/watch success and failure cases using MCP tool calls or a harness-run test harness; direct provider APIs do not satisfy this item.
  - [x] Verify provider setup/status from MCP settings through MCP tool calls and record what visible success and common failure states look like. Non-mutating status passed, but mutation is blocked by shared/global provider state in F-010.
  - [x] Verify brand-new memory initialization and initial bootstrap path through MCP tool calls.
  - [x] Verify existing external memory adoption from a Git repo path or clone through MCP tool calls, including baseline/ledger expectations.
  - [x] Verify repo-local `ar-memory/` restored from Git through MCP tool calls, including resolver behavior and baseline expectations. Classified blocked by F-002.
  - [x] Record every defect or friction point discovered during the MCP validation pass in `findings.md`.
  - [x] Verification: produce an MCP-backed integrity matrix that marks each path as pass, blocked, or docs-only with evidence and next action.

### S2 - Chat And Light Workflow Integrity

- [x] Validate normal task workflows under the MCP-first install model through real MCP tool calls.
  - [x] Verify chat mode can resolve context, run drift checks, perform a small controlled change, and complete through direct closeout preview/apply in an isolated repo using MCP tools.
  - [x] Verify light task creation, approval gate, checklist execution, onboarding update expectations, and closeout preview behavior using MCP tools.
  - [x] Verify the user-facing interaction can be phrased as prompts to the model, with manual tool calls kept as troubleshooting references.
  - [x] Record every defect or friction point discovered during S2 in `findings.md`.
  - [x] Verification: record exact prompts, MCP tool calls observed, expected outputs, and any friction points that must become docs notes.

### S3 - Worktree Workflow Integrity

- [x] Validate worktree-backed task behavior through real MCP tool calls before documenting it as a user path.
  - [x] Verify worktree start creates isolated code and memory worktrees from a clean baseline using MCP tools.
  - [x] Verify existing memory is copied or mapped into the worktree context correctly and is the context read during task execution using MCP tools.
  - [x] Verify provider preparation for worktrees creates independent provider/runtime state where intended and does not accidentally watch the global code or memory provider roots using MCP tools. Classified blocked for real provider mutation by F-010; dry-run showed CGC worktree runtime paths.
  - [x] Verify worktree closeout preview/apply sequence preserves separate implementation and commit approvals using MCP tools.
  - [x] Verify integration and cleanup gates using MCP tools.
  - [x] Verify/classify whether cleanup removes worktree-specific provider state when that state exists, while preserving shared/global provider state using MCP tools. Code/memory cleanup passed; provider-runtime cleanup remains blocked by F-003/F-010.
  - [x] Record every defect or friction point discovered during S3 in `findings.md`.
  - [x] Verification: record any product defects separately from documentation tasks and do not paper over them in the manual.

### S4 - Defect Fixes And Retest

- [ ] Fix defects discovered during workflow validation before writing the manual.
  - [ ] Triage `findings.md` into documentation-only notes, implementation defects, test defects, and deferred issues.
  - [ ] Fix implementation defects required for the happy path to be true.
  - [ ] Fix or stabilize the GrepAI and CodeGraphContext integration tests.
  - [ ] Retest every fixed path and update each `findings.md` item with the fix commit/path and retest result.
  - [ ] Identify any deferred issues explicitly and keep them out of happy-path docs.
  - [ ] Verification: all happy-path install, provider, chat, light-task, and worktree flows are either passing or intentionally excluded from the first manual.

### S5 - User Manual Information Architecture

- [ ] Design the new documentation structure after integrity findings are known.
  - [ ] Define the first-run path for someone who has never seen the repo.
  - [ ] Define where software requirements live and make them visible before install commands.
  - [ ] Separate happy-path prompts from operator/tool-call troubleshooting references.
  - [ ] Add explicit restart/reload guidance after MCP registration, runtime install, and skills install where harnesses require it.
  - [ ] Split bootstrapping new memory from installing/adopting external memory repos and repo-local `ar-memory/` from Git.
  - [ ] Define docs for chat mode, light task, and worktrees at user-facing detail.
  - [ ] Decide how to merge or supersede the older harness MCP compatibility task without losing researched facts.
  - [ ] Verification: present the proposed docs map and before/after examples for approval before rewriting docs.

### S6 - Documentation Rewrite

- [ ] Rewrite the public docs and model-facing skill guidance after approval.
  - [ ] Add or update a software requirements section/page covering base MCP requirements, optional provider requirements, and harness-specific requirements.
  - [ ] Update `README.md` and `docs/getting-started.md` around PyPI MCP installation and first-run flow.
  - [ ] Update `docs/install/` pages for harness-specific MCP registration, restart/reload behavior, and skill exposure.
  - [ ] Update `docs/workflows.md` with chat mode, light task, and worktree paths grounded in validated behavior.
  - [ ] Update guides for new memory bootstrap and existing memory adoption.
  - [ ] Update reference pages so MCP tool calls are available for troubleshooting without dominating the main path.
  - [ ] Update installed runtime skills only where they still teach stale script choreography or unclear MCP-first expectations.
  - [ ] Verification: run markdown link checks or equivalent local checks, `git diff --check`, and repo-specific checks from the resolved `system/tools.md`.

### S7 - Onboarding And Closeout Readiness

- [ ] Refresh durable memory and prepare closeout.
  - [ ] Route durable current-state findings through `C-05-create-or-update-onboarding-files`.
  - [ ] Run C-02 drift detection after docs and skill changes.
  - [ ] Run the full project-owned quality wrapper if Python code changes become necessary; otherwise record why documentation-only checks are sufficient.
  - [ ] Present changed docs, integrity results, onboarding updates, verification results, and proposed closeout messages.
  - [ ] Stop for explicit commit/closeout approval before any real commit, direct closeout apply, worktree closeout apply, integration, push, or cleanup.

---

## Proposed Code Examples

### E1 - Happy-Path User Prompt

Distinct change covered: The manual should teach users to ask their model to use Agents Remember once the MCP server is running.

Why this example is included: This is the core UX change from manual tool choreography to model-mediated operation.

```markdown
Ask your agent:

"Use Agents Remember for this repository. Check the MCP server, install or refresh
the runtime, install the skills for this harness, initialize memory if it is
missing, then tell me what you found before bootstrapping onboarding."
```

### E2 - Troubleshooting Tool Reference

Distinct change covered: Manual tool calls stay documented, but they move into troubleshooting/reference sections.

Why this example is included: Advanced users still need exact MCP calls when the model or harness gets confused.

```text
server_info()
runtime_install(dry_run=true)
runtime_install(dry_run=false)
skills_install(dry_run=true)
memory_init(repo_id="<repo-id>", dry_run=true)
context_packet(repo_id="<repo-id>", include_providers=true)
```

### E3 - Workflow Integrity Matrix Shape

Distinct change covered: Documentation rewrite waits for evidence from real workflow checks.

Why this example is included: The task must not let docs outrun actual install and workflow behavior.

```markdown
| Path | Evidence | Result | Docs consequence |
| --- | --- | --- | --- |
| PyPI install + server_info | clean venv, package version, tool list | pass | happy path |
| Chat direct closeout | isolated repo, preview/apply | pass | user workflow |
| Worktree provider isolation | worktree provider roots/status | blocked | document limitation or fix first |
```

### E4 - Software Requirements Shape

Distinct change covered: The manual must tell first-time users what has to exist on their machine before the MCP can run.

Why this example is included: Missing prerequisites are one of the easiest ways for a frictionless install guide to become confusing.

```markdown
| Requirement | Needed for | How to check | Notes |
| --- | --- | --- | --- |
| Python 3.11+ | MCP server | `python3 --version` | Required by the PyPI package. |
| Git | memory and closeout | `git --version` | Required for repository and memory verification. |
| Docker + Compose | optional providers | `docker compose version` | Needed only when enabling provider watchers. |
```

---

## Decision Log

| Date-Time | Decision | Rationale |
| --- | --- | --- |
| 2026-05-27T12:27 | Create a new standalone light task for the PyPI MCP install and documentation overhaul. | The documentation update is a primary product-facing effort, not a side note of the existing harness MCP compatibility planning task. |
| 2026-05-27T12:27 | Put workflow integrity before documentation rewrite. | The manual should describe proven install/task behavior rather than hoping chat, light-task, provider, and worktree paths still work after the PyPI MCP packaging change. |
| 2026-05-27T12:27 | Treat model-mediated MCP use as the happy path and manual MCP calls as troubleshooting/reference. | The target user is a first-time vibe coder who should ask their model to use Agents Remember once MCP is running, while still having exact calls available when debugging. |
| 2026-05-27T12:56 | Add software requirements as a first-class documentation and verification target. | First-time users need prerequisites before commands; the docs should verify and explain base MCP requirements separately from optional provider/runtime requirements. |
| 2026-05-27T13:02 | Resolve the open questions: test with Codex, fully validate GrepAI and CGC through integration tests, cover both external-memory and repo-local `ar-memory` adoption, and log defects in `findings.md` before fixing and retesting. | The docs should be written from passing behavior, not from hoped-for behavior; defects found during the integrity pass need one durable task-local home before implementation fixes and documentation work begin. |
| 2026-05-27T13:02 | Begin the approved first validation pass. | The developer approved starting S1-S3, with a stop after findings are recorded so fixes and documentation strategy can be discussed separately. |
| 2026-05-27T14:30 | Redo workflow validation through a fresh Codex session registered to the PyPI-installed MCP server. | The first pass used direct Python/API calls for most workflow checks, which does not validate the user-facing MCP installation path. |
| 2026-05-27T14:25 | Complete pass 02 as the first valid MCP-backed validation pass and pause before fixes/docs. | Chat, light-task, worktree core, new memory, and existing external-memory paths now have MCP evidence; repo-local memory and provider mutation are blocked defects that need triage before documentation rewrite. |
| 2026-05-27T14:50 | Add a provider workflow compatibility follow-up task. | Provider isolation, safe cleanup, and provider-data copy/seed/rewrite behavior are large enough to own separately before the PyPI MCP manual can promise worktree and benchmark provider workflows. |

---

## Open Questions

- None.

---

## References

- [PyPI publish workflow](/home/mohamedreadone/Projects/agents-remember-md/.github/workflows/publish-mcp-to-pypi.yml)
- [MCP package metadata](/home/mohamedreadone/Projects/agents-remember-md/mcp/pyproject.toml)
- [MCP server tool registration](/home/mohamedreadone/Projects/agents-remember-md/mcp/src/agents_remember/mcp/server.py)
- [MCP tool payloads](/home/mohamedreadone/Projects/agents-remember-md/mcp/src/agents_remember/mcp/tools.py)
- [Current README](/home/mohamedreadone/Projects/agents-remember-md/README.md)
- [Getting Started](/home/mohamedreadone/Projects/agents-remember-md/docs/getting-started.md)
- [Install guide index](/home/mohamedreadone/Projects/agents-remember-md/docs/install/README.md)
- [Workflows docs](/home/mohamedreadone/Projects/agents-remember-md/docs/workflows.md)
- [Skills reference](/home/mohamedreadone/Projects/agents-remember-md/docs/reference/skills.md)
- [Worktrees reference](/home/mohamedreadone/Projects/agents-remember-md/docs/reference/worktrees-c09.md)
- [Chat workflow skill](/home/mohamedreadone/Projects/.codex/skills/agents-remember-md/W-03-chat-task-workflow/SKILL.md)
- [Light task workflow skill](/home/mohamedreadone/Projects/.codex/skills/agents-remember-md/W-02-light-task-workflow/SKILL.md)
- [Worktree manager skill](/home/mohamedreadone/Projects/.codex/skills/agents-remember-md/U-01-core-skills/C-09-git-worktree-manager/SKILL.md)
- [Closeout skill](/home/mohamedreadone/Projects/.codex/skills/agents-remember-md/U-01-core-skills/C-12-closeout/SKILL.md)
- [Memory initialization skill](/home/mohamedreadone/Projects/.codex/skills/agents-remember-md/U-01-core-skills/C-00-initialize-memory-repo/SKILL.md)
