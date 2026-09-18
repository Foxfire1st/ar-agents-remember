# mcp/src/agents_remember/models/knowledge/classification.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/knowledge/classification.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-18T15:30+02:00 |
| lastVerifiedCommitHash | `a7076008db4772554123794392f84b51143004ec` |
| lastVerifiedCommitDate | 2026-09-18T16:14:01+02:00 |
| reviewedWorkingCandidate | `ar/260915-ks-l20` uncommitted staged source; base `9f88a6de572dc15bbed1802cf08b77c1193fb24c` |
| governingOverview | `mcp/src/agents_remember/models/overview.md` |

## Governing Overview

[models route overview](../overview.md)

## Purpose

The closed provenance vocabulary of `KS-R20@v1` §2: the module whose docstring names it "``authored`` or
``mechanical``: the closed provenance class, and the closed registry of rules", and which says the
prohibition of `Doc13:243` acquires here "an owning surface" with its answer being "**data**, not
vigilance". It declares the two-member class set, the closed four-member ordering-input vocabulary quoted
from that prohibition, the closed registry of mechanical rules with the identity and version each one
travels under, the record shape that keeps an authored determination and a mechanical one from merging,
and the three functions that are the only way to obtain a rule. **What it deliberately does not have** is
stated by the docstring in its own words: "No ordering comparator, no sort key, no score, no rank, no
weight, no severity, no percentage, and no field a caller could read as an assessment", nothing that
"derives an ordering key from a symbol name's spelling, a path prefix, a directory depth, a file extension
or a repository location", nothing that "reads another view's result", and — because it is "Derived, never
canonical" — "no store, no cache and no persistence in this module", so recomputing a classification
writes nothing and a rule's version change cannot alter a stored record, a dataset digest or an authored
value.

## Code Commentary

### Logic

**The class set is closed at two members, and the runtime tuple is derived from the literal.** `ProvenanceClass`
is `Literal["authored", "mechanical"]`; `AUTHORED_CLASS` and `MECHANICAL_CLASS` are its two members as typed
values, and `CLASSIFICATION_CLASSES` is `get_args(ProvenanceClass)` rather than a hand-written copy, so the
runtime tuple and the type cannot disagree. The module's own comment records the closure — "a third member
cannot be added to one and forgotten in the other" — and the docstring records what happens to a value that
cannot be classified: "There is no ``unknown``, no ``null``, no ``mixed`` and no default", and such a value
"is not emitted with an empty class: the view reports it as an unresolved limitation".

