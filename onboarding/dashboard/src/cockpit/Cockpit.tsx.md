# dashboard/src/cockpit/Cockpit.tsx

## Governing Overview

[overview](../overview.md)

## Purpose

Production dashboard chrome, retained product layers and the review page's shared chat rail. The product bar remains Chats, Operations, Knowledge and File Viewer; the Tray button sits beside that group. Other retained views have no bar entry and can be mounted by an injected view; static imports alone do not establish production bundle exclusion.

## Code Commentary

`Cockpit` connects shared state/events and ready hydration. `CockpitShell` owns presentation, wake-lock lifetime, the revalidation provider and page dispatch. It also holds
the bell's agent request (`agentChat`) and the one handler that names an exact seat and switches to the chats
view, so no panel below it has to write the observed-chat channel. A knowledge-reader URL selects Knowledge. A valid review URL selects Operations and places the review reading column beside the same right chat rail. Ordinary change-set and notes readers retain takeover dispatch; review targets do not pass through `ChangeSetTakeover`. Base review navigation carries repository/master/leaf and recorded-history state. The mounted reviewer separately reads and writes its selection and comparison in the hash using replaceState, without replacing that base target. [72] [97]

Operations, File Viewer, Knowledge and Role chats retain their layers. Entering the review hides the ordinary main layers and Operations task tree; it renders `ReviewMain` in a stable slot immediately before the existing right rail. Leaving review restores the ordinary main layers. Operations exposes independent left/right sidebar toggles outside the memoized detail panel. Hidden child owners receive active predicates separately from component retention. [88] [89]

The right rail has one unkeyed chat wrapper for Operations and review. Operations retains the River/Chat switch and conditionally mounts Event River. Review supplies its task, open state and width to that same rail, uses chat only, and forwards closed-column preload. The shared DocumentChat remains in its wrapper across that transition; the rail gains neither a new frame wrapper nor a key. Component retention and active predicates remain separate from native iframe generations and view-switch timing. [92] [93]

Wide Operations columns use saved widths and give a hidden sidebar's width to the document. The review grid has its reading track plus the open in-grid chat width, or a zero-width chat track and the review gutter when closed or overlaid. At at-most40rem the railed body is one column. Extracted shell styles still own narrow vertical scrolling and wrapped chrome. Only the ordinary change-set takeover consumes the fixed takeover body here. [65] [98]

The shell publishes the shown page and repository for tray provenance and filing scope: Review names its repository, Operations names the viewed document's repository, and File Viewer leaves repository publication to its own owner. The Tray button is outside the four-view tab group, and the page-wide tray layer is outside the railed body.

TopBar consumes served counts and ordered queue state. Its task-count line comes from `topBarCountsLine` in `topBarCounts.ts`: it adds a `waiting` count only when a task waits, and drops the works, waiting and paused words while host activity is unknown, naming that unavailability once; the attention chip (`⚠ N waiting`) draws only when the queue is nonempty. It renders the serving-build stamp owned by `serving-build-stamp/ServingBuildStamp.tsx`; a serving build mismatch is a diagnostic tooltip there. EffectsToggle updates local effects state/storage; shared animation and boot state remain separate owners. Task selection and the Engine Room stable-empty process fallback remain separate projections. [69] [70] [71] [94]

## Evidence

### Docs References

No configured domain documentation; source owners support this current account.

### Repo-Internal References

- The product bar and its order are one list. [32]




- The layer wrapper that hides without unmounting. [37]
- The mode-bar primitive that renders the product entries. [38]






- `EffectsToggle` (✦ Effects / ❄ Calm) — flips `data-effects` + persists `calm-cockpit`. [69]
- The boot-time effects flag it persists to. [70]
- The honest-motion gate the rail transition + the toggle drive. [71]
- Cockpit wires connectState and one connectEvents raw Event River consumer, plus the ready hydration marker; no seat-event reconciler. [72]

- The reader's hash parser. [75]



- The reviewed UI contract owner `ViewLayer`. [90]

- Stored cockpit regression source covering retained product views; it is source evidence, not a fresh test, browser or performance result. [91]



- The header's count line uses shared labels for served taskCounts, adds a waiting count only while a task waits, omits works, waiting and paused words when host observation is unknown, and reports host activity unavailable once rather than drawing an unknown-count bucket. [94]




### Cross-Repo References

No separate cross-repository implementation claim.


- The shell defaults to Chats; a valid review hash selects Operations and a valid knowledge-reader hash selects Knowledge. Persistent product layers remain mounted independently of takeover selection.


- Knowledge is a full-bleed, hidden-not-unmounted layer. [34]


- Full-bleed is derived for the product and retained machine-map views.


- A page outside the bar mounts only through an injected view. [36]


- The Knowledge reader the retained layer mounts. [39]


- The revalidation provider is shown only for ordinary Operations outside takeover and review.

- RailedBody applies saved Operations sidebar widths or the review's reading/chat tracks; its narrow path uses one column. [65]
- Files, Engine Room, Topology, Knowledge, and Chats request the full-bleed layout. [66]

- Rail fade properties are selected by the animation permission.


- The `chatsLayer` keep-alive class used by the Chats layer. [68]

- A `#knowledge?…` reader URL selects the Knowledge view as the shell's initial view. [73]
- The frontend `Analytics` projection includes the `engineProcesses` process-map collection. [79]

- The reviewed UI contract owner `MainLayers`. [88]

- MainLayers mounts the persistent RoleChatsPane with tasks and the visible/non-takeover active predicate, forwarding agentChat as openChat. RailedBody passes shell agentChat to MainLayers and openAgentChat to LeftRail; LeftRail forwards that handler to LifecycleList. Native host transport remains separately owned. [89]

- The right rail keeps one unkeyed chat wrapper across Operations and review; Operations' River still mounts conditionally. [92]

- The hidden chat side stays mounted but out of reach behind display:none and aria-hidden. Anchor: "export function RightRail(props: RightRailProps) {" [93]

- Native task selection and memoization are separate from the Engine Room stable-empty fallback.


- The shell starts the screen wake lock once on mount; the wake-lock helper follows document visibility and releases its held sentinel on stop. [96]


- Base review navigation names repo/master/leaf and recorded history. Separate reviewer hash helpers persist selection/comparison through replaceState without changing that target or adding browser-history entries. [97]


- At at-most40rem the shell admits vertical overflow and single-column railed content. The ordinary change-set takeover uses the fixed takeover body; review is rendered in the railed body. [98]

- Review is explicitly excluded from takeover. [99]
- Independent Operations sidebar toggles outside DetailPanel. [100]
- Review column shares the right rail and DocumentChat wrapper. [101]
- Operations/sidebar and review/chat column sizing. [102]
- Shown page/repository provenance values. [103]

- Tray button outside the view group and layer outside railed body.

- The top bar renders the serving-build stamp from its own module. [106]

- The shared RightRail forwards the review leaf's explainer target into the same DocumentChat wrapper. Operations still uses its ordinary document chat; its active leaf document also mounts ViewedLeafExplainerControl, which can read and retire an existing explainer without visiting Review. The Operations active predicate is shared with DetailPanel, and switching pages adds neither a frame wrapper nor a frame key. [105]
