# docs/guides/providers.md

## Current operative account — MIK-R199

- The page is titled "Providers (Retired)" and opens by stating that Agents Remember "no longer
  ships its two optional context providers", that both are retired, that "no product path installs,
  enables, starts, indexes, or queries them", that "the MCP tools that queried them left the
  surface", and that "the provider lifecycle CLI is gone" (`docs/guides/providers.md:1-8`).
- A table records the retired ids — `codegraphcontext-code` (CGC) for code-relationship search over
  the code repository, and `grepai-memory` (grepai) for semantic-memory search over the memory and
  onboarding — each with state "retired" (`docs/guides/providers.md:10-13`).
- The prose says CGC and grepai answered those questions, "Neither answers anything now", and that
  finding knowledge runs on by-path memory, onboarding notes, and drift checks, with the harness's
  own search tools for source code (`docs/guides/providers.md:15-18`). Durable memory "was never
  theirs" and the providers were "only ever accelerators for *finding* knowledge, never the source
  of truth" (`docs/guides/providers.md:20-22`).
- Under "What remains", the page states that nothing it lists revives a provider, and lists what
  still touches them (`docs/guides/providers.md:24-26`):
  - **Old-install cleanup on explicit request.** `runtime_install` "never deletes provider runtime
    folders"; it "reports the leftover folders with the size of each tree", and deletion "belongs to
    the separate `providers-remove` command", with "nothing is removed unless you run it". The page
    prints both forms, `agents-remember providers-remove --dry-run` and `agents-remember
    providers-remove`. `--dry-run` "reports the folders and their sizes and stops nothing"; without
    it the command "stops the configured watchers first, then removes the provider runtime folders,
    printing each folder's size and the total bytes freed". It "refuses — and removes nothing" when
    its watcher stop fails, when "a live process still holds a folder open (it names the pid and
    command)", or when "the provider root or a deletion target escapes the owned tree". Exit status
    is non-zero on those refusals and `0` "when nothing remained or everything was removed"
    (`docs/guides/providers.md:28-46`).
  - **Old settings keys, reported once.** The settings `providers` block "still parses so an older
    installation keeps loading", but its keys "never count as enabled and drive nothing";
    `runtime_install` "reports them once as unused (`unusedProviderKeys`, mirrored by `server_info`)";
    the block can be removed or omitted for a clean installation (`docs/guides/providers.md:48-53`).
  - **An old watcher, stopped.** `runtime_install` "stops leftover provider watcher processes; that
    stop is its only watcher action", and "A failed stop is recorded in the install result and the
    install continues" (`docs/guides/providers.md:55-57`).
  - **A periodic safety check over leftovers.** The provider-degradation detector "still samples the
    central provider metrics log and writes its state under
    `<coordinationRoot>/logs/observer/providers/`". At `critical`, when the fail-safe is enabled, it
    "can degrade and stop a leftover stack". The page calls it "a safety check, not a revival: it
    starts nothing, and it is not a dashboard provider view — there is no provider panel to read"
    (`docs/guides/providers.md:59-64`). The page does not describe which settings that stop reads.
  - **Unrelated host configuration.** `.paseoRuntime.providers` in the global agentic settings file
    lists the *model* providers (ACP harnesses) the Paseo host launches; it is live configuration
    "with no relationship to the retired search providers, and nothing on this page changes it"
    (`docs/guides/providers.md:66-69`).
- The requirements section scopes its host requirements to leftovers only: Docker "only to
  inspect or clear leftover provider containers from an older installation", and Ollama with
  `nomic-embed-text`, grepai's former embedder run as a Docker container, which "Nothing pulls or
  needs it now" and which "matters only when clearing an old install". It states that nothing
  provider-side "ever started without Docker", that grepai "indexed nothing without Ollama", and
  that the requirements "describe leftover state only" (`docs/guides/providers.md:71-81`).
