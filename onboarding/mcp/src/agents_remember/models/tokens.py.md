# mcp/src/agents_remember/models/tokens.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/models/tokens.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-30T22:29+02:00                     |
| lastVerifiedCommitHash | `0506b57a1a80e0b377e9cc3303e1841d3bd4799a` |
| lastVerifiedCommitDate | 2026-09-01T12:17:08+02:00|
| governingOverview      | `overview.md`                              |

## Purpose

`tokens.py` owns token accounting helpers for modeled MCP responses.

## Code Commentary

The module counts tokens over compact, sorted JSON payloads (`_payload_json`
serializes with `ensure_ascii=False`, `separators=("", ":")`, `sort_keys=True`).
The default counter, `DEFAULT_TOKEN_COUNTER`, is a `TiktokenTokenCounter` on the
`o200k_base` encoding (`exact=True`); an `ApproximateTokenCounter` (compact-JSON
character length divided by four) remains available as a deterministic fallback.

### 260731-EFA-L3 — The Vocabulary Is Vendored, Never Downloaded

`DEFAULT_TOKEN_COUNTER = TiktokenTokenCounter()` is built at **module scope** and
`mcp/tools/base.py` imports this module (`from agents_remember.models.tokens import
finalize_payload_tokens`), so the encoding is loaded while the MCP tool surface is still
importing. That load used to be a network round trip: `tiktoken.get_encoding` fetches the
`o200k_base` vocabulary from `openaipublic.blob.core.windows.net` on a cold cache, and
nothing in the tree warmed one — a fresh container, an offline machine and a hermetic CI
job could not start the server at all. cit:(["DEFAULT_TOKEN_COUNTER = TiktokenTokenCounter()"], mcp/src/agents_remember/models/tokens.py:205-205)

The vocabulary now ships inside the package and the load is scoped to it:

```python
def __post_init__(self) -> None:
    with vendored_vocabulary_cache(self.encodingName):
        object.__setattr__(self, "_encoding", tiktoken.get_encoding(self.encodingName))
```

- cit:([`vendored_vocabulary_path`], mcp/src/agents_remember/models/tokens.py:57-67) derives the file name rather than hard-coding it:
  `hashlib.sha1(VENDORED_VOCABULARY_URL.encode()).hexdigest()` →
  `package_data/tiktoken/fb374d419588a4632f3f557e76b4b70aebbca790`. That digest is not a
  choice — `tiktoken.load.read_file_cached` looks a download up under the SHA-1 of its
  source URL, so it is the only name a cache hit can have.
- `_verify_vendored_vocabulary(encoding_name) -> Path` is the gate, and it runs
  **before** the environment variable is touched. It refuses on three conditions, always
  with `TokenizerVocabularyError` (`agents_remember.errors`), across two messages. cit:(["def _verify_vendored_vocabulary"], mcp/src/agents_remember/models/tokens.py:70-70) The first
  covers an `encoding_name` other than `VENDORED_ENCODING_NAME` (`"o200k_base"`)
  and an absent file (`not path.is_file()`) — the pre-existing "this package ships
  o200k_base only" refusal. cit:(["if encoding_name != VENDORED_ENCODING_NAME"], mcp/src/agents_remember/models/tokens.py:88-88) The second is new and is the one that needs saying:
  `hashlib.sha256(path.read_bytes()).hexdigest() != VENDORED_VOCABULARY_SHA256`, whose
  message deliberately names both the expected and the found digest, because an operator's
  next move is to compare their file against the one tiktoken asks for. cit:(["if digest != VENDORED_VOCABULARY_SHA256", "VENDORED_VOCABULARY_SHA256 ="], mcp/src/agents_remember/models/tokens.py:47-47; mcp/src/agents_remember/models/tokens.py:95-95) On success it
  returns the verified `Path`.
