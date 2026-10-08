# scripts/test-under-load.sh

## Governing Overview

[Scripts overview](overview.md)

## Purpose

Executes a named command on one allowed CPU core shared with ten owned CPU burners, then reports
run-level passes and failures. This is load-independence evidence, not a performance benchmark,
certification or task-acceptance owner.

## Code Commentary

The runner chooses the minimum core in the process's allowed affinity set and pins both burners and
command to it. `AR_LOAD_RUNS` accepts exactly one run for a scheduled full population or three runs
for named checks, defaulting to three. Every burner must be alive before the command runs. Command
failures are counted while remaining runs continue; any failed run makes the script fail. EXIT cleanup
kills and reaps all tracked burner children, including INT/TERM exit paths. No elapsed-time threshold
or machine-wide setting is changed.

## Evidence

Its results apply only to the command population actually invoked; native skips and unrun scheduled
populations retain their own evidence status.


- Only one or three runs are admitted. [1]
- EXIT cleanup kills and reaps the owned burner processes. [2]
- The command shares the burners' allowed core and failures determine the final status. [3]
