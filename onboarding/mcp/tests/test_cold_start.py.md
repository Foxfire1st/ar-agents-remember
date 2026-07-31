# mcp/tests/test_cold_start.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/tests/test_cold_start.py`             |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-31T20:52+02:00                     |
| lastVerifiedCommitHash | `abc7cbcc74921cdcb57a61529445f61641e919e7` |
| lastVerifiedCommitDate | 2026-07-31T21:50:08+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

`test_cold_start.py` proves the MCP server imports and starts with **no network egress**, and that
the tokenizer it builds on the way up needs none. It is a regression guard for a class of defect —
"something on the server's import path reaches the network" — whose cost is that the server cannot
start where there is none: a fresh container, an offline machine, a hermetic CI job. The instance
that motivated it was `models/tokens.py` building `DEFAULT_TOKEN_COUNTER` at module scope, which
made `tiktoken.get_encoding("o200k_base")` download the vocabulary from
`openaipublic.blob.core.windows.net` while `mcp/tools/base.py` was still importing.

The guard has two halves, and only the first is a subprocess. Removal of the vendored blob is the
loudest way to break it and the child sees that. The likelier break is a copy that is present and
**wrong** — line endings rewritten, a partial write, one flipped byte — which no child can observe,
because tiktoken never gets far enough to try the network. `CorruptVendoredVocabularyTests` is that
half, and it runs in-process against corrupted *copies*.

## Code Commentary

### Logic

**Nothing in this file may import `agents_remember.models.tokens` at module scope, and that rule is
load-bearing enough that the docstring spends a paragraph on it (L23-L31).** That module builds
`DEFAULT_TOKEN_COUNTER` at import, so a module-scope import runs the load under test inside the
*parent* pytest process, during collection, before any assertion exists to see what it did — and
the parent has network and a writable checkout, which is exactly the pair of conditions this guard
asserts the absence of. It cost the file its teeth once already: with the load happening at
collection, `tiktoken.load.read_file_cached` met the mismatching bytes first, deleted the vendored
file, re-downloaded it into the package directory, and every test reported green. Every test that
needs the module now calls `tokens_module()` (L160-L169), a helper wrapping
`importlib.import_module("agents_remember.models.tokens")` — `importlib` rather than a
function-level `import` statement because PLC0415 forbids the latter and there is no per-file
ignore. The only module-scope import from the package is `TokenizerVocabularyError` (L72), which
carries no import-time load.

**The cold-start assertions must run in a subprocess, and that is the second thing shaping this
file.** The docstring states it (L11-L21): tiktoken memoizes loaded encodings in
`tiktoken.registry.ENCODINGS`, and any earlier test in the session has already populated it.
In-process, the load under test would be a dictionary hit that never touches the disk — let alone
the network — and the assertion would pass against a package that ships no vocabulary at all. Do
not "simplify" those tests into the parent process; doing so makes them vacuous without making
them fail.

The subprocess's other job is cold caches. `run_cold_start_probe()` (L172-L196) points
`TIKTOKEN_CACHE_DIR`, `DATA_GYM_CACHE_DIR`, `TMPDIR` and `HOME` at one empty directory, so every
place tiktoken looks — including its default `<tmpdir>/data-gym-cache` — is empty. Pointing the
*operator* variable at a cold directory is deliberate: it also proves the package's own vendored
copy wins over an exported one that would send the load back to the network. `PYTHONPATH` is set to
this checkout's `mcp/src` so the child imports the tree under test.

`PROBE` (L98-L157) is the child script, and it closes the network before importing anything it is
testing. It replaces `socket.socket.connect`, `connect_ex`, `socket.create_connection`,
`getaddrinfo` and `gethostbyname` with a raiser (L119-L123) rather than replacing the
`socket.socket` class itself, because replacing the class breaks unrelated imports that subclass
it. It then *proves the block took effect* (L126-L131) — a block that silently did not take would
make every assertion below vacuous — and only then imports `create_server` and
`DEFAULT_TOKEN_COUNTER`, builds a server, and prints the server name, tokenizer name, exactness and
the token count for a fixed payload as JSON.

