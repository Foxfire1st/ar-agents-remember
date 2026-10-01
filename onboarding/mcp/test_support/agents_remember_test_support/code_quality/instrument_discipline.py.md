# mcp/test_support/agents_remember_test_support/code_quality/instrument_discipline.py

## Governing Overview

[overview](overview.md)

## Purpose

Make an inadmissible measurement impossible to *state*. A count, a zero, a pass or a producer
identity is returned only when the instrument carries proof it could have produced the other
answer; when that proof is absent the module raises or returns a refusal reason instead of a
result.

This is the shipped form of one recurring fault class: a measurement taken by an instrument that
could not have detected what it claimed to look for, and a conclusion drawn from it. The four
functions below correspond to the four shapes that class took across
`260915_role-capsules-and-native-eve` — a text probe whose pattern could not match its target, a
capture that ran past the unit it was counting, a run whose crash was read as a pass, and a record
naming a producer that did not produce it.

## Code Commentary

### Logic

Four admissibility conditions, one per function group. Ranges are derived against the **current
432-line** source; the module was revised after this leaf's independent review (§Update History), and
every range on this card was re-derived rather than carried forward.

- `counted_pattern(pattern, text, probe=…)` (173-192) — the only way this module returns a count. It
  calls `_prove_probe` (157-170) first, then counts with `_scan` (153-154). Three conditions now
  refuse: the positive witness must match its own sample, the negative witness must not match its
  own, and — the revision's addition at 185-189 — **`pattern` must be the probe's own positive
  pattern**. The licence a probe carries belongs to the pattern it proved, not to whoever calls with
  it; a proved probe for one shape licenses no zero for another. The returned `PatternCount` (100-106)
  carries both witnesses, so the licensing evidence travels with the number.
- `capture_bounded_window(text, *, start_pattern, boundary_pattern, max_lines)` (202-247) — returns
  the `CapturedWindow` (109-117) the unit actually occupies. The window closes at the first of a
  blank line, a boundary line, or the line cap, and `closed_by` names which one did it: the four
  values are `blank line`, `boundary line`, **`line cap`** and `end of evidence`. The cap check now
  runs inside the loop and sets `closed_by = "line cap"` itself (229-231); before the revision the
  cap sat in the loop condition, so a window cut off at `max_lines` reported `end of evidence` and
  the lines it left unread were invisible. Because the boundary test is skipped on the start line
  itself, a table whose rows have no blank lines between them ends at the next row rather than
  swallowing the rest of the table. `_matching_line` (195-199) finds the opening line; a start pattern
  matching nothing is a refusal, not an empty window.
