# mcp/tests/test_memory_mode_removal.py

## Governing Overview

[Test suite overview](../overview.md)

## Purpose

The executable guard for the removal of `internal` memory mode. It pins four properties, and each is
written to name the failure it prevents rather than merely to pass: the mode is **refused by name**
(never silently substituted with `external` or a default), existing state that records it is
**reported and left byte-identical** (never migrated or deleted), the **supported set is untouched**
(`external` and `disabled` still resolve, write and read through the application layer and the CLI), and
**both shapes an onboarding root legitimately takes are decided structurally** — the leaf enclosure's
`worktrees/<repo>/<group>/memory-<name>/onboarding` is supported and measured, while a directory that
merely resembles it is refused by name rather than guessed at.

## Code Commentary

### Logic

The module is a single file because the properties belong to one removal; it is not a general
memory test suite. Its cases divide into eight groups.

**Vocabulary and narrowers.** The declared literals are asserted to hold no removed member, the two
narrowers are asserted to refuse the removed token by name, and — the distinction that matters — a case
asserts that an *unknown* token is still an ordinary invalid-argument error rather than being reported as
a removal. Both `_topology` and `_normalize_topology` are exercised with `"internal"`, `"bogus"`,
`"external"` and `None`, because the two flag narrowers previously reported every unknown token as a
removed mode.

**Entry-point refusals.** Worktree start refuses an explicit removed mode and a removed topology
argument; the resolver refuses a requested removed topology; `resolve_context_tool` and the baseline
topology flag refuse it; the contract writer refuses a removed mode request.

**Existing-state reporting.** A repository that still carries the removed root is reported, settings and
an onboarding root inside that root are reported *by their own path*, a configured memory root refuses
the removed layout, and the vocabulary derivation refuses it. The central case writes a contract that
records the removed mode and asserts it is reported **and left byte-identical** — the "reported, not
migrated" property in one assertion.

**Supported paths still work.** A removed token is refused while an unknown token still degrades; an
external selection still resolves; the default memory root is the external root when no removed layout
exists; a disabled contract round-trips.

**CLI surface.** The CLI never advertises the removed member, parses the supported set, and hands a
removed token to the typed refusal. A separate case asserts the worktree-start tool documentation no
longer offers the removed mode.

**Operator reporting (integration).** Eight marked cases drive published enclosures and assert the
operator receives the typed refusal with the artifact named: the worktree-status packet and payload, the
configured admission, the terminal admission on a surviving contract, direct landing and its reader, the
unstarted-evidence fact, and the negative case that a removed-mode answer **never claims publication was
lost**.

**The instruction/documentation plane (`L12R-3`).** Thirteen parametrized surfaces, each pairing
forbidden old-doctrine phrases (asserted absent) with a required corrected phrase (asserted present):
the canonical `c-00`, `c-13`, `c-08` and three `c-03` templates, the package-data copy of `c-00`, five
`docs/` pages and one `system/defaults` example. A final case asserts the generated skill copy is
**byte-identical** to the canonical tree it is generated from. This group exists because the removal's
strongest claim — that nothing still teaches the mode — had no executable guard: a reverted canonical
skill propagated to all nine generated copies left every generator check green, and a wholesale revert of
`docs/architecture.md` left the whole unit population green.

**The two onboarding-root shapes (`D-34`, added by `260915-KS-L23`).** Five cases (`:820-931`) pin the
module's own answer about which onboarding roots it will measure. A leaf enclosure's memory worktree —
`worktrees/<code-repository>/<group>/memory-<worktree-name>/onboarding`, which is the exact root the
contract-scoped memory-quality route measures — is **supported** and resolves to `external` topology; four
lookalikes are refused, and the refusal names **both** supported shapes and the root it received; and
`check_missing_onboarding_main` (the CLI entry point, imported at `:64-66`) is driven end to end so the two
answers are shown to differ in one run: the worktree-shaped root is measured and reported as the root that
was asked for, while an unsupported root raises the refusal containing that root's own path. Before the
change the resolver raised out of the module for the worktree shape, so a curator running the module for a
leaf got a traceback where `memory_quality_check` answered for the same tree. The lookalike cases are the
point of the group: the `worktrees` segment plus the `memory-` prefix is what makes the shape decidable, and
an empty name after the prefix, a code worktree, a one-segment-short path and a `not-worktrees` lookalike are
each refused rather than guessed at.

### Conventions

