"""Build task-bound evidence; no source, index, record or family writes."""
from pathlib import Path
import json, hashlib, subprocess
G=Path('/home/firefox/projects/ar-coordination/worktrees/agents-remember/260928-mik-l26-ar')
M=G/'memory-260928-mik-l26'; C=G/'260928-mik-l26'
B=M/'notes/l26-curation-takeover/d7a5e018/o01-after-r3'
S=M/'notes/l26-curation-takeover/d7a5e018/source98-mechanical'
def sha(b):return hashlib.sha256(b).hexdigest()
def digest(p):return sha(p.read_bytes()) if p.is_file() else None
def put(n,j):(S/n).write_text(json.dumps(j,indent=2,ensure_ascii=False)+'\n')
prior=json.loads((B/'source41-all487-current-evidence-binding.json').read_text())
judgments=json.loads((B/'source41-coherence-judgments.prepared.json').read_text())
shared=json.loads((B/'source41-coherence-shared74-evidence.json').read_text())
specific={
'mcp/tests/evidence-lifecycle.toml':'The current parsed lifecycle catalog preserves authored artifact/contract ownership and admitted retirement deltas alongside incoming Investigator consumers. The Source98 independent source-only case supports this exact three-side catalog composition. The companion card describes declarative evidence inventory, current Node consumer normalization and incoming consumers; it does not claim that inventory registration executes a contract. Actual unchanged Source98 catalog PASS83 and oracle COMPARE OK are structural/composition evidence on this subject; all older raw mismatch receipts stay dated and the 424 affected population remains unexecuted.',
'mcp/tests/test-evidence-lanes.toml':'The current parsed lane catalog preserves the held authored retirement deltas, the five already-absent modules and same-lane normalization while retaining incoming Investigator and other admitted modules in their incoming lanes. The Source98 source-only readback supports the complete parsed catalog composition. The companion card describes one lane per current module and separates membership from collection or execution. Neither the catalog check nor a lane declaration certifies the affected population.',
'mcp/tests/test_role_instruction_wording.py':'The current wording source retains all incoming functions/assertions and subTest/assertIn harness plus the held Curator/curation mapping, parser-negative method and three imports. Source98 adds the Investigator scope and negative wording guards while preserving the Curator retirement/writer-boundary controls. Its card keeps the earlier System Specialist paragraph explicitly dated L93 and states current Investigator scope separately. Two self-file references were reauthored at the current composed source without changing card bytes, reference IDs or notes. The retained 40 calls/466 subtests are focused wording/corpus evidence only, not an affected-population or new memory verdict.',
'skills/l-01-agent-lifecycles/composition-manifest.json':'The current authored manifest routes Investigator instead of the earlier System Specialist identity, names parent-supplied concern scope and adds its exact requested tools. The two previously retired Curator tools remain absent. The card describes authoritative routing metadata and current Investigator scope without turning requested tools into execution evidence. Existing proof/realization IDs, origins, roles and rationales are preserved; the imported full-manifest realization range is corrected from 1-613 to the actual composed 1-611.',
'mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/composition-manifest.json':'The packaged manifest preserves the complete incoming Investigator and other fields with only the two previously reviewed retired Curator tool requests removed. The source-only readback supports that exact composition. Its unchanged card describes routing metadata rather than duplicated instruction prose; it makes no obsolete role-name claim or capability execution claim.',
'skills/l-01-agent-lifecycles/operations/coordination.md':'The current coordination paragraph adds Investigator to the Orchestrator and Manager delegation lists while preserving request identity, refusal, same-ID reconciliation and paired-enclosure ownership. The card describes the coordination instruction and manager-side transaction without claiming an old closed role list; current typed realization anchors carry the specific parent duties. This incoming extension does not authorize this Curator to start a role or alter transaction state.',
'skills/l-01-agent-lifecycles/operations/orientation.md':'The current orientation instruction uses the parent first message for an Investigator concern and asks that parent for missing scope, with the developer request used when no parent exists. Its unchanged generic card names context/source orientation without contradicting that division. The existing taskless applicability and realization IDs remain; current incoming scope is preserved without introducing a new permission.',
}
rows=[];changed=[]
for j,p in zip(judgments,prior['rows'],strict=True):
 assert (j['classification'],j['onboardingFile'],j['sourceFile'])==(p['classification'],p['onboardingFile'],p['sourceFile'])
 sp=C/j['sourceFile'];cp=M/'onboarding'/j['onboardingFile']
 ss=digest(sp);cs=digest(cp);se=ss==p['sourceSha256'];ce=cs==p['cardSha256']
 if j['sourceFile'] in specific:j['rationale']=specific[j['sourceFile']]
 elif j['classification']=='entity-row':
  name=j['sourceFile'].removeprefix('entity:')
  lines=[l for l in cp.read_text().splitlines() if name in l]
  j['rationale']=f'The named {name} entity keeps its own recorded contract and ownership. The incoming catalog changes other recorded fingerprints and the Provider Degradation Protocol role path to Investigator; no L26 entity is minted or restamped. The current named-row evidence remains in this catalog, with historical committed fingerprints preserved. This is a source-bound reconciliation, not independent current-parent acceptance.'
 elif not se or not ce:
  j['rationale']=p['rationale']+' The current Source98 incoming route account and carried retirement corrections are read individually here; current Investigator vocabulary is preserved, while historical task and database descriptions remain historical. Generated navigation and anchored source registrations establish no runtime certificate or new semantic verdict.'
 else:
  j['rationale']=p['rationale']+' For the current Source98 mechanical binding, this exact source endpoint and card body are byte-equal to the prior Source41 evidence; its named contract and retirement conditions remain applicable. Earlier acceptance stays tied to its original subject.'
 row={**p,'sourceSha256':ss,'cardSha256':cs,'sourcePresent':sp.is_file(),'cardPresent':cp.is_file(),'sameSourceAsSource41':se,'sameCardAsSource41':ce,'rationale':j['rationale']}
 rows.append(row)
 if not se or not ce:changed.append(row)
