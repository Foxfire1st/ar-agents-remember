"""Bound content reconciliation of the advertised Source87 memory conflicts only."""
from pathlib import Path
import copy
import ast
import hashlib
import json
import os
import stat
import subprocess

GROUP = Path('/home/firefox/projects/ar-coordination/worktrees/agents-remember/260928-mik-l26-ar')
MEM = GROUP / 'memory-260928-mik-l26'
CODE = GROUP / '260928-mik-l26'
INPUT = GROUP / 'task-reports/role-launch/260928-MIK-L26-worker-391d2ccd-9832-4a74-9f35-e2b884946f2d.source87-sync-20261008/memory-conflicts'
OUT = Path(__file__).parent
PREFIX = OUT.relative_to(MEM).as_posix() + '/'
def sha(b): return hashlib.sha256(b).hexdigest()
def load(p): return json.loads(p.read_text())
def save(n, v): (OUT/n).write_text(json.dumps(v, indent=2, sort_keys=True)+'\n')
def git(root, *args):
    return subprocess.check_output(['git','--no-optional-locks','-C',str(root),*args])
def indices(root):
    ip = Path(git(root,'rev-parse','--git-path','index').decode().strip())
    if not ip.is_absolute(): ip=root/ip
    return {'raw':sha(ip.read_bytes()), 'stageNul':sha(git(root,'ls-files','--stage','-z'))}
def physical(root):
    result={}
    for base, dirs, files in os.walk(root):
        if Path(base)==root: dirs[:]=[d for d in dirs if d!='.git']
        for n in files:
            p=Path(base)/n; rel=p.relative_to(root).as_posix()
            if rel=='.git' or root==MEM and rel.startswith(PREFIX): continue
            s=p.lstat()
            b=os.readlink(p).encode() if p.is_symlink() else p.read_bytes()
            result[rel]={'mode':stat.S_IMODE(s.st_mode),'uid':s.st_uid,'gid':s.st_gid,'size':s.st_size,'sha256':sha(b)}
    return result
def git_blob(p):
    b=p.read_bytes(); return hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
def actual_anchor(anchor, owner):
    p=CODE / anchor.get('path',owner)
    return p.is_file() and git_blob(p)==anchor.get('blob')
def actual_symbol_content(anchor, owner):
    p=CODE/anchor.get('path',owner)
    loc=anchor['locator']
    if not p.is_file() or loc.get('kind')!='symbol': return False
    text=p.read_text(); lines=text.splitlines(True)
    matches=[n for n in ast.walk(ast.parse(text)) if isinstance(n,(ast.FunctionDef,ast.AsyncFunctionDef,ast.ClassDef)) and n.name==loc['name']]
    return len(matches)==1 and 'sha256:'+sha(''.join(lines[matches[0].lineno-1:matches[0].end_lineno]).encode())==anchor.get('content')
manifest=load(INPUT/'manifest.json')
assert sha((INPUT/'manifest.json').read_bytes())=='0d8c368f09268bd3c4adaf27bba7fe18408dab77a26c7cb9b645b7b7f9ed923c'
assert sha((INPUT/'current-source-path-addendum.json').read_bytes())=='396902aee674549b05cb816ed2bd1884406e8bcdf2380d09c47a3848feff52a7'
addendum=load(INPUT/'current-source-path-addendum.json')
source_rows=next(v for v in addendum.values() if isinstance(v,list))
source_map={x['path']:x for x in source_rows}
paths={x['path'] for x in manifest['paths']}
assert len(paths)==67 and sum(len(x['stages']) for x in manifest['paths'])==164
before_index={side:indices(root) for side,root in [('code',CODE),('memory',MEM)]}
for side in before_index:
    assert before_index[side]['raw']==manifest['fullFrames'][side]['rawIndexSha256']
    assert before_index[side]['stageNul']==manifest['fullFrames'][side]['semanticIndexSha256']
before={side:physical(root) for side,root in [('code',CODE),('memory',MEM)]}
for side in before:
    frame=load(INPUT/(side+'-physical-all.json'))
    assert all(before[side].get(p)==fact for p,fact in frame.items()), side+' captured physical drift'
    # The Worker frame enumerates Git-admitted paths (including null deleted
    # operands), while this independent frame also measures ignored cache files.
    # Preserve both; do not misstate the extra files as captured by the Worker.