The expected supported set is written out **literally** in the module rather than imported from
`SUPPORTED_MEMORY_MODES`, with a comment stating why: a change to the vocabulary must then be made in two
places, so the test cannot silently agree with a mistake. Both sides of every comparison therefore come
from different sources.

The corpus guard reads files from `_REPO_ROOT` (`parents[2]` of the test file) and fails with the
offending phrase in the message, so a revert names what it re-taught. Parametrized ids are built from the
path so a failure identifies the surface.

Integration-marked cases are separated by the marker rather than by filename, which is why one module
carries both hermetic and published-enclosure cases. The onboarding-root group is hermetic like the rest of
the unit population: it builds its own synthetic enclosure under `tmp_path` (and, for the CLI case, a real
one-file Git repository through the shared `init_repo`/`git` helpers) rather than reading this repository's
own worktrees.

### Invariants And Boundaries

**The module is registered and its evidence lane is declared.** It is registered under
`unit-regression` in `mcp/tests/test-evidence-lanes.toml`, and it is declared in two `consumers` lists in
`mcp/tests/evidence-lifecycle.toml`. The lane loader is fail-closed and is not loaded by ordinary pytest,
so a new module without a row ships unregistered under green suites; this module carries its row — and it
already had it, which is why this leaf's five added cases changed no lane and no catalog row. The one
import this pass added is a **production** entry point, `check_missing_onboarding_main` from
`memory_quality/integrity/check_missing_onboarding.py`, so the module now exercises the shipped CLI rather
than a re-implementation of its resolver.

**The case population, measured rather than restated.** At this leaf's base the module held **34** collected
cases (26 unit + 8 integration) and the working tree holds **41** (33 unit + 8 integration) — the five
onboarding-root cases are the difference. The instruction-corpus group is the case class
that fails when the corrected doctrine is reverted, and the operator group is the class that fails when
the typed refusal stops reaching the operator ahead of a generic `ValueError` clause.

**The card's earlier "46 collected cases, 38 unit and 8 integration" matches neither tree.** It is
superseded here rather than patched in place, because **no earlier history entry can be rewritten** (the
section is append-only): the count above is a measurement from this module, taken by AST over its own test
functions (38 at the base, 42 now, none generated in a loop) expanded by its two parametrized decorators
(13 corpus surfaces and the 4 refused-lookalike paths). A reader who needs a number should take it from the
tree, not from a count that a history entry recorded against a different one.

**A test module is not authority.** The corpus guard asserts that the *shipped* surfaces do not teach the
removed default; it does not prove that the copies were generated rather than hand-edited, which is what
the generator's own `--check` mode proves.

## Evidence

### Docs References

No Domain Documentation entries are configured in this memory root. These are repository-owned refusal,
migration-boundary and instruction-corpus assertions.

No configured domain evidence applies to the file-local claims above.

### Repo-Internal References

- The three pinned properties, each named with the failure it prevents. [1]
- The expected supported set is written literally, not imported, so a vocabulary change must be made twice. [2]
- The declared vocabulary holds no removed member. [3]
- A removed token is refused by name while an unknown token stays an invalid-argument error. [4]
- Existing state recording the removed mode is reported and left byte-identical. [5]
- The supported paths are unaffected: external still resolves, disabled still round-trips. [6]
- The CLI never advertises the removed member and hands a removed token to the typed refusal. [7]
- The tool documentation no longer offers the removed mode. [8]
- The operator receives the typed refusal with the recorded value, the supported set and the artifact. [9]
- A removed-mode answer never claims the publication was lost. [10]
- Both flag narrowers distinguish a typo from a removal. [11]
- Thirteen corpus and documentation surfaces are guarded against re-teaching the removed default. [12]
- The generated skill copy must equal the canonical tree it is generated from. [13]
- The module's evidence lane is declared under `unit-regression`. [14]
- **The leaf enclosure's memory worktree is a supported onboarding root, and the resolver reports the root it was given rather than the official one.** [15]
- **The four lookalike shapes refused structurally — a `not-worktrees` path, a code worktree, an empty name after the prefix, and a one-segment-short path.** [16]
- **The refusal names both supported shapes and the root it received, so it cannot send the caller in a circle.** [17]
- **The CLI entry point measured end to end: the leaf enclosure's root is measured and named, an unsupported root raises the refusal containing its own path.** [18]
- The module is declared in three evidence-lifecycle consumer lists: the shared curator-coherence support artifact's list and two further artifact lists. [19]

### Cross-Repo References

No cross-repository implementation evidence is required for these local refusal and corpus assertions.
