"""Read the public-owner candidate trees and native state; never create a tree or stage."""
from pathlib import Path
import hashlib, json, os, subprocess, datetime
BASE=Path('/home/firefox/projects/ar-coordination/worktrees/agents-remember/260928-mik-l26-ar')
TASK=Path('/home/firefox/projects/ar-coordination/tasks/agents-remember/260928_maintained-invariant-knowledge')
OUT=BASE/'task-reports/role-launch/260928-MIK-L26-curator-d7a5e018-b7ac-441b-86b0-e147b890d32c.source87-final-native-readback.json'
ENV=dict(os.environ,GIT_OPTIONAL_LOCKS='0')
def git(root,*args):
    return subprocess.check_output(['git',*args],cwd=root,env=ENV)
def sha(data):return hashlib.sha256(data).hexdigest()
def index(root):
    p=Path(git(root,'rev-parse','--git-path','index').decode().strip())
    if not p.is_absolute():p=root/p
    return {'rawSHA256':sha(p.read_bytes()),'semanticNulSHA256':sha(git(root,'ls-files','--stage','-z')),'unmerged':git(root,'ls-files','-u','-z').decode()}
manifest=json.loads((TASK/'notes/reports/260928-MIK-L26-curator-coherence.json').read_text())
record=json.loads((TASK/manifest['recordPath']).read_text())
result={'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'recordDigest':manifest['currentRecordDigest'],'codeTree':record['codeCandidateTree'],'memoryTree':record['memoryCandidateTree'],'surfaces':{}}
for key,name,tree in [('code','260928-mik-l26',result['codeTree']),('memory','memory-260928-mik-l26',result['memoryTree'])]:
    root=BASE/name;before=index(root);tracked=git(root,'diff','--name-only','-z','HEAD').decode().split('\0');tracked=[p for p in tracked if p];others=[p for p in git(root,'ls-files','--others','--exclude-standard','-z').decode().split('\0') if p]
    states=[]
    for p in sorted(set(tracked+others)):
        target=root/p
        if not target.exists() and not target.is_symlink():states.append({'path':p,'presence':'absent'});continue
        s=target.lstat();data=os.readlink(target).encode() if target.is_symlink() else target.read_bytes();states.append({'path':p,'presence':'present','sha256':sha(data),'size':s.st_size,'mode':s.st_mode,'uid':s.st_uid,'gid':s.st_gid,'symlink':target.is_symlink()})
    tree_entries={}
    for row in git(root,'ls-tree','-r','-z',tree).split(b'\0'):
        if not row:continue
        left,path=row.split(b'\t',1);mode,kind,blob=left.decode().split();tree_entries[path.decode()]={'mode':mode,'kind':kind,'blob':blob}
    # Match every changed/untracked endpoint to its already owner-created tree object.
    mismatches=[]
    for s in states:
        p=s['path'];entry=tree_entries.get(p)
        if s['presence']=='absent':
            if entry is not None:mismatches.append({'path':p,'reason':'deleted path remains in candidate'})
        else:
            target=root/p;data=os.readlink(target).encode() if target.is_symlink() else target.read_bytes();blob=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest();mode='120000' if target.is_symlink() else '100755' if s['mode']&0o111 else '100644'
            if not entry or entry['blob']!=blob or entry['mode']!=mode:mismatches.append({'path':p,'reason':'working endpoint differs from candidate','entry':entry,'workingBlob':blob,'workingGitMode':mode})
    diffs={k:git(root,'diff','--binary',*args) for k,args in [('working',['HEAD']),('staged',['--cached']),('unstaged',[])]}
    for k,data in diffs.items():OUT.with_name(OUT.stem+'.'+key+'-'+k+'.diff').write_bytes(data)
    after=index(root);assert before==after and not before['unmerged'];assert not mismatches,mismatches[:10]
    result['surfaces'][key]={'root':str(root),'HEAD':git(root,'rev-parse','HEAD').decode().strip(),'indexBefore':before,'indexAfter':after,'trackedDeltaCount':len(tracked),'untrackedCount':len(others),'deltaCount':len(states),'states':states,'diffs':{k:{'sha256':sha(v),'size':len(v)} for k,v in diffs.items()},'candidateTreeReadback':{'state':'confirmed','tree':tree,'entries':len(tree_entries),'checkedEndpoints':len(states),'mismatches':mismatches},'noIndexOrObjectWrite':True}
assert result['codeTree']=='715ee46e34ef5c421c540314b882c04d1676e08d'
assert result['surfaces']['code']['diffs']['working']['sha256']=='60906382a032543186e2728c62275a857f7bdcd7ab06932a9fa1d21acb9fa4e5'
OUT.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'path':str(OUT),'sha256':sha(OUT.read_bytes()),'trees':[result['codeTree'],result['memoryTree']],'counts':{k:v['deltaCount'] for k,v in result['surfaces'].items()}}))
