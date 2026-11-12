# skills/l-01-agent-lifecycles/core/launcher.md

## Purpose

Describe the developer-facing chat without a role. It answers research inline and hands managed work to a distinct host agent; it never becomes the Architect.

## Code Commentary

The current source has no spawn-role or plane identity selector. The launcher has no seat binding or worktree; its free-chat routing name does not imply an ambient session lifecycle. It resolves the sprint and writes the developer’s request into its canonical document before one `role_start` call. An Architect start carries neither a brief nor a document reference; the developer is told where the request lives and speaks with the agent in the dashboard. Launch settings supply the choices. `role_message` from this unbound chat is refused, and a refused start never falls back to another tool.

For a first sprint only, the launcher creates the sprint document, a master and its first leaf before it starts the Architect, and writes into them only the developer's request and scope: no requirement packets and no approved order.

An explicit developer-named role and task selects the bounded takeover route through the same `role_start`; no incumbent is privately replaced and no exact-id attachment is improvised. After a start the launcher stops local role work. The launcher remains outside `roles/`, because it is not a role seat.

Retained corpus composition metadata is not proof of what a native launched agent receives.

## Evidence

- Unbound free chat has no role binding or worktree; research stays inline and does not become a role. [8]

- Managed work is written into the sprint before one parentless Architect start without a brief or document reference. [9]

- Only an explicitly developer-named role and task takes the bounded takeover route. [10]

- No other start or message route and no local work after start is permitted. [11]

- The launcher remains outside roles because it is not a role seat. [12]

- The manifest retains ambient-launcher metadata outside the role registry; this is not the native routing-condition set. [13]

- The source assertions exclude launcher from roles, retain ambient metadata and separately check the two native routing conditions; this is not an executed PASS. [14]