save('before-indices.json',before_index)
save('before-memory-physical.json',before['memory'])
save('before-code-physical.json',before['code'])
plans=[]
for row in manifest['paths']:
    path=row['path']; stages=row['stages']; owner=source_map[path]['canonicalCurrentSourcePath']
    src=CODE/owner; exists=src.is_file()
    assert exists==source_map[path]['currentLeafSourceExists']
    blobs={}
    for stage, operand in stages.items():
        b=Path(operand['blobFile']).read_bytes()
        assert sha(b)==operand['sha256'] and len(b)==operand['size']
        assert hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==operand['blob']
        blobs[stage]=b
    plan={'path':path,'orientation':manifest['orientation'],'source':owner,'sourceExists':exists,
          'sourceSha256':sha(src.read_bytes()) if exists else None,'changes':[]}
    if '3' not in blobs:
        assert not exists, 'Leaf-absent live source requires individual disposition: '+path
        plan.update(action='delete',result=None,rationale='The preserved leaf retired this source sidecar; the actual current source is absent. Incoming changes refresh evidence for the retired source and do not restore its source or current contract.')
    elif path.endswith('.md'):
        assert path=='onboarding/mcp/tests/test_knowledge_reopen.py.md' and exists
        leaf=blobs['3'].decode()
        paragraph='The same-size, same-second Git rewrite scenario imports the single `rewrite_in_the_second_of_the_index_write` owner from [knowledge_index_test_support.py](knowledge_index_test_support.py.md). Its real clock alignment is the scenario\'s subject; the 120-second alignment guard does not assert scheduler speed. The original captured-tree/currentness assertions remain at this file\'s test owner.'
        assert paragraph in blobs['2'].decode() and paragraph not in leaf
        leaf=leaf.replace('## Evidence',paragraph+'\n\n## Evidence',1)
        leaf+='\n- The shared owner establishes a same-size rewrite in the index-write second. [29]\n'
        plan.update(action='write',result=leaf,rationale='Preserve the repaired compact current test account. Add only the incoming shared rewrite-owner meaning and its evidence, using free reference 29 because leaf reference 25 already cites its reopen assertion.')
    else:
        a,b,c=[json.loads(blobs[n]) for n in ['1','2','3']]
        result=copy.deepcopy(c)
        assert set(a)|set(b)|set(c) <= {'schema','path','references','realizes','proves'}
        assert a['schema']==b['schema']==c['schema'] and a['path']==b['path']==c['path']
        # References have local numbering. Match the exact retained target lineage;
        # never revive a removed citation just because the upstream number exists.
        for number, oldref in a.get('references',{}).items():
            newref=b.get('references',{}).get(number)
            if oldref==newref or newref is None: continue
            assert oldref['note']==newref['note'], (path,number,'changed note')
            for leafnum, leafref in result.get('references',{}).items():
                if leafref['note']!=oldref['note']: continue
                for target in leafref['targets']:
                    matches=[i for i,t in enumerate(oldref['targets']) if t.get('kind')==target.get('kind') and t['anchor'].get('path',owner)==target['anchor'].get('path',owner) and t['anchor'].get('content')==target['anchor'].get('content')]
                    if len(matches)!=1: continue
                    i=matches[0]
                    if i>=len(newref['targets']): continue
                    newtarget=newref['targets'][i]
                    if actual_anchor(newtarget['anchor'],owner):
                        target.clear(); target.update(copy.deepcopy(newtarget))
                        plan['changes'].append({'reference':leafnum,'action':'accepted incoming exact current-file target'})
                    else:
                        plan['changes'].append({'reference':leafnum,'action':'preserved leaf target; incoming whole-file anchor is not the leaf working source; current scoped citation refresh deferred until completed sync'})
        # Exact typed record IDs retain their authored meaning. Only accepted
        # upstream anchor refreshes may replace anchors, never a leaf rationale.
        for kind in ['realizes','proves']:
            aa={x['id']:x for x in a.get(kind,[])}; bb={x['id']:x for x in b.get(kind,[])}
            for rec in result.get(kind,[]):
                rid=rec['id']
                if rid not in aa or rid not in bb or aa[rid]==bb[rid]: continue
                assert {k:v for k,v in aa[rid].items() if k!='anchor'}=={k:v for k,v in bb[rid].items() if k!='anchor'}
                if actual_anchor(bb[rid]['anchor'],owner):
                    rec['anchor']=copy.deepcopy(bb[rid]['anchor'])
                    plan['changes'].append({'record':rid,'action':'incoming current anchor; leaf rationale/facet/origin untouched'})
                else: plan['changes'].append({'record':rid,'action':'leaf authored record retained; anchor refresh awaits completed-current pipeline'})
            new_ids=set(bb)-set(aa)
            assert new_ids <= {'RLZ-69RY4R'}, (path,kind,new_ids)
            for rid in new_ids:
                assert path=='onboarding/mcp/tests/conftest.py.json' and kind=='realizes' and actual_symbol_content(bb[rid]['anchor'],owner)
                assert all(x['id']!=rid for x in result.get(kind,[]))
                result.setdefault(kind,[]).append(copy.deepcopy(bb[rid]))
                plan['changes'].append({'record':rid,'action':'retain incoming L87 pytest shutdown primary authority, including its original origin and rationale; actual symbol content matches, accepted upstream blob remains pending scoped current-leaf refresh'})
        additions={n:r for n,r in b.get('references',{}).items() if n not in a.get('references',{})}
        allowed={'onboarding/mcp/tests/conftest.py.json':{'16','17','18'},'onboarding/mcp/tests/evidence-lifecycle.toml.json':{'96','97','98'},'onboarding/mcp/tests/test-evidence-lanes.toml.json':{'241','242'},'onboarding/mcp/tests/test_knowledge_reopen.py.json':{'25'}}
        assert set(additions)==allowed.get(path,set()), (path,'unexpected incoming reference additions')
        for n,ref in additions.items():
            target_number='29' if path.endswith('/test_knowledge_reopen.py.json') else n
            assert target_number not in result['references']
            result['references'][target_number]=copy.deepcopy(ref)
            plan['changes'].append({'reference':target_number,'action':'retain incoming documented owner evidence, without resurrecting deleted leaf references'})
        plan.update(action='write',result=json.dumps(result,indent=2,sort_keys=True)+'\n',rationale='Preserve the leaf current contract, record dispositions and retained citations; admit incoming exact-current anchor refreshes and separately named L87 owner additions only. Removed canonical records and references remain removed. Any non-current anchor stays explicitly pending current scoped citation repair after sync completion.')
    plans.append(plan)
save('content-plan.json',plans)
print(json.dumps({'planned':len(plans),'write':sum(p['action']=='write' for p in plans),'delete':sum(p['action']=='delete' for p in plans),'noCandidateContentWritten':True}))
