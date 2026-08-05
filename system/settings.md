# agents-remember Memory Settings

This is the committed memory settings file for the `agents-remember` shared memory repo.

## Scope

The sibling `settings.json` is the machine-readable source for onboarding storage, path eligibility, and cross-repo policy for this memory repo.

This memory repo is selected by the local coordinator at `C:\ew\ar-coordination`, but durable repo policy belongs here, not in the untracked coordinator settings.

## Storage

Onboarding uses `memory-repo` storage. Eligible onboarding artifacts live under this memory repo's `onboarding/` directory.

## Format Ordering

Agents Remember formats list chronological appendices newest-first for reading ergonomics. This applies to update histories, decision logs, ledgers, handoff logs, task-local history sections, and any similar log/history surface unless a format explicitly says otherwise.

When adding an entry, prepend it at the top of the relevant list or table. Use an ISO timestamp where the format carries timestamps. Do not append new entries to the bottom or insert them arbitrarily.

## Path Eligibility

The path rules in `settings.json` are unscoped because this memory repo maps to exactly one code repo: `agents-remember`.

Benchmark case metadata and documentation may be source material, but resettable benchmark workspaces are not. `settings.json` explicitly excludes benchmark `user-runs/`, benchmark workspaces, and packaged benchmark fixture data under `mcp/src/agents_remember/package_data/benchmarks/**` so cloned repos, workspace-local `ar-coordination/` trees, and packaged benchmark memory snapshots cannot recursively generate onboarding for themselves.

The current MCP work adds first-class source under `mcp/**`, source-owned
operational helpers under `scripts/**`, and the authority-settings example
under `examples/mcp/**`. These routes are eligible for onboarding in
`settings.json` so drift detection sees the MCP server, application-layer,
provider adapter, settings-template, and non-runtime script changes.

## Cross-Repo Policy

`crossRepo.allow` is currently empty. Neighboring repositories are not included unless this committed memory settings file explicitly allows them.
