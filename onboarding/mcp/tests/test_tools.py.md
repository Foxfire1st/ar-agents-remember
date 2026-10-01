# test_tools.py

## Governing Overview

[Tests overview](overview.md)

## Purpose

Checks ping and safe server-info payloads, memory-initialization authority repair after config-write failure, and typed CGC/grepAI input refusal before provider execution. Since 260831-LOCR-L29 it also holds the public-surface inventory contract: the live registration order must equal `PUBLIC_TOOLS`, and every advertised name must have a response model that validates; 260831-LOCR-L30 added the per-tool response-model case for the checkpoint landing tool, 260831-LOCR-L36 added the case that pins that tool's **published description** — it must present a partial publication and deny being the pause — and 260831-LOCR-L37 added the matching case for the stop: `worktree_pause`'s description must present a stop that publishes NOTHING and must name `worktree_checkpoint_landing` as the separate, explicitly requested PUBLICATION. 260831-LOCR-L38 extended that stop case so the description must also stay true about a master holding no selection: the removed `atomic-series-activation-selection-missing` refusal is pinned **out** of the registered text and the release the description still advertises is pinned **in**, so the absence cannot be satisfied by emptying the text. These cases establish payload behavior with controlled configuration; the registration probe builds no runtime and no live provider is exercised. Since `260918-TSIP-L3` it also holds the **curator-coherence publish contract** (`T50`): one case compares the registered `curator_coherence` description against the nine fields the validator actually requires and pins that the JSON schema cannot carry the requirement, and its pair drives a real `publish` request once per omitted field — with the complete shape accepted first as the positive control — asserting the refusal names exactly the field it dropped.

## Code Commentary

### Logic

The current evidence boundary is the source-listed behavior below. Earlier coverage claims in
history describe prior populations and must not be used to recreate removed tests or claim they
still run. The retained behavior and its fixture limits, described above, govern this card.

### Conventions

The table lists retained test definitions, not collected parametrized or subtest counts.
Inspect the cited setup and collaborators before treating a focused result as end-to-end evidence.

### Invariants And Boundaries

Preserve exact refusal, identity, and cleanup assertions rather than adding overlapping helper
cases. Coverage percentages are diagnostic and production CRAP 20 prompts review; neither implies
an obligation to restore removed cases. Full suites and whole-candidate review remain master-end
work. This source inspection does not claim a newly executed test or acceptance result.

### Todos

No additional implementation scope is opened by this memory reconciliation.

## Evidence

### Docs References

The repository has no configured Domain Documentation source. These claims concern its own test
fixtures and assertions, so the exact retained source is the direct evidence.

No external domain claim is required.

### Repo-Internal References

Each current definition below can be inspected in the exact source file. Historical references
to removed methods are superseded by this current inventory.

- Ping payload [1]
- Server info payload reports safe config summary [2]
- Memory init repairs authority after config write failure [3]
- Typed cgc payloads reject invalid inputs before provider execution [4]
- Grepai payloads reject invalid scope and trace inputs [5]
- Live FastMCP registration order equals the advertised public tuple [6]
- The record-landing tool has a registered response model that validates [7]
- The checkpoint-landing tool has a registered response model that validates, which the set comparison alone cannot establish [8]
- The checkpoint description presents a partial publication and denies being the pause: it says `PUBLISH`, says "not a pause", says pausing is a "separate matter and is NOT this call", and no longer opens with "Use this to pause". [9]
- The pause description presents a stop that publishes NOTHING, names the checkpoint landing as the separate publication, and — since the already-vacant stop — advertises no refusal the verb no longer performs while still naming the release it does perform. [10]
- The description names every field `curator_coherence`'s `publish` requires, and pins that the JSON schema cannot carry the requirement. [11]
- `publish` refuses by naming **every** missing field, one omission per field with the complete-shape acceptance as the positive control. [12]
- The one list both pins compare — the nine publish-required fields, spelled once. [13]
- The permissive registration-time config stub the registration cases build against [14]

### Cross-Repo References

This card establishes test behavior, not a separate cross-repository protocol or live installation.

No external evidence is needed for these assertions.

## Public-Surface Inventory Coverage (260831-LOCR-L29)

`PublicSurfaceInventoryTests` exists because the advertised surface's own agreement was unenforced.
`server_info` reports `mcp.tools.PUBLIC_TOOLS` itself, so a case that reads that payload and compares
it to the tuple is self-referential. `worktree_record_landing` shipped registered by
`mcp/registration/closeout.py`, advertised by FastMCP, and absent from both `PUBLIC_TOOLS` and
`TOOL_RESPONSE_MODELS`, and the suite stayed green while `finalize_tool_response`'s by-name registry
lookup made the tool unable to return a payload at all.

`test_live_registration_matches_the_public_inventory_in_order` registers every entry in
`TOOL_REGISTRARS` against a probe `FastMCP("inventory-probe")` and compares the
`asyncio.run(server.list_tools())` names to `PUBLIC_TOOLS`. The comparison is ordered because
FastMCP publishes in registration order, so a misplaced row is a reordering bug rather than a
missing one. `test_worktree_record_landing_has_a_response_model_that_validates` asserts
`set(PUBLIC_TOOL_RESPONSE_MODELS) == set(PUBLIC_TOOLS)` and then drives one
`finalize_tool_response("worktree_record_landing", ...)` call — the call a missing registry row
raises on, which the surface comparison alone cannot see.

