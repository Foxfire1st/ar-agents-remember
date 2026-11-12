# mcp/src/agents_remember/cli/paseo_role_recipients.py

## Governing Overview

[Route overview](../../../overview.md)

## Purpose

Resolves role-message recipients from the current line’s receipts and live agents.

## Code Commentary

### Logic

Addresses name either an exact minted agent UUID or a role with its required canonical task references. Self-addresses refuse. Selection lookup excludes the caller, checks live agents, and refuses ambiguity, including two live agents on one leaf seat. It asks at most 24 candidates; a truncated taskless candidate set is ambiguous. An unfinished start returns a held-message refusal; archived recipients are not revived by sending a message. These functions move intact from paseo_role_tools.

## Repo-Internal References

- The source implements the behavior and boundaries described above. [1]

## Docs References

No domain-documentation source is configured for this repository.

## Cross-Repo References

No external repository is cited by this file card.
