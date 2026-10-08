import ast,json,re
from pathlib import Path
root=Path('/home/firefox/projects/ar-coordination/worktrees/agents-remember/260928-mik-l26-ar'); mem=root/'memory-260928-mik-l26';out=mem/'notes/l26-curation-takeover/d7a5e018/fix3';p=out/'O01-sealed84-authored-plan.json';a=json.loads(p.read_text())
changes={
35:[('(`AnchorResolutionState`, mirrored as the runtime tuple `ANCHOR_RESOLUTIONS`)','(`AnchorResolutionState`, declared as a literal type)')],
40:[('while `bind_expected_output_tree` fills an unbound prepared output before commit launch.','and `begin_git_mutation` receives the exact intended output tree before commit launch. The removed late-binding helper does not fill an unbound output.')],
41:[('- `crossing_applies(repository, base, own, incoming)` probes the three layout markers\n  (`knowledge_validation.has_layout_marker`). A probe failure is refused at step `markers`.\n  `merge_base` resolves the base.','- `merge_structure(repository, base, own, incoming)` classifies the actual three marker-bearing trees and selects structural merge or the crossing plan. `merge_base` resolves the base; a failed marker read remains a refusal rather than a guessed format.')],
42:[('`WorktreeArgs` carries normalized closeout input, actual landed code/memory facts, and the one authored knowledge decision a reconcile call may carry.','`WorktreeArgs` carries normalized closeout input and actual landed code/memory facts; no canonical knowledge-reconciliation decision is carried.')],
45:[('`commit_verified_staged` operates on the already prepared index, removes explicitly excluded\nentries, checks the staged diff, and commits with `--no-verify` without restaging. Neither helper\ncreates a commit for cache-only dirt. Hook execution remains a separate explicit helper.','`publish_tree_commit` publishes the admitted exact tree through `commit-tree` and an expected-old branch update. It settles the message before the per-worktree publication lock, refuses an unfinished Git action or a moved/detached admitted ref, stages the supplied tree, runs the supplied confirmation, then writes and publishes the object. A failure gives the index back only while it still holds this call\'s staged state. Assume-unchanged, skip-worktree and intent-to-add facts are preserved. This primitive runs no Git commit hook; the reference-transaction hook still runs and its refusal retains Git\'s diagnostic. Prepared closeout hook policies are separate and are not changed here.'),('Verified-index commit does not pull in later working-tree changes or rerun hooks.','Exact-tree publication does not pull in later working-tree changes. Its hook behavior is separate from prepared closeout policy.')],
57:[('`open_leaf_owners`','`_open_histories`')],
60:[('- `RenameInferenceSources` carries the two trees and the probe together; `no_rename_inference` is the\n  probe for a caller that must run no Git command.','- `RenameInferenceSources` carries the two exact trees and an optional probe. `_inference_for` reports the absence of a measurement when the probe is absent; it does not run a substitute Git command. The former `no_rename_inference` factory is removed.')],
69:[('- **The key.** `planned_subject(subject, effect)` builds it; `parse_planned_subject` returns the\n  `(subject, effect)` pair or `None`.','- **The key.** `planned_subject(subject, effect)` builds it; `PLANNED_SUBJECT_PATTERN` declares its subject/effect grammar. This module has no `parse_planned_subject` function; history-model validation owns parsing.')],
76:[('  - `test_a_tree_projection_carries_every_row_of_a_view`: a view of more than 64 rows is projected whole on a tree (carried 2026-09-29 19:56:40 Q7; ruling 23:21:57).\n','')]
}
symbols={35:['AnchorResolution'],40:['begin_git_mutation','prove_git_commit','reconcile_closeout_mutations'],41:['merge_structure','crossing_plan','apply_crossing'],42:['WorktreeArgs'],43:['_commit_memory_content','_restore_preparations','_refuse_ungated_memory','require_gated_recovery'],45:['worktree_candidate_tree','stage_tree','publish_tree_commit','_move_admitted_ref'],57:['_open_histories','_source','direct_verdict'],60:['with_rename_inferences','_inference_for','git_rename_inference'],69:['planned_subject','planned_item_open'],76:['test_identity_seeds_on_a_tree_keep_the_scope_read_beside_the_leaf','test_a_path_selects_one_family_hop_in_the_declared_order','test_a_tail_longer_than_one_queue_is_refused_by_name_within_the_threshold']}
for r in a['rows']:
 n=r['ordinal']
 if n not in symbols:continue
 old=(mem/r['card']).read_text(); text=old
 for before,after in changes.get(n,[]):
  assert before in text,(n,before)
  text=text.replace(before,after)
 if n==43:text=text.replace('`_restore_ignore_file`','`_restore_preparations`')
 # Replace the evidence projection of the removed names with the actual retained owner boundaries.
 text=text.split('## Evidence')[0].rstrip()+'\n\n## Evidence\n\n### Repo-Internal References\n\n| Finding | Anchor | Source |\n| --- | --- | --- |\n'
 defs={x.name:x for x in ast.parse((root/'260928-mik-l26'/r['sourcePath']).read_text()).body if isinstance(x,(ast.ClassDef,ast.FunctionDef))}
 for s in symbols[n]:
  x=defs[s];text+=f'| `{s}` implements the retained boundary described above. | `{s}` | {r["sourcePath"]}:{x.lineno}-{x.end_lineno} |\n'
 r['replacement']=text;r['action']='named-owner-and-evidence-correction';r['basis']='The existing contract is retained; its removed construct or stale evidence claim is replaced by the actual current owner. The old account remains in the reviewed Git before-half.'
p.write_text(json.dumps(a,indent=2)+'\n');print('84 rows,',sum(x['replacement'] is not None for x in a['rows']),'changed plans')
