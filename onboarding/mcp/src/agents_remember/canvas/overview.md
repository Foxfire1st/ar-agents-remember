# Generated Page Host And Review Presenter — Canvas

## Governing Overview

[mcp/src/agents_remember overview](../../../overview.md)

## Purpose

The canvas package owns the execution environment for a generated review page and the capability that authors one. It states a single isolation policy, creates host-owned sessions, speaks a closed message protocol, resolves evidence requests against an admitted revision, gates publication on a model-free load, serves a pinned offline kit, and keeps the presenter's attempts and publication confined. It does not own evidence admission (MIK-R102), durable revision lineage and reclamation (MIK-R103), or product assembly and comprehension examples (MIK-R106), and a generated page receives no dashboard, AR, local-service or credential authority.

## Hot Path Summary

A viewer opens a frame from one admitted revision; the host creates a session bound to that frame, revision and comparison, and serves the revision's own bytes under the policy whose digest the shipped proof must name. Generated scripts are enabled only while that proof covers the policy now served. The frame speaks one protocol version and four operations; an evidence request resolves against the revision's own admitted packet or is refused by name. The presenter starts only on an explicit activation, records a durable attempt, and publishes through the confined frame store after a model-free prospective load. Kit files are carried under the manifest's contract path when an attempt is authored, compared with the manifest as they are carried.

## Isolation Policy And The Proof Gate

One policy is stated once so the served bytes, the browser proof and the runtime gate cannot drift apart. `policy_digest` hashes the enforcement facts a proof is bound to; `frame_sandbox` never carries `allow-same-origin`, so a frame document runs on an opaque origin; `document_headers` and `asset_headers` carry the policy a document or an admitted asset is served with. `scripts_enabled` reads the shipped proof record and answers true only when that record covers every clause of the policy now served, and `scripts_gap` names the reasons it does not — an unproven or drifted policy therefore serves an inert page rather than a scripted one. `proof_gaps` and `record_gaps` check the record's own check table and observations, so a table that cannot be read covers nothing.

The proof record is a generated artifact: it binds the served policy, the enforcement modules' own bytes, the built frontend and the browser that ran the checks. Regenerating it after a sync changes those bindings and nothing else, which is why the record can be refreshed with the composed frontend while the backend enforcement facts stay identical.

## Sessions, Documents And The Protocol

`SessionRegistry.open` creates one session and reports the frames displaced to keep the active-frame ceiling; `CanvasSession` carries what it serves, its binding and its bounded request ledger. Revocation is by name — `revoke_frame` for navigation, replacement or a review-scope change, `revoke` for one channel — and the tombstone keeps the reason, not the content. A session string authenticates nothing by itself: `SessionBinding` records the frame, revision and comparison the bytes were served from, and the host compares a request to that record.

`document.bound_document` delivers the binding to the admitted document itself rather than to a navigated window, announcing departure on pagehide, so a page that navigates during parsing loses its channel instead of inheriting one. The frame's own navigation is an accepted browser capability, not a boundary the host claims to deny.

`parse_frame_message` refuses what a parser can see: malformed, oversized, wrong-version, unknown-op, foreign-session, stale-revision and foreign-comparison; `RequestLedger.admit` refuses `replayed`, `rate-limited` and `exhausted` after `charge` took the token, and revocation is the session's. The four frame operations are `ready`, `status`, `open-evidence` and `request-explanation`.

## Exact Evidence

The frame may ask to open something; the host decides what that is. `resolve_evidence_reference` answers only with a reference the revision's own admitted packet carries — a claim's basis, a claim, a collection item or a supplemental receipt — requires the packet and the binding to name the same comparison, and answers an unavailable or unsupported destination with its own limitation rather than substituting today's record. Two claims carrying one unnamed reference are refused as ambiguous instead of answered with a guessed basis.

## Presenter Authoring And Publication

`PresenterRunner` is the authoring port and its shipped default is `NativePresenterHarness`, whose launch carries only the confined tool server and which refuses with `presenter-confinement-unavailable` when it cannot confine; `UnconfiguredPresenterRunner` is what a caller that supplies no harness gets, so the refusal is by name rather than a claim of confinement.

## Readiness And The Prospective Load

`check_page` is the static check a prospective revision passes before it is offered as ready: it follows the document's own references, refuses one that leaves the revision or names no admitted asset, and reports reduced-motion and evidence-reference facts. `BrowserProspectiveLoad` performs the load itself in the selected browser through the package-owned runner, stages the exact prospective bytes, and downgrades a claim of success that contradicts its own observations. A revision whose load fails or is unavailable is refused with the failure named to the presenter; the check says nothing about how good an explanation is.

## The Pinned Kit

`kit_files` indexes the shipped manifest's entries, and `_read_verified` compares an entry's size and digest before a byte is handed out, and `_read_verified` compares those values before a byte is handed out; `kit_assets` exposes those files under the contract path a page names them by, so a revision carries the kit as its own admitted assets, and no later check refuses a kit path, so a presenter may publish its own bytes there. A page names a kit library by that relative path; serving the published revision adds no check, because the frame route serves the revision's own admitted assets.

## Dashboard Write Guard

The dashboard is local and unauthenticated, which is a deployment posture and not a write authorization. `RefuseCrossOriginWrites` sits in front of every route and refuses a state-changing browser request that does not come from the dashboard's own page — `Sec-Fetch-Site` other than `same-origin`, or, when that header is absent, a foreign or `null` `Origin` — with a named 403 that never reaches a route. `RefuseForeignHosts` refuses every request, reads included, whose `Host` names another host or port, against DNS rebinding. A request carrying neither header comes from no browser page, so CLI and tool-server calls keep working.

**L184.** The presenter's send stays outside the limit check by design, so this route changes nothing beyond the presenter's own outbound path.

## Evidence

- One policy, hashed into the value a proof record must name, so served bytes, the proof and the runtime gate cannot drift apart. [1]
- A frame document is sandboxed without `allow-same-origin`, so the generated document runs on an opaque origin. [2]
- Generated scripts are served enabled only when the shipped proof covers the policy now served. [3]
- The proof record's own check table and observations must cover every clause; a table that cannot be read covers nothing. [4]
- One session is created per frame and bound to the frame, immutable revision and comparison the bytes were served from. [5]
- Revocation ends one channel or every channel of a frame, and the tombstone keeps the reason rather than the content. [6]
- The binding is delivered to the admitted document, never to a navigated window, and departure is announced on pagehide. [7]
- One protocol version with a closed operation set validates an envelope against the session's binding before any effect. [8]
- A request is debited from the session's rate before the caller parses it, so refusal work is bounded as well. [9]
- The host resolves an evidence reference only against the revision's own admitted packet, or refuses it by name. [10]
- An explicit activation starts one authoring attempt, which is recorded durably before any host call. [11]
- Publication loads the exact prospective revision once without a model before any ready pointer moves. [12]
- The static readiness check refuses a page that names something its revision does not carry. [13]
- The prospective load runs in the selected browser through the package-owned runner and cannot report a pass that contradicts its own observations. [14]
- Kit files are carried under the manifest's contract path and compared with the manifest when carried; nothing refuses a kit path afterwards, so the kit is the page's offline toolbox and the sandbox is the boundary. [15]
- A state-changing browser request from another page is refused with a named 403 before it reaches a route. [16]
- Every request, reads included, answers only the dashboard's own host and port, against DNS rebinding. [17]
- The frame surface serves one live session's own document and admitted assets and nothing else. [18]
- Both canvas surfaces are registered after the API routes and before the static mount. [19]
