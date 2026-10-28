# Generated Page Host And Explainer Environment — Canvas

## Governing Overview

[mcp/src/agents_remember overview](../../../overview.md)

## Purpose

The canvas package owns the execution environment for a generated review page and the capability that authors one. It states a single isolation policy, creates host-owned sessions, speaks a closed message protocol, resolves evidence requests against an admitted revision, gates publication on a model-free load, serves a pinned offline kit, and keeps the presenter's attempts and publication confined. It does not own evidence admission (MIK-R102), durable revision lineage and reclamation (MIK-R103), or product assembly and comprehension examples (MIK-R106), and a generated page receives no dashboard, AR, local-service or credential authority.

## Hot Path Summary

A viewer opens a frame from one admitted revision; the host creates a session bound to that frame, revision and comparison, and serves the revision's own bytes under the policy whose digest the shipped proof must name. Generated scripts are enabled only while that proof covers the policy now served. The frame speaks one protocol version and five frame operations, with a separately validated host stale-part notice; an evidence request resolves against the revision's own admitted packet or is refused by name. The first explicit Send builds or attaches one derived explainer seat, prepares its bound environment and records the request; publication still goes through the frame store after readiness and a model-free prospective load. Opening the page starts nothing. Kit files are carried under the manifest's contract path when an attempt is authored, compared with the manifest as they are carried.

## Isolation Policy And The Proof Gate

One policy is stated once so the served bytes, the browser proof and the runtime gate cannot drift apart. `policy_digest` hashes the enforcement facts a proof is bound to; `frame_sandbox` never carries `allow-same-origin`, so a frame document runs on an opaque origin; `document_headers` and `asset_headers` carry the policy a document or an admitted asset is served with. `scripts_enabled` reads the shipped proof record and answers true only when that record covers every clause of the policy now served, and `scripts_gap` names the reasons it does not — an unproven or drifted policy therefore serves an inert page rather than a scripted one. `proof_gaps` and `record_gaps` check the record's own check table and observations, so a table that cannot be read covers nothing.

The proof record is a generated artifact: it binds the served policy, the enforcement modules' own bytes, the built frontend and the browser that ran the checks. Regenerating it after a sync changes those bindings and nothing else, which is why the record can be refreshed with the composed frontend while the backend enforcement facts stay identical.

## Sessions, Documents And The Protocol

`SessionRegistry.open` creates one session and reports the frames displaced to keep the active-frame ceiling; `CanvasSession` carries what it serves, its binding and its bounded request ledger. Revocation is by name — `revoke_frame` for navigation, replacement or a review-scope change, `revoke` for one channel — and the tombstone keeps the reason, not the content. A session string authenticates nothing by itself: `SessionBinding` records the frame, revision and comparison the bytes were served from, and the host compares a request to that record.

`document.bound_document` delivers the binding to the admitted document itself rather than to a navigated window, announcing departure on pagehide, so a page that navigates during parsing loses its channel instead of inheriting one. The frame's own navigation is an accepted browser capability, not a boundary the host claims to deny.

`parse_frame_message` refuses what a parser can see: malformed, oversized, wrong-version, unknown-op, foreign-session, stale-revision and foreign-comparison; `RequestLedger.admit` refuses `replayed`, `rate-limited` and `exhausted` after `charge` took the token, and revocation is the session's. The five frame operations are `ready`, `status`, `open-evidence`, `request-explanation` and `offer-selections`. A selection offer carries confirmed question/choice text into the trusted tray and sends no message. The host’s `stale-parts` notice carries at most thirty-two admissible ids and the true count; marks inside the page are advisory, while the trusted panel owns the reasoned list.

## Exact Evidence

The frame may ask to open something; the host decides what that is. `resolve_evidence_reference` answers only with a reference the revision's own admitted packet carries — a claim's basis, a claim, a collection item or a supplemental receipt — requires the packet and the binding to name the same comparison, and answers an unavailable or unsupported destination with its own limitation rather than substituting today's record. Two claims carrying one unnamed reference are refused as ambiguous instead of answered with a guessed basis.

## Presenter Authoring And Publication

The standalone presenter native launch is retired. A bare `Presenter` now selects `UnconfiguredPresenterRunner` and refuses `no-confined-harness`; an explicitly supplied confined runner can still use the retained attempt implementation. The normal explainer uses its bound task server and the shared `AuthoringTools` implementation, with no standalone presenter server.

The leaf’s environment lives outside worktrees, memory repositories and task folders. Build, Update, grades and Retire use its one leaf lock; the build writes snapshots, instructions and packet before binding last, then sends after releasing the lock. Update rebinds without waking a turn and refuses while in turn or retired. Retire waits for the lock and durably records the process tree, archive, process cleanup and workspace removal, preserving an unfinished receipt for retry. Retained pages and grades stay with the task.

## Readiness And The Prospective Load

`check_page` is the static check a prospective revision passes before it is offered as ready: it follows the document’s own references, refuses one that leaves the revision or names no admitted asset, and reports reduced-motion and evidence-reference facts. It also derives the part map from static `data-part` and claim-id marks, refuses invalid parts, unknown or unmapped claims and unresolved bases, and carries the map into publication. A page declaring no parts is answered whole-page. `BrowserProspectiveLoad` performs the load itself in the selected browser through the package-owned runner, stages the exact prospective bytes, and downgrades a claim of success that contradicts its own observations. The browser runner observes legacy evidence references and claim ids in separate bounded inventories, including marks scripts add during the load window; the trusted caller resolves both against the exact packet. A revision whose load fails or is unavailable is refused with the failure named to the presenter; the check says nothing about how good an explanation is.

