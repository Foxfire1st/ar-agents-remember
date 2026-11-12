# Task Publication — the GitHub Issue Surface

Agents Remember stays the authority for task identity, requirements, execution and acceptance. This
repository publishes a view of that work on GitHub, and nothing here writes back: no issue, comment,
label or board change moves an AR stage, requirement, review, landing or acceptance. An agent does the
publishing itself, with the commands below. That is the whole mechanism.

This file is in force only when the resolved memory layer carries it. Absent, nothing is published.

## What a reader sees

A person outside this machine, who can open `Foxfire1st/agents-remember`,
`Foxfire1st/ar-agents-remember` and the issues, and nothing else.

So the agent writes every body itself, in plain prose, from the task and its current requirement — never
copied, never mechanically rendered — and leaves out:

- decision and task numbers, and master or sprint codes;
- local paths and the names of folders, notes, scratch files and reports;
- checksums and commit hashes as text;
- agent IDs;
- review rounds, verdicts and rulings;
- version history and amendment notes;
- any remark that something is local or cannot be opened.

Requirement IDs are the only abbreviations allowed. Figures, dates, ports, commands and product names
stay. An obligation that only concerns local files is described by its effect, not its path.

Links lead only to pages of those two repositories — files, folders, commits, pull requests — or to
issues that exist when the text is written. Another task is named by its issue link once that issue
exists, otherwise by its title.

A task's requirement section is one consolidated text: every obligation of the current requirement in
substance, amendments folded in, superseded wording gone, nothing added, nothing summarised away.

A body stays under 65,536 bytes. Write tighter; never split a body into comments.

## The shape

**The status line**, near the top of every leaf body:

- `in progress`;
- `landed on <date>`, with a link to the merged pull request or the commit of each changed side, and any
  unchanged side named as unchanged;
- `abandoned on <date>`, with one sentence on why.

**A leaf body**: what it does and why; links to its master and its sprint; its requirement IDs; the
status line; what it waits for; then, leaving out any that would be empty — When this task is done,
Requirements (with the ID), Not part of this task, Must not break, If something fails, What the evidence
contains.

**A master**: what it is for; what has been delivered, by theme, in plain sentences with a count; what is
still open, each by link with one line and the order it lands in; every requirement in a folded table
with ID, title and state.

**A sprint**: what it is for; its masters by link; how it ends.

**A summary of a completed master**: what it set out to do, what it delivered, when it ran.

## The hidden marker

The body begins with these lines, copied as they are. GitHub does not show them, and they are the only
hidden content — no title prefix, no body checksum, no part index.

```text
<!-- ar-task: 260928-MIK-L194 -->
<!-- ar-kind: leaf -->
<!-- ar-parent: 260928-MIK -->
<!-- ar-requirement: MIK-R202@v4 source-sha256:<64 hex> -->
```

`ar-parent` is absent only on the sprint issue. One `ar-requirement` line per current requirement.

## Check your own text before you post

Read the title and body against the list above and fix the text. One line finds the usual leaks in a
body file:

```text
grep -nE '/home/|/mnt/|\bD[0-9]{3,}\b|2[0-9]{5}-(MIK|IAS)|\b[0-9a-f]{7,}\b' <body file>
```

Not every hit is a leak — a hex run can be an ordinary word — but each one is looked at, and a real leak
is rewritten in the text. Nothing is published with a hit still in it.

## Labels and the board

Three labels, once per repository, and no status or progress label:

```text
gh label create "kind:sprint" --color 6F42C1 --description "AR sprint" --force --repo Foxfire1st/agents-remember
gh label create "kind:master" --color 0E8A16 --description "AR master" --force --repo Foxfire1st/agents-remember
gh label create "kind:leaf"   --color 1D76DB --description "AR leaf"   --force --repo Foxfire1st/agents-remember
```

One public board, **"Agents Remember tasks"**, with a `Status` field whose options are `Todo`,
`In progress` and `Done`, and a view grouped by `Status`. Adopt the board, its field and its option IDs
from what these answer; never create a second board or a second `Status` field.

```text
gh project list --owner Foxfire1st --format json
gh project field-list <project> --owner Foxfire1st --format json
gh project item-add <project> --owner Foxfire1st --url <issue url> --format json
gh project item-edit --project-id <PVT_…> --id <PVTI_…> --field-id <id> --single-select-option-id <id>
gh project edit <project> --owner Foxfire1st --visibility PUBLIC
```

State lives in the issue's open or closed state, its assignee and the board's `Status` — one place each.

## The steps, in the order the local steps run

Each step below is done in the same turn as the local step it mirrors, and by the same role. One write at
a time; after every write, read it back and compare.

### 1. Registration — the Architect creates the issue

At the moment the task is registered.

**Look before you create.** An issue that already carries the marker is edited; only when none does,
create.

```text
gh issue list --repo Foxfire1st/agents-remember --state all \
  --search '"ar-task: 260928-MIK-L194" in:body' --json number,url,title,state
gh issue create --repo Foxfire1st/agents-remember --title "<plain title>" \
  --body-file <body file> --label "kind:leaf"
```

**Read it back.**

```text
gh issue view <number> --repo Foxfire1st/agents-remember \
  --json number,url,title,body,state,labels,assignees
```

It must carry what you sent: the marker lines, the status line, the labels. A difference is named and the
write redone. The number in the URL is that issue's identity from here on.

**Link it** — the child is named by its database id, not its number — and put it on the board as `Todo`.
A master or sprint issue is linked from its parent and links its children in turn.

```text
gh api repos/Foxfire1st/agents-remember/issues/<child> --jq .id
gh api -X POST repos/Foxfire1st/agents-remember/issues/<parent>/sub_issues -F sub_issue_id=<child id>
```