- cit:([`vendored_vocabulary_cache`], mcp/src/agents_remember/models/tokens.py:109-146) is a `@contextmanager` that calls
  the verifier first and then points `TIKTOKEN_CACHE_DIR` at **`str(path.parent)` — the
  directory of the file it just verified**, not at the `VENDORED_VOCABULARY_DIR`
  constant re-derived independently, so tiktoken can never be handed a directory whose
  contents were not checked. It restores the previous value (or pops it) in a `finally`.
  It **overrides** an operator-exported `TIKTOKEN_CACHE_DIR`: theirs may be cold, and
  honouring a cold one is exactly the download this removes. It is scoped rather than
  exported process-wide because the vendored directory lives inside the installed package,
  which is routinely read-only — left set, any *other* tiktoken encoding loaded later would
  try to write its download there, and `read_file_cached` re-raises write failures for a
  caller-specified cache dir (it swallows them only for its own default).
- cit:([`_CACHE_DIR_LOCK`], mcp/src/agents_remember/models/tokens.py:54-54) is a **`threading.RLock()`**, not a plain `Lock`. The guarded
  region spans the `yield` of a public context manager, so the obvious use of what this
  module exports — `with vendored_vocabulary_cache(name): TiktokenTokenCounter()` — has the
  counter's own `__post_init__` re-enter the manager on the same thread. On a plain `Lock`
  that is a permanent hang with no timeout and no traceback.

**Why this module verifies the digest instead of leaving it to tiktoken.** tiktoken does
check the SHA-256, but it does not fail closed on a mismatch: `read_file_cached` answers one
by `os.remove(cache_path)` and then `read_file(blobpath)`, writing the download back over
the cache path. Pointed at this package's directory that turns a corrupt vendored copy into
a silent network fetch on the startup path *and* a rewrite of the installed tree — or, on
the read-only install this code is written for, into a `PermissionError` from the write-back
instead of the designed refusal. Checking the digest before tiktoken is told where to look
is what makes corruption behave like absence. This was not theoretical: while the guard's
own test module still imported this module at collection time, a CRLF-mangled vendored blob
and a blob truncated to half its bytes were both silently deleted and re-downloaded, and the
suite reported green.

Counts are unchanged: the shipped bytes are byte-identical to the download, so the same
`o200k_base` counts and the same `tiktoken:o200k_base` tokenizer name ride the wire. There
is deliberately **no** approximate fallback on the cold path — that would make a reported
count depend on whether the producing machine had network, silently mixing exact counts with
estimates inside one dashboard aggregate.

`VENDORED_VOCABULARY_SHA256` restates a value tiktoken already holds (`expected_hash` in
`tiktoken_ext/openai_public.py::o200k_base`), which it has to, because the check must happen
before tiktoken sees the file. It is not a second source of truth:
`test_the_shipped_file_is_the_one_tiktoken_asks_for` re-derives the hash from the installed
tiktoken and asserts the constant equals it, so a release that changes what tiktoken asks
for turns that test red rather than leaving the two to drift.

`finalize_payload_tokens()` stamps `tokenizer` and `tokenCountExact` onto an
already-serialized response dict, then resolves `tokens` through
`_finalize_token_count()`, which recounts until the value stops changing —
necessary because writing the count into the payload alters the payload's own
length. `response_payload()` serializes a model and delegates to
`finalize_payload_tokens()`, and `dump_with_token_count()` is its
backward-compatible alias. Both serializers accept any `ResponseModel`, not only
operation-bearing `ToolResponse` envelopes, because the token fields live on the
shared `ResponseModel` base and the dispatch path stamps tokens onto
operation-less responses such as `ping`.

## Invariants And Boundaries

- Token counts are response-overhead metadata, not session/task logging.
- The MCP dispatch path applies these counts at the single choke point
  `_tool_payload()` (`mcp/tools/base.py`), which calls `finalize_payload_tokens()`
  on every public tool response.
- Use the canonical JSON form here when writing token-budget tests.
- **No network on the import path.** Building a `TiktokenTokenCounter` must resolve from
  the vendored file; it may never fall back to a download. Anything added here that loads
  another tiktoken encoding reintroduces the cold-start defect and will raise
  `TokenizerVocabularyError` instead — only `o200k_base` is shipped.
