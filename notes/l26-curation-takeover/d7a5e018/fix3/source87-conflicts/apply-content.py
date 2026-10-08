from pathlib import Path
import hashlib
import json
import os
import stat
import subprocess
OUT=Path(__file__).parent
GROUP=OUT.parents[6]
# Resolve the roots from this helper's fixed selected memory root, not ambient cwd.
MEM=next(p for p in OUT.parents if p.name=='memory-260928-mik-l26')
GROUP=MEM.parent
CODE=GROUP/'260928-mik-l26'
PREFIX=OUT.relative_to(MEM).as_posix()+'/'
def sha(b): return hashlib.sha256(b).hexdigest()
def load(n): return json.loads((OUT/n).read_text())
def save(n,v): (OUT/n).write_text(json.dumps(v,indent=2,sort_keys=True)+'\n')
def git(root,*args): return subprocess.check_output(['git','--no-optional-locks','-C',str(root),*args])
def indices(root):
    p=Path(git(root,'rev-parse','--git-path','index').decode().strip())
    if not p.is_absolute(): p=root/p
    return {'raw':sha(p.read_bytes()),'stageNul':sha(git(root,'ls-files','--stage','-z'))}
def physical(root):
    result={}
    for base,dirs,files in os.walk(root):
        if Path(base)==root: dirs[:]=[d for d in dirs if d!='.git']
        for n in files:
            p=Path(base)/n; rel=p.relative_to(root).as_posix()
            if rel=='.git' or root==MEM and rel.startswith(PREFIX): continue
            s=p.lstat(); b=os.readlink(p).encode() if p.is_symlink() else p.read_bytes()
            result[rel]={'mode':stat.S_IMODE(s.st_mode),'uid':s.st_uid,'gid':s.st_gid,'size':s.st_size,'sha256':sha(b)}
    return result
plan=load('content-plan.json'); paths={r['path'] for r in plan}
assert len(paths)==67
oldindices=load('before-indices.json')
before={s:load('before-'+s+'-physical.json') for s in ['code','memory']}
assert {s:indices(r) for s,r in [('code',CODE),('memory',MEM)]}==oldindices
assert physical(CODE)==before['code'] and physical(MEM)==before['memory']
results=[]
for row in plan:
    p=MEM/row['path']; src=CODE/row['source']
    assert src.is_file()==row['sourceExists']
    if src.is_file(): assert sha(src.read_bytes())==row['sourceSha256']
    if row['action']=='delete':
        assert not src.exists()
        if p.exists(): p.unlink()
    else:
        if row['path'].endswith('.json'): json.loads(row['result'])
        p.write_text(row['result'])
    results.append({k:v for k,v in row.items() if k!='result'} | {'resultSha256':sha(p.read_bytes()) if p.exists() else None,'resultSize':p.stat().st_size if p.exists() else None,'resultMode':stat.S_IMODE(p.stat().st_mode) if p.exists() else None,'beforePhysical':before['memory'].get(row['path'])})
after={s:physical(r) for s,r in [('code',CODE),('memory',MEM)]}
afterindices={s:indices(r) for s,r in [('code',CODE),('memory',MEM)]}
outside=[p for p in before['memory'].keys()|after['memory'].keys() if p not in paths and before['memory'].get(p)!=after['memory'].get(p)]
assert not outside and after['code']==before['code'] and afterindices==oldindices
for side,frame in after.items(): save('after-'+side+'-physical.json',frame)
save('after-indices.json',afterindices)
save('per-path-resolution.json',results)
report={'state':'content-resolved-not-staged','advertisedPaths':67,'nativeUnmergedOperandsRetained':164,'retainedPresent':30,'verifiedCurrentSourceAbsentDeletions':37,'outsidePhysicalDifferences':outside,'outsideMemoryPathCount':len(set(before['memory'])-paths),'fullCodePhysicalPreserved':True,'bothRawAndSemanticIndexesPreserved':True,'beforeIndices':oldindices,'afterIndices':afterindices,'noStageRefSyncContinueQAOrKnowledgeIngest':True,'sourceOrderingException':'test_knowledge_reopen.py source is present; its current leaf card remains and receives incoming helper evidence, not retirement','pendingAnchorWork':'Retained leaf anchors and incoming accepted-source additions require supported scoped citation/current-quality reconciliation only after actual public sync completion; this content result claims no READY or reference-health pass.','ignoredPhysicalCoverage':'Worker Git-admitted captured physical facts checked; independent before/after frame additionally preserves ignored physical files. Own evidence prefix is explicitly excluded.','ownEvidencePrefix':PREFIX,'noOwnedProcessInFlightAfterThisCommand':True,'captureFailures':[{'step':'initial independent all-physical equality','result':'AssertionError: code physical drift','explanation':'Worker frame enumerates Git-admitted paths/null deletions, whereas independent traversal also measured ignored cache files; each actual captured Worker fact subsequently matched exactly. No candidate content written.'},{'step':'first plan new L87 record whole-file-anchor check','result':'AssertionError at new RLZ-69RY4R anchor admission','explanation':'Leaf working file differs from upstream whole-file blob, while exact pytest_unconfigure symbol content matches incoming SHA4b6630a8. New record preserves original incoming anchor for post-completion citation refresh. No candidate content written.'}]}
save('resolution-proof.json',report)
manifest={p.name:{'sha256':sha(p.read_bytes()),'size':p.stat().st_size} for p in sorted(OUT.iterdir()) if p.is_file() and p.name!='resolution-manifest.json'}
save('resolution-manifest.json',{'state':'content-only-finished','artifacts':manifest,'perPath':'per-path-resolution.json','proof':'resolution-proof.json'})
print(json.dumps({'state':report['state'],'paths':67,'present':30,'absent':37,'outsidePhysicalDifferences':len(outside),'indexesUnchanged':afterindices==oldindices,'manifestSha256':sha((OUT/'resolution-manifest.json').read_bytes())}))
