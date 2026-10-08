"""Plan only the 75 returned native memory conflicts; never stage or sync."""
from pathlib import Path
import ast, copy, hashlib, json, os, stat, subprocess

OUT = Path(__file__).parent
MEM = next(p for p in OUT.parents if p.name == 'memory-260928-mik-l26')
GROUP = MEM.parent
CODE = GROUP / '260928-mik-l26'
INPUT = GROUP / 'task-reports/role-launch/260928-MIK-L26-worker-391d2ccd-9832-4a74-9f35-e2b884946f2d.source41-sync-20261008/memory-conflicts'
PREFIX = OUT.relative_to(MEM).as_posix() + '/'
def sha(b): return hashlib.sha256(b).hexdigest()
def load(p): return json.loads(p.read_text())
def save(name, value): (OUT/name).write_text(json.dumps(value, indent=2, sort_keys=True)+'\n')
def git(root, *args): return subprocess.check_output(['git','--no-optional-locks','-C',str(root),*args])
def indices(root):
    p = Path(git(root,'rev-parse','--git-path','index').decode().strip())
    if not p.is_absolute(): p=root/p
    return {'raw':sha(p.read_bytes()), 'stageNul':sha(git(root,'ls-files','--stage','-z'))}
def physical(root):
    files, dirs_out = {}, {}
    for base, dirs, names in os.walk(root):
        if Path(base)==root: dirs[:]=[n for n in dirs if n!='.git']
        relbase=Path(base).relative_to(root).as_posix()
        if root==MEM and (relbase+'/'==PREFIX or relbase.startswith(PREFIX)):
            dirs[:]=[]; continue
        for name in dirs:
            p=Path(base)/name; rel=p.relative_to(root).as_posix()
            if root==MEM and rel+'/'==PREFIX: continue
            s=p.lstat(); dirs_out[rel]={'mode':s.st_mode,'uid':s.st_uid,'gid':s.st_gid,'link':os.readlink(p) if p.is_symlink() else None}
        for name in names:
            p=Path(base)/name; rel=p.relative_to(root).as_posix()
            s=p.lstat(); b=os.readlink(p).encode() if p.is_symlink() else p.read_bytes()
            files[rel]={'mode':s.st_mode,'uid':s.st_uid,'gid':s.st_gid,'type':'symlink' if p.is_symlink() else 'file','size':s.st_size,'sha256':sha(b)}
    return {'files':files,'directories':dirs_out}
def source_path(path):
    s=path.removeprefix('onboarding/').removesuffix('.json').removesuffix('.md')
    if s=='overview': return '.'
    return s.removesuffix('/overview') if s.endswith('/overview') else s
def blob(p):
    b=p.read_bytes(); return hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
def exact_current(anchor, owner):
    p=CODE/anchor.get('path',owner)
    return p.is_file() and blob(p)==anchor.get('blob')
def symbol_current(anchor, owner):
    p=CODE/anchor.get('path',owner); loc=anchor.get('locator',{})
    if not p.is_file() or loc.get('kind')!='symbol': return False
    text=p.read_text(); lines=text.splitlines(True)
    nodes=[n for n in ast.walk(ast.parse(text)) if isinstance(n,(ast.FunctionDef,ast.AsyncFunctionDef,ast.ClassDef)) and n.name==loc['name']]
    return len(nodes)==1 and anchor.get('content')=='sha256:'+sha(''.join(lines[nodes[0].lineno-1:nodes[0].end_lineno]).encode())
def same_target_lineage(a,b,owner):
    if a.get('kind')!='code' or b.get('kind')!='code': return False
    aa,bb=a['anchor'],b['anchor']
    return a['kind']==b['kind'] and aa.get('path',owner)==bb.get('path',owner) and aa.get('content')==bb.get('content') and aa.get('locator')==bb.get('locator')

manifest=load(INPUT/'manifest.json')
assert sha((INPUT/'manifest.json').read_bytes())=='b0ae2c5fc6c10920cd861e667a4d907f3e805ff7dda9ce39e835c95eeb40f08a'
assert len(manifest['paths'])==75 and sum(len(r['stages']) for r in manifest['paths'])==181
before_indices={s:indices(r) for s,r in [('code',CODE),('memory',MEM)]}
for side, frame in manifest['fullFrames'].items():
    assert before_indices[side]['raw']==frame['metadata']['rawIndexSHA256']
    assert before_indices[side]['stageNul']==frame['metadata']['stageNulSHA256']
