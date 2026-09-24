# mcp/src/agents_remember/application/curator_family_planning.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/curator_family_planning.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-24T07:54+02:00 |
| lastVerifiedCommitHash | `06ed70cfcde7e3860ee5b53435727e7512e4335c` |
| lastVerifiedCommitDate | 2026-09-24T10:53:01+02:00|
| governingOverview | `mcp/src/agents_remember/application/overview.md` |

## Governing Overview

[application route overview](overview.md)

## Purpose

**The curator's authored family plane resolved into exact identities, plans and batch commands
(ICR-R28@v2).** `curator_family_authoring.py` reads what the curator declared; this module resolves it
against the candidate: it allocates the identity pair each declared guarantee holds — recorded in the
candidate's **own** journal so a retry resolves to the same family — reads what the dataset already
records, which is how a reused guarantee is *examined* rather than restated, and turns each entry's
decision into the shipped commands `AddFamily`, `AddFamilyRevision`, `AddFamilyMember` and
`RemoveFamilyMember`.

**Nothing here writes the dataset.** The commands travel into the one batch
`knowledge_ingest.py` builds, so the one writer and the one transaction stay the only implementations.

**Four properties are load-bearing (`:11-25`):**

| Property | What it means |
| --- | --- |
| Identity is **allocated**, never derived from the key | Two independent tasks that spell one local key alike mint two families; a repeat of one operation finds its own allocation and is handed back what it already holds, while the same key arriving with a *changed* guarantee is refused rather than rewritten |
| A named identity is **checked, not trusted** | A declaration that reuses a `family_id` must find that identity in the candidate, and a membership that names a stored `family_revision_id` must find that revision, so an invented canonical ID cannot become a stored family |
| A stored row **contributes no command** | Re-declaring or re-inserting what the dataset holds is refused by the batch's own insert-absence preconditions — the right answer to "write this again" and the wrong answer to "repeat the operation that already wrote it" |
| A retirement **names the row this run read** | The expected-row digest comes from the dataset's own stored row through the shipped owner, so a removal cannot be authored against a row the run never read |

## Code Commentary

### Logic

**The identity journal is this operation's own, and it is deliberately not the invariant journal.**
`_FAMILY_ALLOCATION_JOURNAL_NAME` (`:83`) is `"curator-family-allocation-journal.json"`;
`_MEMBERSHIP_NAMESPACE` (`:88`) is the fixed UUID a membership identity is derived under, because a
membership is not an authored truth of its own — it is the recorded edge between two exact revisions —
so its identity comes from exactly those endpoints and repeating one operation derives the same row
rather than a second one.

**One allocation is the identity pair plus the content it was minted for.**
`FamilyAllocation` (`:96-120`) carries `retry_key`, the two identities and a `content_digest`. Both
identities are fresh `uuid4` values that carry no task, no enclosure and no key, so a stored family
stays usable from any later task; **what makes a repeat of one operation resolve to them is the retry
key** — the enclosure's own scope joined with the family key — and the digest is the guard that refuses
a different guarantee arriving under one key.

**An unreadable journal is not an absent one.** `FamilyAllocations` (`:123-135`) carries the path, the
records and an `unreadable` sentence. `read_family_allocations` (`:138-158`) reads an absent journal as
the ordinary first-run case (no records); a journal that is present and is not readable JSON, is not a
list, or carries a record this code cannot read is reported with its reason, and every declaring entry
is then refused with `family_allocation_unreadable` (`:389-395`) — minting without answering "does this
operation already hold an identity?" is how a retry becomes a second family.

**`record_family_allocations` runs before the batch that could still refuse** (`:173-201`). The order is
the one the invariant journal keeps and for the same reason: a run whose batch refuses has still made
this operation's allocation, and the retry of that operation has to resolve to it rather than mint a
second family for one guarantee. It writes atomically and reads the bytes back, raising rather than
returning when they do not match. (Whether a run writes anything at all is the operation's decision,
not this module's: `knowledge_curator_ingest._record_what_the_batch_will_write` calls this only for a
run whose batch carries commands.)

**`read_stored_family_facts` answers `None` for a candidate that does not exist yet** (`:252-299`), and
its docstring states why that is the honest answer: an empty mapping would say "this dataset records no
family", which is a different fact from "there is no dataset here". Otherwise it reads the dataset's own
`family_revision`, `family` and `family_member` rows through the shipped decoder —
`StoredFamilyFacts` (`:204-222`) keeps `member_rows` keyed by membership identity and `member_ids` keyed
by the exact endpoint pair, because that pair is what the dataset's own unique tuple means — and exposes
five accessors (`recorded_version`, `recorded_guarantee`, `members_of`, `recorded_membership`,
`endpoints_of`).

