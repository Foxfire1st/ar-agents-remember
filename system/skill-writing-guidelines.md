# Skill and instruction writing guidelines

These rules apply to every text an agent receives as instructions: role files, capsules, digests, operation files, reference and detail files, templates and skill files. They sit beside `coding-guidelines.md` and are reviewed the same way. A text change that breaks one of these rules is a review finding, just like a code change that breaks a coding rule.

## 1. Purpose and reader

Every instruction text has two readers, and both must be able to use it:

- **The agent**, which reads it cold, with nothing but what it was given.
- **The developer**, who must be able to read the file on its own and see what behaviour it asks for.

A text that only one of them can read is a defect. Open each file with one or two sentences saying what it is for and who reads it.

## 2. Where guidance belongs

Put each piece of guidance in exactly one place, chosen by when it is needed:

- **Always-loaded text** (role file, capsule, digest): what every path of the role needs. If an agent would do the wrong thing without it, it belongs here.
- **Detail files**: material needed only on one branch or at one step, such as formats, field lists and longer procedures.
- **Task documents and requirement packets**: facts about one task. They never go into instruction texts.
- **Knowledge records and code comments**: facts about the code. Instruction texts tell the agent how to find them, not what they say.

Do not move a must-have rule into a detail file to save words. Agents often do not open offered files.

Instruction texts name no harness, provider or model. A role's harness and model come from its role settings; a harness's own quirks go on that harness's documentation page.

**Workspace and repository instruction files**

- Guidance that holds for every repository goes into the coordination root's `system/` files: `settings.md`, `tools.md` and `sources.md`.
- Guidance for one repository goes into that repository's memory layer: `system/settings.md` for instructions, `system/settings.json` for storage, path rules and cross-repository policy, `system/tools.md` for commands and checks, `system/sources.md` for documentation and references, `system/coding-guidelines.md` and this file for writing rules, and `system/task-publication.md` for landing and publication. A rule that holds for one repository never goes into a coordination-root file.
- Agents Remember installs no `AGENTS.md` file, in the coordination root or in a memory repository. Harnesses load such files on their own, beside the role instructions, where they drift from them. Instructions reach agents through the role instructions and the homes above.

## 3. Readable structure

- Use headings that say what the section is for. A file longer than about one screen has sections.
- One topic per section, one idea per paragraph. Prefer short paragraphs to long ones.
- Use a numbered list for a real sequence and a bulleted list for real alternatives or sets. Do not turn every sentence into a bullet.
- Name who acts: "The Curator writes…", not "History rows are written…".
- Keep a rule next to its exceptions and its definition.
- Sentences of about 20–25 words are the normal target. A precise sentence may be longer; never cut a condition to make it shorter.

## 4. Words, terms and codes

- Use familiar words, and one term for one concept everywhere.
- Write abbreviations out. A local term the agent must know is defined where it is first used.
- **No ephemeral codes in instruction texts.** Decision numbers (D301), Manager rulings (M9-34), packet lines (v6:358), review finding ids, task and leaf ids, and paths to scratch notes or reports do not survive. They point at text the reader cannot open later. State the rule itself in plain words. Where it came from belongs in the requirement packets, decisions and Git history.
- **Stable internal ids** that link instruction documents to each other may stay, for example a rule id defined in one instruction file and referred to from another. They must:
  - be defined in the instruction corpus itself;
  - resolve to a heading or entry the reader can open;
  - add something for the reader.
  An id that only a build tool uses, such as the unit codes of a digest map, lives in that tool's map, not in the prose the agent and the developer read.
- **Invariant ids** do not belong in instruction texts. They belong in the knowledge and, where useful, in code comments, where an agent can look up the knowledge on demand.

**Present tense, no history**

- Say what the agent does now. Do not describe earlier versions, removed features or past instructions: no "no longer", "used to", "was replaced by", "is retired", "formerly". A fresh agent never saw them, so such passages cost space and can bring the old behaviour back.
- A past behaviour appears only when models keep showing it. Then it is a prohibition with its alternative, for example "Do not copy skills into the project folder; the tool server serves them."
- Instructions do not explain migrations from old to new structures. Old or incompatible memory and settings are migrated to the current structure; instructions describe only the current structure.
- The history of a rule belongs in the requirement packets, the decisions, Git and the memory's invariant history, never in instruction texts.

