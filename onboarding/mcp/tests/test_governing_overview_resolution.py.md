# mcp/tests/test_governing_overview_resolution.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/tests/test_governing_overview_resolution.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-09-17T19:30+02:00 |
| lastVerifiedCommitHash | `5e4eb651be0691e2d2a90ea59bc662f92050db25` |
| lastVerifiedCommitDate | 2026-09-18T20:35:53+02:00|
| reviewedWorkingCandidate | `ar/260915-caps-l20-ar` uncommitted source; base `621db8981aba09a6f17880d2138cf76a37332c6c` |
| governingOverview      | `overview.md`                              |

## Governing Overview

[overview](overview.md)

## Purpose

The falsifiable guard for `memory_quality/integrity/governing_overview_resolution.py`
(D3/D16, `260915-CAPS-L20`). Its subject is **discrimination**, not coverage: each case
seeds the defect it claims to catch and asserts the refusal, and each carries its own
non-vacuity control **inside the same tree** — a resolving card that must stay green — so
a checker that flagged everything could not pass.

## Code Commentary

### Logic

One case, and its shape is the point. It seeds three shapes at once — a card with a live
field and a dead body link (D3's shape), a card whose field no base resolves and which is
broken in the body too (D16's shape, the card the per-declaration rule exists for), and
two observation shapes — beside a clean card and a route overview that must stay green.
It then asserts the exact finding set as `(card, code)` pairs, the two counters
independently (`unresolvedField` 1, `unresolvedLink` 2), the observation list, the walk
population and the flagged count.

The per-declaration assertion is the one that matters most. Asserting a **count** of
findings cannot show that both representations were reported; asserting the identity of
the set can. The card seeded broken in both must appear **twice** in `findings`, once per
code, because the two declarations fail independently.

The observation axis is asserted in both of its live forms rather than only one. A card
that declares the field and carries no `## Governing Overview` section at all, and a card
whose section carries no link, are both observed and neither is failed — with
`assertFalse(result.ok)` above them, so a checker that turned observations into findings
would red this case.

### Conventions

Both card bodies are module-level templates so the seeded shape is readable as markdown
rather than as an escaped string, and `_write_card` is the single seam that materialises
one — with `section=False` selecting the no-heading template. The whole tree is built
inside a `TemporaryDirectory`, so the case writes nothing outside `/tmp` and is safe to
run in parallel with the rest of the unit population.

### Invariants And Boundaries

- The case never walks this repository: its root is a temporary directory holding exactly
  six markdown files, and it asserts `cardsWalked == 6` so a widened walk would red it.
- A resolving card and a route overview sit in the same tree as the seeds; a checker that
  failed anything it saw could not pass.
- Observations are asserted by card **and** by code, and `ok` is asserted `False`, so an
  observation promoted to a finding fails the case twice over.
- The module is one case, not four, and the second half of the defect — the wiring that
  carries the findings into the curator's gated repair set — lives in
  `mcp/tests/test_memory_quality_runs.py` instead, because the silence was the product
  defect and a correct checker whose findings never reach the actionable set still reports
  clean.
- **Correction made by the `260915-CAPS-L20` curator, recorded here rather than edited
  into the source (this seat writes onboarding only):** the module docstring's lines 12
  and 16 still read *"Two cases, not four"* and *"this module spends one and the wiring
  case beside it … spends the other"*. The shipped module carries **one** case; the
  consolidation this leaf made left the sentence stale, and the authoritative statement of
  the delta is `grep -c '    def test_'` — 1 here and 11 → 12 in
  `test_memory_quality_runs.py`, a net **+2** that reconciles to the measured battery
  delta. The card records the shipped fact rather than the docstring's draft.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The `(card, code)` set assertion is what pins per-declaration reporting; the card broken in both appears twice. | `test_every_dead_declaration_form_is_reported_and_no_clean_card_is` | mcp/tests/test_governing_overview_resolution.py:92-155 |
| The two counters are asserted separately, so a first-match-wins regression cannot hide behind a total. | "self.assertEqual(result.unresolvedField, 1)" | mcp/tests/test_governing_overview_resolution.py:143-143 |
| None | `test_every_dead_declaration_form_is_reported_and_no_clean_card_is` | mcp/tests/test_governing_overview_resolution.py:92-155 |
| The walk scope is pinned so a widened root would red the case. | "self.assertEqual(result.cardsWalked, 6)" | mcp/tests/test_governing_overview_resolution.py:149-149 |
| The single seam that materialises a seeded card, with `section=False` selecting the no-heading template. | `_write_card` | mcp/tests/test_governing_overview_resolution.py:66-88 |
| The check under test, its three-bases field probe, and the observation classification. | `check_governing_overview_resolution` | mcp/src/agents_remember/memory_quality/integrity/governing_overview_resolution.py:211-251 |
| The second half of the same defect: a dead governing overview must arrive in the gated repair set the curator's loop reads. | `test_a_dead_governing_overview_reaches_the_gated_repair_set` | mcp/tests/test_memory_quality_runs.py:355-458 |
| The population ceiling the module's one-case budget was measured against. | `unit_case_budget` | pyproject.toml:244-244 |
| The collector that refuses the entire run when the population exceeds that ceiling. | `pytest_collection_finish` | mcp/tests/conftest.py:148-159 |

## Update History
- 2026-09-18T17:30:57+00:00: Generated citation repair: `pytest_collection_finish` repointed to mcp/tests/conftest.py:132-143. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T15:12:32+00:00: Generated citation repair: `unit_case_budget` repointed to pyproject.toml:244-244. No content impact: mechanical anchor-range projection bound to citation source snapshot 418f5ce580b3710b5d8fe417585d48fd22eccd55346c84b05f01fef243a17917; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T14:49:10+00:00: Generated citation repair: `pytest_collection_finish` repointed to mcp/tests/conftest.py:143-154. No content impact: mechanical anchor-range projection bound to citation source snapshot 4fb0a4d92072964079a2a144c1f1da15ff07327804a09730959bc69f38a7e98f; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: `unit_case_budget` repointed to pyproject.toml:214-214. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
2026-09-18T06:55+02:00 — 260915-CAPS-L24 curator: **stale citations repaired in this document.** This leaf's curator re-derived every failing citation row against the file it cites: each Anchor cell now names text that exists inside the cited range, each Source cell is a plain `path:start-end` in bounds of the file as it stands, and a claim whose construct the source no longer carries was re-worded to what the source now says rather than re-pointed at something adjacent. Mechanically regenerable ranges were rewritten by the shipped citation fixer; the rest were repaired by reading the source. No verification stamp advanced on content alone: the candidate is uncommitted and the governed closeout owns the real code and memory commits.
- 2026-09-18T01:52:52+00:00: Generated citation repair: `unit_case_budget` repointed to pyproject.toml:168-168. No content impact: mechanical anchor-range projection bound to citation source snapshot 1b549a05c7448b2578454675e173eaf65501170ee85e72dbbfb2c4a4132b3242; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T19:30+02:00 — 260915-CAPS-L20 curator: created this card for the new test module the leaf added, so the new source file has its 1-to-1 onboarding pair before closeout. Verification metadata is left at the leaf's frozen code base `621db8981aba09a6f17880d2138cf76a37332c6c`; the governed closeout stamps the real code commit. The card records the shipped case count (1) and names the module docstring's stale "two cases" sentence as a correction rather than silently repeating it — this seat writes no source.
