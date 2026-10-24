# dashboard/src/panels/detail-panel/legacyProviderSnapshot.test.tsx

## Current operative account — MIK-R199

- The module feeds the store a projection payload of a shape the current wire contract cannot express. `LegacyProviderNode`,
  `LegacySetupProgress` and `LegacySetupSummary` are declared inside the test module, and `LegacyProjection` adds
  `providers`, `analytics.setupProgress` and `analytics.setupSummaries` on top of `WorkspaceProjection`. The module
  comment records why the shapes are local: the `types/projection.ts` mirror no longer carries the fields, so the
  payload is a shape only an older server could send.
- `applyLegacy()` is the single entry point: it hands `legacy()` to `dashboardStore.getState().applySnapshot(...)` as a
  value. Nothing is cast — the extra keys are declared on the local type, which is how the case proves the store is fed
  a payload it never asked for.
- `legacy()` is `clean()` plus the retired material: provider nodes for the `code` and `memory` roles (the memory node
  names its worktree group), a failed setup-progress record naming a failed phase, a failed setup summary in the failed
  state, and an attention queue carrying the `provider-down` and `failed-setup` items. `clean()` is the same projection
  without any of it — same leaf, same enclosure, same active worktree group.
- `afterEach` unmounts rendered trees with `cleanup()` and calls `dashboardStore.getState().reset()`, so each case
  starts from an empty store and no case inherits the previous one's snapshot.
- `spineHtml()` renders `DetailPanel` for `taskdoc:<leaf key>`, captures `worktree-spine`'s `innerHTML`, unmounts, and
  refuses the retired engine vocabulary in the panel's text before returning the HTML. Every case that builds spine HTML
  therefore carries the vocabulary assertion as well as its own.
- The store case applies the legacy payload and asserts the state has no `providers` key at all (`'providers' in state`
  is false), that `activeWorktreeGroups` equals the payload's group, and that the `enclosures` map holds the payload's
  enclosure alone. The case comment is explicit about the boundary: the analytics object rides through whole because the
  server owns that wire object, so its legacy keys are still on it; what must not exist is anything derived from them.
- The rendering case builds spine HTML from the legacy snapshot, resets the store, applies the clean snapshot, and
  asserts the legacy-derived HTML equals the clean HTML. It then asserts the clean HTML still carries the worktree path, the code
  repo name, the memory repo name, and `worktree present · pending cleanup` — so identity is not achieved by rendering
  an empty spine.
- The attention case applies the legacy payload, renders `AttentionQueue`, and asserts the bell's `aria-label` is
  `Attention: nothing waiting` with empty text. The retired kinds are present in the payload and publish nothing.

### Source and authority bounds

- Source comparison: `dashboard/src/panels/detail-panel/legacyProviderSnapshot.test.tsx:1-232`, read in full.
- Source comparison: `dashboard/src/panels/detail-panel/legacyProviderSnapshot.test.tsx:150-197` (store entry, payload
  builders, spine capture).
- This card records what each case body asserts. No test run, runner invocation or coverage result is claimed here.
- The card does not claim `applySnapshot` ignores unknown keys in general; it records only what these cases assert about
  this payload. Nor does it claim which attention kinds the server emits — the retired kinds are fixture data here.

## Evidence

- The superseded wire shapes are declared inside the test, and the payload reaches the store as a value rather than a cast. [1]
- The legacy payload and the clean payload differ only by providers, setup buckets and the retired attention kinds. [2]
- The store keeps no provider map from a payload that carries one, and keeps the enclosure and group it can derive. [3]
- The Tasks view renders identical spine HTML with and without the legacy records, and the spine is not empty. [4]
- `provider-down` and `failed-setup` reach the queue as fixture items and leave the bell with nothing waiting. [5]
