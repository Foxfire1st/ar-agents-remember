import hashlib,json,os,stat,subprocess
from pathlib import Path
root=Path('/home/firefox/projects/ar-coordination/worktrees/agents-remember/260928-mik-l26-ar'); mem=root/'memory-260928-mik-l26';out=mem/'notes/l26-curation-takeover/d7a5e018/fix3/native-checkpoint';out.mkdir(exist_ok=True)
def git(repo,*args):return subprocess.check_output(['git','-C',str(repo),*args])
def sha(b):return hashlib.sha256(b).hexdigest()
frames={}
for side,repo in [('code',root/'260928-mik-l26'),('memory',mem)]:
 d=out/side;d.mkdir(exist_ok=True)
 idx=Path(git(repo,'rev-parse','--git-path','index').decode().strip());idx=idx if idx.is_absolute() else repo/idx
 raw=idx.read_bytes();native=git(repo,'ls-files','--stage','-z');debug=git(repo,'ls-files','--debug','-z')
 (d/'index.raw').write_bytes(raw);(d/'index-stage.nul').write_bytes(native);(d/'index-debug.nul').write_bytes(debug)
 diff=git(repo,'diff','--binary','HEAD');staged=git(repo,'diff','--cached','--binary','HEAD');unstaged=git(repo,'diff','--binary');(d/'working.diff').write_bytes(diff);(d/'staged.diff').write_bytes(staged);(d/'unstaged.diff').write_bytes(unstaged)
 tracked=set(x.decode() for x in git(repo,'ls-files','-z').split(b'\0') if x);untracked=set(x.decode() for x in git(repo,'ls-files','--others','--exclude-standard','-z').split(b'\0') if x);heads=set(x.decode() for x in git(repo,'ls-tree','-r','--name-only','-z','HEAD').split(b'\0') if x)
 excluded=out.relative_to(mem).as_posix()+'/' if side=='memory' else None
 paths=sorted(x for x in tracked|untracked|heads if not excluded or not x.startswith(excluded));facts=[]
 for path in paths:
  p=repo/path
  try:
   s=p.lstat();mode=s.st_mode
   if stat.S_ISLNK(mode):content=os.readlink(p).encode();kind='symlink'
   elif stat.S_ISREG(mode):content=p.read_bytes();kind='file'
   else:content=b'';kind='other'
   facts.append({'path':path,'state':'present','kind':kind,'sha256':sha(content),'size':len(content),'mode':mode,'uid':s.st_uid,'gid':s.st_gid,'tracked':path in tracked,'untracked':path in untracked})
  except FileNotFoundError:facts.append({'path':path,'state':'absent','tracked':path in tracked,'untracked':path in untracked})
 (d/'physical-facts.json').write_text(json.dumps(facts,indent=2)+'\n')
 assert raw==idx.read_bytes();assert native==git(repo,'ls-files','--stage','-z')
 frames[side]={'root':str(repo),'head':git(repo,'rev-parse','HEAD').decode().strip(),'rawIndexSHA256':sha(raw),'semanticStageNUlSHA256':sha(native),'workingDiffSHA256':sha(diff),'stagedDiffSHA256':sha(staged),'unstagedDiffSHA256':sha(unstaged),'unmerged':git(repo,'ls-files','-u','-z').decode(),'tracked':len(tracked),'untracked':len(untracked),'physicalPathCount':len(paths),'selfCaptureExcludedPrefix':excluded,'captureDidNotChangeIndex':True}
manifest=[]
for f in sorted(out.rglob('*')):
 if f.is_file() and f.name!='manifest.json':b=f.read_bytes();manifest.append({'path':f.relative_to(out).as_posix(),'sha256':sha(b),'bytes':len(b)})
report={'schema':'l26-held-source107-six-repair-native-checkpoint/v1','frames':frames,'artifacts':manifest,'noOperationsInFlight':True,'authority':'Manager Source87 timing disposition; checkpoint before SAME Worker supported sync','notFinalREADY':True,'note':'Read-only capture of full HEAD/index/untracked path union and literal physical content/absence. Only this capture directory is excluded from its self-referential memory physical frame; its artifacts are enumerated separately. No private tree object or index restoration/staging.'}
(out/'manifest.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({'path':str(out/'manifest.json'),'sha256':sha((out/'manifest.json').read_bytes()),'frames':frames},indent=2))