- **Corruption is refused, never repaired.** The SHA-256 check must stay *ahead* of the
  `TIKTOKEN_CACHE_DIR` assignment, and the directory handed to tiktoken must stay
  `path.parent` of the file that was just verified. Reordering these, or re-deriving the
  directory from the constant, hands tiktoken an unchecked directory and restores the
  delete-and-re-download behaviour this module exists to prevent.
- **`TIKTOKEN_CACHE_DIR` is borrowed, not owned, and the lock's scope is honest about it.**
  It is set only inside `vendored_vocabulary_cache` and restored on exit, so nothing
  downstream inherits a read-only cache directory it would try to write into. But the
  variable is process-global and belongs to tiktoken: `_CACHE_DIR_LOCK` serializes only the
  callers that come through this function. A thread touching `os.environ` directly can
  still observe the override or clobber it, and nothing at this layer can stop it. The
  guarantee's real scope is "the counters this package builds".
- **`_CACHE_DIR_LOCK` must stay reentrant.** Downgrading it to `threading.Lock` deadlocks
  the documented usage `with vendored_vocabulary_cache(...): TiktokenTokenCounter()`;
  `test_holding_the_context_open_around_a_counter_does_not_deadlock` joins with a bounded
  timeout so a regression reports the hang instead of reproducing it inside the suite.
- The vocabulary's file name **is** `sha1(VENDORED_VOCABULARY_URL)`; renaming it turns the
  cache hit back into a download. Letting a `core.autocrlf=true` checkout rewrite its line
  endings — hence the `-text` entry in `.gitattributes` — no longer downloads, it now
  refuses to start, because the rewritten bytes fail the digest check here.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Shared response envelopes define the token metadata fields on the `ResponseModel` base. | `ResponseModel` | mcp/src/agents_remember/models/base.py:66-88 |
| `_tool_payload` finalizes token metadata on every public tool response via this module. | `_tool_payload` | mcp/src/agents_remember/mcp/tools/base.py:77-79 |
| Direct tests for the counters, serializers, and the fixpoint self-consistency guarantee. | `FinalizePayloadTokensTests` | mcp/tests/test_tokens.py:80-104 |
| `TokenizerVocabularyError` — the typed refusal raised instead of downloading a vocabulary this package does not ship. | `TokenizerVocabularyError` | mcp/src/agents_remember/errors.py:284-292 |
| The shipped vocabulary, why its name is `sha1(url)`, the SHA-256 this module checks before every load, and how to refresh it (including replacing `VENDORED_VOCABULARY_SHA256`). | `VENDORED_VOCABULARY_SHA256` | mcp/src/agents_remember/package_data/tiktoken/README.md:46-46 |
| The cold-start guard: `ColdStartTests` starts the server in a child with every socket blocked and cold tiktoken caches; `VendoredVocabularyTests` re-derives both hashes from the installed tiktoken (asserting `VENDORED_VOCABULARY_SHA256` equals the one it asks for), proves the cache-dir override does not outlive the load, pins the `.gitattributes` entry to the shipped file name, and joins a re-entrant load on a timeout to catch an `RLock` downgrade; `CorruptVendoredVocabularyTests` corrupts *copies* of the blob in a temp directory — CRLF-mangled, truncated, one flipped byte — and requires the refusal each time. | `ColdStartTests`; `VendoredVocabularyTests`; `CorruptVendoredVocabularyTests` | mcp/tests/test_cold_start.py:199-218; mcp/tests/test_cold_start.py:221-331; mcp/tests/test_cold_start.py:334-417 |
| The `-text` attribute that stops a line-ending filter from changing the bytes this module hashes. | "-text" | .gitattributes:13-13 |

## Update History

- 2026-08-02T21:14+02:00 — W2-B03 curator: resolved 12 initial citation findings (3 anchor, 6 prose, 3 source); scoped recheck PASS (0 findings). Verification metadata unchanged.

