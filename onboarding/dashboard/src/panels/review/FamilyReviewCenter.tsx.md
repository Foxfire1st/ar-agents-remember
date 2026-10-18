# dashboard/src/panels/review/FamilyReviewCenter.tsx

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

The selected family/member reading center composes authored guarantee/intent content, bounded member context,
focused code/test expressions, recorded judgments/proof source state and selected-record worklist content. It
does not manufacture an authored judgment from a source, membership or guarantee change. The workspace supplies
layout, open-path and leaf-wide comparison data; the center asks `useReviewTreeEntries` for the selection's
invariant keys and uses leaf-wide planning marks only when the comparison number matches. The former dataset
accordion and external-assessment reading channel are historical, not active fallbacks.
## Code Commentary

Expression keys come from both loaded family sides. A selected invariant remains an independent seed when
there is no family entry OR the loaded roster contributes no invariant key; keys are deduplicated and sorted.
The extracted `FamilyGuarantees.tsx` owner retains authored wording and comparison cases. This source supplies
keys and props; it does not itself establish backend reads, whole-family completeness or a fresh execution.


### Recorded semantic change steps

The selected family/member reading area joins MeaningBlock to its own canonical record beside the guarantee or intent content, never to a kept family’s history. The no-subject and member-without-identity branches use MeaningFieldGuard: a missing field is failure while a present empty collection remains valid. Recorded steps are open content outside disclosures, preserve own row revisions and reasons, and do not replace the before/after wording diff or the independent source/judgment owners.


### Which centre

- `FamilyReviewCenter` wraps the body in `IntentWordDiffScope`, which marks a tree comparison for the
  word-level wording diff. `ReviewCenterBody` reads the selection with `centerSelection` and renders one
  of four centres: `MemberCenter` when the addressed subject is an invariant; otherwise `UnselectedCenter`
  when no family entry is selected, `UnavailableMember` when a member row is selected (a row that names
  no invariant identity addresses no subject), and `FamilyCenter` for a family.
- `centerSelection` now returns only the selected family entry, selected revision row and listed-path set.
  It no longer derives a subject-filtered members collection or `linksIncomplete` for a dataset renderer.
  `ReviewCenterBody` constructs the expressions/selected-record knowledge once, and `SelectedCenter` chooses
  the four display branches.
- `membersComplete` requires, for each side, either the state `not_recorded`, or `recorded` with a
  truthy complete page, exactly as many loaded members as the side's total, and every member row `recorded`.
  This governs the member-context partial-roster label; it is distinct from `focusedCards.cardScope`.

### What each centre shows

- `FamilyCenter`: the family label with open comparison details, the guarantee comparison
  (`GuaranteeComparisonBlock`), `FamilyMemberContext` with distinct member revisions ordered by
  `orderedCenterMembers`, the expressions, an open realization-resolution section, the family judgment/proof panel
  and the selected record's worklist items.
- `MemberCenter`: the member label and `MemberFamilyLabel`, the family guarantee when present,
  `SelectedStatement` with `subjectRows` kept per side, the expressions, open independent facts and
  selected roster-revision context, subject judgments/proofs, selected-record worklist items and the roster
  continuation. These semantic facts are not behind a disclosure.
- `UnselectedCenter`: selected statements or an explicit unselected/source-only sentence; the leaf's
  complete worklist is a separate workspace destination, not an automatically embedded patch panel.
- `UnavailableMember`: the guarantee comparison, the member's statement, the sentence that this page
  did not supply the member's invariant identity, and the roster continuation. It shows no knowledge
  panel and claims no judgment absence.
- `FamilyMemberContext` delegates the carried member statement to `memberStatementPairs`/`FamilyMemberStatement`,
  rather than treating each raw row statement as the complete before/after presentation. It retains the
  distinct revision list, member-count/roster state and owner-supplied next-page callback.
- `FamilyCenter` now includes both supplied origin objects. `IndependentFacts` reports selected revision,
  carried member/claim and attributed-location facts, then points to Judgment/proofs; those counts and changes
  are not an authored judgment. `FamilyJudgment` delegates the canonical family identity to `SubjectJudgment`.

