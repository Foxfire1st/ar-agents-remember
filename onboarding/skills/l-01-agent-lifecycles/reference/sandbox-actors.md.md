# skills/l-01-agent-lifecycles/reference/sandbox-actors.md

## Governing Overview

[overview](../overview.md)

## Purpose

Rules for roles that set up or inspect sandbox actors—per-run harness settings, user-owned configuration boundaries, model selection, launch homes, and binding proof—and for keeping working files in the handover's scratch roots. It grants no additional authority.

## Code Commentary

No role writes user-level harness configuration; each sandbox actor is bound per run, or the role stops and asks. A user-level harness configuration file that an agent created is left unchanged and reported to the parent, who routes one notice to the developer. Test actors need no extra permission under Agents Remember's rules, though a harness's own approval review may still ask the developer; they use the cheapest model of the harness the run is set up for, named in the command and the record, under ordinary sandbox isolation. The product never edits a harness file the user owns and ships a needed setting through its own launch settings or the harness's documentation page. Credentials stay out of a sandbox-local harness home, and model turns run through the sandbox product's launch home. Before sandbox actors start, their tool-server binding is proved with a stub, and the host's agents are counted before and after the first `role_start`. Under `## Keep working files in the handover's scratch roots`, agent-authored temporaries, experiments, and working copies stay in `workspace.scratchRoot` (outside code, memory, and task folders), `workspace.outsideScratchRoot` holds work that must live outside the projects home (especially a sandbox root) and one short `TMPDIR`, `XDG_CONFIG_HOME` stays inside `workspace.scratchRoot`, neither root is removed by the seat, a brief does not substitute another scratch path, product/test-runner/sandbox temporaries follow their owners, and reports/evidence go in the handover's local report folder. The manifest lists all eight roles as readers, and every role's Reference index points here.

## Evidence

- Sandbox settings are bound per run; a user-level harness file created by an agent is reported, not changed. [1]
- Test actors use the cheapest model of the configured harness, named in the command and record. [2]
- The product never edits user-owned harness files, and model turns run through the sandbox product's launch home. [3]
- Actor binding is proved with a stub and an agent count around the first start. [4]

- The Worker role links this detail from its Reference index. [5]

- Working files stay in `workspace.scratchRoot`, `workspace.outsideScratchRoot` holds outside-projects sandbox roots and one short `TMPDIR`, `XDG_CONFIG_HOME` stays in `workspace.scratchRoot`, and neither root is removed by the seat. [6]