**The declaration is resolved once for the whole list, before any entry is planned.**
`plan_declarations` (`:341-373`) exists because two entries in one list may name one family and only one
of them authors its guarantee. `DeclarationPlan` (`:326-338`) carries the plans by key, the ordered
declarations, the refusals, and `refused_keys` — which is what lets a membership resting on a refused
declaration be refused with a reason of its own instead of silently placing nothing.

**One declaration's identity pair: reused when this operation holds one, else minted.**
`_plan_declaration` (`:376-429`) computes the retry key as `<retry_scope>:family:<key>` and the content
digest over the authored guarantee (`_declaration_digest` `:469-480` — the content, **never** the local
key). A held allocation with a different digest is refused with `family_allocation_conflict`
(`:396-406`), and its own sentence tells the curator the shape of the answer: a changed guarantee is a
**successor**, so declare it under a new key naming the stored `family_id` and the superseded revision
in `predecessor_revision_ids`. `GuaranteePlan.examined` (`:319-323`) is exactly `not declares_revision`
— the candidate already held the revision, so this run read rather than wrote it.

**Naming an identity is a claim about what the repository holds, so each named identity is checked.**
`_reusefamily_refusal` (`:432-466`) refuses an invented family identity with `family_identity_not_stored`
and a predecessor that no dataset holds *or that belongs to another family* with
`family_predecessor_not_stored`, instead of writing the claim as if it were true.