lookup={(j['classification'],j['onboardingFile'],j['sourceFile']):j for j in judgments}
for r in shared['rows']:
 key=(r['classification'],r['onboardingFile'],r['sourceFile']);j=lookup[key]
 st=(C/r['sourceFile']).read_text();ct=(M/'onboarding'/r['onboardingFile']).read_text()
 r['sameSourceBytesAsSource41']=st==r['source'];r['sameCardBytesAsSource41']=ct==r['card']
 r.update(source=st,card=ct,sourceSHA256=sha(st.encode()),cardSHA256=sha(ct.encode()),rationale=j['rationale'],independentAcceptance=False)
 r['whyEvidenceApplies']=f"Shared row {r['ordinal']} contains the whole actual {r['sourceFile']} and its own companion {r['onboardingFile']}, each with its measured current digest. This judgment is about that exact pair: "+j['rationale']+' The individual full source/card account, rather than a shared count or deletion hunk, establishes applicability for this row.'
 r['action']='preserve current accepted intent and independently account for actual Source98 source/card bytes; no new semantic review'
 j['evidenceRef']='memory:'+str((S/'source98-coherence-shared74-evidence.json').relative_to(M))
put('source98-coherence-shared74-evidence.json',{**shared,'sourceHead':'a1b7c898ab896c00cffe68d31efb643b65538e06','codeTree':'6a13d562cd5d03b6fdb8ddfad688c5f48c3f34d2','sourceChangeSha256':'5fc74bb690883b329c0187336b6b1ef2b1036d3c4bceb18c23991df4e3c8357a','sourceEnvelopeSha256':'d7e3d77a1494940c133dbce2b25a014cb8a20e7eaf5b12e5a515c04b45675e2d','productionAuthority':'f1a8984a1ff57d91ca7dbd53de8fab8c6597d4be7e5109ab9f684397c71e74d8','predecessor':{'path':str((B/'source41-coherence-shared74-evidence.json').relative_to(M)),'sha256':digest(B/'source41-coherence-shared74-evidence.json')},'rows':shared['rows']})
assert len(shared['rows'])==74 and len(rows)==487
put('source98-all487-current-evidence-binding.json',{'schema':'l26-current-coherence-binding/v1','codeTree':'6a13d562cd5d03b6fdb8ddfad688c5f48c3f34d2','changeSha256':'5fc74bb690883b329c0187336b6b1ef2b1036d3c4bceb18c23991df4e3c8357a','rows':rows,'actualChangedRows':changed,'originalCandidatePopulationPreserved':True,'independentAcceptance':False,'sharedEvidenceEachJudgmentMeasured':74,'sharedEvidenceChangedPairs':[r['ordinal'] for r in shared['rows'] if not r['sameSourceBytesAsSource41'] or not r['sameCardBytesAsSource41']]})
put('source98-coherence-judgments.prepared.json',judgments)
before=json.loads((S/'history-refresh-authored-evidence.json').read_text())['existingEntryFields'];found={}
for p in (M/'onboarding').rglob('*.json'):
 try:d=json.loads(p.read_text())
 except Exception:continue
 for e in [*d.get('realizes',[]),*d.get('proves',[])]:
  if e.get('id') in before:found[e['id']]=e
checks=[]
for ident,b in before.items():
 e=found[ident]
 fields={k:e.get(k) for k in ['role','rationale','facet','origin']}
 assert fields=={k:b[k] for k in fields},(ident,fields,b)
 checks.append({'id':ident,'fields':fields,'locatorBefore':b['locator'],'locatorAfter':e.get('anchor',{}).get('locator'),'pathBefore':b['path'],'pathAfter':e.get('path')})
put('existing-typed-entry-readback.json',{'count':len(checks),'allRolesRationalesFacetsOriginsPreserved':True,'checks':checks,'writerRecordCount':0,'writerEntryCount':0})
print(json.dumps({'judgments':len(judgments),'shared':74,'changedShared':[r['ordinal'] for r in shared['rows'] if not r['sameSourceBytesAsSource41'] or not r['sameCardBytesAsSource41']],'changedCandidates':len(changed),'typedEntriesPreserved':len(checks)}))
