# mcp/src/agents_remember/canvas/presenter.py

## Governing Overview

[governing route overview](overview.md)

## Purpose

The review-presenter capability: one exact comparison, one authored page. It admits an explicit authoring attempt, records it durably, hands it to a confined runner, publishes only through the frame store, and serves the saved-first view without starting or resuming anything.

## Code Commentary

- `Presenter.start` refuses an activation it was not given and admits the attempt's comparison, instrument and design text before any durable effect.
- `PresenterRunner` is the authoring port. The dedicated native presenter launch is retired: constructing `Presenter` without an explicitly supplied runner selects `UnconfiguredPresenterRunner`, whose start refuses `no-confined-harness`. A bare presenter therefore starts no seat with a missing tool surface.
- `say`, `status`, `transcript`, `resume`, `cancel` and `replace` are identity-bound operations with truthful local answers when no host session exists.
- `publish` moves the attempt's own folder into a new ready revision, and `_require_prospective_load` loads the exact prospective revision once without a model before the pointer moves.

`publish` carries the explicit part map admitted by readiness into the new revision, and propagates the frame store’s own refusal reason instead of replacing it with a generic publication error.

## Evidence

- An explicit activation starts one durable authoring attempt. 
- Publication loads the prospective revision once without a model before any ready pointer moves. [2]
- A runner that cannot confine its writes refuses by name. [3]

- The current implementation adds readiness part-map persistence and typed publication refusal propagation; the existing prospective-load and attempt identity account remains valid. [4]

- Retired at the fifth freeze d59c3493: mcp/src/agents_remember/canvas/presenter.py::Presenter - the bytes it recorded now occur 64 times in the file, so no single home can be named and it is not given to the likelier one. Retired means the anchor no longer stands, not that the cited subject was deleted.