`ColdStartTests` (L199-L218) reads that JSON. L200-L205 asserts the child exited zero and the
server is `"Agents Remember"`. L207-L218 asserts the behaviour that must **not** have changed:
`tokenizer == "tiktoken:o200k_base"`, `exact is True`, and the child's count for `PROBE_PAYLOAD`
equals the count the parent's `DEFAULT_TOKEN_COUNTER` — reached through `tokens_module()`, not an
import — produces for the same payload. That comparison is the point of the fixed payload at L96:
a lazy load with an approximate fallback would pass the start test and fail this one.

`VendoredVocabularyTests` (L221-L331) runs in-process because it tests the loader's own contract,
not the cold path.

- L222-L244 re-derives everything from the *installed* tiktoken rather than restating it: it
  patches `openai_public.load_tiktoken_bpe` to record the URL and `expected_hash` that
  `o200k_base()` passes, then asserts the recorded URL equals `VENDORED_VOCABULARY_URL`, that
  `vendored_vocabulary_path().name` equals `sha1(url)`, that **`VENDORED_VOCABULARY_SHA256` equals
  the hash tiktoken asks for** (L243), and that `sha256` of the shipped bytes equals it too. That
  third assertion is why the loader may hold its own copy of the digest without it becoming a
  second source of truth: the loader must check before tiktoken sees the file, so it needs the
  value, and this pins it to tiktoken's.
- L246-L259 pins the `.gitattributes` entry to the file actually shipped. The entry is a literal
  path and the path is `sha1(url)`, so a tiktoken release that moves the URL renames the file and
  leaves the rule naming a file that no longer exists — an orphaned `-text` rule protects nothing,
  silently, and only on `core.autocrlf=true` clones. The test finds candidate lines by the
  directory prefix `VENDORED_VOCABULARY_ATTRIBUTE_PREFIX` (L85) and asserts the whole list is
  exactly `[[prefix + name, "-text"]]`.
- L261-L269 points `VENDORED_VOCABULARY_DIR` at an empty directory and requires
  `TokenizerVocabularyError` — an absent vocabulary must never fall through to a download.
- L271-L277 requires the same error for `"cl100k_base"`: only the one vendored encoding may load.
- L279-L286 and L288-L297 pin the scoping of the `TIKTOKEN_CACHE_DIR` override: inside the context
  manager the variable is `VENDORED_VOCABULARY_DIR`; on exit an originally-absent variable is
  removed again and an operator's pre-existing value is restored verbatim.
- L299-L305 builds a real `TiktokenTokenCounter`, checks its reported name, and asserts the
  process is left with no `TIKTOKEN_CACHE_DIR` behind it.
- L307-L331 guards the reentrancy of `_CACHE_DIR_LOCK`. `with vendored_vocabulary_cache(name):
  TiktokenTokenCounter()` is the obvious use of a context manager this package exports, and the
  counter's own load re-enters it on the same thread; against a non-reentrant lock held across the
  `yield` that is a permanent hang, not a failure. The work runs on a daemon thread joined with
  `REENTRANT_LOAD_TIMEOUT_SECONDS` (L91, `60.0`) and the assertion is `worker.is_alive()` is false
  — a regression must *report* the deadlock, not reproduce it inside the suite.

`CorruptVendoredVocabularyTests` (L334-L417) covers the case the cold-start probe structurally
cannot see: a vendored file that is present but *wrong*. No child can observe it, because tiktoken
never gets far enough to try the network. If the digest check were left to tiktoken,
`read_file_cached` would answer each mismatch by deleting the file and downloading a replacement
over it — measured, on this very suite: CRLF-mangling the vendored file and truncating it to half
its bytes both passed while the file was quietly restored.

- `assert_corruption_is_refused()` (L350-L376) is the shared shape. It copies the shipped blob into
  a `TemporaryDirectory`, applies the caller's corruption **to the copy**, asserts the copy's digest
  differs from `VENDORED_VOCABULARY_SHA256`, patches `VENDORED_VOCABULARY_DIR` at the temp
  directory, and requires `TokenizerVocabularyError`. It then asserts the message names three
  things — the copy's path, the expected digest and the found digest — because the operator's next
  move is to compare their file against the one tiktoken asks for, and a message that says only
  "corrupt" does not say against what. Finally it asserts `copy.is_file()`: nothing deleted it and
  nothing downloaded a replacement over it.
