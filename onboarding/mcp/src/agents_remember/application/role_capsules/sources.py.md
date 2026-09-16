# mcp/src/agents_remember/application/role_capsules/sources.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/application/role_capsules/sources.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-09-16T08:56+02:00 |
| lastVerifiedCommitHash | `e9300687218205ec1c4b0b86f96d3ac7c2f344d3` |
| lastVerifiedCommitDate | 2026-09-16T09:41:55+02:00|
| governingOverview      | `../overview.md`                           |

## Governing Overview

[application overview](../overview.md)

## Purpose

Source admission: read an explicit, root-confined source set from a canonical tree. This is the
**one place in the role-capsule path that touches the filesystem**.

## Code Commentary

### Logic

Admission is deliberately explicit rather than eager: cit:([`CapsuleAdmissionRequest`], mcp/src/agents_remember/application/role_capsules/sources.py:38-77) names every path the
caller wants admitted, and cit:([`admit_capsule_sources`], mcp/src/agents_remember/application/role_capsules/sources.py:78-94) resolves each one inside the root,
proves it is a regular file, reads its bytes, and records their digest. It does **not** consult
the manifest to decide what to read — *the compiler needs to be able to discover that a required
block was not admitted, and a loader that only ever fetched what the manifest asked for could not
express that.*

Containment is proven **before any byte is read**, so a traversal attempt fails without the root
ever being probed outside itself. cit:([`_require_confined_relative`], mcp/src/agents_remember/application/role_capsules/sources.py:169-196) rejects an absolute path or any
path containing an empty, `.`, or `..` segment; cit:([`_require_root`], mcp/src/agents_remember/application/role_capsules/sources.py:97-113) proves the root is an existing
directory; cit:([`_read`], mcp/src/agents_remember/application/role_capsules/sources.py:114-149) performs the confined read and the
one-admission duplicate check.

The returned order is fixed — manifest first, then the four composition roots in contract order,
each alphabetically — so the admitted set itself is reproducible and two admissions of one tree
are directly comparable. cit:([`_identity_for`], mcp/src/agents_remember/application/role_capsules/sources.py:150-158) gives the manifest the reserved metadata
identity `meta:composition-manifest` rather than a block identity, because the manifest is
metadata: it is composed into no capsule and must still be read so selections can be validated
against what it declares.

### Conventions

Every requested path is a **root-relative POSIX path**. `CapsuleAdmissionRequest.manifest` is kept
separate from the four instruction-root tuples for exactly that reason.

### Invariants And Boundaries

- **Containment before reading.** No byte is read before the path is proven confined; a traversal
  attempt must not probe outside the root.
- The manifest path is read but is **not** an instruction block; its identity is the reserved
  metadata identity and it is composed into no capsule.
- The admitted order is fixed (manifest, then `core`, `role`, `operation`, `specialization`, each
  alphabetical). Do not derive it from directory listing order.
- A missing file, an unreadable root, and a path requested twice in one admission are typed
  refusals — never a skip, and never a silent dedupe.
- This module reads bytes and computes their digest. It holds no selection or composition rule;
  a rule added here would put policy in the I/O tier.

### Todos

None recorded.

## Docs References

No external or domain documentation is configured for this memory root
(`system/sources.md` has no entries), so no external documentation claim is made.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant documentation found after checking live sources. | n/a | n/a |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The loaded-source value this module produces and the digest it records. | `CapsuleSource`; `compute_content_digest` | mcp/src/agents_remember/models/role_capsules/sources.py:49-91; mcp/src/agents_remember/models/role_capsules/types.py:81-85 |
| The refused source set is validated against the locked plan in both directions after admission. | `admit_source_set` | mcp/src/agents_remember/models/role_capsules/source_set.py:86-100 |
| The application entry point that admits and then compiles, returning a refusal as a value. | `compile_admitted_capsule`; `CapsuleCompilationOutcome` | mcp/src/agents_remember/application/role_capsules/compilation.py:89-122; mcp/src/agents_remember/application/role_capsules/compilation.py:46-88 |
| The typed source-refusal base and the codes raised here. `source-root-invalid`, `source-root-missing`, `source-path-invalid`, `source-path-escapes-root`, `source-missing`, and `duplicate-identity` are raised by this module and are deliberately **not** members of `CAPSULE_STATUSES`. | `CapsuleSourceError` | mcp/src/agents_remember/errors.py:512-513 |
| Traversal, missing-source, non-directory-root, double-request and unreadable-source cases. | `test_admission_refuses_a_path_that_escapes_its_root`; `test_admission_refuses_a_missing_source_instead_of_skipping_it`; `test_admission_refuses_a_root_that_is_not_a_directory`; `test_admission_refuses_the_same_path_requested_twice`; `test_an_unreadable_source_returns_a_refusal_rather_than_raising`; `test_admission_is_reproducible_over_one_unchanged_tree` | mcp/tests/test_role_capsule_admission.py:301-310; mcp/tests/test_role_capsule_admission.py:311-319; mcp/tests/test_role_capsule_admission.py:320-326; mcp/tests/test_role_capsule_admission.py:327-334; mcp/tests/test_role_capsule_admission.py:335-358; mcp/tests/test_role_capsule_admission.py:290-300 |

## Cross-Repo References

No sibling-repository contract defines source admission.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-09-16T08:56+02:00 — 260915-CAPS-L2 curator: created this card for the filesystem admission
  boundary added by the deterministic capsule compiler leaf (`CAPS-R02@v1`). Records the
  explicit-not-eager read (so a missing block stays discoverable), containment-before-read, the
  reserved manifest metadata identity, the fixed admission order, and the five-plus-one refusal
  codes this module raises outside `CAPSULE_STATUSES`. Verification metadata is left at the leaf
  base commit because the source is uncommitted — the governed closeout stamps the real code
  commit.
