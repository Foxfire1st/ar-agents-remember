# mcp/tests/test_knowledge_bootstrap.py

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Checks the taskless bootstrap command's current admission and converted named-wave write boundary.

## Code Commentary


The cases refuse an undeclared repository, refuse an unconverted root without writes, and reject database arguments. A converted-root case drives the named-wave file route. Other cases check memory-init's empty/recorded/partial text states and the skill's account of those states. The old canonical bootstrap staging, resume, publication and retry scenarios were removed. These are test definitions and assertions; no execution or broader environment qualification is claimed by this card.

### Conventions

Cases carry `pytest.mark.evidence_unit` and are driven through the shipped `main()` rather than through a
private function, so the surface under test is the one an operator has. No case reads a private helper of
the modules it covers.

The shared `entry` builder gives every target its own authored `rationale` (leaf `260921-ICR-L45`):
the writer both paths drive now refuses a new realization with no rationale, so a builder that omitted
it would turn every case into a `realization_rationale_absent` refusal.

### Todos

None recorded.

## Evidence


### Repo-Internal References

- `test_a_repository_the_settings_do_not_declare_is_refused_by_name` owns the current boundary described above. [34]
- `test_an_unconverted_memory_root_is_refused_as_legacy_format_and_nothing_is_written` owns the current boundary described above. [35]
- `test_a_converted_memory_root_is_written_as_the_named_wave` owns the current boundary described above. [36]

### Docs References

No configured Domain Documentation source applies.

No external documentation is required for the bootstrap case module.

- The Git and filesystem helpers the world is built with. [37]
- **The fixture: a real code checkout, a real external memory repository and a real settings document.** [38]
- The hand-off list builder. [39]
- The hand-off entry builder; since leaf `260921-ICR-L45` each target it writes carries its own authored `rationale`, because the writer refuses a new realization with none (`realization_rationale_absent`) and no longer generates one. [40]
- An undeclared repository refused by name. [41]
- The memory initializer naming the knowledge foundation and its measured state. [42]
- The admission the cases exercise through the shipped command line. [43]

- The invocation builder and the driver that returns the exit code beside the parsed JSON. [44]

### Cross-Repo References

No cross-repository behavior is exercised: every case builds its own single-repository coordination world
under a temporary root. The resolved settings' `crossRepo.allow` is empty, so nothing here names, reads
or writes another repository.

No meaningful cross-repo references found.
