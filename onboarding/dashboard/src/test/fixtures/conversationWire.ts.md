# dashboard/src/test/fixtures/conversationWire.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/test/fixtures/conversationWire.ts` |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-01T10:40+02:00                           |
| lastVerifiedCommitHash | `e52edaf5b655f495580efd93306afdf922b19b51`       |
| lastVerifiedCommitDate | 2026-08-01T11:01:51+02:00|
| governingOverview      | `../../overview.md`                              |

## Governing Overview

[dashboard/src overview](../../overview.md)

## Purpose

**The one place a dashboard test may build a node of the conversation wire grammar** —
`data/conversation/types.ts` (← `serving/conversation/models.py`) and
`data/conversation-library/types.ts` (← `library/api.py`). Companion to `fixtures/wire.ts`, which does
the same job for the served projection; that file's header carries the R6 reasoning both share.

This grammar had **two failure modes of its own, and both were one token wide** (cit:(["{} as unknown as ConversationCapabilities", "undefined as unknown as ConversationCapabilities"], dashboard/src/test/fixtures/conversationWire.ts:8-8; dashboard/src/test/fixtures/conversationWire.ts:14-14)):

- `{} as unknown as ConversationCapabilities` — a page whose capability tree is EMPTY. The wire model
  declares **twenty-three** capability leaves and the server fills every one, so the fixture asserted
  against a page the server cannot send.
- `undefined as unknown as ConversationCapabilities` — **worse**: `ConversationPage.capabilities` is
  REQUIRED, so this fixture stated that a required field is absent.

The source is explicit about what removing the cast did NOT do: `conversationPage({ capabilities:
undefined })` reaches the same page with no assertion at all, because a `Partial<T>` slot admits an
explicit `undefined` whenever `exactOptionalPropertyTypes` is off — and it is off here. That is why the
builders take `Overrides<O, Node>` rather than a bare `Partial<Node>`.

## Code Commentary

### Logic

- **The three brand mints** (cit:([`pageCursor`, `eventCursor`, `libraryConversationKey`], dashboard/src/test/fixtures/conversationWire.ts:53-55; dashboard/src/test/fixtures/conversationWire.ts:58-60; dashboard/src/test/fixtures/conversationWire.ts:63-65)) — the fixture defines `pageCursor`, `eventCursor`, and `libraryConversationKey` as its three explicit brand-mint functions.
- **`featureCapability`** (cit:([`featureCapability`], dashboard/src/test/fixtures/conversationWire.ts:69-74)) defaults to `{ state: "supported", reason: "", evidenceTier:
  "adapter" }`; **`attachmentCapability`** extends it with `allowedMimeTypes`, `maxBytes`,
  `maxCount`, `description`.
- **`ConversationCapabilityOverrides`** (cit:([`ConversationCapabilityOverrides`], dashboard/src/test/fixtures/conversationWire.ts:99-101)) is DERIVED from the wire type
  (`{ [Group in keyof ConversationCapabilities]?: Partial<ConversationCapabilities[Group]> }`) rather
  than re-listed, so a group the server adds is overridable the day the mirror declares it, and a group
  it drops stops being nameable. **`conversationCapabilities`** (cit:([`conversationCapabilities`], dashboard/src/test/fixtures/conversationWire.ts:103-146)) fills the full tree —
  `live` (6 leaves), `history` (5), `controls` (4 + a 3-leaf `attachments` block), `telemetry` (5) — so a
  test that cares about `controls.interrupt` names `controls.interrupt` and gets the other twenty-two
  for free. cit:([`capabilitiesWithInterrupt`], dashboard/src/test/fixtures/conversationWire.ts:149-153) is the shape the controls tests want.
- **`historyCapabilities`** (cit:([`historyCapabilities`], dashboard/src/test/fixtures/conversationWire.ts:155-168)) — the dormant-library capability block.
- **Identity, status, items, pages** (cit:([`conversationIdentity`, `conversationStatus`, `conversationItem`, `conversationPage`], dashboard/src/test/fixtures/conversationWire.ts:172-185; dashboard/src/test/fixtures/conversationWire.ts:187-207; dashboard/src/test/fixtures/conversationWire.ts:209-226; dashboard/src/test/fixtures/conversationWire.ts:228-243)) — `conversationIdentity`, `conversationStatus` (which
  fills `freshness`, `process`, `turn` and `evidence` sub-objects), `conversationItem` (override REQUIRED
  on `itemId` and `globalOrdinal`, with a derived default block id), and `conversationPage`. Note
  `conversationPage`'s ordering: `...over` is spread BEFORE `items`, and `items` is bound once at the top
  so `page.totalItems` and the final `items` cannot disagree.
