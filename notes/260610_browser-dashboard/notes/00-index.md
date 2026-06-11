# Browser Dashboard — Research Notes Index

| Field | Value |
| --- | --- |
| Repo | agents-remember |
| Created | 2026-06-10 |
| Status | **Pre-task research base.** No `task.md` yet — deliberately. One bounded file per topic so each can be discussed and settled on its own before tasks are defined. |
| Provenance | Recon workflow 2026-06-10 (7 agents: prototype, branches, issues, data surfaces, 2× frame scan, tech research) + developer direction from the same day's session. Inventory baseline: MCP 2.7.0 @ `ab7e21b`; **2.8.0 landed during the session** (issue-54 fix, new `worktree_sync`) — see note 11 item 16. |
| Raw artifacts | `raw/recon-workflow-output.json` (full agent reports) · `raw/mockups/` (the `origin/browser-dashboard` mockup HTMLs — **mc2 is the designated design endpoint** — plus the Open Design iteration screenshots incl. two annotated directions; see note 07) · `raw/Inspirations/` (podracer clip + extracted frames + ui-animations.mp4, added by developer). The issue-#2 mockup image was removed by the developer — older mockup lineage that served only as the Open Design seed. |

## How To Use

Discuss one file per sitting; settled answers get written back into the topic
note (and struck from `11-open-questions.md`). When enough topics are settled,
the task series gets cut from note 11 item 21. Files are numbered in suggested
discussion order: foundations (01–05) before product/visual (06–08) before
stack (09).

## File Map

| File | Hook | Status |
| --- | --- | --- |
| `01-lifecycle-entity.md` | The root primitive: identifiable, observable lifecycles; every action attributable via lifecycle-id | **SETTLED 2026-06-10, sharpened 2026-06-11**: signals-vs-states player model + orthogonal phases, system-managed ids (guarded start, contract-owned resume, `switch_lifecycle` as the only id-carrying signal), fleeting-vs-persistent boundary at the worktree, save gate on switch-from-fleeting (landing zones `0_misc` / `1_inter-repo-work` — Q23), TTL fleeting-only, worktree-only closeouts (spawned follow-up Q22). Small mechanics remain |
| `02-event-model-middle-layer.md` | Point events vs long-running spans; the reducer ("runtime engine", to be renamed) that owns interpretation; what to salvage from the observer branch (concepts, not code) | Concepts accepted; naming + schema open |
| `03-data-surfaces.md` | The 14 artifacts a dashboard can read today + the 12 gaps (= observability backlog) | Inventory; re-verify at 2.8.0 |
| `04-control-plane-interaction.md` | Two-way interaction (act on attention items in the same UX); gates; the deliberate "plan for 3.0, architecture supports the dashboard" posture | Requirement fixed; mechanism open |
| `05-read-packet-paired-reads.md` | #46 paired source+onboarding reads as observable, lifecycle-attributed events | Design-relevant now, implementable later |
| `06-attention-queue-ia.md` | Home-screen working theory (attention queue + ops console IA) + the mandated "Can we do this better?" sub-task | Accepted as working theory |
| `07-prototype-review.md` | `browser-dashboard` branch dissection; harvest list; rebuild verdict; mc2 IA supersedes mc1 | Reviewed; decisions recorded |
| `08-visual-language.md` | The podracer grammar (state by color+silhouette), frame-verified sequences, semantic mapping (two engines = two providers) | Direction aligned |
| `09-tech-stack.md` | Each candidate tool in detail: Motion + anime.js split, uPlot, xyflow, CRT layering, WebAudio, View Transitions, HyperFrames (replays), SSE transport design | Recommendations, not decisions |
| `10-issues-reference.md` | #2 / #43 / #46 / #53 / #54 / #49 — states, key content, corrections (#54 is the worktree_start issue, not #46) | Reference |
| `11-open-questions.md` | All unresolved questions + verification debts, numbered for burn-down | Living list |

## The Frame In One Paragraph

The dashboard is a cockpit, not a chart page: a control plane over the Agents
Remember lifecycle. The **lifecycle** is the root entity (01); **events and
spans** reduced by a single projection layer make it observable (02, 03);
**gates and inline actions** make it controllable from the same UX (04, 05);
the **attention queue** is the human's first screen (06); the **podracer
grammar** is the visual identity that makes state honest and the tool
unforgettable (07, 08, 09). Tool/MCP changes are allowed in service of this —
the architecture supports the dashboard, not vice versa, up to and including a
3.0 jump.
