# mcp/src/agents_remember/package_data/runtime/docs/tool-details.md

## Governing Overview

[Nearest governing overview](../../../../../overview.md)

## Purpose

The shipped longer explanations behind the short `server_info` and `runtime_install`
descriptions. The canonical checkout document is `docs/tool-details.md`; this packaged
copy installs under `<coordinationRoot>/docs/`, making the same relative explanation
pointer openable in both layouts. It is documentation, not another callable interface.

## Code Commentary

`server_info` takes no arguments and reports startup-loaded build/configuration, roots,
allowed repositories, unused provider keys and optional role-launched binding metadata.
It does not enumerate tools. Failure to load configuration is a startup refusal, not an
ordinary argument failure of this no-argument read.

`runtime_install` documents preview, optional benchmark fixture copying, retained provider
knobs, and per-call experimental selection. Its `role-capsules` experiment uses request
then environment selection; unknown ids refuse before mutation, and unselected reruns
restore withheld legacy startup targets. The document separates read-only host preview,
absent-host setup information and needed-restart/outside-host remedies.

Provider setup is retired; old enabled keys are unused and only watcher stop remains.
An installer stop failure is reported while installation continues. User data is preserved;
provider-folder deletion belongs to the explicit `providers-remove` CLI, whose failed-stop,
busy-process and escaped-root refusals are different. Managed scaffold refresh/pruning is
not blanket deletion of the preserved memory/provider trees.

## Boundaries

Answer-field lists describe the delivered inline result and its complete report/log
locations; a short inline message sample is not the complete result. A documentation
claim or dictionary fixture is not evidence of a real host/agent turn. Retained knobs
must not be interpreted as permission to restore provider install/index/watch workflows.

## Evidence

- The complete file owns the behavior and limits described above; documentation/tests are not fresh execution evidence. [1]

## External and cross-repository evidence

No Domain Documentation entries are configured in the resolved source registry.
This card claims only the package-local source contract; no external runtime or
cross-repository acceptance evidence is inferred.