`_permissive_registration_config()` is the stub both cases need. Every registrar only closes over
the config and none validates it while registering, so a permissive chain keeps these cases about
the inventory rather than about building a runtime. The probe starts no server process, reads no
provider state, and reaches no network.

### Why There Is A Case Per Landing Tool (260831-LOCR-L30)

`test_worktree_checkpoint_landing_has_a_response_model_that_validates` exists because the L29 case's
set comparison cannot distinguish the two landing envelopes: `worktree_checkpoint_landing` and
`worktree_record_landing` sit adjacent in `TOOL_RESPONSE_MODELS` and declare the same field names
apart from the operation literal, so a registry swap between them still validates as a set. The L30
case drives `finalize_tool_response("worktree_checkpoint_landing", …)` with the checkpoint payload
(`state: "checkpointed"`, `integratedCodeCommit`, empty memory and ledger commits) and asserts the
returned operation, which is what pins the name to the model that declares its literal.

The general rule the two cases establish: one validating call per public tool name, not one for the
whole registry.

### The Stop's Half Of The Split (260831-LOCR-L37)

`test_the_pause_advertises_a_stop_that_publishes_nothing` is the L36 case's counterpart, and the two
are deliberately a pair. The checkpoint case pins the publication's side of the split; this one pins
the stop's. It registers every registrar against a probe `FastMCP("pause-surface-probe")`, reads the
advertised descriptions, and asserts that `worktree_pause` is a `PUBLIC_TOOLS` member, that
`worktree_checkpoint_landing` is too, and that the stop's text says all three things an agent needs:
that it is a pause of an atomic master, that it **publishes NOTHING**, and that the publication it
must not reach for is named and separate.

Neither case would catch the other's regression. The L36 case cannot see the stop's wording because
it reads only the checkpoint's text, and a description-only edit is invisible to the set comparison
and to the per-name response-model cases. Together they are what makes "two registered tools, not one
verb with two names" an enforced claim rather than a comment.

**The stop case also pins what the description must not say (260831-LOCR-L38).** The pause used to
refuse a master holding no selection with `atomic-series-activation-selection-missing`; it now reports
that master as already stopped, so a registered description still advertising the removed refusal
would describe a tool the caller does not have. The case asserts the identifier is absent — both the
full status and the `selection-missing` fragment — and, in the same case, that
`releases the master's atomic-series activation selection` is still present. The positive half is the
load-bearing one for this check: without it, deleting the description would satisfy the absence. This
is an advertisement pin, not a behavioural one — the behaviour is proved in
`test_pause_stop_only_end_to_end.py` — and it pins the absence, so it constrains no production edit
other than re-advertising a status the verb no longer returns.

## The Curator-Coherence Publish Contract (260918-TSIP-L3)

`CuratorCoherencePublishContractTests` exists because **the published contract and the enforced
contract disagreed, and neither surface could show it** (`T50`). `curator_coherence`'s `publish` was
refused twice on a real curator with *"publish requires every identity, predecessor, and caller
field"* although every field the registered description named had been supplied. The validator
(`models/lifecycles/curator_coherence.py:294-328` `_action_has_one_input_shape`) requires **nine**
non-null fields, and the description named neither `semantic_requirement_revision` nor
`delivery_attempt` nor `caller` as required; the refusal named a class of fields and none of them,
and a model-level validator reports `loc: ()`, so the message was the caller's only route to the
missing field. Two disagreements, pinned separately because either can regress alone:

- `test_the_description_names_every_field_publish_requires` registers every `TOOL_REGISTRARS` entry
  against a probe `FastMCP("curator-coherence-description-probe")`, reads the advertised
  `curator_coherence` text, and asserts each of the nine names appears in it. In the same case
  `CuratorCoherenceRequest.model_json_schema()["required"]` must stay
  `["action", "contract_path"]` — **the schema cannot carry the requirement**, because it is
  conditional on `action == "publish"`, and the pin stops someone "moving the repair into the
  schema" on the assumption that it could.
- `test_publish_refuses_by_naming_every_missing_field` builds the complete nine-field request and
  asserts it is accepted **first**, as the positive control: without that arm a mistyped field name
  would make every later assertion pass for a reason unrelated to the repair. Then, one omission per
  field, it asserts `missing: <field>` is in `errors()[0]["msg"]` — never `str(error)`, because the
  rendered error echoes `input_value` and a substring check against the echo reports "named" for a
  message that names nothing, which is the instrument fault this case exists to catch.

`PUBLISH_REQUIRED_FIELDS` spells the nine once so both arms compare against one list. The two cases
belong to the **integration** lane because that is where the two existing published-description pins
live; the module was already registered, so this leaf added no lane row and **no line of
`mcp/tests/test-evidence-lanes.toml` moved**.