- 2026-07-31T22:10+02:00 — 260731-EFA-L3 curator: reconciled against the fix that followed the
  earlier entry below. Corrected the claim that "tiktoken asserts their SHA-256 on load" — it
  checks the digest but does **not** fail closed: `tiktoken.load.read_file_cached` answers a
  mismatch with `os.remove(cache_path)` then `read_file(blobpath)` and writes the download
  back, which against this package's directory means a startup fetch that rewrites the
  installed tree (or a `PermissionError` on a read-only install). Documented the new
  cit:([`VENDORED_VOCABULARY_SHA256`], mcp/src/agents_remember/models/tokens.py:47-47) and cit:([`_verify_vendored_vocabulary`], mcp/src/agents_remember/models/tokens.py:70-106), which
  runs before `TIKTOKEN_CACHE_DIR` is touched and adds the digest refusal alongside the
  existing absent/wrong-encoding ones; recorded that `vendored_vocabulary_cache` now hands
  tiktoken `str(path.parent)` of the file it just verified rather than re-deriving the
  constant. Corrected `_CACHE_DIR_LOCK` from `threading.Lock` to `threading.RLock` and
  said why — the guarded region spans a `yield`, so `with vendored_vocabulary_cache(...):
  TiktokenTokenCounter()` re-enters on the same thread and hangs forever on a plain `Lock`.
  Narrowed the `TIKTOKEN_CACHE_DIR` invariant to what the lock actually buys: the variable is
  process-global and a non-participating thread can still observe or clobber it. Re-derived
  every citation — `DEFAULT_TOKEN_COUNTER`, `vendored_vocabulary_path()`, and
  `vendored_vocabulary_cache()` — and rewrote
  the `test_cold_start.py` reference row, which described only two test classes and missed
  `CorruptVendoredVocabularyTests`, the `.gitattributes` name test and the deadlock guard.
  Verified by running the 11 in-process tests of `mcp/tests/test_cold_start.py` (all pass) and
  by re-deriving `sha256(fb374d419588a4632f3f557e76b4b70aebbca790)` =
  `446a9538...1a2d`, equal to `expected_hash` in the installed tiktoken 0.13.0's
  `tiktoken_ext/openai_public.py::o200k_base`. cit:([`test_the_shipped_file_is_the_one_tiktoken_asks_for`], mcp/tests/test_cold_start.py:222-244) Metadata cells untouched.

- 2026-07-31T20:55+02:00 — 260731-EFA-L3 curator: the tokenizer no longer downloads its
  vocabulary. Recorded the vendored `o200k_base` file
  (`package_data/tiktoken/fb374d419588a4632f3f557e76b4b70aebbca790`, named
  `sha1(VENDORED_VOCABULARY_URL)` because that is tiktoken's own cache key), the new
  `vendored_vocabulary_path()` / `vendored_vocabulary_cache()` pair, and
  `TiktokenTokenCounter.__post_init__` loading inside that context so the module-scope
  `DEFAULT_TOKEN_COUNTER` — built while `mcp/tools/base.py` is still importing — reads the
  vocabulary from disk instead of opening an HTTPS connection during server import. Added
  the invariants that only `o200k_base` ships (anything else raises
  `TokenizerVocabularyError`), that `TIKTOKEN_CACHE_DIR` is overridden only for the
  duration of one load under `_CACHE_DIR_LOCK` and then restored, and that the file name
  and its `-text` git attribute are load-bearing. Counts and the reported
  `tiktoken:o200k_base` name are unchanged. Verification metadata pinned until closeout
  stamps the L3 commit.

- 2026-05-30T22:29+02:00: S6 wiring completed — `_tool_payload` now calls the new `finalize_payload_tokens()` so every MCP response carries a real `tokens`/`tokenizer`/`tokenCountExact` instead of the Pydantic defaults; `response_payload`/`dump_with_token_count` were widened to accept any `ResponseModel`. Removed the pre-S6 "placeholder defaults" note and repaired the stale `mcp/tools.py` reference to `mcp/tools/base.py`. Verification metadata stays pinned until closeout commits the source change.
- 2026-05-28T19:52+02:00: Created for the token-accounting model helpers planned for S6 wiring.
