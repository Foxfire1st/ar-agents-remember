# dashboard/src/panels/review/familyExpressions.test.ts

## Governing Overview

[panels route overview](../overview.md)

## Purpose

**The unit lane for A4's arithmetic: the family's changed expression excerpts, and the dedup that makes
the collection a family-level reading rather than a concatenation of the member rows.** The module imports
`familyExpressionExcerpts` and the `FamilyMembershipRow` type from `./FamilyReviewCenter` — the shipped
function, never a reimplementation — and holds it to seven properties with no DOM in the way.

**Why it assembles its own payloads while its sibling refuses to, and the module says so in its own
header.** `ReviewWorkspace.family.test.tsx` mounts the real surface over real captured route bodies,
because what it checks is the wire contract. This module checks **one pure function's arithmetic**, and the
captures do not contain every case that arithmetic has to get right: no capture holds two member revisions
that name one address with the same recorded and observed bytes, which is the shape the served family
really has (`knowledge_curator_ingest.py` and `cli/knowledge_ingest.py` are each recorded under two member
revisions). That live case is measured on the mounted product by the sibling module, and the inputs here
are labelled `CONSTRUCTED` where they are invented. **This card does not claim that no part of the leaf rests
on a fixture, and no card may** (F-V1-4, low — the round-1 report's "no claim in this report rests on a
fixture" is falsified by the correction that followed it): the **divergent-rendering** claim rests on the
captured `familyReview.walkFinal` body through a **labelled fixture**, because live data carries no divergent
family — the search reached **3 families served by 1 leaf**, with **35 leaves refusing
`candidate_dataset_absent`** and therefore **absent, not measured**, `260921-ICR-L36` among them. The
`CONSTRUCTED` label here is about *this* module's inputs; it is not a claim about the leaf's evidence.

**The three-way partition the cases pin is the shipped one, not this file's invention.**
`models/knowledge/read.py::ANCHOR_RESOLUTIONS` names the seven resolutions of an address, and
`application/review_attribution.py` partitions them into the resolved state (`exact_recorded_blob`), the
states where the recorded bytes are not at the recorded address, and the observations nobody made. The
component under test follows that partition; these cases are what keep it following it.

## Code Commentary

### Logic

The pure grouping cases import familyExpressions from its extracted owner. Their recorded-address, per-side-reading and deterministic grouping assertions remain unchanged.

**Four builders and one `describe`, and each builder exists so a case can state its input as data.**
`claim(over)` returns a `ReviewFamilyMemberSource` seeded with a generated `claim_id`
(`claimCounter`, module-level at `:23`) and a role, spreading `over` last so a case names only the fields
its property is about — the address, the two source identities, the resolution and the `detail` sentence
that carries the read's own words. Because the mirror now requires `resolved_ranges` and `locator_state`
beside an optional `locator`, the builder **follows the server's own locator rule** for what it
constructs: a claim with an observed address gets a `file` locator and no range, stated `whole_file` when
its resolution is `exact_recorded_blob` and `unresolved` otherwise, and a claim with no address is
`not_observed` with no locator — so a constructed claim can never carry a state the server would refuse.
`member(revision, sources, label?)` (`:36-50`) returns a recorded
`ReviewFamilyMember` carrying those claims. `rows(...)` (`:52-55`) turns `[side, member]` pairs into the
`FamilyMembershipRow[]` the collection reads, which is the one input shape `familyExpressionExcerpts`
takes. The whole module lives in one `describe("the family's changed expression excerpts (A4)")` (`:56`).

**Case 1 — two member revisions recording one address with the same recorded and observed bytes collapse
to one excerpt (`:57-84`).** The `CONSTRUCTED` case that states the live 2-members-1-address shape in its
smallest form: two rows in, `collection.rows` 2, `collection.excerpts` length 1, the excerpt's own `rows`
2, both revisions named, and both membership rows named in side order — so the count the collection carries
is the **distinct** set and not the row count, which is what A4's "deduplicated changed expression
excerpts" asks for.

**Case 2 — one address carrying two different recorded blobs stays two excerpts (`:86-121`).** This is the
case that says the dedup key may **not** be the path alone, and after the F1 repair it is also the case that
says what the key **is**: the prototype's key is the excerpt's address (`path + ':' + start`); the claims
this surface receives carry no line range of their own, so the key is the path **together with the RECORDED
source identity the claim names** (`excerptKey`). The two claims here differ in `recorded` and agree in
`observed`, and they still stay two excerpts — which is the property that survives the repair, because
`recorded` is the only thing in the key that keeps them apart. Two rows in, two excerpts out, both naming
`src/one.py`.

**Case 3 — rows naming one excerpt under different roles merge, and every role is named (`:123-149`).**
`CONSTRUCTED` after the shape the captured `familyReview.walkFinal` body really records: one member
revision whose two claims name one address and one blob pair under two roles. Two rows collapse to one
excerpt carrying both roles (`["enforcement", "support"]`, sorted) and **one** occurrence, because the
occurrence key is the side together with the revision and two claims of one row are one membership row.

**Case 4 — both sides' readings of one divergent address are kept, because the disagreement is the change
(`:151-200`).** This is the case the F1 repair rewrote, and it now builds **the real divergent shape**: one
recorded blob (`recorded` repeated) named by both sides, with the before read observing **that same blob**
(`observed === recorded`, resolving `exact_recorded_blob`) and the after read observing **different bytes**
(`observed_source_identity: "e"*40`, resolving `recorded_blob_mismatch`). Because the key is
`path \0 recorded`, both claims mint one key and the excerpt carries both readings: the case asserts
`readingsBySide` is exactly
`[{ before, resolutions: ["exact_recorded_blob"], observed: [recorded] }, { after, resolutions: ["recorded_blob_mismatch"], observed: ["e"*40] }]`,
and that the resolved side is neither a changed row nor silently dropped (`resolved` 1, one membership row
with a change and one without, one distinct revision). **The fixture's comment states why the shape matters**
and where it was measured: since MIK-L31 it names the captured `familyReview.walkFinal` body's member revision
`a08a87b4` of `retry-budget-family` (the re-captured body; the older capture's revision was `d24e5187`), whose
`src/batch.py` is resolved `exact_recorded_blob` before and `recorded_blob_mismatch` after. The observed identity
is what the read *found*, not part of the address's identity, and keying the excerpt
by it split this one address into two rows that could never be paired, so the row named a single side and
the per-side fact the collection exists for was lost. This case is the counterexample to the old key and is
**not** `CONSTRUCTED` in the sense the first and third cases are — it is the measured shape, typed out.

**Case 5 — two different observed blobs at one address are still ONE excerpt, read once per side
(`:202-247`).** The complement of case 4, and the case that keeps the repair from over-correcting: both
sides carry the address, both are changed (`recorded_blob_mismatch` on each), and each observed different
bytes. That the two readings differ is a fact about the two trees, not about the address, so it is **one**
excerpt carrying two readings — the identity is the address together with its recorded bytes and nothing
else. The case asserts two rows collapsing to one excerpt, `readingsBySide` holding
`[{ before, ["recorded_blob_mismatch"], ["1"*40] }, { after, ["recorded_blob_mismatch"], ["2"*40] }]`, and
two occurrences, one on each side. **Read with case 2 it states the whole key contract:** `recorded` keeps
two blobs at one path apart (case 2), and `observed` may not, because two sides of one address legitimately
observe different bytes (case 5).

**Case 6 — the read's own resolutions are partitioned three ways, and "never asked" is not "different
bytes" (`:249-280`).** One member revision carries six claims: a resolved address, a stale one, a
`path_absent` one, a `recorded_object_unavailable` one, a `not_requested` one and one with no address at
all. Only the two states where the read did not find the recorded bytes at the address become rows;
`resolved` is 1 and `unmeasured` is 3 (the two unmeasured resolutions plus the address-less claim, which
the server refuses to send an address for and which is therefore a non-measurement rather than a change).
Each row prints the read's own resolution rather than this function's reading of it. **The repair added one
assertion here, and it is the per-side observed identity:** the `path_absent` excerpt's
`readingsBySide[0].observed` is `[]` while the stale one's is `["3"*40]`, so an address the read found
nowhere says so per side rather than printing a single observed value.

**Case 7 — an empty collection is a measured empty one, with the carried rows counted (`:282-298`).** One
side's claim resolves and the other side carries none, so `rows` 0 and `excerpts` empty while
`membershipRows` is 2, `distinctRevisions` 2 and both rows are counted as recording no changed
expression. The collection is empty **because it was measured empty**, which is the distinction the
verdict sentence in the component exists to state.

### Conventions

The unit-lane idiom of this route's review modules: `describe`/`expect`/`it` from `vitest` with no
testing-library import and no `fetch` stub, because nothing here renders or reads. Imports are two lines
by kind — the payload types as a type-only import from `../../data/review`, and the function under test
plus its input type from `./FamilyReviewCenter`. The builders are lowercase plain functions, each typed by
its return rather than by an interface; `claimCounter` is the module's only mutable state and exists so
every generated `claim_id` is distinct. `over` is spread last in `claim()` on purpose, so a case's own
fields win over the defaults. Case names state the property in the affirmative and the `CONSTRUCTED`
comments sit directly above the inputs they describe, in the file, where a reader checking the claim will
be. **Only two cases are labelled `CONSTRUCTED`** (the smallest 2-members-1-address shape and the role
merge); the divergent case states the measured shape instead, and the repair round added its complement
(two observed blobs, one excerpt). Since 260921-ICR-L36's fix round the module holds **seven** cases, and the
count is stated because a card whose count disagrees with its own `grep -c '^  it('` is a card a reader
stops trusting.

### Invariants And Boundaries

- **The function under test is imported, not reimplemented.** The cases call the shipped
  `familyExpressionExcerpts`; the sibling mounted module instead recomputes its expectation from the
  captured body, precisely so that one of the two checks the implementation and the other checks the wire.
- **Constructed inputs are labelled, and they prove nothing about the wire.** `CONSTRUCTED` marks the two
  invented shapes; the case that models the captured body says so in its own comment and names the
  revision and path it is modelled on.
- **The dedup key is the address together with the RECORDED source identity, and the observed identity is
  deliberately not in it.** Case 2 is the standing counterexample that keeps `recorded` in the key: two
  recorded blobs at one path are two excerpts. Case 5 is the standing counterexample that keeps `observed`
  out: two sides of one address legitimately observe different bytes and are still one excerpt.
- **Only the resolved state is not a change.** `exact_recorded_blob` is the resolved state, the four
  unresolved states are rows, and `recorded_object_unavailable` and `not_requested` are counted apart —
  never called changed.
- **A read result is a per-side fact, and an address's identity is not.** `readingsBySide` carries each
  side's resolutions **and** the observed identities that side's read found, which is why case 4 asserts two
  readings for one divergent excerpt and case 5 asserts two readings for one non-divergent one.
- **Boundary.** This module owns no production behaviour and asserts nothing about the wire, the rendered
  page or the served bundle. The arithmetic belongs to `FamilyReviewCenter.tsx`, the mounted evidence to
  `ReviewWorkspace.family.test.tsx` over the captured bodies, and the live instance to the leaf's
  enclosure.

### Todos

None recorded. The module deliberately holds only the arithmetic: the mounted product's own rendering of
the collection, over the served family, is the sibling module's and the enclosure's evidence, and the
browser-class journeys remain Dagger-gated by `dashboard/scripts/require-dagger-test-environment.mjs`.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

Every claim on this card is checkable in the shipped candidate: the module's own statement of why it
assembles its own payloads, the four builders, the six cases by their own names with the property each
pins, and the shipped function and partition the cases are held against. Every anchor in a row occurs
inside the range that row cites; the anchor of a case row is that case's own `it(...)` name, which occurs
on the line that opens the case.

- **The module's own statement of why it assembles its own payloads where `ReviewWorkspace.family.test.tsx` refuses to: the captured bodies do not hold every case the arithmetic must get right, and the live 2-members-1-address shape is measured on the mounted product instead.** [1]
- **The shipped partition the cases pin, named as the shipped one rather than this file's invention: the seven `ANCHOR_RESOLUTIONS` and the attribution owner's three-way reading of them.** [2]
- **The imports that fix the boundary: the payload types from the public review entry, and the function and input type from the component module under test.** [3]
- The generator that keeps every constructed claim's identity distinct, and the builder that spreads a case's own fields last so a case names only the fields its property is about. [4]
- **The constructed claim follows the server's locator rule: a file locator on an observed address, `whole_file` on the exact recorded blob, `unresolved` otherwise, `not_observed` with no address, and never a range.** [5]
- The recorded-member builder the cases feed the collection with. [6]
- The one input shape the collection reads: `[side, member]` pairs turned into carried membership rows. [7]
- The one `describe` every case below lives in. [8]
- **Case 1: two member revisions that record one address with the same recorded and observed bytes collapse to one excerpt, and the count carried is the distinct set rather than the row count.** [9]
- **Case 2: the dedup key may not be the path alone — two recorded blobs at one address are two excerpts.** [10]
- **Case 3: rows naming one excerpt under different roles merge into one occurrence that names every role.** [11]
- **Case 4 (its measured-shape comment naming the re-captured `walkFinal` revision since MIK-L31): the divergent address's two readings are kept — the case the F1 repair rewrote. It builds the real shape (one recorded blob, `observed === recorded` on before and different bytes on after) and asserts `readingsBySide` holds both sides' resolutions and both sides' observed identities.** [12]
- **Case 5: the repair's complement, which keeps it from over-correcting — two sides that both changed and both observed different bytes are ONE excerpt with two readings, because the observed identity is a read result and not part of the address's identity.** [13]
- **Case 6: the three-way partition of the read's own resolutions, with the two unmeasured states counted apart and never called changed, and the per-side observed identity asserted at its two extremes (`[]` for the address the read found nowhere, `["3"*40]` for the stale one).** [14]
- **Case 7: an empty collection is a measured empty one, with the carried membership rows still counted.** [15]
- **The function under test, its exported input type, the per-side reading type, and the two-way partition of the resolution vocabulary it reads.** [16]
- The dedup key contains the path and recorded identity; observed identities remain per-side readings. [17]
- The three-way realization classification keeps addressless and unmeasured claims separate from changed rows. [18]

### Cross-Repo References

No cross-repository behavior is exercised here. The module imports one component and one type from its own
directory and asserts arithmetic over values it constructs; it carries no identity that ranges beyond this
repository.

No meaningful cross-repo references found.
