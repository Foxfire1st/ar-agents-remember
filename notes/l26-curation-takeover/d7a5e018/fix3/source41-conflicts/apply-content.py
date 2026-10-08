"""Apply the reviewed exact content plan; verify outside bytes and indexes."""
from pathlib import Path
import hashlib, json, os, stat, subprocess
OUT=Path(__file__).parent
MEM=next(p for p in OUT.parents if p.name=='memory-260928-mik-l26')
CODE=MEM.parent/'260928-mik-l26'
PREFIX=OUT.relative_to(MEM).as_posix()+'/'
def sha(b): return hashlib.sha256(b).hexdigest()
def load(n): return json.loads((OUT/n).read_text())
def save(n,v): (OUT/n).write_text(json.dumps(v,indent=2,sort_keys=True)+'\n')
def git(root,*args): return subprocess.check_output(['git','--no-optional-locks','-C',str(root),*args])
def indices(root):
    p=Path(git(root,'rev-parse','--git-path','index').decode().strip())
    if not p.is_absolute():p=root/p
    return {'raw':sha(p.read_bytes()),'stageNul':sha(git(root,'ls-files','--stage','-z'))}
def physical(root):
    files,dirs_out={},{}
    for base,dirs,names in os.walk(root):
        if Path(base)==root:dirs[:]=[n for n in dirs if n!='.git']
        relbase=Path(base).relative_to(root).as_posix()
        if root==MEM and (relbase+'/'==PREFIX or relbase.startswith(PREFIX)):
            dirs[:]=[];continue
        for name in dirs:
            p=Path(base)/name;rel=p.relative_to(root).as_posix()
            if root==MEM and rel+'/'==PREFIX:continue
            s=p.lstat();dirs_out[rel]={'mode':s.st_mode,'uid':s.st_uid,'gid':s.st_gid,'link':os.readlink(p) if p.is_symlink() else None}
        for name in names:
            p=Path(base)/name;rel=p.relative_to(root).as_posix();s=p.lstat()
            b=os.readlink(p).encode() if p.is_symlink() else p.read_bytes()
            files[rel]={'mode':s.st_mode,'uid':s.st_uid,'gid':s.st_gid,'type':'symlink' if p.is_symlink() else 'file','size':s.st_size,'sha256':sha(b)}
    return {'files':files,'directories':dirs_out}
plans=load('content-plan.json');paths={r['path'] for r in plans}
assert len(plans)==len(paths)==75
before={s:load('before-'+s+'-physical.json') for s in ('code','memory')}
old_indices=load('before-indices.json')
assert {s:indices(r) for s,r in [('code',CODE),('memory',MEM)]}==old_indices
assert physical(CODE)==before['code'] and physical(MEM)==before['memory']
results=[]
for row in plans:
    p=MEM/row['path'];src=CODE/row['source']
    assert src.exists()==row['sourceExists']
    if src.is_file():assert sha(src.read_bytes())==row['sourceSha256']
    if row['action']=='delete':
        assert not src.exists()
        if p.exists():p.unlink()
    else:
        if row['path'].endswith('.json'):
            value=json.loads(row['result']);assert value['schema'] and value['path']
        assert all(marker not in row['result'] for marker in ('<<<<<<<','=======\n','>>>>>>>'))
        p.write_text(row['result'])
    results.append({k:v for k,v in row.items() if k!='result'}|{'resultSha256':sha(p.read_bytes()) if p.exists() else None,'resultSize':p.stat().st_size if p.exists() else None,'resultMode':p.stat().st_mode if p.exists() else None,'resultUid':p.stat().st_uid if p.exists() else None,'resultGid':p.stat().st_gid if p.exists() else None,'beforePhysical':before['memory']['files'].get(row['path'])})
after={s:physical(r) for s,r in [('code',CODE),('memory',MEM)]}
after_indices={s:indices(r) for s,r in [('code',CODE),('memory',MEM)]}
outside=[p for p in before['memory']['files'].keys()|after['memory']['files'].keys() if p not in paths and before['memory']['files'].get(p)!=after['memory']['files'].get(p)]
assert not outside and before['code']==after['code'] and old_indices==after_indices
assert before['memory']['directories']==after['memory']['directories']
for s in after:save('after-'+s+'-physical.json',after[s])
save('after-indices.json',after_indices);save('per-path-resolution.json',results)
proof={'state':'content-resolved-not-staged','advertisedPaths':75,'nativeUnmergedOperandsRetained':181,'retainedPresent':31,'verifiedCurrentSourceAbsentDeletions':44,'outsidePhysicalDifferences':outside,'outsideMemoryFileCount':len(set(before['memory']['files'])-paths),'fullCodePhysicalAndDirectoriesPreserved':True,'outsideMemoryPhysicalAndDirectoryPopulationPreserved':True,'bothRawAndSemanticIndexesPreserved':True,'beforeIndices':old_indices,'afterIndices':after_indices,'noStageRefSyncContinueQAOrKnowledgeIngest':True,'ownEvidencePrefixExplicitlyExcluded':PREFIX,'noOwnedOperationInFlightAfterThisCommand':True,'pendingAnchorWork':'Only after actual paired completion: scoped refresh of retained and incoming accepted-source anchors where current working source differs. No reference-health or READY claim here.','preservedReviewDisposition':'R3 BLOCK remains dated immutable subject; thirteen credited original findings remain accepted and O01 alone rejected. This conflict resolution is not the21 O01 semantic repair or an extra verification.','captureFailuresBeforeAnyCandidateWrite':[{'step':'first metadata read','result':'KeyError rawIndexSha256','correction':'Use actual fullFrames.metadata.rawIndexSHA256/stageNulSHA256 fields.'},{'step':'first code reference lineage walk','result':'KeyError anchor','correction':'Only kind=code targets participate in code-anchor lineage; external/task targets retained unchanged.'},{'step':'incoming skill addition strict current-blob check','result':'AssertionError','correction':'Two named skill references carry accepted incoming anchors; actual working skill preserves retirement meaning at moved lines. Refresh deferred and pending explicitly recorded, no invented fingerprint.'},{'step':'atomic cleanup reference construction','result':'KeyError RLZ-RBHN6V','correction':'Use the exact incoming realizes collection rather than the subsequent proves collection.'}]}
save('resolution-proof.json',proof)
artifacts={p.name:{'sha256':sha(p.read_bytes()),'size':p.stat().st_size} for p in sorted(OUT.iterdir()) if p.is_file() and p.name!='resolution-manifest.json'}
save('resolution-manifest.json',{'state':'content-only-finished','artifacts':artifacts,'perPath':'per-path-resolution.json','proof':'resolution-proof.json'})
print(json.dumps({'state':proof['state'],'paths':75,'present':31,'absent':44,'outsidePhysicalDifferences':len(outside),'indexesUnchanged':old_indices==after_indices,'manifestSha256':sha((OUT/'resolution-manifest.json').read_bytes())}))
