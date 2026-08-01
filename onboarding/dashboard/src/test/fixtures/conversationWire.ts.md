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

This grammar had **two failure modes of its own, and both were one token wide** (L6-L20):

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

- **The three brand mints** (L50-L65) — `pageCursor`, `eventCursor`, `libraryConversationKey`.
  `ActivePageCursor` / `ActiveEventCursor` / `LibraryConversationKey` are `string & { __brand }`: opaque
  server-issued strings whose brand exists only so a page cursor can never be handed to an event route.
  There is no structure to get wrong and no other way to make one, so the previously scattered
  `"evt-0" as ActiveEventCursor` casts (seventeen of them, per the header) collapse into these three.
  Each is registered in `wireFixtureGuard.test.ts` with its reason — **which is what makes them the only
  three rather than the first three.**
- **`featureCapability`** (L69-L74) defaults to `{ state: "supported", reason: "", evidenceTier:
  "adapter" }`; **`attachmentCapability`** (L76-L88) extends it with `allowedMimeTypes`, `maxBytes`,
  `maxCount`, `description`.
- **`ConversationCapabilityOverrides`** (L99-L101) is DERIVED from the wire type
  (`{ [Group in keyof ConversationCapabilities]?: Partial<ConversationCapabilities[Group]> }`) rather
  than re-listed, so a group the server adds is overridable the day the mirror declares it, and a group
  it drops stops being nameable. **`conversationCapabilities`** (L103-L146) fills the full tree —
  `live` (6 leaves), `history` (5), `controls` (4 + a 3-leaf `attachments` block), `telemetry` (5) — so a
  test that cares about `controls.interrupt` names `controls.interrupt` and gets the other twenty-two
  for free. `capabilitiesWithInterrupt` (L148-L153) is the shape the controls tests want.
- **`historyCapabilities`** (L155-L168) — the dormant-library capability block.
- **Identity, status, items, pages** (L170-L243) — `conversationIdentity`, `conversationStatus` (which
  fills `freshness`, `process`, `turn` and `evidence` sub-objects), `conversationItem` (override REQUIRED
  on `itemId` and `globalOrdinal`, with a derived default block id), and `conversationPage`. Note
  `conversationPage`'s ordering: `...over` is spread BEFORE `items`, and `items` is bound once at the top
  (L232) so `page.totalItems` and the final `items` cannot disagree.
- **The dormant library** (L245-L272) — `conversationLibraryRow` and `conversationLibraryAgentRow`.

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

| Finding | Citations | Source Path |
| --- | --- | --- |
| An assertion through `unknown` is the documented way to assert between unrelated types, which is precisely why `{} as unknown as ConversationCapabilities` compiled against a required, fully-populated wire model. | Type Assertions | [TypeScript Handbook — Everyday Types / Type Assertions](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#type-assertions) |
| With `exactOptionalPropertyTypes` off, an optional property's type implicitly includes `undefined` — the reason removing the cast did not close the hole and the builders needed `Overrides`. | `exactOptionalPropertyTypes` | [TSConfig Reference — exactOptionalPropertyTypes](https://www.typescriptlang.org/tsconfig/#exactOptionalPropertyTypes) |
| Intersecting a primitive with a unique object type ("branding") is the idiom behind `string & { __brand }`, which gives an opaque token nominal identity without changing its wire form. | Nominal typing / branding | [TypeScript Handbook — Object Types / Intersection Types](https://www.typescriptlang.org/docs/handbook/2/objects.html#intersection-types) |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The two one-token failure modes, and why removing the cast alone did not close the second one. | L1-L28 | [conversationWire.ts](conversationWire.ts) |
| The three brand mints that replaced the scattered inline casts. | L50-L65 | [conversationWire.ts](conversationWire.ts) |
| `ConversationCapabilityOverrides` derived from the wire type, and the full twenty-three-leaf tree `conversationCapabilities` produces. | L90-L146 | [conversationWire.ts](conversationWire.ts) |
| `conversationPage` binding `items` once so the page's `totalItems` cannot disagree with its contents. | L228-L243 | [conversationWire.ts](conversationWire.ts) |
| `ConversationPage.capabilities` is REQUIRED — the fact that made the second defect an impossible fixture rather than an unusual one. | L286-L298 | [../../data/conversation/types.ts](../../data/conversation/types.ts) |
| The full `ConversationCapabilities` tree the builder must fill, and the branded cursor types the mints produce. | L26-L27; L253-L284 | [../../data/conversation/types.ts](../../data/conversation/types.ts) |
| `LibraryConversationKey` and the library rows the last two builders produce. | L16; L27; L40 | [../../data/conversation-library/types.ts](../../data/conversation-library/types.ts) |
| The override constraint every flat builder here takes, and the "one level deep only" limit that exempts `conversationCapabilities`. | L23-L69 | [overrides.ts](overrides.ts) |
| The registry entries that make the three mints the only three assertions allowed in this file. | L158-L169 | [../wireFixtureGuard.test.ts](../wireFixtureGuard.test.ts) |
| `ConversationCapabilities` asserted present in the guard's discovered vocabulary, so these builders are policed rather than merely conventional. | L209-L215 | [../wireFixtureGuard.test.ts](../wireFixtureGuard.test.ts) |
| The probe proving `conversationPage({ capabilities: undefined })` is now rejected at the call site. | L29-L38; L91-L99 | [../fixtureOverrides.test.ts](../fixtureOverrides.test.ts) |
| The companion builder module for the served projection, whose header carries the shared R6 reasoning. | L1-L46 | [wire.ts](wire.ts) |

## Cross-Repo References

No cross-repository boundary. The conversation grammar's producing models
(`serving/conversation/models.py`, `library/api.py`) and its consuming mirrors are all in
`agents-remember`; the harnesses these conversations come from are external processes, but no fixture
here crosses that boundary.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The mirror's own header names its in-repo Python sources, confirming the boundary is a language seam inside this repository rather than a repository boundary. | L1-L4 | [../../data/conversation/types.ts](../../data/conversation/types.ts) |
| The library grammar's mirror likewise cites in-repo `library/api.py` / `models.py`. | L1-L2 | [../../data/conversation-library/types.ts](../../data/conversation-library/types.ts) |

## Update History

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