- L378-L381 CRLF-mangles the copy (`data.replace(b"\n", b"\r\n")`) — what a `core.autocrlf=true`
  checkout does to a file git thinks is text, which opens fine and looks right.
- L383-L386 truncates the copy to `data[: len(data) // 2]` — an interrupted download or partial
  write, whose prefix is byte-identical, so anything short of hashing the whole file accepts it.
- L388-L417 goes through the production entry point: `TiktokenTokenCounter()`, the statement that
  runs while `mcp/tools/base.py` is importing. The corruption is a **single flipped byte**
  (`data[0] ^= 0x01`) — same length, same line endings, same everything a cheaper check than a
  digest could look at. It also patches `tiktoken_load.read_file` with an `unreachable` raiser,
  which earns its place twice: it asserts no read was attempted at all, and it stops a regression
  here from actually downloading 3.6 MB over the corrupt copy.

**Every corruption is applied to a copy, never to the shipped file.** Mutating the real blob would
leave the checkout damaged whenever one of these failed part-way, and the suite would then be
asserting against its own debris.

### Conventions

The child is a source string in this module rather than a fixture file, so the thing under test and
the environment it runs in are read together. The probe reports through JSON on stdout and the
parent asserts on parsed fields; `result.stderr` is passed as the `msg` of the return-code
assertion so a child traceback is what a failure shows.

Production symbols reach the assertions through `tokens_module()`, **never** through a module-scope
import — `tokens.VENDORED_ENCODING_NAME`, `tokens.VENDORED_VOCABULARY_DIR`,
`tokens.VENDORED_VOCABULARY_URL`, `tokens.VENDORED_VOCABULARY_SHA256`,
`tokens.vendored_vocabulary_cache`, `tokens.vendored_vocabulary_path` and
`tokens.TiktokenTokenCounter` are all attribute reads on the module object returned by that helper.
The one deliberate exception is `TIKTOKEN_CACHE_DIR_ENV`, which is **restated as a literal** at L78
with a comment saying why: importing it from the module under test is the defect this file guards
against. Its siblings (`DATA_GYM_CACHE_DIR`, `TMPDIR`, `HOME`) stay literals inline; that one is a
constant only because two places need it. Both hashes are still derived at assertion time from the
installed tiktoken, never hard-coded here.

Test names are full sentences (`test_the_shipped_file_is_the_one_tiktoken_asks_for`,
`test_a_truncated_copy_is_refused`), and the reason a case exists lives in a comment or docstring
immediately inside it rather than in the name.

### Invariants And Boundaries

- **No module-scope import of `agents_remember.models.tokens`, ever.** It builds
  `DEFAULT_TOKEN_COUNTER` at import, so a module-scope import runs the load under test in the
  parent process during collection — with network and a writable checkout — and
  `read_file_cached` silently repairs any corrupt vendored blob before a single assertion runs.
  Everything goes through `tokens_module()`.
- The cold-start assertions must stay in a child process. In-process they pass against a package
  with no vendored vocabulary, because `tiktoken.registry.ENCODINGS` is already warm.
- The child must block egress **before** importing the server, and must verify the block took.
- All four cache variables must keep pointing at an empty directory. Honouring a warm one anywhere
  reintroduces the false pass.
- **Corruption tests mutate copies only.** The shipped blob at
  `mcp/src/agents_remember/package_data/tiktoken/fb374d419588a4632f3f557e76b4b70aebbca790` is the
  subject of these tests, not their scratch space; a test that corrupted it in place would leave
  the checkout damaged on any part-way failure.
- The re-entrancy check must keep a **bounded** join. The failure mode it guards is an unbounded
  wait, so a regression has to be reported, not reproduced inside the suite.
- The counter identity is part of the contract: `tiktoken:o200k_base`, `exact=True`, and a count
  identical to the warm parent's. An approximate fallback is not an acceptable degradation.
- This suite proves the tokenizer's import-time network behaviour and the loader's refusals only.
  `test_tokens.py` owns the counters' arithmetic and the payload-finalization fixpoint.

### Todos

