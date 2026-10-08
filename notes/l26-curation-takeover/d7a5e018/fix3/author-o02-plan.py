import ast,json,re,hashlib
from pathlib import Path
root=Path('/home/firefox/projects/ar-coordination/worktrees/agents-remember/260928-mik-l26-ar');mem=root/'memory-260928-mik-l26';out=mem/'notes/l26-curation-takeover/d7a5e018/fix3'
repairs={
'onboarding/mcp/src/agents_remember/application/knowledge_views.py.md':[
('4','The derived-index seam checks ordering, namespace and continuation binding before reading rows and returns a typed refusal.', [('mcp/src/agents_remember/application/knowledge_views.py','_admit'),('mcp/src/agents_remember/application/knowledge_views.py','_refused')]),
('15','The former projection writer and MCP seam call were retired. The current public knowledge tool reads a converted tree through read_tree_page, rather than calling read_knowledge_view.', [('mcp/src/agents_remember/mcp/tools/knowledge.py','knowledge_read_payload'),('mcp/src/agents_remember/mcp/tools/knowledge.py','_read_result')])],
'onboarding/mcp/src/agents_remember/application/review_final_output_receipt.py.md':[
('29','The published-intent resolver selects the converted memory tree and its derived index; a legacy root refuses rather than supplying a canonical published dataset.', [('mcp/src/agents_remember/application/published_intent.py','resolve_published_intent')])],
'onboarding/mcp/src/agents_remember/models/knowledge/view.py.md':[
('11','Ordering admits only the four declared inputs; the request validator refuses other spellings and order_candidates raises its named error rather than choosing a fallback.', [('mcp/src/agents_remember/models/knowledge/view.py','require_admitted_ordering_input'),('mcp/src/agents_remember/application/knowledge_view_render.py','order_candidates')])]
}
plans=[]
for path,rs in repairs.items():
 old=(mem/path).read_text();new=old
 for n,finding,targets in rs:
  hits=[line for line in new.splitlines() if line.rstrip().endswith('['+n+']')];assert len(hits)==1,(path,n,hits)
  sources=[];symbols=[]
  for source,symbol in targets:
   defs={x.name:x for x in ast.parse((root/'260928-mik-l26'/source).read_text()).body if isinstance(x,(ast.FunctionDef,ast.ClassDef))};x=defs[symbol];sources.append(f'{source}:{x.lineno}-{x.end_lineno}');symbols.append('`'+symbol+'`')
  table='| Finding | Anchor | Source |\n| --- | --- | --- |\n| '+finding+' ['+n+'] | '+'; '.join(symbols)+' | '+'; '.join(sources)+' |'
  new=new.replace(hits[0], '\n'+table+'\n')
 if path.endswith('/knowledge_views.py.md'):
  start=new.index('Every claim on this card');end=new.index('\n- The seam',start)
  new=new[:start]+'The current seam, derived-index reader and typed cursor models establish the boundaries below. The public converted-tree tool is a separate entry path; the former projection writer is retired.\n'+new[end:]
 plans.append({'card':path,'beforeSHA256':hashlib.sha256(old.encode()).hexdigest(),'replacement':new,'repairedReferences':[r[0] for r in rs]})
(out/'O02-original27-authored-plan.json').write_text(json.dumps({'schema':'l26-o02-original27-authoring-plan/v1','rows':plans},indent=2)+'\n');print('3 cards/4 original references; six stale code legs and retired-caller rationale replaced')
