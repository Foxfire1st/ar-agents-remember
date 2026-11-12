# ACP provider verdict reader

## Governing Overview

[Observer overview](overview.md)

## Purpose

Answer one launch question from the plugin's own written verdict file: is this seat's provider on an ACP connection, and so does its prompt carry the helper-wait instruction. It reads, never asks the host, and never guesses a provider's transport.

## Contract

The document is `acp-providers.json` beside `host-activity.json`, schema `ar-acp-providers/v1`, admitted by strict frozen models that refuse an extra key at the top level or inside an entry. A missing file, an unreadable one, non-JSON bytes, a foreign schema and an unnamed provider are one answer — no instruction — and `read_acp_providers` returns `None` rather than raising, with no logging, no partial parse and no cache.

Only a provider the document carries with `acp` true counts; the verdict is never read from the provider's name, its class string or a reason prefix. A skip names its own reason: an unreadable or absent document, a provider the document does not name, and a provider named as not ACP are three different records a receipt reader can tell apart. The instruction is one fixed paragraph, identical for every role and every helper count: it names the declaration line the plugin scans, asks for a progress report per helper, tells the seat to write progress only in its own chat, and forbids waiting inside a turn or waking itself.

## Evidence

- One frozen schema admits the document; a foreign schema, extra key or unreadable body reads as no answer and never raises. [1]
- Strict frozen models with `extra="forbid"` are what make a foreign document unreadable rather than partly trusted. [2]
- Only an explicit ACP verdict adds the instruction, and each outcome carries its own reason. [3]
- The one instruction sentence the launch appends, with the declaration keyword the plugin scans for. [4]
