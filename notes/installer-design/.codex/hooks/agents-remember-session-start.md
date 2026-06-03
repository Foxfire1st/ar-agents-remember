MANDATORY FIRST ACTION for this workspace

You are not allowed to read, write, or execute code on any repository until you
read `/home/foxfire/Projects/ar-coordination/AGENTS.md` and start its `l-01`
procedure.

Before relying on Agents Remember memory, providers, task files, onboarding, or
repository source, run the startup context packet for the target repository:

```text
context_packet(repo_id="<repo-id>", include_providers=true, include_drift=true)
```

Do not use `include_drift=false` for startup context. That call is for a narrow,
intentional optimization after the full startup state is already known.