- `crash_scan(text)` (250-286) — returns a `CrashScan` (120-127) carrying the crash line numbers, the
  pass line numbers, and `crashed_before_pass`. `check_artifact_refusal(...)` (300-351) is the verdict
  built on it and now names **four** refusals: a transcript whose crash precedes a pass claim
  (`crash_scan`'s own finding); an artifact evidencing **no run at all** — no recorded exit status
  and no producer transcript; a run that **exited non-zero and reported no result at all**, which is
  the shape a crash takes when it leaves no traceback and so cannot be seen by `crash_scan`; and the
  vacuity refusal, when nothing shows the check could fail and the caller has not stated
  `can_fail_evidence`.
- `producer_identity_refusal(record, *, worktree)` (354-370) — refuses a `ProducerIdentity` (130-136)
  whose named script is not a file in the worktree, or whose command or revision is blank.
  `reproduce_recorded_producer(...)` (373-432) then re-runs the producer through `sys.executable` and
  compares sha256 digests byte-exactly, returning a `ProducerReproduction` (139-146). Its scratch
  output now goes to a `tempfile.TemporaryDirectory` (395-398) instead of beside the recorded
  artifact, so re-running a producer cannot write into — or temporarily overwrite — the evidence it
  is being checked against. A producer that exits non-zero, and a producer that exits 0 without
  writing its output argument, are both reported as `matches=False` with `produced_digest=None`
  (405-422) rather than raising.

Two further module-level declarations are contract, not configuration. `TRANSCRIPT_EXIT` (67-71) is
the revision's second exit-status rule: an exit status is evidence of a run only where the artifact
records it **as one** — on a command line carrying its status, or on a standalone status line —
because the older bare `EXIT_CODE` (61) also matched prose that merely describes the convention
("it will exit 0 on success, exit 1 on a mismatch"), which is how a document containing no run at all
came to satisfy the no-run refusal. `EXIT_CODE` is retained and is still live: the suite uses it as
the contrast that shows the narrow pattern refusing what the loose one matched. `NONZERO_FINDINGS`
(79) is the vacuity rule's quantity: the evidence is a **non-zero** count of findings, errors or
violations, because `0 errors found; no finding was produced` is a disclaimer and a disclaimer is not
evidence that the check can fail. It is a named heuristic, not a proof — it under-admits, and a result
phrased otherwise has to be stated through `can_fail_evidence`. `CRASH_MARKERS` (42-50) and
`PASS_MARKERS` (54-59) are kept deliberately narrow so a transcript that merely *discusses* a failure
is not flagged as one.

Three dataclasses are inputs, three are outputs: `Witness` (82-89) and `Probe` (92-97) are what the
caller must supply to license a pattern, `ProducerIdentity` is what a record must supply to be
reproducible, and `PatternCount` / `CapturedWindow` / `CrashScan` / `ProducerReproduction` are the
results that carry their own evidence.

### Conventions

Every refusal is a `ValueError` built by `_refuse` (149-150) and prefixed with `REFUSAL_PREFIX` (38)
— `instrument discipline:` — so a caller can distinguish an inadmissible measurement from a bad
argument. Private helpers are `_`-prefixed and the module exposes no CLI and no registry entry: it is
a helper library for the tests and for verification work, not a quality gate.
`_recorded_exit` (289-292) and `_reports_findings` (295-297) are the two thin readers the verdict
consults, kept separate from the patterns they apply so the heuristic each encodes is named once.

`check_artifact_refusal` takes a `probe` and re-derives it with `_prove_probe` rather than trusting
the caller, so no path reaches an admissibility verdict without having licensed its own pattern
first. This is the module enforcing its own rule on itself.

### Invariants And Boundaries

- **A count carries the licence for the pattern it counted.** `counted_pattern` proves its probe
  *and* binds the counted pattern to the probe's own positive pattern, so neither the historical fault
  (a grep returning 0 and being read as "the family is not live") nor its successor (a proved probe
  lent to an unrelated pattern) can be expressed through this surface.
- **A captured count states the boundary that closed it, the cap included.** `closed_by` is one of
  `blank line`, `boundary line`, `line cap`, `end of evidence`. A caller that reads `items` without
  reading `closed_by` has what it needs to notice it captured the wrong unit; a capped capture and a
  complete one are otherwise the same shape.
- **A pass claim after a crash is not attributable to a completed run.** `crashed_before_pass` is
  computed as the last pass line falling after the first crash line. `crash_scan` can only see a crash
  that left a marker, which is why the exit-status refusal exists beside it and not instead of it.
- **Vacuity is judged on a non-zero result, never on the presence of a word.** The earlier
  `^[\W\d]*(?:finding|error|violation)` scan had two defects and both are now closed: it lacked a
  working word-boundary assertion (`\b` cannot match between the `g` of `finding` and the `s` of
  `findings`), and it matched the word in a *disclaimer* such as `0 errors found`. A hand-written
  fixture passed with the first defect in place; only the real artifact caught it, and only a
  non-zero-count rule closes the second.
- **An exit status is evidence of a run only where the artifact records it as one.** Prose describing
  an exit convention is not a run, and a non-zero status with no result after it is a crash.
- **Reproduction never writes beside the evidence it is checking, and it answers rather than
  raises.** The scratch path is a `TemporaryDirectory`; a non-zero exit and a missing output argument
  are both `matches=False`.
- **Byte-exactness is the standard for reproduction.** A near-match is a different producer or a
  different input; `matches` compares sha256 digests, never a normalized form.

### Todos

- The module docstring (22-24) still says these helpers "never touch the filesystem except in
  `producer_identity_refusal`, which is handed the paths it may read". That is **not accurate and was
  not accurate before the revision either**: `reproduce_recorded_producer` reads the recorded
  artifact, creates a scratch directory and executes a subprocess. Recorded here rather than silently
  repeated; correcting the docstring is a code change and belongs to the owning leaf, not to this
  seat.
- The `\b` above is retained as history, not as an open gap. No further known gap is carried by this
  file at this revision.

## Evidence

### Docs References

No external Domain Documentation source is configured for this repository: `system/sources.md`
carries no entries, so no `Domain Documentation` category is available to cite. This card records
repository-owned behavior from the source references below; no external documentation claim is made.

External domain documentation is not configured in this memory root.

### Repo-Internal References

The source owners below establish these file-local behaviors; this read does not claim a test or
certification pass. The four functions are the historical faults' shipped countermeasures, and the
contract test that pins them is cited with the source. Every range below was re-derived against the
current 432-line source.

- The refusal prefix every inadmissible-measurement error carries. [1]
- Crash text that means a command failed, kept narrow so a transcript discussing a failure is not flagged. [2]
- Text that claims the thing a crash would have prevented. [3]
- The loose exit-status probe, retained as the contrast the narrow rule is checked against. [4]
- The narrow rule: an exit status is evidence of a run only where the artifact records it as one. [5]
- The vacuity rule's quantity: a non-zero count of findings, errors or violations. [6]
- One known answer a pattern must reproduce before its count means anything. [7]
- The positive and negative witness pair that licenses a pattern. [8]
- A count over real text, carrying the witnesses that licensed it. [9]
- The lines a unit occupies, and which boundary closed the window (its own `closed_by` field names that boundary). [10]
- Whether a captured transcript's producer ran to completion (its own `crashed_before_pass` field). [11]
- The three facts a reproducible record must carry. [12]
- The outcome of re-running a recorded producer against the recorded artifact (its own `matches` field, a byte-exact digest comparison). [13]
- The shared precondition: a probe that cannot see its own positive, or cannot exclude its own negative, is refused. [14]
- The only counting surface, refused unless the probe was proved first **and the counted pattern is the one it proved**. [15]
- The unit-bounded capture that names the boundary closing it, the line cap included. [16]
- A pass line printed after a crashed command is not attributable to that run. [17]
- The exit status the artifact records as a run, or `None` when it only describes one. [18]
- Whether the artifact reports a non-zero result of its own. [19]
- The admissibility verdict over a recorded artifact, with its four named refusals. [20]
- A record naming a producer absent from the package, or with no command or revision, is refused. [21]
- Reproduction is byte-exact, writes its scratch output outside the evidence directory, and answers `matches=False` instead of raising. [22]
- The five classes of contract test that pin these behaviours against the historical cases. [23]

### Cross-Repo References

No separate cross-repository protocol is established by this file. The configured cross-repository
allowance is empty and no external source is relied upon here. The historical artifacts the checks
were proved against live under the previous master's task root in the coordination tree, which is
task-local evidence rather than a repository boundary; the contract test cites them by absolute
coordination path and skips when that package is absent.

No cross-repository evidence is required for these file-local claims.