A parent holds at most 100 direct sub-issues.

**Record the identity.** The issue URL goes into the task document's `references` through
`task_doc set_field`, which replaces the whole list — keep every existing entry. Nothing else is kept
beside the issue itself.

### 2. Start — the Manager assigns the issue and sets In progress

At the moment the leaf starts, before the work begins.

```text
gh issue edit <number> --repo Foxfire1st/agents-remember --add-assignee Foxfire1st
```

Then set the board item's `Status` to `In progress` with the item command above. A start that later fails
leaves the issue at the stage the leaf actually reached, not at the stage that was intended.

### 3. Landing — the Manager lands, updates the status line, closes, sets Done

This is the largest step, because a landing publishes its code and its issue in the same turn. It applies
where the setting below is `pull-request`; the issue part applies to every landing.

`system/settings.json` holds `landing.workflow` at the root: `local`, which is the default and what a
missing key means, or `pull-request`. This repository is `pull-request`. Three letters carry the steps:
**`B`** is that side's master position before the integration, **`H`** the accepted integrated landing
commit, and **`M`** the publication merge whose parents are `B` and `H` in that order and whose tree is
`H`'s.

For each changed side, code then memory, where `H` differs from `B`:

1. **Pin.** `gh api repos/Foxfire1st/<repo>/git/ref/heads/<master>` — the remote tip must equal `B`, and
   `H` must descend from it. A mismatch stops before any write.
2. **Push once.** `git push origin H:refs/heads/land/<slug>`. A refused push stops here: no pull request,
   no issue change.
3. **Open the pull request.**
   `gh pr create --repo Foxfire1st/<repo> --base <master> --head land/<slug> --title "<plain title>" --body-file <body file>`
   — the body says in one or two plain sentences what landed and links the task's issue.
4. **Merge.** `gh pr view <n> --json headRefOid,baseRefOid` must show `H` and `B`, then
   `gh pr merge <n> --merge --admin`. Squash and rebase are refused: the merge must keep both parents.
5. **Read back and pull.** `gh pr view <n> --json mergeCommit,mergedAt`; `M`'s parents must be `B` and
   `H` and its tree `H`'s. Then `git pull --ff-only` on the master branch. `merged: true` alone is not
   the end of a side.
6. **Delete** `land/<slug>`.

Then, in the same turn, the issue:

```text
gh api -X POST repos/Foxfire1st/agents-remember/issues/<number>/comments \
  -F body=@<comment file> --jq '{id, url}'
gh issue edit <number> --repo Foxfire1st/agents-remember --body-file <body file>
gh issue close <number> --repo Foxfire1st/agents-remember --reason completed
```

The comment says what landed and links it; the edit sets the status line to `landed` with its links; the
close comes after both, so the reader's last state is a closed issue whose evidence is already there. Set
the board item to `Done`, and update the master's delivered summary, its count and its open list. A master
closes `completed` when its last leaf lands; a closed leaf or a summary never measures sprint completion
on its own.

**Branch policy.** `main` is pull-request gated: never push to it directly. Ordinary work uses
`feat/<slug>` or `fix/<slug>`; AR work uses the task lines `ar/<task id>`, a leaf in its worktree. Delete
a head branch only when it is finished as a unit of work — a master's line only once that master is
terminal, a super line only once the sprint is.

### 4. Abandonment — the Manager closes the issue as not planned

In the same turn as the abandonment. The status line says `abandoned on <date>` with one sentence; then:

```text
gh issue edit <number> --repo Foxfire1st/agents-remember --body-file <body file>
gh issue close <number> --repo Foxfire1st/agents-remember --reason "not planned"
```

Set the board item to `Done` and take the leaf out of the master's open list. An abandoned leaf keeps its
issue: nothing is deleted, and nothing is republished under the same task.

### When a requirement changes

The Architect rewrites that requirement's section of every issue it governs as one consolidated text, in
the same turn as the approved change. Nothing else on the issue moves.

## Ordinary development, and releases

An ordinary change opens an issue (none for pure research), cuts `feat/<slug>` or `fix/<slug>` from
`main`, works in a worktree, and lands through a pull request with a merge commit — squash only where the
branch's own commits carry no value, never a rebase of pushed history. Nothing is committed before the
explicit approval and the closeout preview. After the merge,
`worktree_record_landing(contract_path=…, landed_code_commit=<the commit the pull request landed>)`
records it: without that call the contract's integration stays `not-started`.

There is no `CHANGELOG.md`; release notes live in GitHub Releases. The canonical tag is `mcp-vX.Y.Z`, and
pushing it runs `publish-mcp-to-pypi.yml`. A release bumps `mcp/pyproject.toml` `version`, the fallback
in `kernel/primitives/version.py`, and the `README.md` Status line, then lands through the pull request,
is tagged on the merge commit, and gets a GitHub Release.

## Recovery

| Situation | What to do |
| --- | --- |
| The create's answer is lost | Look the marker up and edit what is found. Never create twice. |
| The read-back differs | Name the difference, rewrite the text or the file, and write again. |
| A rate-limit answer | Wait as the answer says, then continue one write at a time. |
| A marker or repository mismatch | Stop that write and report the object and the mismatch. |
| A refused push after a landing | Leave the issue open with its last confirmed truth and report the refusal. |

Claiming an issue grants nothing, and a rejection publishes nothing: the issue keeps the last approved
truth.

## Where the bar is

The approved reference leaf issue in this repository's requirement corpus — MIK-R202@v3,
`v3-reference-leaf-issue-example` — is the shape and tone to match. Read it before writing a body; it is
what a Reviewer reads against.