**One membership resolves to its two exact endpoints.** `_membership_endpoints` (`:598-635`) takes the
declared stored `family_revision_id` when the membership names one — refusing it with
`family_revision_not_stored` when the candidate holds no such revision — and otherwise resolves the
membership's *key* against the declaration plan. A membership whose key has no plan is refused by
`_declarationfamily_refusal` (`:638-655`), which distinguishes the two reasons a reader would otherwise
merge: `family_declaration_refused` when that key's declaration was itself refused, and
`family_not_declared` when no entry in this list declares it and the membership names no stored
revision. **This is the single implementation of the undeclared-key answer** — the read half
deliberately does not answer it, because only the candidate knows whether a stored revision exists
(`curator_family_authoring.read_family_plane`'s docstring says so). A membership whose exact endpoint
pair is already recorded is marked `stored` (`:621-623`), so an exact retry reports the membership it
already placed instead of re-issuing an insert the dataset's own unique tuple would refuse. The member
identity is `uuid5(_MEMBERSHIP_NAMESPACE, f"{family_revision_id}:{revision_id}")`.

**A retirement resolves against the row this run read.** `_retirement_plans` (`:658-685`) refuses
`membership_not_stored` when the candidate holds no such membership, and otherwise carries the
dataset's own row digest as `expected_row_digest` — "a removal names a row this run read, never one it
assumed".

**`plan_entry_family` keeps all three outcomes apart** (`:536-595`). An entry with **no** assignment at
all is carried as a `CuratorFamilyAuthoring` with nothing authored — the entry is reported as not
examined rather than dropped out of a list that would then look complete; a deliberate `no_family`
assignment carries its basis; and a member decision resolves its memberships and retirements.
`CuratorFamilyAuthoring.examined` (`:524-533`) is the predicate the report reads: a decision is a
deliberate no-family outcome, a membership, **or** a retirement, and an entry with none of them is the
unexamined case rather than an empty family result. `no_family_basis` travels into the revision's
recorded conditions so a reader of the *dataset*, not only of the report, can tell a family-free
obligation from an unexamined one.

**`family_commands` states the batch's order as a contract, not an accident** (`:693-744`): an identity
before the revision that belongs to it, a membership after the revision it cites, and a plan the
candidate already holds contributing nothing for that row. `projected_family_commands` (`:747-766`)
counts what a dry run would carry from the *same* plans, so the projection arithmetic stays over what
the run already resolved instead of a second construction of the command list.

### Conventions

This module reads the candidate and writes exactly one artifact of its own — the family allocation
journal — through `atomic_write_bytes` with a read-back. It builds the shipped command vocabulary
rather than a private one, and it takes the admitted destination's own `authorship` for the provenance
of every row it drafts, so nothing a caller authors can become stored provenance.

### Invariants And Boundaries

- A family identity is **allocated** (`uuid4`), never derived from the local key; the retry key is what
  makes a repeat find it.
- One key names one creation operation: the same key with a changed guarantee is refused, and the
  answer is a successor under a new key naming the stored identity and its predecessor.
- A named family identity and a named predecessor are checked against the candidate before use.
- A plan the candidate already holds contributes no command; a stored membership is reported as reused
  rather than re-inserted.
- A membership identity is derived from its exact endpoint pair, so repeating one operation derives one
  row.
- A retirement carries the dataset's own row digest; a removal is never authored against an assumed row.
- `None` for the dataset means "no dataset here", never "this dataset records no family".
- The unexamined case is a carried entry with nothing authored, never an absent entry.

### Todos

None recorded.

## Docs References

No configured Domain Documentation source applies; this is the resolution of the repository's own
authored hand-off vocabulary against its own candidate.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external documentation is required for resolving the authored plane. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| **The module's own statement of the four load-bearing properties and that nothing here writes the dataset.** | "Four properties are load-bearing"; "Nothing here writes: the commands travel into the one batch" | mcp/src/agents_remember/application/curator_family_planning.py:1-31 |
| The published surface: the plans, the journal readers and writers, and the two command builders. | `__all__` | mcp/src/agents_remember/application/curator_family_planning.py:62-78 |
| **The operation's own allocation journal, deliberately separate from the invariant journal, and the fixed namespace a membership identity is derived under.** | `_FAMILY_ALLOCATION_JOURNAL_NAME`; `_MEMBERSHIP_NAMESPACE` | mcp/src/agents_remember/application/curator_family_planning.py:83-88 |
| **One allocated identity pair with the content it was minted for: the retry key joined to the operation's scope is what a repeat resolves to.** | `FamilyAllocation` | mcp/src/agents_remember/application/curator_family_planning.py:96-120 |
| **An absent journal is the first run; a present journal that cannot be read refuses every declaring entry rather than minting over an unknown answer.** | `FamilyAllocations`; "family_allocation_unreadable" | mcp/src/agents_remember/application/curator_family_planning.py:123-135 |
| The journal reader, which distinguishes absent, unreadable and readable-with-records. | `read_family_allocations` | mcp/src/agents_remember/application/curator_family_planning.py:138-158 |
| One journal record as an allocation, or `None` when it is not one this code wrote. | `_allocation_record` | mcp/src/agents_remember/application/curator_family_planning.py:161-170 |
| **Identities are journalled before the batch that could still refuse, written atomically and read back.** | `record_family_allocations` | mcp/src/agents_remember/application/curator_family_planning.py:173-201 |
| **What one dataset records about families, with the member index keyed by the exact endpoint pair the dataset's own unique tuple means.** | `StoredFamilyFacts`; "member_ids" | mcp/src/agents_remember/application/curator_family_planning.py:204-222 |
| The five measured accessors the report and the planners read the dataset through. | `recorded_version`; `recorded_guarantee`; `members_of`; `recorded_membership`; `endpoints_of` | mcp/src/agents_remember/application/curator_family_planning.py:224-249 |
| **`None` means "there is no dataset here", which is a different fact from "this dataset records no family".** | `read_stored_family_facts`; "an empty mapping would say" | mcp/src/agents_remember/application/curator_family_planning.py:252-299 |
| **One guarantee resolved against the candidate, and `examined` meaning the candidate already held the revision.** | `GuaranteePlan`; "def examined" | mcp/src/agents_remember/application/curator_family_planning.py:302-323 |
| **The whole list's declarations resolved together, with the refused keys carried so a dependent membership can be refused with its own reason.** | `DeclarationPlan`; "refused_keys" | mcp/src/agents_remember/application/curator_family_planning.py:326-338 |
| The list-level resolution pass, run before any entry is planned. | `plan_declarations` | mcp/src/agents_remember/application/curator_family_planning.py:341-373 |
| **The retry key joined to the operation's scope, the content digest taken over the authored guarantee rather than the key, and the refusal that names a changed guarantee a successor.** | `_plan_declaration`; "family_allocation_conflict"; "a changed " | mcp/src/agents_remember/application/curator_family_planning.py:376-429 |
| **A named identity is a claim about the repository, so an invented family identity and a predecessor of another family are both refused by name.** | `_reusefamily_refusal`; "family_identity_not_stored"; "family_predecessor_not_stored" | mcp/src/agents_remember/application/curator_family_planning.py:432-466 |
| The content one allocated pair stands for: the authored guarantee, never the local key. | `_declaration_digest` | mcp/src/agents_remember/application/curator_family_planning.py:469-480 |
| One membership placed at two exact endpoints, with `stored` marking the pair the dataset already records. | `MembershipPlan` | mcp/src/agents_remember/application/curator_family_planning.py:483-493 |
| One retirement carrying the digest of the row this run read. | `RetirementPlan` | mcp/src/agents_remember/application/curator_family_planning.py:496-504 |
| **One entry's resolved plane, and `examined` as the predicate that keeps a deliberate no-family outcome, a membership and a retirement apart from no decision at all.** | `CuratorFamilyAuthoring`; "def examined" | mcp/src/agents_remember/application/curator_family_planning.py:507-533 |
| **The entry-level resolution, where an entry with no family decision is carried with nothing authored rather than dropped.** | `plan_entry_family`; "No family key at all is a *third* outcome" | mcp/src/agents_remember/application/curator_family_planning.py:536-595 |
| **The membership endpoint resolution: a named stored revision is checked against the candidate, and a key otherwise resolves against the list's declarations.** | `_membership_endpoints` | mcp/src/agents_remember/application/curator_family_planning.py:598-635 |
| **The single implementation of the undeclared-key answer, keeping "the declaration was refused" apart from "no entry declares it".** | `_declarationfamily_refusal`; "family_not_declared"; "family_declaration_refused" | mcp/src/agents_remember/application/curator_family_planning.py:638-655 |
| **A removal names a row this run read, never one it assumed.** | `_retirement_plans`; "membership_not_stored"; "holds no such membership" | mcp/src/agents_remember/application/curator_family_planning.py:658-685 |
| **The command order as the batch's contract: identity, then revision, then membership, then removal, with a stored row contributing nothing.** | `family_commands` | mcp/src/agents_remember/application/curator_family_planning.py:693-744 |
| The dry run's count taken from the same plans, so the projection is not a second construction. | `projected_family_commands` | mcp/src/agents_remember/application/curator_family_planning.py:747-766 |
| The writer this module's single artifact goes through, and the canonical bytes its journal is made of. | `atomic_write_bytes`; `canonical_json_bytes` | mcp/src/agents_remember/kernel/atomic_write.py:53-72; mcp/src/agents_remember/kernel/canonical_json.py:27-31 |
| The shipped member-row decoder the stored facts are read through, rather than a second reading of the table. | `decode_member_row` | mcp/src/agents_remember/memory/knowledge/records.py:413-426 |
| The command vocabulary this module builds instead of restating: the family and family-member drafts and the four commands. | `AddFamily`; `AddFamilyRevision`; `AddFamilyMember`; `RemoveFamilyMember` | mcp/src/agents_remember/models/knowledge/candidate.py:370-375; mcp/src/agents_remember/models/knowledge/candidate.py:378-382; mcp/src/agents_remember/models/knowledge/candidate.py:408-412; mcp/src/agents_remember/models/knowledge/candidate.py:415-420 |
| The drafted provenance every family row carries comes from the admitted destination, not from the caller. | `FamilyRevisionDraft`; `FamilyMemberDraft` | mcp/src/agents_remember/models/knowledge/family.py:58-102; mcp/src/agents_remember/models/knowledge/graph.py:49-55 |
| The operation that calls the journal writer only for a run whose batch writes something, and that builds the one batch these commands join. | `_record_what_the_batch_will_write`; `curator_command_list` | mcp/src/agents_remember/application/knowledge_curator_ingest.py:1319-1364; mcp/src/agents_remember/application/knowledge_ingest.py:238-262 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. A family allocation, a stored revision and a
membership endpoint are all records of one candidate dataset under one coordination root.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-09-24T07:54+02:00 — 260921-ICR-L28 curator (uncommitted change set on `ar/260921-icr-l28`, base
  `63b476297708f779de8ed5c0bf3555b9d1de70c2`): created this one-to-one card for the module
  `ICR-R28@v2` introduced as **the resolution half of the curator's family plane**. The stamp basis is
  the leaf's base commit, because the module is untracked there and no commit contains what a stamp
  would otherwise claim to have verified. Two things a reader must carry away, because both were live
  defects during the leaf: **a family identity is allocated from the operation's own journal and never
  derived from the local key**, so the same key spelled by two tasks mints two families while a repeat
  of one operation finds its own pair, and the same key arriving with a *changed* guarantee is refused
  with `family_allocation_conflict` — the refusal names the successor shape rather than rewriting a
  revision an earlier membership still cites; and **the undeclared-key answer has exactly one
  implementation** (`_declarationfamily_refusal`), because a second copy in the read half answered a
  question that depends on the dataset. The unexamined case is a carried entry with nothing authored,
  never an absent entry, and a stored row contributes no command so an exact retry reports rather than
  re-inserts. No verification stamp beyond the leaf's base is advanced: the candidate is uncommitted
  and the governed closeout owns the real commit.
