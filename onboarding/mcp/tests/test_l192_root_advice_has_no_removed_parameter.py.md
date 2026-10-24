# mcp/tests/test_l192_root_advice_has_no_removed_parameter.py

## Current operative account — MIK-R199

- The docstring states the rule the file enforces and where the admitted set comes from: the shipped tool registration and the internal `ContextPacketRequest` admit `repo_id`, `include_drift`, `include_freshness` and the leaf's `task_context`; `include_providers` is gone and the packet's provider projection is fixed to `include_providers=False`. Advice that still tells a reader to pass the removed flag therefore names an invalid invocation of a shipped tool.
- The removed knob is spelled once, as `REMOVED_PARAMETER`, so every case compares against the same token instead of a repeated literal. `TOOL_NAME` is `context_packet`.
- The carrier inventory is declared as globs, not as a file list: the root `AGENTS.md`, `README.md`, `mcp/README.md`, `agents-md-files/`, `docs/`, `skills/`, `system/`, `dev-skills/`, the packaged runtime copies, plus one expansion per root in `GENERATED_SKILL_COPIES` — the docstring's reason is that a generated copy is added per committed projection root so a new harness cannot ship an unreported call. `REQUIRED_SURFACE_ROOTS` names one shipped surface per entry so a carrier glob that silently stops matching becomes a failure rather than a quiet pass.
- `_advertised_parameters` derives the admitted names from the shipped server: it builds a `FastMCP` instance, runs every registrar in `TOOL_REGISTRARS` against it, lists the tools, requires `context_packet` among them, and returns the property names of that tool's `inputSchema`. The comparison set is therefore the advertised schema, not a hand-kept list in the test.
- Reading a written call is staged, each step tolerant of prose: `CALL_SITE` finds a `context_packet(` occurrence, `_arguments` walks parentheses while tracking quotes and escapes and returns `None` for a call that never closes, and `_parameters` rewrites JSON-ish `true`/`false`/`null` into Python literals before parsing the argument text with `ast.parse` and returning the keyword names — `None` when the text is not a call.
- `carrier_paths` collects matches from every glob into a dict keyed by repository-relative posix path and returns them sorted, so a file matched by several globs is counted once. `carrier_calls` records each unreadable call site by `path:line` and asserts that list empty before returning, on the stated grounds that unparseable prose would otherwise slip past the parameter check. `CarrierCall.location()` renders the same `path:line` form for failure messages.
- The cases split into schema, request, instruction and inventory checks: the schema must not admit the removed name while still admitting `repo_id`, `task_context`, `include_drift` and `include_freshness`; the request's fields must not re-admit it, with `repo_id`, `include_drift` and `include_freshness` required in both the request and the schema and a comment recording that internal knobs like a drift limit or fetch timeout are not advertised arguments, so the request need not be a subset of the schema; no carrier call may name the removed parameter; every carrier call may name only admitted parameters; and the inventory must cover `AGENTS.md`, every required surface root and every generated copy root, with floors asserted on both the generated-copy list and the written-call inventory — the case's own comment is that the canonical skills tree and its copies must resolve to real files rather than a stale glob. The module's stated position is that it fixes nothing — a failing case names the file and line that still prescribes the removed argument.

### Source and authority bounds

- Source inspection: `mcp/tests/test_l192_root_advice_has_no_removed_parameter.py:1-18`.
- Source inspection: `mcp/tests/test_l192_root_advice_has_no_removed_parameter.py:36-64`.
- Source inspection: `mcp/tests/test_l192_root_advice_has_no_removed_parameter.py:66-93`.
- Source inspection: `mcp/tests/test_l192_root_advice_has_no_removed_parameter.py:96-135`.
- Source inspection: `mcp/tests/test_l192_root_advice_has_no_removed_parameter.py:138-179`.
- Source inspection: `mcp/tests/test_l192_root_advice_has_no_removed_parameter.py:182-228`.
- Source inspection: `mcp/tests/test_l192_root_advice_has_no_removed_parameter.py:231-244`.

The carrier files this module scans are outside it; the card states what the scan requires of them, not what any one carrier currently says.

## Evidence

- The admitted parameter set is read from the advertised schema of a server built from `TOOL_REGISTRARS`, not from a literal list. [1]
- The removed knob is spelled once and compared against everywhere. [2]
- The carrier inventory is glob-based, with a required-surface list that fails when a glob stops matching. [3]
- Written calls are parsed with a quote-aware parenthesis scan and an `ast` parse after normalising prose literals; unparseable calls are reported rather than skipped. [4]
- The schema case requires the removed name absent while `repo_id`, `task_context`, `include_drift` and `include_freshness` stay admitted. [5]
- The internal request may not re-admit the removed name and must forward only names the schema advertises. [6]
- Offending carriers are named by `path:line` for both the removed-parameter case and the admitted-parameters-only case. [7]
- Every required surface root and every generated copy root must contribute a carrier, with floors on the generated-copy list and the written-call inventory. [8]
