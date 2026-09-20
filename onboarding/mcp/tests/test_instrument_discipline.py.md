# mcp/tests/test_instrument_discipline.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_instrument_discipline.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-18T12:30+02:00 |
| lastVerifiedCommitHash | `3888cd8600e39a52c540d6038820759e3d4ffa7a` |
| lastVerifiedCommitDate | 2026-09-20T20:02:13+02:00|
| reviewedWorkingCandidate | `ar/260918-tsip-l1-ar` uncommitted source (this file is an addition, 537 lines, materially revised after the leaf's independent review); base `f031314345b674d0733c4619fe34d78c1b02ba26` |
| governingOverview | `overview.md` |

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Pin the admissibility conditions of
`mcp/test_support/agents_remember_test_support/code_quality/instrument_discipline.py` against the
historical artifacts they were written for, in **both** directions: the shipped function refuses the
artifact that carried the fault, and it accepts the artifact that replaced it. A check with only the
refusal direction cannot be shown to be non-vacuous, which is the module this suite exists to guard.

Most constants in this file are evidence transcribed from the record of
`260915_role-capsules-and-native-eve`, at the path named in its own comment, so the cases test the
functions against real bytes rather than against fixtures written from the same mental model as the
pattern. That distinction is why the suite's own history is worth keeping on the card: it passed
16/16 while the module it tests still carried a `\b` that could not match the plural `findings`.

## Code Commentary

### Logic

**Twenty-seven cases, and which number this card means.** The file defines **26 `def test_` methods**
inside five classes plus **1 module-level `def test_` function**, and pytest collects **27**. There is
**no parametrisation** (`grep -c parametrize` = 0) and the module uses **no subtests**
(`grep -c subtests` = 0), so the run's `27 passed` and the file's 27 test functions are the same 27 —
the 26-versus-27 gap is entirely the one module-level function, not a parametrised case. This card
reports **27** (the collected/passed count, which is what a run reports) and states the 26+1
decomposition beside it, because a bare "26" would undercount the suite and a bare "27" would not
explain itself. Both figures were measured on this candidate: `grep -c '^    def test_'` = 26,
`grep -c '^def test_'` = 1, `pytest --collect-only -q` → `27 tests collected`.

- `PatternProbeWitnessTests` (129-179), **4 cases** — a probe that cannot match its own positive is
  refused; a probe whose negative witness matches is refused as non-discriminating; the corrected
  `n/a`-link pattern counts the family the faulty one could not (the whole fault in two lines: the
  record's own row, which `NA_FAULTY_PATTERN` (69) cannot match and `NA_CORRECTED_PATTERN` (71) does);
  and — the revision's addition — a pattern the probe did **not** prove is refused even though the
  proof itself is sound, because a licence binds to the pattern it proved.
- `BoundedCaptureTests` (182-231), **4 cases** — the row-bounded capture over `CHECKLIST_TAIL` (51-61)
  yields `start_line == end_line == 2`, `closed_by == "boundary line"`, 21 commas and 22 items; the
  same start line captured to the next blank line takes the following table rows with it, so the count
  measures the table rather than the row; a window cut off at `max_lines` reports `closed_by ==
  "line cap"` and leaves exactly the unread lines visible (this is the case that pins the repair: the
  earlier capture reported `end of evidence` with 391 lines still below it); and a blank line closes
  the window on its own, observed as the third boundary the docstring names.
- `CrashReadAsPassTests` (234-247), **2 cases** — `E13_CRASHED` (78-84) is caught with
  `crashed_before_pass is True`; `E13_REPAIRED` (87-92) is clean.
- `ArtifactAdmissibilityTests` (250-365), **8 cases** — the shipped declared-tools baseline is
  admissible; a transcript with no run and no verdict is refused for having no exit status and no
  producer transcript; a run with no stated way to fail is refused as **vacuous** and then becomes
  admissible once `can_fail_evidence` states how the producer fails; a crashing artifact is refused
  before its result is read; a run that **exited non-zero with no result** is refused as a crash even
  though `crash_scan` sees no crash marker; **prose that describes the exit convention is not a run**
  (the case asserts the loose `EXIT_CODE` still matches the prose while the narrow rule refuses it);
  a **clean disclaimer** (`0 errors found; no finding was produced`) is not evidence the check can
  fail; and an unproved probe refuses **before any verdict is reached**.
- `ProducerIdentityTests` (368-520), **8 cases** — a producer named in prose and absent from the
  package is refused; a present producer without a command or without a revision is refused; a fully
  identified producer passes; a record naming **no producer script at all** is refused by its own
  branch rather than by the next refusal answering for it; reproduction is byte-exact so a different
  table is not a reproduction; a producer that **exits non-zero** is not a reproduction even when it
  wrote the recorded bytes; a producer that **exits 0 writing nothing** is a mismatch rather than an
  exception; and the reproduction **does not write beside the recorded artifact** — the producer is
  made to report the directory it was handed, and the case asserts that path is not the evidence
  directory.

`_probe` (112-126) is the shared licensing probe: the corrected `n/a` pattern as positive against
`NA_LINK_ROW` (64-67), the faulty anchor-cell-first pattern as negative against the same sample.

The final case (523-537) is not a unit case. It re-reads the published evidence object at
`memory-refresh-finding-21-routes.json` under the previous master's task root and asserts that
`ATTESTATION_MESSAGE` (24-43) is byte-equal to the record's `message`, is 1,343 characters, carries 21
commas, and is paired with `route_count == 21` and 21 routes. It **skips** when that package is absent
from the workspace, so the transcription is checked where the record still exists and does not fail
the suite where it does not.

### Conventions

The evidence constants are module-level and each carries a comment naming the path and line range it
was transcribed from. `REPO_ROOT` (20) is unused by the cases and retained as the module's declared
repository anchor. Assertions state the historical number rather than a recomputed one, because the
number *is* the claim. Class names describe the fault, not the function:
`CrashReadAsPassTests`, not `CrashScanTests`.

`E13_CRASHED` (78-84) is deliberately **not** presented as a transcription. The raw
`E13-render-verification.txt` was overwritten in place by its own repair, so the constant is a
**reconstruction in the verdict's own terms** — the comment at 73-77 says so and names the verdict and
the lines it cites. That is the honest form of a fixture whose original bytes no longer exist, and it
is recorded here rather than described as a transcription.

### Invariants And Boundaries

- **Both directions are asserted for every function.** A refusal-only case proves the function rejects
  something; only a paired acceptance case shows it would have passed a good artifact, so the check is
  not vacuous. The revision added cases in the refusal direction for enforcement points that had
  escaped mutation testing, which is the same rule applied where coverage was thin.
- **A refusal case asserts the refusal's own reason**, not merely that something was raised — the
  revision's cases match on `"line cap"`, `"a crash, not a pass"`, `"wrote no artifact"` and
  `"names no producer script"`, so a case cannot pass by being refused for the wrong cause.
- **The evidence is transcribed where the bytes exist, and reconstructed where they do not.**
  `ATTESTATION_MESSAGE` is the record's bytes and the transcriber case holds it to that; `E13_CRASHED`
  is a reconstruction and says so.
- **The suite does not run the historical artifacts.** It asserts against transcribed text and, for
  reproduction, against producers it writes itself under `tmp_path`. The executed positive controls
  against the real historical artifacts are the leaf's census report, not this file.
- **A skip is not a pass.** The transcriber case skips when the `260915` evidence package is absent; a
  green run in a workspace without that package has not checked the transcription.
- **Fixtures cannot license a pattern.** The suite's own history is the proof that it is necessary and
  not sufficient: 16 cases passed with the module's `\b` bug in place, and only the real artifact
  caught it. The later disclaimer defect has the same shape — a fixture cannot show that a pattern
  admits too much.
- **A producer that fails is a non-reproduction, not an exception.** The reproduction cases pin
  `matches=False` with `produced_digest is None` for both the non-zero-exit and the wrote-nothing
  shapes, because the helper's contract is to answer the question "did this reproduce?".

### Todos

None. This card was written by reading the current 537-line source in the code worktree and by
measuring the case population on this candidate; no case in this file is known to be vacuous, and no
case was added or removed by the curator.

## Docs References

No external Domain Documentation source is configured for this repository: `system/sources.md`
carries no entries, so no `Domain Documentation` category is available to cite. These are
repository-owned fixture and assertion contracts; no external library behavior is inferred.

| Finding | Anchor | Source |
| --- | --- | --- |
| External domain documentation is not configured in this memory root. | N/A | N/A |

## Repo-Internal References

The retained source anchors below support the fixture roles and assertion boundaries described above.
The historical evidence constants live under the previous master's task root in the coordination tree
and are cited by the source that transcribes them, not linked as durable memory. Every range below was
re-derived against the current 537-line source.

| Finding | Anchor | Source |
| --- | --- | --- |
| The shared licensing probe: corrected pattern positive, faulty pattern negative, both against the record's own row. | `_probe` | mcp/tests/test_instrument_discipline.py:112-126 |
| The record's 1,343-character attestation message, transcribed. | `ATTESTATION_MESSAGE` | mcp/tests/test_instrument_discipline.py:24-43 |
| The checklist row carrying that message, in a table with no blank lines between rows, and the two rows below it. | `ATTESTATION_ROW`; `CHECKLIST_TAIL` | mcp/tests/test_instrument_discipline.py:48-61 |
| The live `n/a`-link row, the pattern that returned 0 on it, and the pattern the curator ran instead. | `NA_LINK_ROW`; `NA_FAULTY_PATTERN`; `NA_CORRECTED_PATTERN` | mcp/tests/test_instrument_discipline.py:64-71 |
| The `E13` transcript whose crashed `awk` invocations sit above the pass line — a reconstruction in the verdict's own terms, because the raw file was overwritten in place — and the repaired producer's clean transcript. | `E13_CRASHED`; `E13_REPAIRED` | mcp/tests/test_instrument_discipline.py:78-92 |
| The shipped declared-tools baseline and the silent before-file that evidences no run. | `DECLARED_TOOLS_RESULT`; `DECLARED_TOOLS_SILENT` | mcp/tests/test_instrument_discipline.py:96-109 |
| A zero from a text probe is admissible only when the probe was shown to see the other answer — and only for the pattern it proved. | `PatternProbeWitnessTests` | mcp/tests/test_instrument_discipline.py:129-179 |
| A count taken from a capture that ran past its unit is a count of something else, and a capped window says so. | `BoundedCaptureTests` | mcp/tests/test_instrument_discipline.py:182-231 |
| A pass line printed after a crashed command does not describe the command that produced it. | `CrashReadAsPassTests` | mcp/tests/test_instrument_discipline.py:234-247 |
| A clean result is evidence only when the artifact also shows the check could have failed; an exit status with no result is a crash and prose is not a run. | `ArtifactAdmissibilityTests` | mcp/tests/test_instrument_discipline.py:250-365 |
| A record names the producer that made it, or it is not a record of a measurement — and a failing producer is a non-reproduction, not an exception. | `ProducerIdentityTests` | mcp/tests/test_instrument_discipline.py:368-520 |
| The transcription is the one the record carries, checked against the record where it still exists. | `test_the_evidence_transcription_is_the_one_the_record_carries` | mcp/tests/test_instrument_discipline.py:523-537 |
| The module whose admissibility conditions these cases pin. | `counted_pattern`; `capture_bounded_window`; `check_artifact_refusal`; `producer_identity_refusal` | mcp/test_support/agents_remember_test_support/code_quality/instrument_discipline.py:173-370 |
| The narrow exit-status rule and the vacuity rule's non-zero quantity. | `TRANSCRIPT_EXIT`; `NONZERO_FINDINGS` | mcp/test_support/agents_remember_test_support/code_quality/instrument_discipline.py:67-79 |
| The lane this module is registered in, so the fail-closed manifest admits it. | "mcp/tests/test_instrument_discipline.py" | mcp/tests/test-evidence-lanes.toml:290-290 |

## Cross-Repo References

No separate cross-repository protocol is established by this file. The configured cross-repository
allowance is empty and no external source is relied upon here.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repository evidence is required for these file-local claims. | N/A | N/A |

## Update History
- 2026-09-20T17:17:10+00:00: Generated citation repair: "mcp/tests/test_instrument_discipline.py" repointed to mcp/tests/test-evidence-lanes.toml:290-290. No content impact: mechanical anchor-range projection bound to citation source snapshot 02d8f0b256fe50bf7458ae56160b7e02e4466423e76d3ab197e12477f370f5b8; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T14:49:10+00:00: Generated citation repair: "mcp/tests/test_instrument_discipline.py" repointed to mcp/tests/test-evidence-lanes.toml:233-233. No content impact: mechanical anchor-range projection bound to citation source snapshot 4fb0a4d92072964079a2a144c1f1da15ff07327804a09730959bc69f38a7e98f; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-18T12:30+02:00 — 260918-TSIP-L1 curator, **second pass** (uncommitted change set on
  `ar/260918-tsip-l1-ar`, base `f0313143`): the leaf's independent review returned three blocking
  findings, the fix worker revised this suite **350 → 537 lines and 16 → 27 cases**, and the body was
  **corrected, not annotated**. The case count was **re-measured on this candidate** rather than
  carried: `grep -c '^    def test_'` = **26** class methods, `grep -c '^def test_'` = **1**
  module-level function, `pytest --collect-only -q` → **`27 tests collected`**, with **0**
  `parametrize` decorators and **0** subtests — so the 26-versus-27 gap is the module-level
  transcriber test and nothing else, and this card reports **27** with the 26+1 decomposition stated
  beside it. The 11 added cases pin the enforcement points that had escaped mutation (line cap, blank
  line, unproved probe before verdict, record naming no producer script, producer exiting non-zero)
  and close the revision's five defects: the pattern-licence binding, the unwritten output argument,
  the write-beside-the-evidence behaviour, the loose exit-status rule, and the vacuity rule that
  admitted a disclaimer. Every range on the card was re-derived (the class blocks moved
  `PatternProbeWitnessTests` 126-166 → 129-179, `BoundedCaptureTests` 169-188 → 182-231,
  `CrashReadAsPassTests` 191-204 → 234-247, `ArtifactAdmissibilityTests` 207-252 → 250-365,
  `ProducerIdentityTests` 255-333 → 368-520, `_probe` 109-123 → 112-126, the transcriber case
  336-350 → 523-537, and the constants likewise). The card now also records what the suite itself
  states: `E13_CRASHED` is a **reconstruction in the verdict's own terms**, not a transcription of
  bytes that no longer exist. `lastUpdated` tracks this body edit; `lastVerifiedCommitHash`/
  `lastVerifiedCommitDate` are deliberately unchanged because the source is an uncommitted candidate
  and the governed closeout owns the real code commit. This seat writes no source and ran no product
  test beyond read-only collection.

- 2026-09-18T11:46+02:00 — 260918-TSIP-L1 curator (uncommitted change set on `ar/260918-tsip-l1-ar`,
  base `f0313143`): created this card for the new test module the leaf added, so the new source file
  has its 1-to-1 onboarding pair before closeout. The shipped case count was measured on that
  candidate rather than taken from prose (**16**: 15 class methods + 1 module-level function), and
  every range was derived by reading the then current 350-line source. The card recorded the suite's
  own limitation — those 16 cases passed while the module under test still carried the `\b` bug, so a
  hand-written fixture cannot license a pattern. Verification metadata is left at the leaf's frozen
  code base `f031314345b674d0733c4619fe34d78c1b02ba26` with the reviewed working candidate named.