- **The dormant library** (cit:([`conversationLibraryRow`, `conversationLibraryAgentRow`], dashboard/src/test/fixtures/conversationWire.ts:247-260; dashboard/src/test/fixtures/conversationWire.ts:262-272)) — `conversationLibraryRow` and `conversationLibraryAgentRow`.

### Conventions

- Every builder except one takes `Overrides<O, Node>`. The exception is `conversationCapabilities`,
  which takes per-GROUP overrides because it is a level deeper than the flat builders.
- Defaults are plausible-but-obviously-synthetic (`codex`, `vc-1`, `digest-1`, `key-parent`,
  `P4R3NT`), so nothing here reads as captured production data.
- The only assertions in the file are the three brand mints, each one line long and each registry-listed.

### Invariants And Boundaries

- A conversation-grammar fixture is built here or annotated/`satisfies`'d — it is not cast. The three
  mints are the sanctioned exception and the registry counts them, so a fourth fails.
- `conversationCapabilities` must keep producing the FULL tree. An empty or partial tree is the exact
  shape of the first defect this file was written to remove.
- `ConversationCapabilityOverrides` must stay derived from `ConversationCapabilities`. Re-listing the
  groups reintroduces a hand-kept copy that can fall behind the mirror.
- Projection nodes are NOT here — `fixtures/wire.ts` owns those.

### Todos

**Known, stated in the source, not fixed here.**

- **`conversationCapabilities` is one level too shallow to constrain.** It takes
  `{ controls?: Partial<ConversationCapabilities["controls"]> }`, so
  `conversationCapabilities({ controls: { interrupt: undefined } })` still writes an explicit `undefined`
  onto a required leaf. Left as-is rather than half-generalized — see the closing note in `overrides.ts`.
  Nothing in `wireFixtureGuard.ts` sees it either: it is a value, not a name.
- **The rest of `overrides.ts`'s residue applies here too** — the constraint binds a FRESH literal at the
  call site, so an override pre-widened through a variable admits `undefined` again.
- The three brand mints are unchecked by construction. A brand carries no structure, so a wrong *value*
  (a page cursor minted where an event cursor belongs, both minted from the same raw string) is
  indistinguishable to every rule; only the type of the slot it lands in separates them.

## Docs References

The failure modes are TypeScript behaviours: a double assertion through `unknown` suppresses
assignability as well as excess-property checking, and with `exactOptionalPropertyTypes` off an optional
slot still admits an explicit `undefined`. The branded-string pattern is the standard nominal-typing
idiom for opaque server-issued tokens.

