# mcp/tests/test_role_handover_locator.py

## Governing Overview

[Route overview](overview.md)

## Purpose

The request's own directory alias is what makes a hand-over artifact reachable at any report depth: the artifact keeps its canonical place, name and bytes beside the report, and the launch names it through `~/projects/.agents-remember/handover-locators/<request id>/<artifact name>`, whose length does not grow with the folder. These cases hold the alias to its request — reused by a repeat, rebuilt when lost, refused when it would lead elsewhere — and hold its removal to the end of the seat's resumability, never the reports it leads to.

## Code Commentary

`LocatorTestCase` gives each case a home of its own and report folders whose depths differ widely. `LocatorLinkTests` checks that one request keeps one link with a stable inode, that a retarget or a real directory at the locator's name is refused before anything is written, and that a lost link is rebuilt over the same artifact bytes with their inode and modification time intact. `PublishedArtifactTests` publishes at a deep folder and asserts the artifact's `path` sits under the request locator, its `canonicalPath` beside the report, both reach the same bytes, the stored file is read-only, and the artifact line and first message name the locator; another case compares a shallow and a deep publication and finds the locator path exactly as long, and a third plants a link at the artifact's own name inside the report folder and shows the write refuses rather than following it through the locator. `LocatorLifeTests` covers removal: the end of resumability removes the alias and reports `no-locator` on a repeat, a link leading outside the reclaimed folders is left standing, closing an execution removes the launch's locator while its report and hand-over are collected to their durable place, and a group cleanup previews and then removes each launch locator with the collected reports still readable. `LocatorHousekeepingTests` refuses names that cannot be a request id and shows that a failed collection raises before any alias is removed.

## Evidence

- The locator is one link of the report folder, and a repeat of the same request reuses the link it made. [1]
- A locator that would lead to another folder, or a real directory standing at its name, is refused and nothing is changed. [2]
- A lost locator is rebuilt at the same place over the same bytes, leaving the artifact's inode and modification time as they were. [3]
- A deep report folder publishes one bounded locator whose path opens the artifact's own read-only bytes and is named by the artifact line and the first message. [4]
- The locator path is exactly as long at a shallow and a deep folder, and is the product root plus the request id plus the artifact name. [5]
- A link at the artifact's own name is never followed through a locator. [6]
- The end of resumability removes the alias and never the report folder or its report. [7]
- A locator that leads outside the reclaimed folders is left standing and reported. [8]
- Closing an execution removes its locator while its reports and hand-over are collected to their durable place. [9]
- A group cleanup previews and removes its launches' locators while every collected report survives. [10]
- A name that cannot be a request id names no locator. [11]
- A failed collection raises before any alias is removed. [12]