## 5. Actions and completion

For each thing the agent must do, the text makes these clear: when it applies, what to do, what not to do (with the alternative), what counts as done, and whom to tell. A rule without an observable end ("make sure the memory is good") is not finished.

## 6. Pointers to detail

A pointer names the action it must come before, what the file holds, and where the file is:

> Before you write history rows, read the card detail file (`reference/curator/card-formats-and-citations.md#choose-the-history-disposition`) for the disposition and evidence rules.

- Point at the action ("before you write history rows"), not only a step name ("at Curation workflow 2").
- Write each pointer once, where the action is described.
- Link directly to the file the agent needs, not to a file that points onward to it.
- Say what the file holds in words that name its content; "for the applicable conditions and actions" says nothing.
- When a detail file serves several actions, the pointer links the section for this action.

**When a detail file earns its read**

- Opening a detail file costs the agent a tool call. A file earns that only when it holds more than its pointer costs: a format, a field list, a procedure, or a group of related rules, usually 150 words or more.
- A rule of one or two sentences is written where its action is described, not behind a pointer.
- Rules that the same action or the same few actions need go into one file, reached by one pointer that names that group ("before you start, replace or recover a seat").
- Where a role text describes those actions together, one pointer names the group; where it describes them apart, each action has its own pointer to its section.
- Do not split a file per heading. Split it when it serves actions read at different steps, or when one part is read far more often than the rest.
- Before putting a rule into a text that several roles receive, check that every role that needs it receives that text in its first message. When only the all-role digest reaches them all, a rule of a sentence or two goes into the digest with its roles named; a longer group of rules goes into a small detail file instead of into every role's digest.

**Folders and names**

- Group detail files in folders by subject, like code modules: `reference/<subject>/`, and where a subject has role-specific parts, `<subject>/<role>/` beside `<subject>/shared/`.
- Within a subject that has role folders, a file read by one role goes in that role's folder; a file read by several goes in `<subject>/shared/`.
- A file name says what the file holds, in plain words: `seat-recovery.md`, `closeout-trees.md`. No prefix that repeats the folder (`coord-topic-…`), no decision codes (`-d301`), no catch-all names (`working-rules.md`, `misc.md`, `details.md`).
- A folder holds at least two files; a single file stays in its parent.
- When a file is renamed or moved, every pointer, manifest entry and test follows in the same change.
- After a merge, the file's title and opening line cover everything it holds.

## 7. Rules and examples

- Add a rule when a measured failure shows an ambiguity. Do not add rules for failures nobody has seen.
- Use a short example or counterexample where a distinction is hard to state, for example a sentence that names a log path versus one that claims logs are written.
- Keep necessary prohibitions, and give the allowed alternative beside each one.
- When a new rule is added, check that it does not invite the opposite mistake. Rules that pull in opposite directions caused mirror-image failures in our measurements.
- Prefer removing a rule that no longer earns its place to adding another one.

## 8. One authoritative statement

Each rule is stated once, in its home. Other texts may refer to it, but never copy it. When the rule changes, change it in its home and check every place that refers to it.

## 9. Size

Size is a review signal, not a target. Measure what is actually delivered: the rendered first message with its detail files, not only the source files. A file that grows needs a reason, and so does a file that was shortened. Never compress a text into one block, drop structure, or replace words with codes to meet a number. Budgets are set per file after the text reads well, and the developer decides any case where a file goes over.

## 10. Editing and rereading

- After any edit, and always after a mechanical one (search and replace, generated splits, scripted rewrites), reread the whole affected section in its delivered form.
- Check for duplicated sentences, merged or broken sentences, contradictions, lost conditions, broken links and leftover codes.
- Deterministic checks catch duplicates, links and codes. They do not prove the meaning is right; a reader does.

## 11. Testing

An instruction change is tested by fresh readers who see only what the role receives:

- Does the agent find and read the right file before it acts?
- Does it do the work correctly?
- Does it avoid unwanted work?

Check each of these separately, with realistic cases and at least one case where the rule must not apply. Record the text version, model and results. The author's own session hides gaps and is no test.

## 12. Ownership

Each instruction file has an owner: the task that changes it. A change goes through the normal build, review and curation steps, and the reviewer checks it against these guidelines. A guideline change is decided with the developer.
