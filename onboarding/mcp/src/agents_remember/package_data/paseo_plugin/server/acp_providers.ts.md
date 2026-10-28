# ACP provider verdict and its written file

## Governing Overview

[Plugin overview](../overview.md)

## Purpose

Decide, once per boot, which of the installed host's providers speaks ACP, keep that verdict where the launch and the turn-end decision can read it, and keep a provider out of ACP once a helper of it has reported back to its seat.

## Contract

The root is the installation the plugin is running from — the segments up to and including the last `@getpaseo` of the entry path — and with no such segment nothing is readable. From it the set reads the server package version, the host's provider registry and manifest, and every provider module the registry imports; a provider's class is followed through the files' own imports until a class is known to be, or known not to be, the ACP client, with a chain bound so a cycle cannot hang the boot.

Resolution follows the host's own order: a built-in id takes its factory class, an id the host configuration names but the registry does not define is not ACP, an `extends: 'acp'` takes the derived or generic ACP class, an id extending a built-in takes that built-in's class, and anything else is left unread rather than assumed. Each verdict carries its class, its boolean and its reason, so a reader can tell "resolved, not ACP" from "unresolved".

A helper that reports a provider — any upsert carrying the helper's own `provider`, before its parent is even read — drops that provider out of ACP for the rest of that process and every later one, because a provider whose helpers report back needs no wait instruction. The written file holds the schema, the host version, the files read, every provider's verdict and the drop-outs, and is written by staging and rename so a reader never sees a partial document; a failed write is logged and swallowed, leaving the in-memory verdict intact. An unreadable installation leaves every provider not ACP and still writes that verdict, and one row per provider per process names an unread verdict without costing the seat its answer.

## Evidence

- The set is the one place the host's classes are read, resolved, dropped out and published, so the verdict is a decision and not a copied list. [1]
- The installation root comes from the entry path alone, and the absence of `@getpaseo` makes nothing readable. [2]
- The resolution order — built-in, configured, extends ACP, extends a built-in, unread — with a reason per verdict. [3]
- A helper's own provider report drops that provider out, and the first report is the one kept. [4]
- The document's body and its staging-then-rename write. [5]