**The admitted ordering inputs are a closed four-member vocabulary, and what a rule may determine is closed
at two.** `OrderingInput` declares `declared_priority`, `registered_role`, `stable_ordering` and
`explicit_trigger_rule` — the four inputs `Doc13:243` names — with `ORDERING_INPUTS = get_args(OrderingInput)`
as the runtime sequence; the comment beside it states that "An ordering that cannot name which of these four
produced it is not admitted at all -- there is no fifth value and no 'other'". `DeterminationKind =
Literal["ordering", "no_consequence"]` closes what a rule is allowed to determine, so a rule "cannot determine
an effect label, an assessment or a severity". `MECHANICAL_RULE_REGISTRY_VERSION` is the integer `1`, recorded
beside every mechanical classification so a reader can tell which registry produced it, and
`REGISTERED_ROLE_ORDER` is `get_args(RealizationRole)`, read from the realization-role vocabulary's own
declaration in `models/knowledge/graph.py` rather than hand-copied, so "a role added to the vocabulary cannot
silently acquire a position here".

**One registered rule carries its identity, its version, its determination and the recorded values it reads.**
`MechanicalRule` declares `rule_id` bounded by `LABEL_MAX_LENGTH`, `rule_version` with `ge=1`, `determination`,
an optional `ordering_input`, `reads: tuple[str, ...]` and a `summary` bounded by `PROSE_MAX_LENGTH`. Its
`_require_an_admitted_ordering_input` validator enforces the closure at the registry's own boundary rather than
at a call site: an `ordering` rule that names no input is refused, a `no_consequence` rule that names one is
refused, and an empty `reads` is refused because "a rule that reads nothing is a constant, and a constant is
not a determination". The class docstring gives the reason both halves of the identity travel together: a
classification that "named only one of the two could not be reproduced after the rule changed".

**The registry is one tuple of eight rules — four per determination — and the lookup map is derived from it.**
`MECHANICAL_RULES` is a `tuple[MechanicalRule, ...]` declared in source order, "so its order is a property of
this declaration and not of a mapping's iteration". Exactly one ordering rule exists per admitted input:
`ordering.declared-priority` (reads `authored_priority.position`, `authored_priority.author`,
`authored_priority.rationale`), `ordering.registered-role` (reads `realization_claim.role` and
`REGISTERED_ROLE_ORDER`), `ordering.declared-tiebreak` (reads `row.subject_record_id`) and
`ordering.trigger-rule` (reads `detection_condition.condition_code` and `detection_condition.matched_facts`).
The four `no_consequence` rules are `consequence.anchor-byte-equal`, `consequence.anchor-text-whitespace-only`,
`consequence.record-payload-byte-equal` and `consequence.path-absent-in-both-states`, each reading recorded
object identities, recorded text or a recorded resolution state. Every rule is version `1`, and
`_MECHANICAL_RULES_BY_IDENTITY` is the `(rule_id, rule_version)`-keyed dictionary built from that same tuple.

**Three module functions are the only route into the registry, and a miss raises rather than degrading.**
`mechanical_rule(rule_id, rule_version)` looks the pair up in the derived map and raises
`MechanicalRuleNotRegistered` when it is absent, naming the sorted registry in its message; the exception's
own docstring states it is "deliberately an exception and not a refusal value", because a caller that names an
unregistered rule "has a programming defect, and returning an empty or default classification would be exactly
the 'emit the row as if it were classified' failure requirement 2.1 forbids". `mechanical_rules_for(determination)`
filters the tuple and returns the matching rules in registry order. `ordered_input_of(rule_id, rule_version)`
resolves the rule through `mechanical_rule` first and raises the same exception when the rule determines a
consequence and therefore names no ordering input.

**The two determinations are separated by a validator, not by convention.** `AuthoredDetermination` carries an
`author_ref` bounded by `REFERENCE_MAX_LENGTH` — "an authored determination is attributable or it is not
authored" — and the author's own `rationale`, bounded by `PROSE_MAX_LENGTH` and "copied and never composed by a
renderer". `Provenance` carries `provenance_class` beside an optional `authored`, `rule_id` and `rule_version`,
and `_require_exactly_one_branch` refuses, in the authored branch, a missing `AuthoredDetermination` ("a class
without them is an unclassified value wearing a class") and any named rule ("an authored determination never
cites a mechanical rule as its reason"); in the mechanical branch it refuses a present `authored`, requires both
`rule_id` and `rule_version`, and calls `mechanical_rule(self.rule_id, self.rule_version)`, so a rule outside
the registry cannot produce a `Provenance` at all. `authored_provenance` and `mechanical_provenance` are the two
module-level builders, one per branch, so the docstring's "the mechanical determination never writes an authored
record, and an authored determination never cites a mechanical rule as its reason" is enforced by the only
constructors that exist.

**The deliberate absences are properties of the field sets this module declares.** Read together, the file
declares three models: `MechanicalRule` (identity, version, determination, one optional admitted input, the
recorded values read, a summary), `AuthoredDetermination` (an author reference and a rationale) and `Provenance`
(a class, the authored branch and the mechanical rule pair). No name among those declared fields is a score, a
rank, a weight, a severity, a percentage, a comparator or a conclusion, and no function signature in the file
takes a path, a symbol spelling, a depth, an extension or another view's output — which is how the docstring's
claim about what "nothing here" does is checkable. The file's only non-stdlib imports are `pydantic` and two
sibling model modules, and there is no file, connection, store or cache anywhere in it.

### Conventions

Every shape is a `KnowledgeModel` subclass, so `extra="forbid"` and `frozen=True` inherited from
`models/knowledge/base.py` are what refuse a payload arriving with an undeclared field — a fourth determination
kind, a fifth ordering input, an assessment attached to a rule — and what make a constructed classification
immutable once built. Bounded text reuses the base constants rather than literals: `LABEL_MAX_LENGTH` for
`MechanicalRule.rule_id` and `Provenance.rule_id`, `PROSE_MAX_LENGTH` for `MechanicalRule.summary` and
`AuthoredDetermination.rationale`, `REFERENCE_MAX_LENGTH` for `AuthoredDetermination.author_ref`.
`PATH_MAX_LENGTH` is not imported, because nothing here holds a filesystem location.

Declarations that must agree are one declaration. `CLASSIFICATION_CLASSES` is `get_args(ProvenanceClass)`,
`ORDERING_INPUTS` is `get_args(OrderingInput)` and `REGISTERED_ROLE_ORDER` is `get_args(RealizationRole)` — all
three derived at import time — while `_MECHANICAL_RULES_BY_IDENTITY` is built from `MECHANICAL_RULES` and the
registry stays a tuple because its order is meaningful. The vocabularies belonging to other modules are imported
and reused rather than re-declared: `RealizationRole` from `models/knowledge/graph.py` supplies the registered
role vocabulary whose declared order `REGISTERED_ROLE_ORDER` reproduces, and the docstring names
`models/knowledge/view.py`'s `UnresolvedLimitation` as the record where a value that cannot be classified is
reported instead of being given an empty class. `__all__` names the sixteen public names this module adds — seven
constants (`AUTHORED_CLASS`, `CLASSIFICATION_CLASSES`, `MECHANICAL_CLASS`, `MECHANICAL_RULES`,
`MECHANICAL_RULE_REGISTRY_VERSION`, `ORDERING_INPUTS`, `REGISTERED_ROLE_ORDER`), the two literal aliases
(`OrderingInput`, `ProvenanceClass`), four classes (`AuthoredDetermination`, `MechanicalRule`,
`MechanicalRuleNotRegistered`, `Provenance`) and three functions (`mechanical_rule`, `mechanical_rules_for`,
`ordered_input_of`). The two builders `authored_provenance` and `mechanical_provenance` are defined at module
level and imported by name elsewhere in the repository, but `__all__` does not name them.

### Invariants And Boundaries

- **Two classes and no third.** `ProvenanceClass` is a two-member `Literal` and `CLASSIFICATION_CLASSES` is
  `get_args` of it, so a value carrying anything else cannot be constructed; a value that cannot be classified is
  not given an empty class and instead reaches `models/knowledge/view.py`'s `UnresolvedLimitation`.
- **No classification can come from an unregistered rule.** `mechanical_rule` raises `MechanicalRuleNotRegistered`
  for a pair the registry does not carry, `ordered_input_of` raises through it, and `Provenance`'s validator calls
  it, so the registry is the only source of a mechanical class.
- **The two determinations never merge.** An authored `Provenance` with no `AuthoredDetermination` is refused, an
  authored one naming a rule is refused, a mechanical one carrying an author is refused, and a mechanical one
  missing either half of the rule pair is refused.
- **An ordering rule must name one of the four admitted inputs and a consequence rule must name none.** This is
  enforced inside `MechanicalRule`, so an unadmitted ordering input cannot be registered at all.
- **A rule may not be a constant.** `MechanicalRule.reads` must be non-empty; the validator's stated reason is
  that a rule reading nothing is a constant and a constant is not a determination.
- **The registry is closed and its order is declaration order.** `MECHANICAL_RULES` is a tuple of eight rules,
  four ordering and four `no_consequence`, with exactly one ordering rule per admitted input, and
  `mechanical_rules_for` preserves that order rather than sorting.
- **No declared field can hold an assessment.** The only field names the file declares are rule identity,
  versions, determination, ordering input, read values, summaries, an author reference, a rationale and a class;
  there is no comparator, sort key, score, rank, weight, severity or percentage anywhere in them.
- **The module performs no I/O and persists nothing.** Its only non-stdlib imports are `pydantic` and the two
  sibling model modules `base.py` and `graph.py`, so recomputing a classification writes nothing and a rule
  version change cannot alter a stored record or an authored value.
- **One exported function has no caller at all.** `ordered_input_of` is declared and named in `__all__` and no
  module or test in the shipped candidate calls it; `mechanical_rules_for` is called only by
  `mcp/tests/test_knowledge_views_and_projection.py`, and the two builders are called from
  `mcp/src/agents_remember/application/knowledge_view_render.py` and by the tests.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no `Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

