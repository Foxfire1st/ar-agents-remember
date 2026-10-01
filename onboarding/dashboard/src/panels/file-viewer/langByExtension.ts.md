# dashboard/src/panels/file-viewer/langByExtension.ts

## Governing Overview

[file-viewer/ overview](overview.md)

## Purpose

Lazily maps the L1 `language` id (from `/api/files/read`) to a `@codemirror/lang-*` extension, with each
pack code-split so it loads only when a file of that language is first opened. Exports the async
`langExtension`.

## Code Commentary

### Logic

`langExtension(language)` is `async` and returns `Extension | null`. A switch on the L1 `language` id
dynamically `import()`s the matching pack: `typescript`/`tsx`/`javascript`/`jsx` all resolve
`@codemirror/lang-javascript` with the right `{ typescript, jsx }` options; `python`/`json`/`css`/
`html`/`markdown` each resolve their own pack. The `default` branch returns `null` (bash/toml/yaml/sql/
text/binary → plain text); a comment notes `@codemirror/legacy-modes` can be pulled in later only if a
real need appears.

### Invariants And Boundaries

The keys are the L1 read endpoint's `language` ids (`FileContent.language`), not file extensions — keep
this switch in sync with the server's language detection. Every pack import is dynamic so unused
languages never enter the initial bundle; callers must `await` the promise and guard against a late
resolve after teardown. Returning `null` is the explicit unknown-language path (plain text), never an
error.

## Evidence

### Repo-Internal References

- `FilePane` awaits this and pushes the result as an editor extension, guarding a late resolve. [1]
- The `language` id is produced by the L1 read client. [2]