### Member order

The center retains distinct member revisions from both sides. Where the served outlined comparison covers the family, `displayedMemberRanks` takes invariant positions from its own `outlineGroups(outline, [], walked, order)` call, whose code-fact map is empty, under the stored triage/authored preference; the sidebar's own call supplies `codeFacts`, and `changeTriage` assigns badges and sorts by that map. A member can therefore hold a different position in the center than in the sidebar, and both revisions of one invariant take the center's position for it. Members without a position remain last with stable relative order. Without an outlined group, `orderedCenterMembers` falls back to `orderMemberRows`; it does not invent an outline, reclassify change facts or discard semantic siblings. The tree is one row per invariant, while the center remains one row per revision.

### Guarantee comparison

`GuaranteeComparisonBlock` renders, on a tree comparison whose two sides both carry a guarantee with
differing text, the word-diffed `GuaranteeTextChange`. Otherwise it renders by the kind `guaranteeComparison` returns: a sentence when
neither snapshot selected a family revision; a one-sided guarantee labelled "Added guarantee" or "Removed
guarantee" (on a tree comparison through `OneSidedGuaranteeLabel`); "Guarantee unchanged · same recorded
revision"; "Wording unchanged" with both revisions when two revisions carry identical text; and a diff of
the two texts when they differ.

### Expressions

`CenterExpressions` passes the sorted `cardInvariants` keys and payload comparison number to
`useReviewTreeEntries`. Its `null` branch states that code locations require a measured tree comparison,
not a dataset file-view fallback. Otherwise it supplies `ExpressionCards` with `cardScope(entry)`, the
selected invariant seed and `pinnedWorklist` planning marks. The planning helper checks the supplied tree
read's phase and comparison number; that check alone is not an independent lineage or execution audit.

Historically `ReviewExpressions`, subject-filtered member rows and `linksIncomplete` served the dataset
branch. Those consumers/props are removed; retaining this provenance does not resurrect their implementation.

### Record worklist items

The selected family/member receives `SubjectWorklistItems` bound to its canonical record identity and
the payload's comparison. A missing/mismatched/unavailable read remains explicit; no subject filter is
invented from labels. The complete worklist belongs to `LeafWorklistView` in the workspace's own view.
Neither subject review nor that worklist embeds knowledge-file patches.

## Evidence

### Docs References

No Domain Documentation source is configured for this slice.

### Repo-Internal References

- Guarantee comparison is delegated to its surviving extracted owner. [12]
- Unselected source/intent content with a meaning-field guard. [13]
- The roster partial label uses complete pages, exact row totals and recorded member content. [14]
- The family center composes origins, guarantee, semantic steps, member context, expressions and judgment. [15]
- Independent selected revision, membership and attribution facts do not manufacture a judgment. [16]
- Member center preserves its own subject, statement, expressions, resolution and judgment/proof context. [17]
- The wrapper supplies the wording-diff scope. [18]
- Composition and four branch selection preserve expressions and onRosterNext propagation. [19]
- Planning uses only the supplied ready leaf-wide read of the displayed comparison number. [20]
- Focused tree entries or an explicit measured-comparison-required sentence, not a dataset accordion. [22]
- Sorted loaded family keys, with a selected-invariant fallback when the family contributes no key. [23]
- Selection returns entry, selected member row and listed paths, not the retired members/linksIncomplete props. [24]
- Authored guarantee rendering lives in FamilyGuarantees; same wording and one-sided/comparison states are not run evidence. [26]
- One carried expression excerpt shows roles, side resolutions, occurrences and source identities. [27]
- The member renderer retains its canonical subject and side context. [28]
- Card read assembly carries bounded cardScope and the selected seed. [31]
- Canonical family/member MeaningBlock and no-subject/unidentified-member guards are composed separately. [32]
- Distinct member revisions use displayed outline positions or the carried ordering fallback. [33]
- Member statements use the extracted pairing renderer while bounded counts and roster continuation remain here. [34]
- The family judgment delegates the actual canonical family subject. [35]

### Cross-Repo References

No cross-repository boundary is asserted.
