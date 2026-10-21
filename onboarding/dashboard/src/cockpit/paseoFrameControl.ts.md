# dashboard/src/cockpit/paseoFrameControl.ts

## Governing Overview

[Route overview](../overview.md)

## Purpose

Steer one existing native frame and own its bounded control-channel lifetime and tray-channel attachment.

## Code Commentary

Wanted, pending, settled and URL-loaded identities distinguish the selected agent, its unanswered open, a completed answer and the current loaded route. `receive` accepts only the configured embedded origin and exact iframe window. Native selected rows and source-scoped Parent errors retain their own authority. [1] [5]

A ready selection sends `ar.open` immediately. Each load waits ten seconds for readiness, then sends one ping; ten more seconds without that ping's answer make control unavailable. A pong during readiness wait counts as readiness. Changes during that load wait are held and the latest is messaged when readiness returns. A ready open past its own ten-second deadline remains late while pings are answered, without resending the open; a newer selection still switches by message. [1] [2] [6] [7]

When control is unavailable outside a load-readiness wait, the trailing settle window coalesces selections and loads the latest URL. Explicit Retry and returned-host recovery start the frame again. Only an explicit capability list lacking `open-agent` selects URL-only navigation; an absent list retains message steering. Each load raises generation once. [1] [3] [4]

Ordinary document startup names the wanted target in its URL; opt-in hidden preload starts without an agent. Ready document steering sends exact agent and workspace and announces `ar.page`; the URL retains `arPage=document`.

Trusted `pick`, pick-unavailable, composer and composer-unavailable messages are forwarded to the pane's tray channel. Readiness replaces that pane's tray attachment and re-announces current tray wishes; stop or a plugin without a usable attachment clears it. These messages use the same exact origin/window receiver as navigation. [5]

The controller also publishes the native chat the frame shows, separately from launcher selection. A plugin with `showing` owns that value directly. For a plugin without it, one native selected agent identifies the chat; a plural selection retains the previous known chat only while it remains a member. An empty compact selection is not interpreted as proof that no chat is shown. A fresh load clears the report to unknown.

## Invariants And Boundaries

After initial startup, recovery loads require an unanswered application ping, explicit Retry, returned host or the explicit URL-only plugin exception. Missing readiness alone first asks a ping. Slow host or drawing answers do not themselves authorize a new generation.

`navigated` separates completed host lookup from drawing. `on-chat` permits input on the selected native screen before the conversation is drawn. `shown` and the native `load-failed` pane settle only the pending agent; the latter retains the application's own failure text and Retry. Other or superseded pending identities have no settlement effect. Navigation acknowledgement does not establish native selected rows or task scope. [8]

Tray reporting does not navigate the native frame or change the launcher's selection. Shown-chat identity, pending request identity and plural selected rows remain separate values.


## Evidence

- Ready changes message immediately; readiness-held changes and unavailable trailing settlement differ. [1]
- Ready capability negotiation attaches tray reporting and sends the latest held target. [2]
- URL loading remains bounded by unavailable state and outstanding readiness. [3]
- One load produces one generation and its own readiness wait. [4]
- All accepted control and tray messages require exact frame origin and window. [5]
- Missing readiness probes before unavailable control. [6]
- A late answered request stays pending without resending its open. [7]
- Only the pending agent settles on drawn chat or the native load-failed pane. [8]
- Startup distinguishes ordinary document load from hidden preload. [9]
- Tray attachment is replaced on readiness and cleared on stop. [10]
- Native showing reports and bounded older selection inference publish the frame's chat independently. [11]
