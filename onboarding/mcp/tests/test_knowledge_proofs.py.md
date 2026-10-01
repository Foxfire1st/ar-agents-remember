# mcp/tests/test_knowledge_proofs.py

## Governing Overview

[tests route overview](overview.md)

## Purpose

**The MIK-R28 cases: tests that prove an invariant are first-class proof entries.** The module covers
rule 2 (both evidence forms, the curator's facet, unresolvable evidence reported), rule 4 (the `proofs` of
the `invariant` and `family` views of a converted tree, and none for a database), rule 5 (the index's
"without proof" list and the informational checklist section) and rule 6 (migrated evidence listed, then
turned into a proof by a curator pass through the writer). Rule 3 and the stale-proof clause are not
covered here: by architect ruling they belong to L08 and L03.

## Code Commentary

### Logic

- **Rule 2, the parser.** A parametrized case reads `path::Class::method` as `Class.method`, `path -k name`
  (bare, quoted, backticked, bracketed, parenthesized, double-quoted), `-k` expressions that name only the
  file, a bare test module, helper modules that are never reported, and text with no test. A second case checks that a file
  named with a test anywhere in the evidence is not also reported bare, in both string orders.
- **Rule 2, the writer.** Both forms become `PRF-` proofs with symbol anchors once `proofs` carries a
  facet; an absent `-k` test and a bare file are `unresolvable`, and the rendered report says so. A proof
  waits for the curator's facet: no sidecar is written until it is authored, the report offers the
  statement as a draft, and a blank facet is refused and writes nothing.
- **Rule 4.** A review tree (`write_review_tree`) with a proven and an unproven invariant: the `invariant`
  view carries the proof or `[]`, the `family` view carries every member's proofs, and no pass or result
  key exists. The parity database fixture's `invariant` and `family` reads, and the other views, carry no
  `proofs`. A family whose members have no proof shows `[]`.
- **Rules 5 and 6.** The index lists live invariants without proof and excludes a retired one. The
  checklist renders the section as information: the wire summary is identical with and without the list,
  the count stays 0, and an unconverted checklist has no section. Migrated evidence is listed with its
  named test, the controller hands exactly that list to the checklist (`None` for an unconverted tree), and a
  writer pass with `invariant_id` and `proofs` writes the proof and empties the list. The list reuses the
  cached index and reports a refused cache location as `unreadable` without creating it.

### Conventions

- The writer cases build their worlds with `knowledge_writer_test_support`; the view and list cases use
  `knowledge_index_test_support`'s review tree. Both are catalog rows this module consumes (see
  `evidence-lifecycle.toml`).

### Invariants And Boundaries

- No case runs a test or asserts a pass: a proof is what its test demonstrates, not a result.
- The module is registered in the `unit-regression` lane (`test-evidence-lanes.toml:112`).

### Todos

None recorded.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is the requirement packet `MIK-R28@v1` of task
`260928_maintained-invariant-knowledge` (with the architect rulings in `28_first-class-test-proofs.json`);
it lives outside the code and memory repositories, so it is named here and not cited as a row.

No configured live documentation source was available for this pass.

### Repo-Internal References

The cases, by rule.

- The module's statement of the rules it covers. [1]
- The writer runs as this leaf's owner. [2]
- The parser's forms, expressions and helper modules. [3]
- No bare row for a file named with a test elsewhere. [4]
- Both forms become proofs once faceted; unresolvable evidence is reported. [5]
- A proof waits for the curator's facet. [6]
- The view cases' tree and read helper. [7]
- Invariant and family views carry their proofs. [8]
- A database read and the other views carry none. [9]
- A family with no proof shows `[]`. [10]
- Live invariants without proof; a retired one is excluded. [11]
- The checklist section is information that moves no count. [12]
- Migrated evidence is listed, then a curator pass writes the proof. [13]
- The cached index is reused and an unreadable one reported. [14]

### Cross-Repo References

No meaningful cross-repo references found: every case builds its own temporary code and memory
repositories.

No cross-repo boundary is crossed by this file.
