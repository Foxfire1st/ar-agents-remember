# mcp/src/agents_remember/serving/review.py

## Governing Overview

[Owning route overview](overview.md)

## Purpose

Register the read-only review, subject-catalogue and source-content HTTP routes over injected application ports, admitting query shapes and mapping their typed results.

## Code Commentary

The three GET routes remain /api/review/intent, /api/review/intent/entries and /api/review/intent/source-content and must register before static mounting. Each missing port returns its own named503 rather than an empty review, catalogue or file. The registrar discards config: resolution stays behind application-ranked ports.

KnowledgeReviewEntriesPort now takes repository/master/leaf plus optional recorded comparison number. The catalogue route forwards that selector; omitted uses the leaf resolution, a supplied unrecorded number earns the owner refusal and a negative value is the route own400 bad-request, with offendingInput, expected and nextAction. Port absence is checked before the negative-number branch.

ReviewQuestionRef bundles selector kind/id, recorded-history spelling and previous-binding digest; ReviewSelectorRef remains the same-class alias, not a duplicate admission. Neither selector parameter means task context; a half pair or a kind outside invariant/family is refused. paged_review_request admits paging and question once, then builds the typed task/subject request. The simpler review_request_from_query preserves its selector-only None-on-failure contract.

Empty history/digest/pageOf/continuation spellings mean absent. Only recorded history is admitted, and the previous digest is checked against the model-owned shape without selecting/resolving a comparison. A continuation must name its collection; pageOf uses REVIEW_PAGED_COLLECTIONS and page size0..MAXIMUM_REVIEW_PAGE_SIZE is admitted without narrowing. UnadmittedReviewQuery names the actual failed input, expected shape and detail; the route returns actionable400.

SourceContentRef holds task context, a repository-relative entry path and both explicit tree ids. A blank component gives incomplete-generation400, never a server-chosen tree. This transport checks completeness only; the application owner admits the measured entry/generation. No route accepts a filesystem root or chooses a dataset.

_port_outcome is shared by review and source-content only: AuthorityError maps to actionable bad-path400, FileNotFoundError to not-found404 with path/offendingInput. Other exceptions propagate. The catalogue calls its port directly and adds no such catch. _status_for maps review_adapter_unavailable503, four candidate/subject absence codes404 and other typed refusals400; no refusal is200.

_json serializes typed results once with model_dump(mode=json, exclude_none=True). None fields are omitted; empty tuples are not omitted by that setting. The transport computes no scope, ordering, measurement, semantic verdict or publication action. Current declarations rather than historical public-name counts own exports.

## Invariants And Boundaries

Caller task identities, relative source addresses and retained comparison numbers are inputs to their application owners, not path authority. The page/digest transport admits shapes and never compares or repairs their meaning. Same admitted owner composition does not prove two temporally separate reads cannot drift. There is no assessment-publication route here and no fallback dataset selection.

## Evidence

- Route vocabulary and numbered catalogue port remain application-injected values. [25]
- The shared exception mapping is actionable and catches exactly the two named exceptions. [26]
- Whole query admission distinguishes task context and subject without guessing selectors. [27]
- History/digest/paging admission names the input that failed. [28]
- The catalogue forwards its optional number and refuses negatives after missing-port handling. [29]
- The negative-number body and one model serializer keep explicit expected/action fields and omit only None. [30]
- Source-content completeness and transport retain their own refusal rather than substituting a generation. [31]
