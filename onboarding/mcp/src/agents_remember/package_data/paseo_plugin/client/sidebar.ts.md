# mcp/src/agents_remember/package_data/paseo_plugin/client/sidebar.ts

## Governing Overview

[Route overview](../../../../../overview.md)

## Purpose

The plugin's document-page sidebar policy: on a document page it collapses the host's list, hides its toggle and keeps the page's mode, without ever writing the rail's in-memory choice into the host's shared stored state.

## Code Commentary

`documentSidebar` installs one document-local style that hides `[data-testid="menu-button"]`, collapses the host's own toggle when it is open, and re-collapses after every native DOM/`aria-expanded` change; its cleanup removes the observer, style and the active-sidebar marker (`__arDocumentSidebar`), while the persistent page mode (`__arEmbedPageMode`) is retained for plugin reevaluation. `preserveSidebarChoice` intercepts native panel-state writes only while the page mode is `document` and restores the stored `desktop.agentListOpen` choice, so the rail's collapsed view never becomes another frame's or a standalone tab's remembered choice. The mode is set only after the parent is verified (the bridge accepts `ar.page` from the listed origin); a trusted Chats transition changes the mode and runs the cleanup, and the standalone look path clears the mode without touching the isolation. A standalone tab keeps the user's own sidebar and toggle.

## Evidence

- A document-mode write keeps the actual shared stored sidebar choice instead of the rail's local closure. [1]
- The document page hides the toggle, re-collapses on native changes, and cleans all effects on teardown. [2]
- Page mode is explicit, clearable and survives a plugin reevaluation through the page's own state. [3]
- The trusted Chats transition changes the persistent mode and runs `documentSidebar`'s cleanup, which removes the observer, style and active marker. [4]

- The standalone look path clears the persistent mode flag without touching the isolation. [6]
- The mode is also recoverable from the frame address for the plugin's own reload path. [5]
