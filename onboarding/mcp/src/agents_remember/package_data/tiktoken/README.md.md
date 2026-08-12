# mcp/src/agents_remember/package_data/tiktoken/README.md

| Field                  | Value                                                          |
| ---------------------- | -------------------------------------------------------------- |
| repository             | agents-remember                                                |
| path                   | `mcp/src/agents_remember/package_data/tiktoken/README.md`      |
| doc_type               | `file-level-onboarding`                                        |
| lastUpdated            | 2026-07-31T20:52+02:00                                         |
| lastVerifiedCommitHash | `c9ae4dbd8adb650f116b9d4f86343b496c3e5f32`                     |
| lastVerifiedCommitDate | 2026-08-12T17:53:40+02:00|
| governingOverview      | `../../../../overview.md`                                      |

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
shipped file is byte-identical to the download it replaces and token counts are unchanged
(cit:([`test_the_shipped_file_is_the_one_tiktoken_asks_for`], mcp/tests/test_cold_start.py:222-244)).

**What holds it shut** (cit:([`test_the_shipped_file_is_the_one_tiktoken_asks_for`, `test_the_gitattributes_entry_names_the_shipped_file`, `CorruptVendoredVocabularyTests`], mcp/tests/test_cold_start.py:222-244; mcp/tests/test_cold_start.py:246-259; mcp/tests/test_cold_start.py:334-417)). `mcp/tests/test_cold_start.py` re-derives the URL's SHA-1 and the
expected SHA-256 from the installed tiktoken and fails if either stops matching the shipped file, so
a version bump that moves the URL is caught. It corrupts *copies* of this file in a temporary
directory — CRLF-mangled, truncated to half its bytes, one byte flipped — and requires the refusal
each time, **never touching the file here**. And it fails if the `.gitattributes` entry stops naming
the file that is actually shipped.

**How to refresh it** (cit:([`## Refreshing it`], mcp/src/agents_remember/package_data/tiktoken/README.md:42-67)). A short `python -` snippet fetches the URL tiktoken names, writes
it under `sha1(url)`, and prints the SHA-256 to compare. The README then states the two obligations
that are easy to miss: the new digest also replaces **`VENDORED_VOCABULARY_SHA256` in
`models/tokens.py`** (cit:([`VENDORED_VOCABULARY_SHA256`], mcp/src/agents_remember/models/tokens.py:47-47)), and the `-text` entry in the repository's `.gitattributes` must be
renamed to match the new file name (cit:([`test_the_gitattributes_entry_names_the_shipped_file`], mcp/tests/test_cold_start.py:246-259)). Neither can be forgotten silently:
`test_the_shipped_file_is_the_one_tiktoken_asks_for` re-derives the digest from tiktoken and
compares it to the constant, and `test_the_gitattributes_entry_names_the_shipped_file` stays red
until the entry is renamed. That entry is what stops a `core.autocrlf=true` checkout from rewriting
the line endings of a file whose bytes are its identity — which now leaves that clone, and only that
clone, unable to start the server at all.

**Why this one is committed** (cit:(["/mcp/src/agents_remember/package_data/dashboard/"], .gitignore:23-23), cit:(["this file is committed"], mcp/src/agents_remember/package_data/tiktoken/README.md:64-67)). Unlike the cockpit bundle in `package_data/dashboard/`,
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

## Repo-Internal References

Every claim in this README is enforced somewhere else in the repository: by the loader that reads
the blob, by the attribute that protects its bytes, by the packaging glob that ships it, and by the
test that re-derives its two hashes.

| Finding | Anchor | Source |
| --- | --- | --- |
| The token module defines the vendored URL, directory, and digest constants. | `VENDORED_VOCABULARY_URL`; `VENDORED_VOCABULARY_DIR`; `VENDORED_VOCABULARY_SHA256` | mcp/src/agents_remember/models/tokens.py:38-38; mcp/src/agents_remember/models/tokens.py:47-48 |
| The loader derives the hash-named path and verifies the file before loading. | `vendored_vocabulary_path`; `_verify_vendored_vocabulary` | mcp/src/agents_remember/models/tokens.py:57-67; mcp/src/agents_remember/models/tokens.py:70-106 |
| The cache context scopes `TIKTOKEN_CACHE_DIR` to the verified file and restores it after the load. | `vendored_vocabulary_cache` | mcp/src/agents_remember/models/tokens.py:109-146 |
| `TiktokenTokenCounter` is the production counter that reads the verified vocabulary. | `TiktokenTokenCounter` | mcp/src/agents_remember/models/tokens.py:183-202 |
| `DEFAULT_TOKEN_COUNTER` constructs the default token counter at module scope. | `DEFAULT_TOKEN_COUNTER` | mcp/src/agents_remember/models/tokens.py:205-205 |
| The `-text` attribute this README says must be renamed on refresh, with a comment that points back at this file and names the test that stays red until it is renamed. | "-text" | .gitattributes:12-13 |
| The `package-data` glob is recursive, so whatever is present under `package_data` at build time ships — which is how this blob reaches an installed wheel or sdist; the same file pins the tiktoken range the vendored bytes must satisfy (`tiktoken>=0.12,<1`). | "tiktoken>=0.12"; "package_data/**/*" | mcp/pyproject.toml:26-26; mcp/pyproject.toml:86-86 |
| The test that re-derives both hashes from the installed tiktoken and additionally asserts `VENDORED_VOCABULARY_SHA256` equals the one tiktoken asks for, so a moved URL cannot silently fall back to the network and the loader's copy of the digest cannot become a second source of truth. | "test_the_shipped_file_is_the_one_tiktoken_asks_for" | mcp/tests/test_cold_start.py:222-244 |
| The test that pins the `.gitattributes` `-text` entry to the file actually shipped — the enforcement behind this README's refresh instruction. | "test_the_gitattributes_entry_names_the_shipped_file" | mcp/tests/test_cold_start.py:246-259 |
| The corruption cases this README describes, each applied to a *copy* in a temp directory and never to the blob here: CRLF-mangled, truncated to half its bytes, one flipped byte through the production `TiktokenTokenCounter()` entry point. | `CorruptVendoredVocabularyTests` | mcp/tests/test_cold_start.py:334-417 |
| The contrast the README draws: the cockpit bundle and its fingerprint sidecar are git-ignored, while this content-addressed blob is committed. | "this file is committed"; "/mcp/src/agents_remember/package_data/dashboard/" | mcp/src/agents_remember/package_data/tiktoken/README.md:64-67; .gitignore:19-24 |

