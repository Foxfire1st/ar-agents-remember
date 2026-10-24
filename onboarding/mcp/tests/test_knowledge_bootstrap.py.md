# mcp/tests/test_knowledge_bootstrap.py

## Governing Overview

[Tests route overview](overview.md)

## Purpose

Covers the taskless knowledge bootstrap: authority comes from the settings document, knowledge is written
only as files, and the database bootstrap is retired. An undeclared repository is refused by name, an
unconverted memory root is refused as legacy format with nothing written, and a planning run writes nothing
until the commit is asked for. The memory-initializer reporting cases separately distinguish measured knowledge
state from the next action: resolved complete and nonlegacy unavailable answers hand the developer to
the Architect for a regular foundation task with a Curator, while partial-index repair and legacy
conversion keep their existing guidance. Those reporting assertions do not retire the taskless CLI
fixtures or turn them into the normal setup continuation.

## Code Commentary

### Logic

`World` builds one real coordination world — a code checkout at `workspace_root / repo_id`, its external
memory repository, and the settings file — through `_git()`, `_write()` and `_commit()`. `entry()` writes one
hand-off entry in the file writer's shape, carrying its own authored `rationale` because the writer refuses a
new realization with none; `hand_off()` builds the list, and `argv()`/`tree()` give the invocation and the
files a case compares before and after.

- **Authority.** `test_a_repository_the_settings_do_not_declare_is_refused_by_name` proves the settings
  document, not the caller, decides what has a context.
- **Legacy roots.** `test_an_unconverted_memory_root_is_refused_as_legacy_format_and_nothing_is_written`
  refuses with nothing written, and `test_the_command_takes_no_database_argument` proves no argument names a
  dataset, a staging candidate or a destination, with the parser refusing one.
- **The file writer.** `test_a_converted_memory_root_is_written_as_the_named_wave` reaches the real
  admission: a planning run writes nothing and the commit writes the named wave.
- **Reporting.** `test_memory_init_reports_empty_recorded_and_partial_text_knowledge` reports content and
  completeness independently of index existence. Its complete `not-recorded` and `recorded` answers use
  `_assert_architect_handover`: the measured state precedes the Architect, and the action names a regular
  task with a Curator and no knowledge-bootstrap command. The same case retains exact partial-index
  repair and legacy conversion guidance.
- **Unavailable publication.** `test_memory_init_hands_unavailable_nonlegacy_knowledge_to_the_architect`
  obstructs the derived-cache directory with a file, reaches the real resolver's
  `PublishedIntentUnavailable` branch, preserves state/path/code/detail, and checks the same handover.
  It compares the authored memory bodies and obstruction bytes before and after reporting. This is not
  a claim that derived index work never occurs.
- **Skill text.** `test_the_bootstrap_skill_describes_the_states_memory_init_reports` still requires the
  skill's paragraph to name the measured states.

### Conventions

Cases build a real Git checkout and a real external memory repository rather than mocking the writer, so a
wrong path or a missing rationale fails as it would in production.

### Invariants And Boundaries

- A run that is not asked to commit writes nothing.
- The bootstrap has no database argument and no dataset: knowledge is files.

## Evidence

- An undeclared repository is refused by name. [34]

- An unconverted memory root is refused as legacy format with nothing written. [35]

- A converted memory root is written as the named wave, with a planning run writing nothing. [36]

- The Git and filesystem helpers the world is built with. [37]

- The fixture is a real code checkout, a real external memory repository and a real settings document. [38]
- The hand-off list builder. [39]
- The hand-off entry builder writes each target's authored `rationale`, because the writer refuses a new realization without one. [40]
- An undeclared repository is refused by name through the shipped command line. [41]

- The initializer distinguishes complete empty/recorded states, emits the Architect/regular-task/Curator handover for those states, preserves exact partial-index and legacy guidance, and compares authored memory bodies around reporting. [42]
- A real nonlegacy unavailable-publication result caused by an obstructed derived-cache path retains state/datasetPath/code/detail and names the measured state before the Architect handover; authored memory bodies and the obstruction bytes stay unchanged. [45]

- The admission the cases exercise is `AdmittedKnowledgeBootstrap`. [43]
- The invocation builder and the driver that returns the exit code beside the parsed JSON. [44]