before={s:physical(r) for s,r in [('code',CODE),('memory',MEM)]}
for side in before:
    captured=load(INPUT/(side+'-physical-all.json'))
    for p,fact in captured.items():
        assert before[side]['files'].get(p)==fact, (side,p,'captured physical drift')
save('before-indices.json',before_indices)
for side in before: save('before-'+side+'-physical.json',before[side])
plans=[]
allowed_additions={'onboarding/mcp/overview.json':{'253'}, 'onboarding/mcp/src/agents_remember/worktrees/overview.json':{'75','76','77','78'}, 'onboarding/overview.json':{'72'}}
atomic='onboarding/mcp/src/agents_remember/kernel/atomic_write.py.json'
for row in manifest['paths']:
    path=row['path']; owner=source_path(path); src=CODE/owner
    blobs={}
    for stage,v in row['stages'].items():
        b=Path(v['blobFile']).read_bytes()
        assert sha(b)==v['sha256'] and len(b)==v['bytes']
        assert hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==v['blob']
        blobs[stage]=b
    plan={'path':path,'orientation':manifest['orientation'],'source':owner,'sourceExists':src.exists(),'sourceSha256':sha(src.read_bytes()) if src.is_file() else None,'changes':[]}
    if '3' not in blobs:
        assert not src.exists(), ('leaf absence is not source absence',path)
        plan.update(action='delete',result=None,rationale='Retain the leaf retirement: this exact current source is absent. Incoming evidence refreshes do not restore the retired source or its sidecar.')
    elif path.endswith('.md'):
        text=blobs['3'].decode()
        if path.endswith('/kernel/atomic_write.py.md'):
            old='`atomic_write_bytes` writes and flushes the sibling temporary file, calls `os.fsync` on its descriptor, then delegates to `atomic_replace`. A failed replacement leaves the previous destination intact and removes the temporary file. After a successful replacement, directory fsync can still fail: the destination has already changed and the source temporary file is gone. This failure window must not be described as rollback. The removed `fsync_file` helper has no current public implementation; file fsync is performed inside the writer.'
            new='`atomic_write_bytes` writes, flushes and fsyncs its unique sibling temporary file, then calls `os.replace` directly. Its failure handler removes that temporary file, and its `finally` block releases the in-process in-flight mark. After replacement it removes only same-target abandoned temporaries whose writers are proven gone, then fsyncs the destination directory. A live or unknown writer keeps its temporary file; an invalid process number is treated as unknown, and Windows skips this cleanup. Cleanup does not promise that every leftover is removable. [9]\n\n`atomic_replace` separately reports rename failure while the destination retains its previous bytes, or directory-fsync failure after the destination has changed and the source is absent. Neither a post-replacement directory-fsync failure nor cleanup is rollback. The removed `fsync_file` helper has no current public implementation; file fsync is performed inside `atomic_write_bytes`.'
            assert old in text
            text=text.replace(old,new)
            text+='\n- The process probe and same-target abandoned-temp cleanup retain live, unknown and unremovable writers. [9]\n'
            plan['changes'].append({'body':'direct replacement and post-publication cleanup','basis':'actual current atomic_write_bytes/_writer_is_gone/_remove_abandoned_temps, plus exact incoming three realization records'})
        plan.update(action='write',result=text,rationale='Keep the compact leaf account rather than reintroducing retired reference prose. Atomic publication alone also incorporates the actual incoming post-publication cleanup/process-probe meaning; the other two cards already exclude the changed historical citation claims.')
    else:
        a,b,c=[json.loads(blobs[s]) for s in ('1','2','3')]; result=copy.deepcopy(c)
        assert set(a)|set(b)|set(c)<= {'schema','path','references','realizes','proves'}
        assert a['schema']==b['schema']==c['schema'] and a['path']==b['path']==c['path']
        for oldnum,oldref in a.get('references',{}).items():
            newref=b.get('references',{}).get(oldnum)
            if newref is None or newref==oldref: continue
            for leafnum,leafref in result.get('references',{}).items():
                if leafref==oldref and all(exact_current(t['anchor'],owner) for t in newref['targets']):
                    result['references'][leafnum]=copy.deepcopy(newref)
                    plan['changes'].append({'reference':leafnum,'action':'incoming exact retained reference successor, including corrected note','incomingNumber':oldnum})
                    continue
                for t in leafref['targets']:
                    matches=[i for i,ot in enumerate(oldref['targets']) if same_target_lineage(t,ot,owner)]
                    if len(matches)!=1: continue
                    i=matches[0]
                    if i>=len(newref['targets']): continue
                    nt=newref['targets'][i]
                    if exact_current(nt['anchor'],owner):
                        t.clear();t.update(copy.deepcopy(nt)); plan['changes'].append({'reference':leafnum,'targetIndex':i,'action':'incoming exact current target; leaf note retained'})
                    else: plan['changes'].append({'reference':leafnum,'targetIndex':i,'action':'leaf target retained; incoming blob differs from actual working source; scoped refresh pending after completion'})
        for kind in ('realizes','proves'):
            aa={v['id']:v for v in a.get(kind,[])}; bb={v['id']:v for v in b.get(kind,[])}
            for rec in result.get(kind,[]):
                rid=rec['id']
                if rid not in aa or rid not in bb or aa[rid]==bb[rid]: continue
                assert {k:v for k,v in aa[rid].items() if k!='anchor'}=={k:v for k,v in bb[rid].items() if k!='anchor'}
                if exact_current(bb[rid]['anchor'],owner):
                    rec['anchor']=copy.deepcopy(bb[rid]['anchor']);plan['changes'].append({'record':rid,'action':'incoming current anchor; leaf rationale/origin/facet preserved'})
            additions=set(bb)-set(aa)
            assert additions==({'RLZ-RBHN6V','RLZ-S9Z4DX','RLZ-YW24RV'} if path==atomic and kind=='realizes' else set())
            for rid in sorted(additions):
                assert exact_current(bb[rid]['anchor'],owner) or symbol_current(bb[rid]['anchor'],owner)
                assert all(v['id']!=rid for v in result.get(kind,[]))
                result.setdefault(kind,[]).append(copy.deepcopy(bb[rid]))
                plan['changes'].append({'record':rid,'action':'retain exact incoming L41 process-probe/cleanup realization with its own original rationale/origin; matching actual symbol content'})
        added=set(b.get('references',{}))-set(a.get('references',{}))
        assert added==allowed_additions.get(path,set()), (path,'unexpected new reference',added)
        for n in sorted(added,key=int):
            assert n not in result['references']
            matches=all(exact_current(t['anchor'],owner) for t in b['references'][n]['targets'])
            if not matches:
                assert (path,n) in {('onboarding/mcp/overview.json','253'),('onboarding/overview.json','72')}
                skill=(CODE/'mcp/src/agents_remember/package_data/runtime/skills/c-12-closeout/SKILL.md').read_text()
                assert 'Finalizing a master never archives it' in skill and '`retire_master` is the one operation that archives a master' in skill
            result['references'][n]=copy.deepcopy(b['references'][n]);plan['changes'].append({'reference':n,'action':'retain exact incoming master-retirement evidence at free leaf number; current whole-file anchor matched' if matches else 'retain incoming master-retirement skill meaning and original accepted-source anchor; actual working skill has same meaning but line positions/blob differ, so scoped citation refresh remains pending after paired completion'})
        if path==atomic:
            assert '9' not in result['references']
            bb={v['id']:v for v in b['realizes']}
            result['references']['9']={'note':'The process probe and same-target abandoned-temp cleanup retain live, unknown and unremovable writers.','targets':[{'kind':'code','anchor':copy.deepcopy(bb[rid]['anchor'])} for rid in ('RLZ-RBHN6V','RLZ-YW24RV')]}
            plan['changes'].append({'reference':'9','action':'carry the two exact incoming cleanup-owner anchors for the merged current card; no invented record'})
        plan.update(action='write',result=json.dumps(result,indent=2,sort_keys=True)+'\n',rationale='Keep the preserved leaf schema/current contract, exact typed records and retained reference lineage. Admit only identified incoming current targets, the exact L41 cleanup realizations and explicit retirement-guard evidence additions. References absent from leaf remain retired; numbering or directory similarity never creates a semantic union. Nonmatching current anchors remain pending scoped refresh after actual paired completion.')
    plans.append(plan)
save('content-plan.json',plans)
print(json.dumps({'state':'planned-no-candidate-write','paths':len(plans),'writes':sum(p['action']=='write' for p in plans),'sourceQualifiedDeletions':sum(p['action']=='delete' for p in plans),'changes':sum(len(p['changes']) for p in plans)}))
