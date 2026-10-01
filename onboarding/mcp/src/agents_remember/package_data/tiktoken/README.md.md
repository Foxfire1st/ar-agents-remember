# mcp/src/agents_remember/package_data/tiktoken/README.md

## Governing Overview

[mcp overview](../../../../overview.md)

## Purpose

This README is the operator-facing explanation of the one file sitting beside it: the vendored
`o200k_base` vocabulary blob named `fb374d419588a4632f3f557e76b4b70aebbca790` (3,613,922 bytes). It
answers the questions an agent has on first sight of an opaque 3.6 MB hash-named file in the package
tree — what it is, why its name is a hash, **who checks its bytes and why it cannot be tiktoken**,
and how to refresh it — and it records the `.gitattributes` obligation that comes with refreshing
it. There is no route-local overview for `package_data/`, so this sidecar is the durable onboarding
for that directory's contents.

## Code Commentary

### Logic

The README is prose, not code, and it documents five things.

**What the directory is**. The directory *is* a tiktoken cache directory shipped inside
the package, holding the vocabulary `agents_remember.models.tokens` counts response tokens with. It
exists so the server starts with no network egress. The token module builds the default counter at
module scope, so `tiktoken.get_encoding("o200k_base")` runs while the server is still importing.
Without a warm cache that call downloads the vocabulary, and a fresh container, an offline machine or
a hermetic CI job cannot start the server at all.

**Why the file name is a hash** (cit:(["byte-identical", "expected_hash", "The file name is not a choice", "446a9538cb6c348e3516120d7c08b09f57c36495e2acfffe59a5bf8b0cfb1a2d"], mcp/src/agents_remember/models/tokens.py:34-34; mcp/src/agents_remember/models/tokens.py:39-39; mcp/src/agents_remember/models/tokens.py:47-47; mcp/src/agents_remember/models/tokens.py:60-60)). `tiktoken.load.read_file_cached` looks a download up
under the SHA-1 of its source URL, so `sha1(url) = fb374d419588a4632f3f557e76b4b70aebbca790` is the
only name a cache hit can have. The indented block at L18-L20 records the URL, that name, and the
content hash `sha256(file) = 446a9538cb6c348e3516120d7c08b09f57c36495e2acfffe59a5bf8b0cfb1a2d`,
which is the value tiktoken itself names in `tiktoken_ext/openai_public.py::o200k_base` — so the
shipped file is intended to be byte-identical to the download it replaces and preserve token counts.

**Runtime integrity.** `_verify_vendored_vocabulary` refuses a missing or corrupt bundled vocabulary before the cache is primed; its computed SHA-256 must equal `VENDORED_VOCABULARY_SHA256` (cit:(["def _verify_vendored_vocabulary"], mcp/src/agents_remember/models/tokens.py:70-106)). The former installed-library hash and corruption tests are historical, not current coverage.

**How to refresh it** (cit:([`## Refreshing it`], mcp/src/agents_remember/package_data/tiktoken/README.md:42-67)). A short `python -` snippet fetches the URL tiktoken names, writes
it under `sha1(url)`, and prints the SHA-256 to compare. The README then states the two obligations
that are easy to miss: the new digest also replaces **`VENDORED_VOCABULARY_SHA256` in
`models/tokens.py`** (cit:([`VENDORED_VOCABULARY_SHA256`], mcp/src/agents_remember/models/tokens.py:47-47)), and the `-text` entry in the repository's `.gitattributes` must be
renamed to match the new file name. The exact shipped path has Git text conversion disabled (cit:(["mcp/src/agents_remember/package_data/tiktoken/fb374d419588a4632f3f557e76b4b70aebbca790 -text"], .gitattributes:13-13)). This protects the content-addressed bytes from checkout line-ending conversion; removed tests no longer enforce refresh consistency.

**Why this one is committed** (cit:(["/mcp/src/agents_remember/package_data/dashboard/"], .gitignore:26-26), cit:(["this file is committed"], mcp/src/agents_remember/package_data/tiktoken/README.md:64-67)). Unlike the cockpit bundle in `package_data/dashboard/`,
which is git-ignored and rebuilt on every release, this is third-party data addressed by its own
hash: written once, changed only when tiktoken changes what it asks for. It carries none of the
churn that kept the generated bundle out of version control.

### Conventions

Indented literal blocks rather than fenced code blocks, so the hash table and the refresh snippet
read the same in a terminal `cat` as in a renderer. Hashes are written out in full so a reader can
compare them against `ls` and `sha256sum` without following a link. The document names the exact
upstream symbol behind each claim (`tiktoken.load.read_file_cached`,
`tiktoken_ext/openai_public.py::o200k_base`) rather than describing the behaviour generically, and
it names in-repo enforcement by test function
(`test_the_gitattributes_entry_names_the_shipped_file`) so the reader can grep for what would go
red.

### Invariants And Boundaries

- The blob's file name is not a choice. It must remain `sha1(<source URL>)` or tiktoken's cache
  lookup misses and the download returns.
- The blob's bytes are its identity, and this repository — not tiktoken — is what enforces that.
  `models/tokens.py` verifies the SHA-256 before every load; tiktoken's own check repairs instead
  of refusing. Any edit to this README that hands the guarantee back to tiktoken is wrong.
- The `.gitattributes` `-text` entry must always name the current file, and any refresh must rename
  it *and* replace `VENDORED_VOCABULARY_SHA256` in `models/tokens.py` in the same change.
- This README must stay next to the blob it describes. It is the only in-tree explanation of an
  otherwise opaque hash-named binary.
- It documents; it does not load. Path derivation, the digest verification, the scoped
  `TIKTOKEN_CACHE_DIR` override, and the fail-loud absent/corrupt behaviour all live in
  `models/tokens.py`.
- The refresh snippet is a documented manual procedure, not an automated step. Nothing in the build
  regenerates this file.

### Todos

None known. The README already names its own trigger for change: a refresh is needed only when
`mcp/tests/test_cold_start.py` reports a new URL.

## Evidence

### Repo-Internal References

Every claim in this README is enforced somewhere else in the repository: by the loader that reads
the blob, by the attribute that protects its bytes, by the packaging glob that ships it, and by the
test that re-derives its two hashes.

- The token module defines the vendored URL, directory, and digest constants. [1]
- The loader derives the hash-named path and verifies the file before loading. [2]
- The cache context scopes `TIKTOKEN_CACHE_DIR` to the verified file and restores it after the load. [3]
- `TiktokenTokenCounter` is the production counter that reads the verified vocabulary. [4]
- `DEFAULT_TOKEN_COUNTER` constructs the default token counter at module scope. [5]
- The `-text` attribute this README says must be renamed on refresh, with a comment that points back at this file and names the test that stays red until it is renamed. [6]
- The `package-data` glob is recursive, so whatever is present under `package_data` at build time ships — which is how this blob reaches an installed wheel or sdist; the same file pins the tiktoken range the vendored bytes must satisfy (`tiktoken>=0.12,<1`). [7]
- The corruption cases this README describes, each applied to a *copy* in a temp directory and never to the blob here: CRLF-mangled, truncated to half its bytes, one flipped byte through the production `TiktokenTokenCounter()` entry point. [8]
- The contrast the README draws: the cockpit bundle and its fingerprint sidecar are git-ignored, while this content-addressed blob is committed. [9]
