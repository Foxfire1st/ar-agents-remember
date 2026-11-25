# mcp/src/agents_remember/application/knowledge_writer/code_anchors.py

## Governing Overview

[application route overview](../overview.md)

## Purpose

**Anchor resolution at the leaf's code candidate tree C (MIK-R12 rule 2, MIK-R07 rule 0).**
`CodeSnapshot.capture` captures the code worktree, committed and uncommitted, as a tree through the shipped
private-index capture (`worktrees/modules/git.worktree_candidate_tree`) and lists regular-file and symlink
entry blobs (modes `100644`, `100755`, `120000`). A link binds its target bytes, not referent contents
and not `absent`; only a missing entry is absent. `symlinks` records the mode-`120000` paths.
`CodeSnapshot.resolve` turns a locator into an `Anchor{locator, blob, content}`, hashing the located bytes
through `models/knowledge_files/anchor_content.py`.

## Code Commentary

### Logic

- `symbol`: a path in `CodeSnapshot.symlinks` raises a named `AnchorResolutionError` before blob
  parsing or extraction; cite the file or a line range of the link bytes instead. Otherwise, the one
  extent the shipped citation extractor (`memory_quality/style/citations/extents`) binds
  for the name. Symbol extraction requires valid UTF-8 and an available reader. The resolver calls
  `extents.qualified_spans` with the file's definitions and selected grammar. For Lean it looks up the
  whole name and gives verified full names precedence over written aliases. If the scope is uncertain,
  the refusal offers a line range. If several verified bindings share a written name, the refusal gives
  their distinct full names when available. Outside Lean, an undefined symbol can still yield a
  script test-case diagnostic.
- `line_range`: the recorded lines, which must be lines the blob holds (`RangeOutsideBlobError` becomes
  `AnchorResolutionError`).
- `file`: every byte of the entry blob; on a symlink this is the link-target text. `line_range` also
  reads these entry bytes, never follows the link.
- Blob bytes are read on demand and cached per blob.
- **`file_subject_mismatch` (MIK-R10).** For a `no_invariant` row with a `file:<path>@<object>` subject, it
  reads the path's tree entry at C (`git rev-parse --verify --quiet <tree>:<path>`, with the metadata timeout
  `GIT_METADATA_TIMEOUT_SECONDS` since review N5) and returns why the subject names no change at C, or
  `None`. The object is a regular file's blob, a symlink's blob or a submodule's commit; `absent` means C holds
  nothing at the path. Any other subject passes. The refusal reads "names no change at C: the code candidate
  holds … (unknown subject)".
- **`CodeSnapshot.at_commit(repository, commit)`.** A committed snapshot resolves the supplied operand to a Git commit and records its full ID beside the commit's tree. A tree or blob operand raises `AnchorResolutionError`. The constructor checks 40- or 64-character hexadecimal syntax for a supplied commit ID. `capture` reads the working tree and carries no commit. The crossing route supplies the sync's settled commit, which identifies the code used to confirm dependent links.

### Conventions

- Every failure is an `AnchorResolutionError` whose message the authoring step turns into a `Problem`.

### Invariants And Boundaries

- Nothing is read from `HEAD` or any other tree: a path C does not hold does not resolve.
- The writer never guesses between definitions or accepts a mention.
- `content` is computed only through `anchor_content` (architect ruling 5: one definition).

### Todos

- Reviewer R2-1 (low, non-blocking): `file_subject_mismatch` has no unit assertion for a symlink object or an
  `@absent` subject; the reviewer verified both by a probe on a scratch repository.

### Strict symbol decoding and case diagnostics

For a supported language, `_symbol_range` strictly decodes the candidate blob as UTF-8 before extracting definitions. A decoding failure is translated to `AnchorResolutionError` naming the source path. An unavailable grammar is also translated to that error type. If extraction returns no spans, the writer checks for an uncertain Lean scope first, then asks `grammars.test_case_refusal(path, lines, name)` for a script test-case diagnostic. The ordinary refusal says the path at C does not define the requested name. Multiple spans still refuse with their line ranges, and exactly one span is returned.

This decoding rule is specific to symbol extraction. File and line-range locators continue to bind the selected entry bytes, and the early symlink-symbol refusal remains before blob parsing. A case-specific refusal is diagnostic evidence, not proof that a test ran or that a dynamic case acquired a bindable extent.


## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is the requirement packet `MIK-R12@v2` of task
`260928_maintained-invariant-knowledge` (with its architect rulings in the task's leaf document
`12_category-authoring-through-the-curator-workflow.json`) and the coordination-root note Doc14
(`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`); they live outside the
code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

Capture and resolution.

- A locator that does not resolve at C. [1]

- The captured tree C and its blobs. [2]

- A `file:` row subject must name the path's object at C, or `absent` (MIK-R10). [3]
- Capture through the private-index candidate tree. [4]

- A symbol must bind exactly once. [6]





- The snapshot of a committed code state, for a master line's crossing. [8]


- Symbol extraction rejects invalid UTF-8 with a named anchor error and uses case-specific diagnostics when no definition binds. [11]
- Symlink symbols refuse before blob parsing; file and line-range anchors still hash the selected entry bytes. [12]

### Cross-Repo References

No cross-repo boundary is crossed: the writer reads the paired code worktree and writes the paired memory
worktree of one repository.

No cross-repo boundary is crossed by this file.


- Resolve file/line-range locators against entry bytes; refuse symlink symbols before parsing. [5]


- Both constructors read regular files and symlink entries of one tree, retaining a symlink path set. [9]


- Current source delta inspected statically: Fix regular-file/symlink snapshot scope and early symbol refusal; retain ordinary symbol/range binding. [10]

- The writer passes the selected grammar to shared qualified lookup. Lean keys are exact. Other readers can use dotted containment after an exact-key miss. [7]

- The writer refuses an unverifiable Lean key with a line-range remedy and reports full-name choices for a multiply bound alias. [14]
