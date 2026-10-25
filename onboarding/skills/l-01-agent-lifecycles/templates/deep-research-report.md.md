# skills/l-01-agent-lifecycles/templates/deep-research-report.md

## Governing Overview

[skills/l-01-agent-lifecycles overview](../overview.md)

## Purpose

The reusable deep-research report shape keeps findings, evidence, proof inventory, remaining truth gaps and the final research recommendation together without moving lifecycle authority into a formatting template. It supplies full and compact forms, an evidence-ledger format, evidence kinds and explicit limits on each claim.

## Code Commentary

### Logic

The template places the report after the developer-agreed reframe and before the lifecycle's `decide` step; those are the template's stated usage context, not evidence of a particular task's progress. Small research-only answers use the compact shape; ambiguous, architectural, taxonomy-heavy, bug-root-cause, triage-routing and build-spawning work use the full shape. The full form captures frame, short answer, findings, evidence ledger, proof inventory, remaining truth gaps and decision. The compact form retains answer, evidence, proof inventory, gaps and decision.

Evidence rows are proof records rather than activity logs. Each finding cites evidence IDs, each evidence row identifies its supported claim, inference is distinguished from direct evidence, and limits state what the evidence does not prove. Concrete paths, queries, anchors and command names make the account inspectable without repeating the whole investigation.

### Conventions

The supplied examples use `F-01`/`F-02` finding labels and `E-01`/`E-02`/`E-03` evidence labels. The ledger columns are ID, Kind, Source / Query, Claim Proven and Limits. Full-shape proof inventory includes onboarding reads, route-index and onboarding searches, native code searches for callers/callees/dependencies, inspected source, external references and executable validations; compact inventory retains the first four categories.

Evidence kinds are Semantics, Relationship, Intent, External, Executable, Developer and Inference. Semantics uses the route index plus a capped native search over onboarding text; Relationship uses native search for callers, callees, dependencies, impact or neighboring structure. Intent pairs onboarding with bounded source confirmation. Developer clarification is checked against source before it becomes durable current-state knowledge; inference cites its input evidence and remaining uncertainty. The ledger examples use route-index/onboarding searches and native callers/dependency searches.

The full decision block asks for a research-only exit, whether to spawn a build, the suggested artifact shape (minimal `w-02` task versus master plus series) and plan-gate status. Preserve that artifact-shape distinction rather than reintroducing the older build-mode axis.

### Invariants And Boundaries

The lifecycle owns when deeper research happens and the required proof categories; this file owns report shape, evidence labels and optional sections. Decision fields record a recommendation or status, not launch authority, approval or executable validation. Report completion, independent review, curation, semantic acceptance and paired Git publication remain separate facts under the current router.

Earlier companion-list and router-rebasing notes associated this report with the lifecycle entry contract and detailed spine. Their continuing useful meaning is the separation of report formatting from lifecycle authority. The current entry source is a thin role-capsule router: selected role plus one applicable operation, with canonical task facts and workspace bindings arriving separately. An old companion-list citation must not be read as proof that this template is injected into every role capsule.

### Documentation Scope

This is a repository-local Markdown report contract. The inherited card required no external domain standard or sibling-repository evidence to explain its shape; that bounded account is not a fresh survey of external documentation. Its empty TODO declaration recorded no template-specific maintenance obligation.

## Evidence

- Usage context, shape selection and formatting/lifecycle split are explicit template declarations. [1]
- Claims cite evidence, inference is distinguished and limits remain visible. [2]
> Retained earlier citation wording: - The full report supplies frame, findings, ledger, proof inventory, gaps and artifact-shape decision fields. [3]
> Retained earlier citation wording: - Compact research retains answer, evidence, proof inventory, gaps and decision. [4]

- The evidence taxonomy defines Semantics as route-index plus capped onboarding-text search and Relationship as native structural search, while requiring bounded Intent, source-verified developer clarification and explicit inference uncertainty. [5]

- Ledger guidance asks for inspectable source detail and guards against overclaiming. [6]
- Current capsule composition is role plus operation, not a shared lifecycle or template-injection claim. [7]
- Turn completion, review, curation, semantic acceptance and publication have separate owning evidence. [8]

- The full report supplies frame, findings, ledger, proof inventory, gaps and artifact-shape decision fields.  Anchor: `Suggested artifact shape if spawned` [3]


- Compact research retains answer, evidence, proof inventory, gaps and decision.  Anchor: `## Compact Shape` [4]
