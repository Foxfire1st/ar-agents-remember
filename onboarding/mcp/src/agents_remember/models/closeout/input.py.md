# mcp/src/agents_remember/models/closeout/input.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/closeout/input.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-13T23:52+02:00 |
| lastVerifiedCommitHash | `52875e7a8695fc7b67bff21ebb07a67268213967` |
| lastVerifiedCommitDate | 2026-09-14T00:06:58+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[closeout models route overview](overview.md)

## Purpose

Defines the public and durable closeout-input vocabulary shared by worktree closeout and direct landing: three typed legs (`code`, `memory`, `ledger`), each either enabled with a stripped nonblank explicit message or not applicable with a reason. It also defines field-specific refusal observations, the resolved plan, and the corrected-call shape returned to callers.

It is additionally the closeout-shaped way in to the attribution. `EffectiveCloseoutInput.memory_content_message(code_commit)` renders this closeout's own message with exactly one final-paragraph `Code-Commit: <sha>` trailer naming the code commit the same closeout landed, and it now **delegates** that rendering to `kernel.memory_attribution.render_memory_content_message`, the one writer of the trailer. Neither the key nor the trailer's format is defined here: since 260913-LCA-L2 the key is declared once in `kernel/memory_attribution.py`, and since 260913-LCA-L4 this module does not name it at all.

## Code Commentary

### Logic

`CloseoutMessageInput` is the raw public shape; it preserves omission, empty text, whitespace, and supplied values so the boundary can explain why a request is invalid. `ResolvedCloseoutPlan` states which legs the route and contract require. `EffectiveCloseoutInput` is the discriminated, normalized value that may cross below validation. `EnabledCloseoutLeg` rejects blank messages and stores only stripped text; `NotApplicableCloseoutLeg` carries no message and names why the leg does not apply.

`memory_content_message(code_commit)` (`:148-166`) is a delegation and nothing more: it returns `render_memory_content_message(self.message_for("memory"), code_commit)` (`:166`). The rendering — the caller's body verbatim, a blank line, then the attribution as its own final block — lives in `kernel/memory_attribution.render_memory_content_message`, the module that also declares and reads back the one key literal; this method's job is to be the *closeout-shaped* way in to it, because an enabled memory leg is the only leg that has an attribution to render. The failure the one-writer rule prevents is silent rather than loud: a module that formatted its own trailer would emit a key the reader does not parse, and that looks like "no attribution exists" rather than like a bug. The direction is kernel → models because `layers.toml` ranks `kernel` below `models` and permits an import only from a lower rank, so a kernel module importing this model would import upward. The closeout's own message is the body, never a template, and the trailer is appended after a blank line because `git interpret-trailers` reads a trailer block only from the end of the message — which is also why a `Code-Commit:` line a caller wrote earlier in the body cannot be mistaken for this attribution. Both routes that commit memory content reach this method: `worktrees/modules/closeout_external.py::_commit_memory_content` and `worktrees/integration/direct_landing/direct_landing_execution.py::_direct_memory_commit`, and the closeout recovery route reaches the same producer transitively when it still owes its memory commit. The ledger leg does not: it still calls plain `message_for("ledger")` and carries no trailer, because the `memory.md`-only commit names no code commit.

### Conventions

The model does not decide enabledness. Route- and contract-aware code in `worktrees/closeout_input.py` derives the plan, then constructs this type. `message_for` stays the raw public echo of one enabled leg's message — the code leg, the ledger leg, and the public effective-input echo use it — while the memory-content leg is rendered through `memory_content_message(code_commit)`, which delegates to the kernel's single renderer, so the attribution's format and its key have one definition for every producer in the package and cannot drift between the worktree and direct-landing routes. `enabled` is used when rendering intent.

### Invariants And Boundaries

- An enabled leg always has explicit stripped nonblank intent; a not-applicable leg never carries a sentinel empty message.
- The attribution's **rendering** has exactly one definition, and it is not here: `memory_content_message` delegates to `kernel.memory_attribution.render_memory_content_message`, which is the one writer of the trailer for all five producers. This model contributes the body (the closeout's own memory message verbatim) and the code commit; it never replaces the body and never invents an attribution for a commit that has no code counterpart to name.
- The attribution's **key** is declared once, in `kernel/memory_attribution.py`, and this module does not name it at all — it imports the renderer, not the constant. This module must never re-declare the key and must never spell the trailer as a literal: a second spelling would let a producer emit a trailer the reader does not parse, and that failure looks like "no attribution exists" rather than like a bug. The direction is fixed by `layers.toml` — `kernel` is ranked below `models`, so a kernel module importing a model would import upward.
- The trailer has to be inside the commit object when the object is created, because the message is hashed into it. Both callers render the message at the commit seam for that reason; `prove_git_commit` journals the resulting sha on the next statement, so anything added later could only be a rewrite of an already-proved object (`git notes` is not bound by the hash).
- There is no generated subject, default commit message, or compatibility input alongside this model.
- `CloseoutInvalidField`, `CloseoutCorrectedCall`, and `ResolvedCloseoutPlan` make refusal actionable without acquiring integration authority or touching Git.
- Queue selection has no dependency on this type; it remains a scheduling projection outside L1.

### Todos

None recorded. Public retry/recover/revise controls belong to L2, not this model.

## Docs References

