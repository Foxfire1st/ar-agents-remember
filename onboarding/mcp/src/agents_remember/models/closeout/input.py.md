# mcp/src/agents_remember/models/closeout/input.py

## Governing Overview

[closeout models route overview](overview.md)

## Purpose

Defines the public and durable closeout-input vocabulary shared by worktree closeout and direct landing: two typed legs (`code`, `memory`), each either enabled with a stripped nonblank explicit message or not applicable with a reason. It also defines field-specific refusal observations, the resolved plan, and the corrected-call shape returned to callers.

It is additionally the closeout-shaped way in to the attribution. `EffectiveCloseoutInput.memory_content_message(code_commit)` renders this closeout's own message with exactly one final-paragraph `Code-Commit: <sha>` trailer naming the code commit the same closeout landed, and it now **delegates** that rendering to `kernel.memory_attribution.render_memory_content_message`, the one writer of the trailer. Neither the key nor the trailer's format is defined here: since 260913-LCA-L2 the key is declared once in `kernel/memory_attribution.py`, and since 260913-LCA-L4 this module does not name it at all.

## Code Commentary

### Logic

The closed commit vocabulary is exactly `code` and `memory`. Raw input, resolved plans,
normalized effective input, and field-specific refusals all use those same two legs. The ledger
cache has no enabledness, message, or retry intent to satisfy.

`CloseoutMessageInput` is the raw public shape; it preserves omission, empty text, whitespace, and supplied values so the boundary can explain why a request is invalid. `ResolvedCloseoutPlan` states which legs the route and contract require. `EffectiveCloseoutInput` is the discriminated, normalized value that may cross below validation. `EnabledCloseoutLeg` rejects blank messages and stores only stripped text; `NotApplicableCloseoutLeg` carries no message and names why the leg does not apply.

`memory_content_message(code_commit)` is a delegation and nothing more: it returns `render_memory_content_message(self.message_for("memory"), code_commit)`. The rendering — the caller's body verbatim, a blank line, then the attribution as its own final block — lives in `kernel/memory_attribution.render_memory_content_message`, the module that also declares and reads back the one key literal; this method's job is to be the *closeout-shaped* way in to it, because an enabled memory leg is the only leg that has an attribution to render. The failure the one-writer rule prevents is silent rather than loud: a module that formatted its own trailer would emit a key the reader does not parse, and that looks like "no attribution exists" rather than like a bug. The direction is kernel → models because `layers.toml` ranks `kernel` below `models` and permits an import only from a lower rank, so a kernel module importing this model would import upward. The closeout's own message is the body, never a template, and the trailer is appended after a blank line because `git interpret-trailers` reads a trailer block only from the end of the message — which is also why a `Code-Commit:` line a caller wrote earlier in the body cannot be mistaken for this attribution. Both routes that commit memory content reach this method: `worktrees/modules/closeout_external.py::_commit_memory_content` and `worktrees/integration/direct_landing/direct_landing_execution.py::_direct_memory_commit`, and the closeout recovery route reaches the same producer transitively when it still owes its memory commit. Cache refresh does not call a commit-message renderer and creates no memory.md-only commit.

### Conventions

The model does not decide enabledness. Route- and contract-aware code in `worktrees/closeout_input.py` derives the plan, then constructs this type. `message_for` stays the raw public echo of one enabled leg's message — the code leg and the public effective-input echo use it — while the memory-content leg is rendered through `memory_content_message(code_commit)`, which delegates to the kernel's single renderer, so the attribution's format and its key have one definition for every producer in the package and cannot drift between the worktree and direct-landing routes. `enabled` is used when rendering intent.

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

## Evidence

### Docs References

No external Domain Documentation source is configured. The original CLIVE-L1 explicit-input
requirement remains, with its ledger leg retired by the authorized LCA-L9 change.

No configured external domain-documentation source applies.

### Repo-Internal References

- Raw input, resolved plans, effective input, and message-field vocabulary contain code and memory only. [1]
- Raw observations and typed refusal vocabulary are public data. [2]
- Effective legs are a discriminated union. [3]
- Only enabled legs can return a raw commit message; this stays the public echo. [4]
- The model imports and calls the kernel renderer; the key and trailer rendering have one kernel definition. [5]
- The layer contract that fixes the import direction: `kernel` ranks below `models`, so the model may import the renderer and not the reverse. [6]
- The round trip that proves this module's rendered trailer is the one the kernel reader parses, rather than two keys that merely look alike. [7]
- The census that enforces the one definition this route now depends on — the key identifier and its interpolation in exactly one production module, and all five producers reaching a shared renderer entry, this model's method included. [8]
- The worktree and direct routes render attributed memory messages at their real commit seams (since MIK-R09 the worktree route first validates a converted leaf's exact tree); no ledger commit is produced. [9]
- None [10]
- None [11]

### Cross-Repo References

No meaningful cross-repository reference applies.


No separate external implementation source applies to this file.