None known. The docstring (L33-L46) records that the guard was verified to bite, on a scratch copy
of the tree with the vendored vocabulary deleted: the child dies while importing the server with
**`TokenizerVocabularyError`** raised from `DEFAULT_TOKEN_COUNTER = TiktokenTokenCounter()` — the
designed refusal, *not* a `requests.exceptions.ConnectionError`, because `vendored_vocabulary_cache`
never lets the load reach the network at all. The probe exits 1, both `ColdStartTests` fail on its
return code with that traceback as the message, and the rest of the file fails alongside them
because `tokens_module()` raises the same refusal in-process: **thirteen failures, no collection
error, nothing skipped** (2 + 8 + 3 across the three classes).

## Docs References

The resolved `system/sources.md` registry declares no `Domain Documentation` entries, so there was
no live documentation source to check for this file. The tiktoken facts this suite depends on are
proven against the installed library rather than asserted from prose; see `Cross-Repo References`.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

The suite spans the whole import chain it defends: the tool surface that imports the token module,
the module that builds the counter at import, the vendored blob the counter reads, and the typed
error that must be raised instead of a download.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The module under test: the vendored constants including `VENDORED_VOCABULARY_SHA256` and the `RLock`, `vendored_vocabulary_path()` deriving the file name as `sha1(url)`, `_verify_vendored_vocabulary()` refusing absent / wrong-encoding / wrong-digest before the environment is touched, the scoped `vendored_vocabulary_cache()` handing tiktoken `str(path.parent)` of the verified file, `TiktokenTokenCounter.__post_init__` reading the vocabulary, and `DEFAULT_TOKEN_COUNTER` built at module scope — the statement a module-scope import here would execute during collection. | L37-L54; L57-L67; L70-L106; L109-L146; L191-L195; L205 | [tokens.py](agents-remember/mcp/src/agents_remember/models/tokens.py) |
| The import-path link that puts the counter on the server's startup path: the tool payload builder imports `finalize_payload_tokens` at module level and calls it on every public tool response. | L9; L80-L83 | [tools/base.py](agents-remember/mcp/src/agents_remember/mcp/tools/base.py) |
| `TokenizerVocabularyError` — the one production symbol this file may import at module scope, because it carries no import-time load. Raised instead of letting tiktoken reach for a vocabulary that is missing *or wrong*, precisely because the counter is built while the MCP tool surface is still importing. | L40-L48 | [errors.py](agents-remember/mcp/src/agents_remember/errors.py) |
| The vendored blob's own documentation: why the file name is a hash, why `models/tokens.py` verifies the digest itself rather than leaving it to tiktoken, the copy-based corruption tests this file runs, and how to refresh it. | L1-L11; L26-L40; L42-L62 | [package_data/tiktoken/README.md](agents-remember/mcp/src/agents_remember/package_data/tiktoken/README.md) |
| The `-text` entry that `test_the_gitattributes_entry_names_the_shipped_file` reads and pins: it stops a `core.autocrlf=true` checkout from rewriting the bytes that are the blob's identity, which now makes that clone alone refuse to start rather than re-download. Its comment names this test as the thing that stays red until a refresh renames the entry. | L5-L13 | [.gitattributes](agents-remember/.gitattributes) |
| Packaging ships whatever is under `package_data` recursively, which is how the vendored vocabulary reaches an installed wheel or sdist. | L52-L63 | [mcp/pyproject.toml](agents-remember/mcp/pyproject.toml) |

## Cross-Repo References

The boundary this suite defends is the third-party `tiktoken` package and the Azure blob URL it
would otherwise fetch from. Every fact below was re-read against tiktoken **0.13.0** as installed
in this environment, and against the same files at the `0.13.0` tag upstream. Line numbers are from
the installed 0.13.0 sources. The decisive one is that **`read_file_cached` does not fail closed on
a hash mismatch** — it repairs, from the network — which is why the digest check lives in
`models/tokens.py` and why `CorruptVendoredVocabularyTests` exists at all.

