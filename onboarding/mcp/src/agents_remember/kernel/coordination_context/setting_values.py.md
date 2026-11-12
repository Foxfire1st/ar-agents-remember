# mcp/src/agents_remember/kernel/coordination_context/setting_values.py

## Governing Overview

[coordination_context overview](overview.md)

## Purpose

`setting_values.py` applies the shared `clean_scalar` helper while parsing
mapping, list, boolean, and `crossRepo.allow` values; scalar normalization itself
is owned by that imported helper.

## Code Commentary

For an individual crossRepo.allow entry, malformed repo/expectedBranch or boolean values become an excluded entry plus an indexed explanation. Bad booleans retain the conservative includeCode=True/includeMemory=False defaults with the exclusion reason. This total-entry behavior does not make the outer settings parser total: a non-array allow value still raises. cit:([`parse_cross_repo_allow`, `parsed_cross_repo_allow_entry`, `cross_repo_entry_booleans`], mcp/src/agents_remember/kernel/coordination_context/setting_values.py:44-58; mcp/src/agents_remember/kernel/coordination_context/setting_values.py:86-120).

### Logic

The module normalizes string/list settings, validates booleans and mappings,
and converts strict v2 cross-repo allow objects into `CrossRepoAllowEntry`
models. Legacy string allow entries are retained only as excluded entries with
an explicit migration reason.

### Invariants And Boundaries

- Value parsing is format-neutral and performs no filesystem or Git checks.
- Cross-repo entries require both `repo` and `expectedBranch` before runtime
  resolution can include them.

## Evidence

### Docs References

No external documentation is needed for these local parsing helpers.

No relevant external documentation is needed.

### Repo-Internal References

- None [1]
- Cross-repo runtime resolution consumes parsed allow entries. [2]

### Cross-Repo References

No cross-repository evidence is needed for format-neutral value parsing.

No meaningful cross-repo references found.