- "Troubleshooting leftovers" covers old provider keys reported once by `server_info` and the
  install result, leftover watcher processes stopped by `runtime_install` before the runtime tree is
  refreshed with a failed stop recorded, and leftover runtime folders listed by `runtime_install`,
  re-listed by `providers-remove --dry-run`, and deleted by the same command without `--dry-run`,
  which refuses while a live process holds one open or a watcher stop fails
  (`docs/guides/providers.md:83-94`).
- The closing line says memory, onboarding, drift, and task workflows "all work without the retired
  providers" (`docs/guides/providers.md:96-97`).
- The page gives no provider install, enable, prepare, seed, start, index, query, watch,
  provider-status or provider-lane procedure; it carries no settings `providers` JSON example, no
  provider status command, and states there is no provider panel (`docs/guides/providers.md:1-97`).

### Superseded inventory

- Superseded by MIK-R199: "Agents Remember ships two optional context providers. They are opt-in:
  enable them in the MCP settings, and they run as Docker services." Replaced by the retirement
  opening that says the product no longer ships them, no product path installs, enables, starts,
  indexes, or queries them, and the querying tools and lifecycle CLI are gone
  (`docs/guides/providers.md:1-8`).
- Superseded by MIK-R199: the "## Enable" section and its instruction

  > Add the providers you want to the MCP settings `providers` block:

  Replaced by the treatment of that block as retired: it parses, its keys "never count as enabled
  and drive nothing", and the keys are reported once as unused (`docs/guides/providers.md:48-53`).
- Superseded by MIK-R199: "Providers are optional: Agents Remember's memory, onboarding, drift, and
  task workflows all work without them. They add faster code/memory search on top." Replaced by the
  closing statement that those workflows "all work without the retired providers", with no claim of
  added search (`docs/guides/providers.md:96-97`).
- Superseded by MIK-R199: '**"run runtime_install before provider operations"** — the provider
  runner integrity check failed; run `runtime_install()` first.' That troubleshooting entry is gone;
  the section now covers old keys, leftover watcher processes and leftover runtime folders only
  (`docs/guides/providers.md:83-94`).
- Superseded by MIK-R199: the heading "# Providers". Replaced by "# Providers (Retired)"
  (`docs/guides/providers.md:1`).

### Source and authority bounds

- Document read in full: `docs/guides/providers.md:1-97`.
- Changed regions read in the current file: `docs/guides/providers.md:1-26`,
  `docs/guides/providers.md:28-46`, `docs/guides/providers.md:48-64`,
  `docs/guides/providers.md:66-81`, `docs/guides/providers.md:83-97`.
- Superseded wording was read from the supplied diff hunks for this exact path.
- These bounds record what the page states. They supply no build, test, publication, review or
  acceptance claim for the page or the product.

## Evidence

- The page is a retirement account: no product path installs, enables, starts, indexes or queries the providers, and the querying tools and lifecycle CLI are gone. [1]
- CGC and grepai are recorded as retired, with by-path memory, onboarding notes, drift checks and harness search carrying finding now. [2]
- `runtime_install` reports leftover folders and their sizes but never deletes them; `providers-remove` deletes on explicit request, with `--dry-run` stopping nothing and refusals on a failed watcher stop, a live process, or an escape from the owned tree. [3]
- The retired `providers` settings block parses, drives nothing, and its keys are reported once as unused through `unusedProviderKeys` and `server_info`. [4]
- `runtime_install` stops leftover provider watcher processes as its only watcher action and records a failed stop while continuing. [5]
- The degradation detector samples the central provider metrics log and can stop a leftover stack at critical when the fail-safe is enabled; it starts nothing and there is no provider panel. [6]
- `.paseoRuntime.providers` is recorded as unrelated model-provider configuration. [7]
- Docker and Ollama are scoped to inspecting or clearing old installs. [8]
- Troubleshooting covers old keys, leftover watcher processes and leftover runtime folders. [9]
