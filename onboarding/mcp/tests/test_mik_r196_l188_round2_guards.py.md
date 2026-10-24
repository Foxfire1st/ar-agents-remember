# mcp/tests/test_mik_r196_l188_round2_guards.py

## Governing Overview

[MCP tests overview](overview.md)

## Purpose

Retained setup guards and real benchmark preparation without installed skill copies. Each case stands on a defect
a reviewer found statically in the round-2 candidate: a sandbox builder reading a key its producer does not
return, an enforcing qualification rail calling a script this leaf deleted, the setup skills still assigning
onboarding, and a same-request retry preparing a cold root twice. The first three are checked here as structure;
the fourth is checked as behaviour in `test_mik_r196_l188_preparation_order.py`.

## Code Commentary

### Logic

- **The producer and the builder move together.**
  `test_the_sandbox_builder_reads_the_key_its_producer_returns` reads both `scripts/pnt_sandbox/settings_expectation.py`
  and `scripts/pnt_sandbox/builder.py`: the producer's own key is `preparedSettingsPath`, the builder never names
  `renderedSettingsPath`, and it does read `preparedSettingsPath`. A builder reading the old name raises `KeyError`
  on a real build.
- **Every enforcing rail runs a script the repository holds.**
  `test_every_qualification_rail_runs_a_script_the_repository_holds` walks each rail's `execution.command` in
  `mcp/certification-profile-v1.json`, keeps the arguments shaped like `scripts/...py`, and fails naming the rail
  and the missing script. A rail naming a deleted script cannot run and must not be certified.
- **Setup assigns no onboarding.** `test_the_setup_skills_assign_no_onboarding` reads the canonical
  `skills/c-13-install-and-onboard/SKILL.md` and its packaged copy: both say "Setup authors no onboarding", neither
  says "Scaffold onboarding", and both keep the citation fixer out of setup (MIK-R196 rules 4–5).
- **Benchmark preparation (real clones).**
  `test_benchmark_preparation_discovers_package_skills_without_installing_copies` builds a local origin repository with
  one commit, copies the benchmark templates, and prepares the same case twice. Both prepared trees
  (`source-only/repos/fixture`, `with-memory/repos/fixture`, `with-memory/ar-coordination/memory-repos/ar-fixture`)
  carry the pinned fixture at the case's commit; the coordination root holds `AGENTS.md`, no `.codex` is left in
  the source-only tree, and no `skills` tree is installed anywhere. The written `.codex/config.toml` registers
  `agents_remember_benchmark` with `-m agents_remember.mcp --config <settings>`, the settings resolve the fixture
  repository and the memory coordination root with no providers, and the registered server serves
  `skill://index.json` and the packaged `c-13-install-and-onboard/SKILL.md` and
  `l-01-agent-lifecycles/roles/worker.md` byte-identical out of `package_data`.

### Conventions

`REPOSITORY_ROOT` is the test file's grandparent, so every guard reads the checkout it runs in, and the profile
path is `mcp/certification-profile-v1.json`. The benchmark case is a real local Git repository prepared through
`prepare_case`, not a mock of the runner.

### Invariants And Boundaries

- A consumer's key name is the producer's key name; a stale name is a defect even when both sides import cleanly.
- An enforcing rail names only scripts the repository holds.
- Setup initialises the memory root and authors no onboarding; the knowledge foundation stays a later regular task.
- Preparation registers the packaged skills and installs no copy of them.
- These guards read structure and prepare disposable fixtures; they claim no certification verdict and no
  installed-build acceptance.

## Evidence

- The sandbox builder reads the key its producer returns, and the old name is absent from the pair.
- Every enforcing rail names a script that exists in the checkout.
- The canonical and packaged setup skills both refuse onboarding authorship and keep the fixer out.
- Real benchmark preparation twice over leaves both trees at the pinned commit, installs no skill tree, and serves
  the packaged skill bytes through the registered server.
