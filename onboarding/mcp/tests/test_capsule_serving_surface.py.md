# mcp/tests/test_capsule_serving_surface.py

## Governing Overview

[Onboarding overview](overview.md)

## Purpose

The shipped-surface, protocol-exchange, and guard cases for role-capsule and skill serving. The shipped corpus and manifest, the real client/server exchange over the installed SDK, and the guards the baseline review found unpinned (with the nesting rule) live here; fixture worlds, frozen vocabularies, and the first behaviour blocks stay in the sibling serving module and are imported, so every definition lives exactly once.

## Code Commentary

The shipped-surface block pins the real corpus: every served skill parses with frontmatter, a body digest, and a readable URI; the composition manifest and the catalog agree on skill identity and origin; this server's own index resource keeps the Agent Skills discovery shape (distinct from the extension's enumeration entries); and every extension entry is complete with verbatim frontmatter and per-file digests verified against the bytes on disk.

The protocol block drives one real client session against the real server over stdio and asserts everything the client observed: negotiated capabilities and extension declaration, discovery without bodies, the index naming every served skill, a selected body equal to the exact bytes on disk with its revision and trust metadata, a supporting-file read resolved against the skill root, the not-found refusal, the capsule operation in the tool surface, and both extension methods answered on the same transport with an unregistered method still refused. A separate live-server case proves a traversal URI is refused rather than served, and a sanity case proves the harness's own assertions can fail.

The guard block pins each seeded-mutation proof the baseline review found unpinned: an escaping catalog record is refused by the containment guard, the index loader refuses while a skill cannot be served, a directory/name disagreement is recorded not served, and a second extension declaration installs no second wrapper. The remaining cases pin altitude admission from the task layer itself, the capsule operation serving every seat the document can carry with refusal by name for the rest, flat publication of a nested skill, and the legacy role rename returning the canonical investigator with one notice.

## Evidence

- Split contract: surface cases here, worlds and vocabularies imported [1]
- Shipped corpus, manifest identity, index shape, entry completeness [2]
- Real stdio exchange and its eight client-observed checks [3]
- Live-server traversal refusal and harness-can-fail sanity [4]
- Seeded-mutation guards: containment, index, name rule, idempotence [5]
- Altitude admission, capsule seats, nesting, legacy rename [6]