| Finding | Anchor | Source |
| --- | --- | --- |
| The fixture header documents the former empty-capability double assertion as a failure mode. | "a page whose capability tree is EMPTY" | dashboard/src/test/fixtures/conversationWire.ts:8-8 |
| The overrides fixture records the optional-property `"does not set"` case. | "does not set" | dashboard/src/test/fixtures/overrides.ts:3-3 |
| The library grammar's branded string alias is `LibraryConversationKey`. | `LibraryConversationKey` | dashboard/src/data/conversation-library/types.ts:16-16 |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The two one-token failure modes, and why removing the cast alone did not close the second one. | "{} as unknown as ConversationCapabilities"; "undefined as unknown as ConversationCapabilities" | dashboard/src/test/fixtures/conversationWire.ts:8-8; dashboard/src/test/fixtures/conversationWire.ts:14-14 |
| The three brand mints that replaced the scattered inline casts. | `pageCursor`; `eventCursor`; `libraryConversationKey` | dashboard/src/test/fixtures/conversationWire.ts:53-55; dashboard/src/test/fixtures/conversationWire.ts:58-60; dashboard/src/test/fixtures/conversationWire.ts:63-65 |
| The attachment builder extends the feature capability with the image contract. | `attachmentCapability` | dashboard/src/test/fixtures/conversationWire.ts:76-88 |
| `ConversationCapabilityOverrides` derived from the wire type, and the full twenty-three-leaf tree `conversationCapabilities` produces. | `ConversationCapabilityOverrides`; `conversationCapabilities` | dashboard/src/test/fixtures/conversationWire.ts:99-101; dashboard/src/test/fixtures/conversationWire.ts:103-146 |
| `conversationPage` binding `items` once so the page's `totalItems` cannot disagree with its contents. | `conversationPage` | dashboard/src/test/fixtures/conversationWire.ts:228-243 |
| `ConversationPage.capabilities` is REQUIRED — the fact that made the second defect an impossible fixture rather than an unusual one. | `ConversationPage` | dashboard/src/data/conversation/types.ts:286-298 |
| The full `ConversationCapabilities` interface and fixture builder construct the twenty-three-leaf capability tree. | `ConversationCapabilities`; `conversationCapabilities` | dashboard/src/data/conversation/types.ts:253-283; dashboard/src/test/fixtures/conversationWire.ts:103-146 |
| The fixture's `LibraryConversationKey` alias and the two library-row builders. | "export type LibraryConversationKey"; "export function conversationLibraryRow"; "export function conversationLibraryAgentRow" | dashboard/src/data/conversation-library/types.ts:16-16; dashboard/src/test/fixtures/conversationWire.ts:247-247; dashboard/src/test/fixtures/conversationWire.ts:262-262 |
| The shared `Overrides` mapped type constrains required keys, while `ConversationCapabilityOverrides` gives `conversationCapabilities` its separate per-group override type. | `Overrides`; `ConversationCapabilityOverrides`; `conversationCapabilities` | dashboard/src/test/fixtures/overrides.ts:60-66; dashboard/src/test/fixtures/conversationWire.ts:99-101; dashboard/src/test/fixtures/conversationWire.ts:103-146 |
| The registry entries that make the page-cursor and library-key mints the assertions allowed in this file. | "src/test/fixtures/conversationWire.ts :: as ActivePageCursor"; "src/test/fixtures/conversationWire.ts :: as LibraryConversationKey" | dashboard/src/test/wireFixtureGuard.test.ts:164-164; dashboard/src/test/wireFixtureGuard.test.ts:172-172 |
| `ConversationCapabilities` asserted present in the guard's discovered vocabulary, so these builders are policed rather than merely conventional. | `ConversationCapabilities` | dashboard/src/test/wireFixtureGuard.test.ts:209-215 |
| The probe proving `conversationPage({ capabilities: undefined })` is now rejected at the call site. | "a builder override cannot state that a required field is absent" | dashboard/src/test/fixtureOverrides.test.ts:91-117 |
| The companion builder module for the served projection, whose header carries the shared R6 reasoning. | "R6 in one sentence"; `SERVED` | dashboard/src/test/fixtures/wire.ts:3-3; dashboard/src/test/fixtures/wire.ts:66-66 |

## Cross-Repo References

No cross-repository boundary. The conversation grammar's producing models
(`serving/conversation/models.py`, `library/api.py`) and its consuming mirrors are all in
`agents-remember`; the harnesses these conversations come from are external processes, but no fixture
here crosses that boundary.

| Finding | Anchor | Source |
| --- | --- | --- |
| The mirror's own header names its in-repo Python source, confirming a language seam inside this repository rather than a repository boundary. | "mcp/src/agents_remember/serving/conversation/models.py" | dashboard/src/data/conversation/types.ts:2-2 |

## Update History

- 2026-08-04T14:17+02:00 — 260731-EFA-L6 S18-B13 curator: closed D6-D8 documented failure-mode, capability-construct, and mapped-override evidence for the same-reviewer residual delta.

- 2026-08-02T16:56+02:00 — 260731-EFA-L6 curator W1-B06: anchored 23 citation claims
  (9 Logic citations and 14 Repo-Internal/Cross-Repo reference rows); repaired 1 exact range and normalized 2 duplicate range lists; scoped result clean (0 findings).

- 2026-08-01T10:40+02:00 — 260731-EFA-L4 curator (citation pass): repaired one citation. The
  `ConversationCapabilities`-in-the-vocabulary row cited `wireFixtureGuard.test.ts` L202-L208, which
  is the `describe` opener plus the unrelated "discovers a wire vocabulary rather than an empty one"
  test. The assertion is at L214, inside the test "knows the types the two proven defects lived on"
  spanning L209-L215, so the range is now L209-L215. No body text changed.
- 2026-08-01T10:20+02:00 — 260731-EFA-L4 curator: created. Records the two one-token failure modes (an
  empty capability tree against a twenty-three-leaf wire model, and an `undefined` written into a
  REQUIRED `capabilities`), why removing the cast alone did not close the second, the three
  registry-listed brand mints that replaced seventeen scattered casts, and the derived
  `ConversationCapabilityOverrides`. States the limits rather than flattening them: this file's one
  builder that is deliberately NOT an `Overrides` is still able to write `undefined` onto a required leaf
  one level down, the fresh-literal residue applies here as well, and a brand mint is unchecked by
  construction. Verification metadata pinned to the leaf base
  `abc7cbcc74921cdcb57a61529445f61641e919e7` until closeout stamps the L4 code commit.
