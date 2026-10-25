# mcp/src/agents_remember/models/tools/tool_descriptions.py

## Governing Overview

[Response contract models](../overview.md)

## Purpose

States the character ceilings and the transition ownership used by the registered-tool description checks. It is declaration data, not a runtime answer shaper or a source of permission to call a tool.

## Code Commentary

A normal registered-tool description is bounded to 600 characters and an argument's schema description to 120 characters. The calling agent's longer explanation belongs in an openable skill or reference, rather than in an answer example, refusal catalogue or argument-description overflow.

Description ownership and answer ownership are related but distinct. The current map has no L109 entries: context_packet, read_ar_files, knowledge_read and knowledge_diff have final candidate answer rows and ordinary description bounds; resolve_context is removed, not retained as an interim reader. The interim-owner map records which later reader, memory or task/landing leaf rewrites a retained tool; checks use the answer table's interim marking when available. A finalized answer row subjects its description to the ordinary bound without changing the test. R113 removed `dispatch_agent` and its description-length pin; neither is a surviving exception. The retained interim-owner declaration is transition data, not a promise that removed tools remain registered.

Do not turn the declaration's transition map into a current roster, infer that a listed tool is registered, or claim that every description in an arbitrary build already meets the ordinary ceiling. The roster, actual registration and table-derived test decide those facts.

## Evidence

- The module declares ordinary description and argument-description ceilings of 600 and 120 characters. [1]

- Historical A7 interim ownership declaration contains retained reader/memory/task tools, not a dispatch_agent length exception. [4]


## Preserved incoming L109 source witness

The incoming source witness below is retained at its original epoch; its complete anchor is not a post-composition currency claim. Current declaration bounds, finalized reader ownership and R113's removed dispatch pin are stated above.


- Historical incoming L109 declaration account: Current candidate source supports the operative account; historical sections grant no current tool or execution acceptance. [3]
