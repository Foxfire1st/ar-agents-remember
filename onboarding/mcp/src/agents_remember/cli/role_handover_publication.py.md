# mcp/src/agents_remember/cli/role_handover_publication.py

## Governing Overview

[Route overview](../../../overview.md)

## Purpose

Publishes a launch's two hand-over files as one act: the compiled message and the complete object beside it. A launch that cannot publish both sends nothing.

## Code Commentary

publish_handover_files preflights every target the launch would touch before the first of them is written, so a request that already holds other bytes is refused with both files as they were rather than with one created beside a refusal. It also settles the request's locator before the first file is created: a repeat of the same request reuses the alias, and a name that would lead to another folder refuses the launch before either hand-over file exists. The artifact is then written at its canonical place and named through that locator, while the complete hand-over keeps its sibling path. It is the only place that must see the whole set of targets, which is why the pair is coordinated here and the writing stays in the single-file modules.

## Evidence

- Both files are published as one act, and every target is preflighted before the first write. [1]
