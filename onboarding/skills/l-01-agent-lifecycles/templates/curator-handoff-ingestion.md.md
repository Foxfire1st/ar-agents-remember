# skills/l-01-agent-lifecycles/templates/curator-handoff-ingestion.md

## Governing Overview

[overview](../overview.md)

## Purpose

The Curator's reference for turning producer hand-off lists into knowledge: the keys the Curator authors beside the producer's thirteen fields, the writer's input sections, admission of new records and decision records.

## Code Commentary

The producer contract in `templates/curator-handoff-list.md` keeps the thirteen entry fields (nine producer, four Curator) unchanged; this file holds only what the Curator authors. Before a list entry becomes an invariant the Curator adds `scope` (`applicability`, `conditions`, `exclusions`, all required; `[]` means examined and empty), and missing scope is `unfilled_curation_scope`, reported per entry even in a dry run. Further Curator keys are `admission`, `status`, `invariant_id`, `supersedes`, `proofs` and `title`; a joint obligation is a `family` item in `records`, never an entry key. It describes where records land in the memory repository (`knowledge/<kind-dir>/<ID>-<slug>.json`, schema `ar-<kind>/v1`), family routes, the writer's input sections used by `agents-remember knowledge-ingest` and the mounted `knowledge_write` (invariant entries, other authored records, history rows, local handles, writer-filled values and writer checks), the admission rule that every new invariant, family and decision states an admission criterion with a one-sentence justification, and decision records with at least two ordered alternatives, exactly one chosen. Curator role and reference files (`reference/curator/knowledge-ingest.md`, `worklist.md`, `governing-sources.md`, `card-formats-and-citations.md`) point into its sections.

The candidate template requires a one-line title of up to 80 characters for a new rule. A revised legacy rule may remain untitled and the writer returns a note. The reader uses the first six words until a title is recorded. A title-only edit preserves the revision.

The handoff leaves revision standing and the current writer stamp to the product. The author supplies retirement where appropriate and each decision's own status vocabulary. A history carries Curator judgments beside product-written `written` and `review` facts.

When both sides of a master merge changed a dependent, the Curator plans the resolution through `knowledge_write` with the master contract, open crossing identifier and authorization reference. The handoff names the existing dependent ID, resolved links and confirmation. The plan uses `commit: false` and the reviewed apply uses `commit: true`. The template lists both `dependent` and `weakness` among the accepted record kinds.

The ingestion template also documents consolidation-pass authoring: `stands` and `unresolved` dispositions with `testsRun`/`testsNotRun`/`noProofRecorded` on invariant and family rows, `consolidationSubjects` stamped by the writer, and listed-target scope.

## Evidence


- The producer contract keeps the thirteen entry fields; this file holds the Curator-authored keys and writer input. [1]

- Curator-authored `scope` is required before an entry becomes an invariant, and missing scope is reported per entry. [2]
- Joint obligations are `family` records, not entry keys. [3]

- Every new invariant, family and decision record states an admission criterion and justification. [6]
- A decision record keeps a governing choice with ordered alternatives, exactly one chosen. [7]

- The Curator role points to this file before ingesting a producer list. [8]


- The Curator plans and applies the conflicting dependent through the crossing writer. [9]
- The record-kind list includes dependent and weakness. [10]

- Knowledge records are one JSON file per record under the kind directory. [4]


- The knowledge-ingest command and `knowledge_write` share the curator file writer and require the knowledge layout marker. [5]



- The Curator authors a title for a new rule. A legacy revision may remain untitled, and title-only edits preserve revision identity. [11]
