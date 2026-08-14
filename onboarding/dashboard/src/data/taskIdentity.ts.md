# dashboard/src/data/taskIdentity.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/data/taskIdentity.ts`             |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-08-11T09:45+02:00 |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`       |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[data overview](overview.md)

## Purpose

Centralizes dashboard task-selection keys, canonical task-document references, structural equality,
and real task-tree construction. Qualified leaf keys remain a display/context helper; they are no
longer the hosted-seat address.

## Code Commentary

### Logic

`taskDocumentRefForDoc` turns a projected task document into the repository-qualified reference used
by the runtime, and `sameTaskDocumentRef` compares that identity. `buildTaskTree` constructs the
Operations/Chats task hierarchy from actual sprint, master, and leaf documents. Existing lifecycle and
leaf-key helpers continue to serve selection, labels, and leaf context packages without becoming a
parallel seat identity.

### Conventions

Selection keys are UI namespaces. Structural seats use `TaskDocumentRef`; labels and qualified leaf
keys are presentation/context values.

### Invariants And Boundaries

- Every structural reference points to a real projected task document.
- No synthetic logical seat id or master key is introduced.
- Leaf-key helpers must not be used to address a hosted occupant.
- Lifecycle ids remain optional runtime attachment, not task identity.

### Todos

None.

## Docs References

No Domain Documentation source is configured.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Projected documents become canonical task-document references. | `taskDocumentRefForDoc` | dashboard/src/data/taskIdentity.ts:74-84 |
| Structural equality compares repository, path, and level. | `sameTaskDocumentRef` | dashboard/src/data/taskIdentity.ts:86-95 |
| The dashboard tree is built from real task documents. | `buildTaskTree` | dashboard/src/data/taskIdentity.ts:208-216 |

## Cross-Repo References

No cross-repository implementation dependency governs this file.

## Update History

- 2026-08-11T19:58+02:00 — Aligned the current data-contract card for `taskIdentity.ts` with task-document identity, qualified seat state, and terminal projections represented by this source.
- 2026-08-07T08:19Z — 260731-EFA-L8 curator: reviewed this sidecar against the frontend-rail change set (strict-target lint remediation: complexity, max-lines-per-function, react-hooks, jsx-a11y, and import-cycle fixes). No content impact: behavior-preserving refactor; the file's responsibilities and the claims in this card remain current. Verification metadata stays pinned until closeout stamps the code commit.

- 2026-08-05T00:45:16+02:00 — 260731-EFA-L6 S18-B24 curator: replaced the `n/a` rows with exact
  anchors and fixer-generated ranges; exact non-fixing check returns zero findings.

- 2026-07-18T16:02+02:00 — FEUI MX-FIX-3: replaced retired Chats/`SessionList` consumers with the
  exact landed leaf-title/id and `qualifiedLeafKey` import inventory while preserving the no-live-caller
  status of `leafKeyForSelection`. Verified against code commit
  `31f58834f86c0d98e26b0896e099a2403a8729ee`.

- 2026-07-18T07:22+02:00 — FEUI-L8 manual route refactor: retargeted this direct data file card
  from the packed dashboard/src parent to the new nearest data authority overview. Source behavior
  is unchanged by this memory-only governance move; verification hash/date remain pinned.

- 2026-06-30T00:00:00+02:00 — L5 follow-up: noted that `leafKeyForSelection` is now **superseded/unused** — the rail chat
  keys off the leaf the detail panel is *displaying* (`DetailPanel.onViewLeaf` → `Cockpit.viewedLeafKey`,
  which calls `qualifiedLeafKey` on the displayed leaf doc), not the top-level (master) selection. The
  helper is left exported in this file with no live caller; `qualifiedLeafKey` / `leafTitleForKey` /
  `leafIdFromKey` stay in use. Verification metadata pinned until closeout stamps the L5 commit.
- 2026-06-30T00:00:00+02:00 — L5 (Sidebar chat): added the leaf-key identity helpers — `qualifiedLeafKey(doc)` (durable
  `repo/master/leaf-id` from the task doc, master = the doc's parent folder basename), `leafKeyForSelection`
  (the open task doc's leaf key for a taskdoc/lifecycle selection, mirroring `lifecycleIdForSelection`),
  `leafTitleForKey` (bound-leaf display title), and `leafIdFromKey` (leaf-id fallback). These key the
  sidebar chat's chat⇄leaf binding; derived from the doc, not the enclosure, so they survive finalize.
  Verification metadata pinned until closeout stamps the L5 commit.
- 2026-06-26T19:40+02:00 — Task 20 lifecycle label follow-up: added the shared
  `taskDocumentLabel` helper so lifecycle-visible rows can use projected task
  document titles when enclosure/lifecycle projection metadata is unavailable,
  instead of falling back straight to cryptic lifecycle ids. Verification
  metadata pinned until closeout stamps the reopened task-20 code commit.
- 2026-06-24T16:33+02:00 — Task 17 task-document-first Operations: added typed selection helpers for
  `taskdoc:`, `series:`, and `lifecycle:` keys plus lifecycle extraction for task-document selections,
  replacing parent/task-name inference at the selection boundary. Verification metadata pinned until
  closeout stamps the code commit.
- 2026-06-24T08:59+02:00 — Created for the promoted leaf identity correction: centralizes enclosure
  label lookup and direct lifecycle task-document filtering so UI labels do not become a contract-content
  fallback. Verification metadata pinned until closeout stamps the code commit.