See task `260821-CLIVE-L1`, especially L1-R1 through L1-R3 and L1-R5.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Raw observations and typed refusal vocabulary are public data. | `CloseoutMessageInput`, `CloseoutInvalidField` | mcp/src/agents_remember/models/closeout/input.py:47-55; mcp/src/agents_remember/models/closeout/input.py:79-88 |
| Effective legs are a discriminated union. | `EnabledCloseoutLeg`, `NotApplicableCloseoutLeg` | mcp/src/agents_remember/models/closeout/input.py:99-127 |
| Only enabled legs can return a raw commit message; this stays the public echo. | `message_for` | mcp/src/agents_remember/models/closeout/input.py:142-146 |
| The attribution is delegated rather than formatted here: this model imports the kernel's one renderer at `input.py:9` and calls it at `:166`; the key's single declaration and the trailer's single interpolation both live in the kernel. | `render_memory_content_message` | mcp/src/agents_remember/models/closeout/input.py:9-9; mcp/src/agents_remember/models/closeout/input.py:148-166; mcp/src/agents_remember/kernel/memory_attribution.py:56-56; mcp/src/agents_remember/kernel/memory_attribution.py:72-97 |
| The layer contract that fixes the import direction: `kernel` ranks below `models`, so the model may import the renderer and not the reverse. | "a module in package P may import package Q only when rank(Q) < rank(P)"; `order` | layers.toml:25-25; layers.toml:32-59 |
| The round trip that proves this module's rendered trailer is the one the kernel reader parses, rather than two keys that merely look alike. | `test_the_rendered_trailer_is_the_one_the_reader_parses` | mcp/tests/test_memory_ledger.py:562-597 |
| The census that enforces the one definition this route now depends on — the key identifier and its interpolation in exactly one production module, and all five producers reaching a shared renderer entry, this model's method included. | `test_the_attribution_key_is_named_and_rendered_in_exactly_one_module`; `test_every_census_producer_reaches_the_shared_renderer` | mcp/tests/test_memory_attribution_producers.py:86-117; mcp/tests/test_memory_attribution_producers.py:119-137; mcp/tests/test_memory_attribution_producers.py:55-65 |
| The memory-content message is rendered at the commit seams through the model method: the worktree route and the direct-landing route both call `memory_content_message` (each handing it the code commit it landed), while the ledger leg keeps `message_for("ledger")` and no trailer. | `_commit_memory_content`; `_direct_memory_commit`; `_commit_ledger_mapping` | mcp/src/agents_remember/worktrees/modules/closeout_external.py:165-167; mcp/src/agents_remember/worktrees/integration/direct_landing/direct_landing_execution.py:270-274; mcp/src/agents_remember/worktrees/modules/closeout_external.py:241-243 |

## Cross-Repo References

No meaningful cross-repository reference applies.

## Update History

- 2026-09-13T23:52+02:00 — 260913-LCA-L4 curator (uncommitted change set on `ar/260913-lca-l4-ar`,
  base `5bb124d4`): the delegation moved one rank down. This model no longer names the trailer key at
  all — `input.py:9` imports `render_memory_content_message` instead of
  `CODE_COMMIT_TRAILER_KEY`, and `memory_content_message` (`:148-166`) is now exactly
  `return render_memory_content_message(self.message_for("memory"), code_commit)` (`:166`). Corrected
  the Purpose, the Logic (which still showed the deleted f-string as where the trailer is rendered),
  the Conventions and the two render invariants, added the kernel renderer and the one-definition
  census as evidence, repointed the stale class/method ranges
  (`CloseoutMessageInput` 44-51 → 47-55, `CloseoutInvalidField` 76-84 → 79-88, the leg union
  96-118 → 99-127, `message_for` 139-143 → 142-146) and removed the duplicated commit-seam row this
  table carried. Verification metadata remains closeout-owned; no acceptance claim and no verification
  stamp advanced.

- 2026-09-13T23:28+02:00 — 260913-LCA-L2 (uncommitted change set on `ar/260913-lca-l2-ar`): this
  model is part of the change set now. The trailer key it declares-and-renders is no longer declared
  here: `CODE_COMMIT_TRAILER_KEY` is imported from `kernel/memory_attribution.py` (`input.py:9`), so
  the writer's key and the reader's key are one literal and
  `grep -rn '"Code-Commit"' --include=*.py mcp/` has exactly one hit. Corrected the Purpose, Logic,
  Conventions, the invariants (splitting the
  rendering's one definition from the key's one declaration) and the reference rows, added the layer
  contract and the round-trip case as evidence, and repointed the ranges shifted by the new import
  block — including the record/metadata `governingOverview`, which now points at this leaf's nearest
  route overview (`closeout/overview.md`) instead of the models route. The L1 entry below stands as
  the record of what was true when it was written. Verification metadata remains closeout-owned; the
  `1ddf7fda` stamp is left as it was, since no commit contains this candidate yet — no acceptance
  claim and no verification stamp advanced.

- 2026-09-13T21:42+02:00 — 260913-LCA-L1 (uncommitted change set on `ar/260913-lca-l1-ar`): recorded that this model now owns the attribution as well as the messages — `CODE_COMMIT_TRAILER_KEY` plus `memory_content_message(code_commit)`, which returns the closeout's own message verbatim with exactly one final-paragraph `Code-Commit: <sha>` trailer naming the code commit that same closeout landed. Stated the one-definition rule (both closeout routes render through it; the `memory.md`-only ledger leg keeps `message_for("ledger")` and carries none) and why the seam is the message construction rather than a later step. Verification metadata remains closeout-owned; no acceptance claim and no verification stamp advanced.

- 2026-08-25T08:16+02:00 — 260824-PDLS wave 004: moved this preserved sidecar with its behavior-preserving package split, repointed source evidence, and verified the emergency-landed source path at code commit `cb6623775a04cbdeb0509dc26f08a8268189c3f6`; this is onboarding provenance, not Dagger certification.

- 2026-08-22T10:39+02:00 — 260821-CLIVE-L1: created from accepted candidate tree `4241908c`; verification metadata remains blank until governed closeout stamps the landed code commit.
