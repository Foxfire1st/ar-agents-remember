# dashboard/src/cockpit/serving-build-stamp/ServingBuildStamp.tsx

## Governing Overview

[overview](../../overview.md)

## Purpose

The top bar's muted serving-build stamp: which build and process answer the dashboard, whether the serving process's Python files are still the installed or checked-out ones, and whether this browser tab runs the bundle the server now ships.

## Code Commentary

The stamp reads three store fields: the boot-time `servingBuild`, the live `buildCurrentness` and the `servingProcessId`. It renders nothing until a serving build is known. The visible text is the commit label (or `v<version>` off-checkout) and a humanized uptime from `bootedAt`; when currentness is known it appends the state, prefixed with `checkout` in checkout mode, and a `stale` state takes the warning caution style.

The tooltip, repeated as the accessible label, names the version, commit, a dirty checkout, the absolute boot time, the process id, the currentness mode and state, the loaded and installed Python digests, when a difference was first seen, and the served reason and remedy; absent fields are left out rather than invented. A client-bundle mismatch is shown only when `clientMatchesServingBuild` proves one, as a reload hint in the tooltip; an unknown comparison adds nothing.

These are three separate identities: the immutable boot stamp, the current Python-file state and the client bundle. A currentness update changes only its own part of the stamp; the boot identity stays as served. Data attributes expose the client comparison, the currentness state and the mode for tests.

## Evidence

- The tooltip lists mode, state, digests, first-seen time, reason and remedy, leaving absent fields out. [1]
- The tooltip adds the process id and a reload hint only for a proven client-bundle mismatch. [2]
- The stamp reads the boot build, currentness and process id from the store and renders nothing without a build. [3]
- A stale state takes the warning style; checkout mode is named in the visible text. [4]
