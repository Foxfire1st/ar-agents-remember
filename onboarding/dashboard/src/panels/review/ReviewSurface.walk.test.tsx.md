# dashboard/src/panels/review/ReviewSurface.walk.test.tsx

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

The walked family tree in the mounted reviewer, on real data (requirement MIK-R39): the tree keeps the rows the reader walked. The bodies are the served answers of the scratch leaf 260928-MIK-L33 (`walkReal.capture-provenance.json`), served through the world of `walk.test-utils.tsx`. `ReviewSurface` is the real component and only `fetch` is stubbed. The file holds 8 `it` blocks, one of them an `it.each` over three values: 10 cases.

Family FAM-R6R095RW has seven changes, the last of them the shared member INV-2TQGXFAX; FAM-2HBJREC2 is the other family of that member.

## Code Commentary

### The cases that pin the keeping

1. **By key.** From FAM-R6R095RW's own row, seven presses of `j` select its seven changes, one review request each. After the seventh the tree shows both families and no kept tag. Press 8 selects FAM-2HBJREC2's own row and opens its family review with one request; the first family stays, marked `data-family-kept`, with 24 member occurrences and one kept tag that names INV-2TQGXFAX. Press 9 makes no request and reports "No later change in this tree; the selection stays." Then `k` selects INV-2TQGXFAX under the first family, six more presses reach INV-2E8MG43K, and one more reports "No earlier change in this tree; the selection stays." Every `k` press makes no review request. The workspace is the same DOM node throughout.
2. **By click.** The shared member is chosen from the list of all invariants, and the tree shows both families with no kept tag. A click on the second family's row makes one review request and leaves the first family in the tree, kept, with 24 members. The visible previous-change control then selects INV-2TQGXFAX under the first family.
3. **The tag, the counts and the reading area.** The kept tag reads "kept · last read for invariant INV-2TQGXFAX" and is the kept family row's accessible description; the selected family's row has no description. The scope line contains "1 families · 1 kept". "Family context details" counts one composed family context. The reading area shows the selected family's review and nothing of the kept family: not its title, not an element carrying its family identifier, and not the word "kept".
4. **Catalogue rows.** Without a kept family the catalogue lists no row for the two families the tree shows. With one it lists a row for both, without a change badge, and the tree and those rows are children of the navigation section itself. Choosing the second family there shows that family alone, with no kept tag and no review request; its catalogue row is then gone again.
5. **The filter.** A filter that matches only the second family hides the kept family and the scope line contains "1/2 families (1 of this subject · 1 kept)"; `k` then reports "No earlier change in this tree". Clearing the filter shows the kept family again with its 24 members and its mark, and `k` selects INV-2TQGXFAX.

### The cases that pin the end message

An end message belongs to the rows the tree showed when it was said (rule 11 of the requirement).

6. **A held answer** (`it.each` over 1, 3 and 5 further presses). The shared member's answer is held back. `j` selects that member while its read is pending, and the further presses of `j` report "No later change in this tree". When the held answer brings the second family and React has made every render it still owed, the status is empty, and the next `j` selects that family's row with one request.
7. **A cleared filter.** With the shared member selected, a filter shows the first family alone and `j` reports "No later change in this tree" with no request. Clearing the filter shows the second family again; the status is empty, and `j` selects that family's row.
8. **The same rows again.** The message is said at the end of the tree. A filter hides the first family and the status is empty; the filter is cleared, the tree shows the same two families again, and the status is still empty. A new `j` is answered with the message again.

### Helpers of this file

- `descriptionOf(node)` computes a node's accessible description through the role query.
- `catalogueRows(view)` lists the subject identifiers of the catalogue rows.

## Evidence

- The file's statement of its data and of what its cases pin. [9]
- By key: seven changes, the second family, the kept first family, the end messages, the way back, and the review requests of each press. [10]
- By click: the first family is kept, and the previous-change control reaches the shared member. [11]
- The tag and its accessible description, the scope line, the context details and the reading area. [12]
- A catalogue row for every family the tree shows while one is kept, and the way back to one family. [13]
- A filter hides kept families with the others and restores them. [14]
- "No later change" is dropped when a held answer brings a later change, after one, three and five further presses. [15]
- "No later change" is dropped when the filter that hid the later family is cleared. [16]
- The message does not come back when the tree shows the same rows again. [17]
- The world and the step helper the cases use. [18]