## The Pinned Kit

`kit_files` indexes the shipped manifest's entries, and `_read_verified` compares an entry's size and digest before a byte is handed out, and `_read_verified` compares those values before a byte is handed out; `kit_assets` exposes those files under the contract path a page names them by, so a revision carries the kit as its own admitted assets, and no later check refuses a kit path, so a presenter may publish its own bytes there. A page names a kit library by that relative path; serving the published revision adds no check, because the frame route serves the revision's own admitted assets.

## Dashboard Write Guard

The dashboard is local and unauthenticated, which is a deployment posture and not a write authorization. `RefuseCrossOriginWrites` sits in front of every route and refuses a state-changing browser request that does not come from the dashboard's own page — `Sec-Fetch-Site` other than `same-origin`, or, when that header is absent, a foreign or `null` `Origin` — with a named 403 that never reaches a route. `RefuseForeignHosts` refuses every request, reads included, whose `Host` names another host or port, against DNS rebinding. A request carrying neither header comes from no browser page, so CLI and tool-server calls keep working.

**L184.** The presenter's send stays outside the limit check by design, so this route changes nothing beyond the presenter's own outbound path.

The explainer’s categories and grades remain its judgment, separate from change badges and accepted knowledge. Grades bind to block fingerprints and the comparison at which they were made; unresolved target reads mark parts or grades stale with a reason. The target is the environment binding unless the view explicitly selects another comparison or reads after Retire. Stale grades keep their value in the judgment sort, and a stale-page message regenerates nothing until the developer sends it.

## Evidence

- One policy, hashed into the value a proof record must name, so served bytes, the proof and the runtime gate cannot drift apart.

- A frame document is sandboxed without `allow-same-origin`, so the generated document runs on an opaque origin. 

- Generated scripts are served enabled only when the shipped proof covers the policy now served. 

- The proof record's own check table and observations must cover every clause; a table that cannot be read covers nothing. 

- One session is created per frame and bound to the frame, immutable revision and comparison the bytes were served from. 

- An explicit activation starts one authoring attempt, which is recorded durably before any host call. 

- The prospective load runs in the selected browser through the package-owned runner and cannot report a pass that contradicts its own observations. 

- The frame surface serves one live session's own document and admitted assets and nothing else. 

- Both canvas surfaces are registered after the API routes and before the static mount. 

- Retired at the fifth freeze d59c3493: mcp/src/agents_remember/canvas/policy.py:380-384 - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit 47f69f11afb982e318006209036aed22f1792976; mcp/src/agents_remember/canvas/policy.py::frame_sandbox - the bytes it recorded now occur 2 times in the file, so no single home can be named and it is not given to the likelier one; mcp/src/agents_remember/canvas/policy.py::scripts_enabled - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit 47f69f11afb982e318006209036aed22f1792976; mcp/src/agents_remember/canvas/policy.py::proof_gaps - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit 47f69f11afb982e318006209036aed22f1792976; mcp/src/agents_remember/canvas/sessions.py::SessionRegistry - the bytes it recorded now occur 2 times in the file, so no single home can be named and it is not given to the likelier one; mcp/src/agents_remember/canvas/presenter.py::Presenter - the bytes it recorded now occur 64 times in the file, so no single home can be named and it is not given to the likelier one; mcp/src/agents_remember/canvas/prospective.py::BrowserProspectiveLoad - the bytes it recorded now occur 3 times in the file, so no single home can be named and it is not given to the likelier one; mcp/src/agents_remember/serving/canvas.py::page - the bytes it recorded now occur 19 times in the file, so no single home can be named and it is not given to the likelier one; mcp/src/agents_remember/serving/canvas.py::register_canvas_routes - the bytes it recorded now occur 2 times in the file, so no single home can be named and it is not given to the likelier one. Retired means the anchor no longer stands, not that the cited subject was deleted.

- Revocation ends one channel or every channel of a frame, and the tombstone keeps the reason rather than the content. [6]

- The binding is delivered to the admitted document, never to a navigated window, and departure is announced on pagehide. [7]

- One protocol version with a closed operation set validates an envelope against the session's binding before any effect. [8]

- A request is debited from the session's rate before the caller parses it, so refusal work is bounded as well. [9]

- The host resolves an evidence reference only against the revision's own admitted packet, or refuses it by name. [10]

- Publication loads the exact prospective revision once without a model before any ready pointer moves. [12]

- The static readiness check refuses a page that names something its revision does not carry. [13]

- Kit files are carried under the manifest's contract path and compared with the manifest when carried; nothing refuses a kit path afterwards, so the kit is the page's offline toolbox and the sandbox is the boundary. [15]

- A state-changing browser request from another page is refused with a named 403 before it reaches a route. [16]

- Every request, reads included, answers only the dashboard's own host and port, against DNS rebinding. [17]

- The current implementation introduces bound grades, per-part staleness and explicit regeneration; the existing isolated-page, evidence and kit guarantees remain. [20]
