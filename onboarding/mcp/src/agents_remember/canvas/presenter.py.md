# mcp/src/agents_remember/canvas/presenter.py

## Governing Overview

[governing route overview](overview.md)

## Purpose

The review-presenter capability: one exact comparison, one authored page. It admits an explicit authoring attempt, records it durably, hands it to a confined runner, publishes only through the frame store, and serves the saved-first view without starting or resuming anything.

## Code Commentary

- `Presenter.start` refuses an activation it was not given and admits the attempt's comparison, instrument and design text before any durable effect.
- `PresenterRunner` is the authoring port and its shipped default is `NativePresenterHarness`, which launches the confined tool server; a host that cannot confine the writes refuses with `presenter-confinement-unavailable`, and `UnconfiguredPresenterRunner` is the port implementation for a caller that supplies no harness at all.
- `say`, `status`, `transcript`, `resume`, `cancel` and `replace` are identity-bound operations with truthful local answers when no host session exists.
- `publish` moves the attempt's own folder into a new ready revision, and `_require_prospective_load` loads the exact prospective revision once without a model before the pointer moves.

## Evidence

- An explicit activation starts one durable authoring attempt. [1]
- Publication loads the prospective revision once without a model before any ready pointer moves. [2]
- A runner that cannot confine its writes refuses by name. [3]