| Finding | Citations | Source Path |
| --- | --- | --- |
| `read_file_cached` prefers `TIKTOKEN_CACHE_DIR`, then `DATA_GYM_CACHE_DIR`, then `<tmpdir>/data-gym-cache`, and looks a download up under `hashlib.sha1(blobpath.encode()).hexdigest()` — which is why the probe must point all of them at an empty directory and why the shipped file's name is that digest. | L35-L53 | [tiktoken/load.py @ 0.13.0](https://github.com/openai/tiktoken/blob/0.13.0/tiktoken/load.py) |
| A cached file whose SHA-256 does not match `expected_hash` is **not** rejected: `os.remove(cache_path)` (L62) then `contents = read_file(blobpath)` (L66) then the write-back (L75-L80). This is the exact mechanism that let a CRLF-mangled and a half-truncated vendored blob both report "8 passed" while the file was silently re-downloaded into the package directory — the defect that made this file's module-scope import fatal to its own purpose. | L54-L66 | [tiktoken/load.py @ 0.13.0](https://github.com/openai/tiktoken/blob/0.13.0/tiktoken/load.py) |
| The write-back re-raises `OSError` when the cache directory was caller-specified and swallows it only for tiktoken's own default — so on a read-only install the repair path would surface as `PermissionError` rather than the designed refusal. | L75-L84 | [tiktoken/load.py @ 0.13.0](https://github.com/openai/tiktoken/blob/0.13.0/tiktoken/load.py) |
| `o200k_base()` passes the vendored URL (L97) and `expected_hash="446a9538...1a2d"` (L98) to `load_tiktoken_bpe`; these are the values `test_the_shipped_file_is_the_one_tiktoken_asks_for` records and compares against both the shipped bytes and `VENDORED_VOCABULARY_SHA256`. | L95-L99 | [tiktoken_ext/openai_public.py @ 0.13.0](https://github.com/openai/tiktoken/blob/0.13.0/tiktoken_ext/openai_public.py) |

## Update History

- 2026-07-31T22:25+02:00 — 260731-EFA-L3 curator: reconciled against the substantial rewrite this
  file received after the sidecar below was created. Three claims were outright false. (1) The
  Conventions section said "Production symbols are imported, never restated ... all come from
  `agents_remember.models.tokens` (L48-L57)" — that module-scope import *was* the defect: it ran
  `DEFAULT_TOKEN_COUNTER = TiktokenTokenCounter()` in the parent pytest process at collection,
  where `read_file_cached` deleted and re-downloaded a corrupt vendored blob before any assertion
  ran. No such import remains; everything reaches the module through `tokens_module()` (L160-L169),
  `TIKTOKEN_CACHE_DIR_ENV` is deliberately restated as a literal (L78), and the only module-scope
  package import is `TokenizerVocabularyError` (L72). (2) Todos claimed the guard was proven to
  bite with `requests.exceptions.ConnectionError`; the docstring (L33-L46) now records
  `TokenizerVocabularyError` instead, because `vendored_vocabulary_cache` never lets the load reach
  the network — thirteen failures, not eight. (3) The suite was described as two classes; the third,
  `CorruptVendoredVocabularyTests` (L334-L417), is the half the probe structurally cannot cover.
  Added it, plus `test_the_gitattributes_entry_names_the_shipped_file` (L246-L259), the
  `RLock` deadlock guard (L307-L331), and the new `VENDORED_VOCABULARY_SHA256` assertion inside
  `test_the_shipped_file_is_the_one_tiktoken_asks_for` (L243). Re-derived every citation in the file
  — the docstring L1-L27 → L1-L47, `PROBE` L64-L123 → L98-L157, `run_cold_start_probe` L126-L150 →
  L172-L196, `ColdStartTests` L153-L171 → L199-L218, `VendoredVocabularyTests` L174-L228 →
  L221-L331, `.gitattributes` L5-L11 → L5-L13, and every `tokens.py` citation in the reference
  table. Added the cross-repo row proving tiktoken's `read_file_cached` does *not* fail closed
  (`tiktoken/load.py` 0.13.0 L54-L66: `os.remove` then `read_file`), which is the fact the whole
  rewrite turns on, and the read-only-install re-raise at L75-L84. Verified by running the 11
  in-process tests (all pass, 0.5 s) and confirming the shipped blob's SHA-256 was unchanged
  afterwards. Metadata cells untouched.

- 2026-07-31T20:52+02:00 — 260731-EFA-L3 curator: Created for the no-network cold-start guard
  added by this leaf. Verification metadata is pinned to the leaf's base commit until closeout
  stamps the code commit.
