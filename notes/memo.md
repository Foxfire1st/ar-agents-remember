1. A in-memory task option so a memory repo can be used to hold tasks in a task folder
   instead of using only the coordinator tasks.
2. Cron job scheduler inside the mcp
3. Based on the scheduler create a memory defragmentation job that runs in certain intervals. The job shall be picked up by agents from a certain task folder that is dedicated for system operations. The job will be responsible for improving memory integrity. It shall be able to do simple fixes like checking and repairing link integrity, making sure the files adhere to defined formats etc. But there shall also be looked out for inconsistencies and contradictions against code and official documentation. These inconsistencies are sampled into a report as they should not be automatically fixed but rather need discussion with the dev before action is taken.
4. memory defragmentation should also look for signs of slop in the code. The test can simply look for "legacy" and "fallback" implementations that are not explicitly documented as agreed upon with the developer within the onboardings. These findings need to appear in the report as well.
5. maybe integrate slop detector tooling like: https://github.com/flamehaven01/ai-slop-detector
6. Guided memory-repo scaffolding should take example files so users have code quality and other things setup for them.
7. Convert tool reponses at the emitting boundary from json into toon output for the model. However existing tests should continue consuming json. The conversion should be done via a dependency that can do that automatically for any json input and output that to toon.

Pylint
too-many-branches
too-many-statements
too-many-locals
too-many-arguments
too-many-public-methods
duplicate-code
unused-argument
broad-exception-caught
fixme

complexipy: cognitive complexity
uv run complexipy src --max-complexity-allowed 10 --top 20 --plain

Vulture: dead code finder
uv run vulture src tests --sort-by-size --min-confidence 80

jscpd: duplication detector
npx jscpd --reporters ai src

Import Linter: architecture drift
uv run lint-imports

deptry: dependency slop
uv run deptry .

Semgrep / Bandit / CodeQL: security-shaped slop
uv run bandit -r src
uvx semgrep scan --config auto

## recommended stack for agents-remember-md

### Hard gate immediately

uv run ruff check .
uv run ruff format --check .
uv run deptry .
uv run xenon --max-absolute B --max-modules A --max-average A src

### Advisory report initially

uv run pylint src
uv run radon cc src -s -a
uv run radon mi src -s
uv run complexipy src --top 20 --plain
uv run vulture src tests --sort-by-size --min-confidence 80
npx jscpd --reporters ai src
uvx ai-slop-detector --project . --json --output reports/ai-slop.json

### Add once architecture settles

uv run lint-imports
uv run bandit -r src
uvx semgrep scan --config auto

### Integration Shape

Slop Gate
├─ Complexity
│ ├─ CRAP
│ ├─ Radon / Xenon
│ └─ complexipy
├─ Bloat
│ ├─ file length
│ ├─ function length
│ └─ parameter count
├─ Duplication
│ └─ jscpd
├─ Dead / Orphaned Code
│ ├─ Vulture
│ └─ coverage hints
├─ Dependency Hygiene
│ └─ deptry
├─ Architecture
│ └─ Import Linter
└─ AI-Specific Signals
├─ AI-SLOP Detector
└─ custom Semgrep rules

| Category           | Example                                                 | Tooling                                          |
| ------------------ | ------------------------------------------------------- | ------------------------------------------------ |
| Complexity risk    | 80-line function with nested branches                   | CRAP, Radon, Xenon, complexipy                   |
| Size bloat         | 4,000-line file keeps growing                           | custom file/function size scanner, Pylint        |
| Duplication        | same parsing logic copied into 3 modules                | jscpd, Pylint duplicate-code                     |
| Dead code          | helper created but never called                         | Vulture                                          |
| Fake completeness  | `TODO`, `pass`, placeholder adapters, unused parameters | Ruff, Pylint, custom Semgrep                     |
| Dependency mess    | imports package not declared, unused deps               | deptry                                           |
| Architecture drift | CLI layer importing internals it should not             | Import Linter                                    |
| Test theater       | test exists but asserts almost nothing                  | coverage + mutation testing                      |
| Over-abstraction   | interfaces/factories for one implementation             | harder; needs custom heuristics + review prompts |

### What signals every code repo should emit to ensure code quality and maintainability?

Code Risk Scanner
├─ CRAP risk
├─ complexity risk
├─ file/function bloat
├─ duplication risk
├─ dead-code risk
├─ dependency hygiene
├─ architecture-boundary violations
├─ placeholder/fake-completeness signals
└─ test-quality suspicion

=> SKILL: A bootstrap skill that walks users through identifying the right suite of code quality and maintainability tools and helps them set up those tools for their individual code repositories. These tools should allow individual testing as well as a combined script that runs the whole suite of checks and compiles a report. The suite can be run once an implementation is about to be checked in.
