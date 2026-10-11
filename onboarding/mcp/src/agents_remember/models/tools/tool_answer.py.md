# mcp/src/agents_remember/models/tools/tool_answer.py

## Current operative account — MIK-R112

The current source facts below replace the former operative inventory. The separately labelled superseded claims describe only the pre-repair card. Original paragraphs, dated closures, evidence and citation identities remain intact in the explicitly historical section; they grant no current call, restored route or fresh execution acceptance.

- Current L112 final bounds are runtime_install=600 and dispatch_agent=1500.
- interim_leaf_for now returns None without an explicit interim row.

### Superseded inventory

- Pre-repair card claim: Card says L112 rows remain interim until landing. This is superseded archival wording, not a current prescription.

### Source and authority bounds

- Source comparison: `mcp/src/agents_remember/models/tools/tool_answer.py:151-178`.
- Source comparison: `mcp/src/agents_remember/models/tools/tool_answer.py:180-213`.

Source inspection supplies no new test, native-host, whole-build, landing or memory acceptance. Retained internal services and historical fixtures do not re-advertise deleted MCP tools. Numbered references retain historical custody and may include disclosed inherited stale targets; currentness or proof truth is not inferred from them.

## Historical original card — preserved, not the current operative account

<details>
<summary>Retained original source accounts and producer history</summary>

## Governing Overview

[models overview](../overview.md)

## Purpose

The answer-shaping choke for every tool answer (MIK-R108 rules 1, 2, 4, 6): it strips the four envelope fields, caps lists recursively through retained items and builds the measured 400-token short form for over-bound answers. The per-tool contract table that states each answer's fields, uses, cases and bounds is authored in the test module `mcp/tests/test_tool_answer_table.py` (see that module's card); this module owns shaping, bounds and interim leaves.

## Code Commentary

### Logic

- Bounds and table: `TOOL_ANSWER_MAX_TOKENS = 1500`, exceptions to at most 4000, list cap 20, short-form ceiling 400 (250 fixed + location), error cut 600 chars, code max 120 chars. `TOOL_ANSWER_EXCEPTIONS` holds per-tool bounds; interim rows (bound 4000, no fields) name L109–L112 until those leaves land. `bound_for` resolves a tool's own bound; `interim_leaf_for` names the owning leaf.
- `strip_envelope` removes exactly the envelope fields (`tokens`, `tokenizer`, `tokenCountExact`, `operation`) on all paths through the choke.
- `truncate_lists` applies the twenty-entry cap recursively through retained list items as well as mappings, preserving order, count and location.
- `short_form` builds the measured short form in fixed order — fixed part (never reduced), location (only while the form fits 250), error (cut to 600 chars then end-reduced until the whole fits 400, `errorCut`), short scalars while each fits (`droppedFields`) — and measures what it built.
- `is_valid_tool_code` admits ASCII identifiers of at most 120 chars; a malformed code is a producer defect surfaced as `invalid-code`, never passed on.
- The rule-6 contract table is authored in the test module `mcp/tests/test_tool_answer_table.py`: `ToolAnswerRow` holds a row's fields, uses, cases, bound and interim leaf, and `validate_row_case` fails missing rows, extra fields, unused fields, over-bound cases and bounds over twice the largest case (see that module's card).

### Invariants And Boundaries

- The bounds are ceilings, not allowances; a tool that reaches the guard in a table case fails that row.
- `error` is never dropped, only cut; a valid `code` is never dropped or cut.
- The short-form ceiling (400) holds for every tool and row, interim rows included.

## Evidence

- The choke strips the four envelope fields from every answer. [1]
- The twenty-entry cap recurses through retained list items and mappings. [2]
- The measured short form fits 400 with fixed part, location, cut error and short scalars. [3]
- Each tool resolves its own bound from the exception table or the default. [4]

</details>