The rows below ground the card's claims in the declarations themselves: the closed vocabularies and how each is
derived, the rule record and the validator that closes its inputs, the registry and the lookup built from it, the
three accessors, the two-branch provenance record and its builders, the base constants reused for bounded text,
and the imported vocabularies this module reuses instead of re-declaring.

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's own statement of its subject and of what it deliberately does not have, including the two-member closure, the unclassifiable value routed to an unresolved limitation, and the "no store, no cache and no persistence" claim. | `UnresolvedLimitation` | mcp/src/agents_remember/models/knowledge/classification.py:1-36; mcp/src/agents_remember/models/knowledge/view.py:417-429 |
| The closed two-member class set, its two members as typed values, and the runtime tuple derived from the literal rather than restated. | `CLASSIFICATION_CLASSES` | mcp/src/agents_remember/models/knowledge/classification.py:71-76 |
| The four admitted ordering inputs quoted from the declared prohibition, with the runtime sequence derived from the literal. | `OrderingInput` | mcp/src/agents_remember/models/knowledge/classification.py:78-86 |
| The closed determination kinds and the registry version recorded beside every mechanical classification. | `DeterminationKind`; `MECHANICAL_RULE_REGISTRY_VERSION` | mcp/src/agents_remember/models/knowledge/classification.py:88-95 |
| The registered-role grouping order read from the realization-role vocabulary's own declaration instead of being hand-copied. | `REGISTERED_ROLE_ORDER`; `RealizationRole` | mcp/src/agents_remember/models/knowledge/classification.py:97-102; mcp/src/agents_remember/models/knowledge/graph.py:36-44 |
| The failure that is an exception rather than a refusal value, so an unregistered rule cannot yield a default classification. | `MechanicalRuleNotRegistered` | mcp/src/agents_remember/models/knowledge/classification.py:105-111 |
| One registered rule's declared fields, and the validator that refuses an ordering rule with no admitted input, a consequence rule that names one, and a rule that reads nothing. | `_require_an_admitted_ordering_input` | mcp/src/agents_remember/models/knowledge/classification.py:114-156 |
| The registry itself: eight rules declared as a tuple, four ordering rules with exactly one per admitted input and four no-consequence rules, each reading named recorded values. | `MECHANICAL_RULES` | mcp/src/agents_remember/models/knowledge/classification.py:159-265 |
| The registry's lookup, keyed by rule identity together with rule version so both halves of the identity are required. | `_MECHANICAL_RULES_BY_IDENTITY` | mcp/src/agents_remember/models/knowledge/classification.py:267-269 |
| The one accessor that raises for a pair the registry does not carry, naming the sorted registry in its message. | `mechanical_rule` | mcp/src/agents_remember/models/knowledge/classification.py:272-286 |
| The determination filter that returns the registered rules in registry order. | `mechanical_rules_for` | mcp/src/agents_remember/models/knowledge/classification.py:289-292 |
| The accessor that raises when the named rule determines a consequence and therefore names no ordering input. | `ordered_input_of` | mcp/src/agents_remember/models/knowledge/classification.py:295-304 |
| The authored reason as the author wrote it: an actor reference rather than free text, and a rationale bounded as prose. | `AuthoredDetermination` | mcp/src/agents_remember/models/knowledge/classification.py:307-316 |
| The provenance record that refuses both mixtures of the two determinations, requires both halves of the rule identity in the mechanical branch, and checks the registry on the way. | `_require_exactly_one_branch` | mcp/src/agents_remember/models/knowledge/classification.py:319-370 |
| The two builders, one per branch, so a caller cannot half-fill a provenance record. | `authored_provenance`; `mechanical_provenance` | mcp/src/agents_remember/models/knowledge/classification.py:373-379; mcp/src/agents_remember/models/knowledge/classification.py:382-386 |
| The frozen, `extra="forbid"` base every shape derives from, with the three bounded-length constants this module's fields reuse. | `KnowledgeModel`; `PROSE_MAX_LENGTH`; `LABEL_MAX_LENGTH`; `REFERENCE_MAX_LENGTH` | mcp/src/agents_remember/models/knowledge/base.py:24-37 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. A provenance class is a property of one namespace's
own stored knowledge, the rules it registers are identified and versioned inside this package, and every value a
rule names as read is a recorded value of the same store.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-18T15:30+02:00 — 260915-KS-L20 curator (uncommitted change set on `ar/260915-ks-l20`, base `9f88a6de`): created this one-to-one card for the closed provenance vocabulary — the two-member `authored`/`mechanical` class set, the four admitted ordering inputs, the registered mechanical-rule registry with its identity-and-version lookup, and the validator that keeps the two determinations from merging. It records that the class set is closed at two members with `CLASSIFICATION_CLASSES` derived from the literal, that `MECHANICAL_RULES` is a tuple of eight versioned rules with exactly one ordering rule per admitted input and that `MechanicalRule.reads` may not be empty, that `mechanical_rule` raises `MechanicalRuleNotRegistered` instead of degrading to a default, and that no declared field can hold a comparator, score, rank, weight, severity or percentage. The card also states the deliberate absences the module docstring names — no ordering comparator, no sort key, no store, cache or persistence, and nothing that derives an ordering key from a name, path, depth, extension or another view's result — together with the fact that `ordered_input_of` is exported and has no caller in the shipped candidate. This card carries **no `lastVerifiedCommitHash`**: every construct it cites exists only in this leaf's uncommitted candidate, so no real commit contains the content a stamp would claim to have verified. The `reviewedWorkingCandidate` row states what was actually read, and closeout owns the stamp once the code commit exists.
