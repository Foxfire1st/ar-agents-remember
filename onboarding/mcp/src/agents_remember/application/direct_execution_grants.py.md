# mcp/src/agents_remember/application/direct_execution_grants.py

## Governing Overview

[Nearest governing overview](overview.md)

## Purpose

Owns architect grant authority, pre-start mutation, reclamation and the open-direct-sibling guard.

## Contract

direct_execution_grant_tool admits only a launch-bound architect and implements give, revoke and reclaim. Canonical subTask resolution and the ordinary unstarted proof guard mutation; existing give and absent revoke are unchanged outcomes. Exclusive publication chooses one giver, with post-publication start proof removing only the new grant; revoke attempts exclusive recreation of the removed record when a start interleaves. FileExistsError preserves another giver's grant and OSError is suppressed; this does not establish exact-record restoration or serial consistency, so the unchanged INV-X16RQH promise fails on these inherited branches. Reclaim takes only abandoned never-worked leaves with determinably clean checkouts; status masking does not discard seat, report, locator, enclosure, operation or commit evidence, and uncertainty preserves the grant. Occupancy releases an abandoned leaf or landed=True first. A non-Completed sibling occupies when document start markers exist; a Completed sibling occupies only when markers exist and either checkout_dirty=True or landed=False. landed=None (no matching/readable generation) is not False: clean or undeterminable dirt can release that Completed sibling.

## Evidence


- Owns architect grant authority, pre-start mutation, reclamation and the open-direct-sibling guard [1]