## Update History
- 2026-08-12T15:19+02:00 — L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges; verification provenance remains closeout-owned.

- 2026-08-04T13:15:12+02:00 — 260731-EFA-L6 S18-B02 curator: extended the hash/provenance paragraph through local verifier evidence, narrowed the module-scope row, and regenerated both final ranges with the scoped fixer.

- 2026-08-03T23:26:43+02:00 — 260731-EFA-L6 S18-T3: replaced the stale direct-import claim with
  the current three-hop application/model response-finalization chain into token finalization. New
  ranges were normalized by the scoped fixer.

- 2026-08-03T10:30+02:00 — 260731-EFA-L6 W3-B07 curator: repaired 25 of 28 retained citation findings (16 table anchors/sources and 9 prose citations); 3 Tier-3 findings remain for the stale direct-import claim. Deleted five external-source rows (10 diagnostics) under the max-reviewer 2026-08-02 14:10 disposition because those sources are outside the frozen roots. Max-reviewer Tier-2 subject-binding addendum bound both sides of the ignored-versus-committed contrast.

- 2026-07-31T22:35+02:00 — 260731-EFA-L3 curator: reconciled against the rewrite the README itself
  received after the sidecar below was created. The false claim was the attribution of the byte
  check: this sidecar said the SHA-256 is "the value tiktoken itself asserts on load ... so the
  shipped file is byte-identical" and left it there, but tiktoken's check **does not fail closed** —
  `read_file_cached` answers a mismatch with `os.remove(cache_path)` then `read_file(blobpath)` and
  a write-back (`tiktoken/load.py` 0.13.0 L54-L66, L75-L84), which against this directory is a
  startup download that rewrites the installed package, or a `PermissionError` on a read-only
  install. The README now says `models/tokens.py` verifies the digest itself *because* of that, and
  the sidecar documents it as its own section ("Who checks the bytes, and why it cannot be
  tiktoken", README L26-L33). Added the section the README gained on what holds it shut
  (L35-L40: hashes re-derived from installed tiktoken, corruption applied to *copies* only, the
  `.gitattributes` name test), and the second refresh obligation the README now states —
  `VENDORED_VOCABULARY_SHA256` in `models/tokens.py` must be replaced alongside the blob. Re-derived
  every line range against the README as it now stands (67 lines): "why the name is a hash"
  L13-L28 → L13-L24, "how to refresh" L30-L47 → L42-L62, "why committed" L49-L52 → L64-L67
  (L1-L11 was unchanged). Fixed the reference table: `tokens.py` citations L44-L54/L57-L95/L132-L151/L154 →
  L57-L67/L109-L146/L191-L195/L205 plus the new `_verify_vendored_vocabulary()` at L70-L106;
  `.gitattributes` L5-L11 → L5-L13; `test_cold_start.py` L174-L192 → L222-L244, with new rows for
  the `.gitattributes` name test (cit:([`test_the_gitattributes_entry_names_the_shipped_file`], mcp/tests/test_cold_start.py:246-259)) and `CorruptVendoredVocabularyTests` (cit:([`CorruptVendoredVocabularyTests`], mcp/tests/test_cold_start.py:334-417)).
  Corrected the blob size from 3.4 MB to 3.6 MB (3,613,922 bytes, re-measured). Verified
  `sha256` of the shipped blob still equals `446a9538...1a2d`, matching `expected_hash` at
  `tiktoken_ext/openai_public.py` L98 in the installed tiktoken 0.13.0, and confirmed the blob was
  untouched after running the corruption tests. Metadata cells untouched.

- 2026-07-31T20:52+02:00 — 260731-EFA-L3 curator: Created for the vendored tiktoken vocabulary
  README added by this leaf. Verification metadata is pinned to the leaf's base commit until
  closeout stamps the code commit.
