## Installation Order

1. Started from the freshly cloned code repository at `/home/foxfire/Projects/agents-remember`.
2. Created the initial `ar-coordination` structure so the workspace had a coordination root, MCP settings location, provider directories, and memory-repo slot.
3. Removed the auto-generated memory scaffold after confirming the workspace should use the existing memory repository instead.
4. Cloned the existing memory repository `https://github.com/Foxfire1st/ar-agents-remember.git` into `/home/foxfire/Projects/ar-coordination/memory-repos/ar-agents-remember`.
5. Registered the Agents Remember MCP server in `/home/foxfire/.codex/config.toml`.
6. Wrote the MCP runtime settings at `/home/foxfire/.codex/mcp/agents-remember.settings.json`, pointing it at `/home/foxfire/Projects/ar-coordination` and `/home/foxfire/Projects`.
7. Enabled the provider entries in the MCP settings:
   - `codegraphcontext-code`
   - `grepai-memory`
8. Set MCP timeout caps to `toolSeconds = 30` and `providerSeconds = 1800` so longer provider startup or indexing work could finish.
9. Installed and staged provider runtime files under `/home/foxfire/Projects/ar-coordination/providers`.
10. Installed Docker after it was confirmed missing.
11. Started the provider backing services through Docker:
    - `ar-ollama`
    - `ar-cgc-falkordb`
    - `ar-grepai-postgres`
12. Updated the MCP server command to run through `sg docker -c ...` so it can access Docker even before the current login session picks up the Docker group membership.
13. Started the CodeGraphContext watcher for `/home/foxfire/Projects/agents-remember`.
14. Started the GrepAI watcher for the `agents-remember-memory` workspace with the configured provider log directory.
15. Verified the provider containers and watcher processes:
    - CodeGraphContext watcher PID: `21059`
    - GrepAI watcher PID: `22034`
16. Verified the MCP/provider path with `context_packet(repo_id="agents-remember", include_providers=true)`.

## Issues Encountered

1. The first memory bootstrap created a fresh scaffold, but the workspace already had an intended external memory repo. The scaffold had to be removed and replaced with `Foxfire1st/ar-agents-remember.git`.
2. The MCP server was not enough by itself because provider-backed retrieval was configured but the provider runtimes were not installed yet.
3. Docker was initially missing, which blocked the provider containers for Ollama, FalkorDB, and PostgreSQL.
4. After Docker was installed, the current shell still could not access `/var/run/docker.sock` directly because the Docker group membership had not propagated into the active session. Direct `docker ps` returned permission denied, while `sg docker -c "docker ps ..."` worked.
5. The MCP launch command needed the same Docker group workaround, so `/home/foxfire/.codex/config.toml` now launches the MCP server via `/usr/bin/sg docker -c ...`.
6. GrepAI indexing successfully started, but its `--background` startup wrapper gave up after 60 seconds on this machine during the initial scan.
7. GrepAI had to be started as a detached foreground watcher using the same runtime environment, then adopted into provider state with its real PID.
8. GrepAI status can be misleading if checked without the configured `--log-dir`; the plain status command reported it was not running even when the MCP/provider state showed the configured watcher as healthy.
9. Provider startup/indexing is slower than the default short readiness windows, so the MCP settings needed a longer provider timeout cap.
