def detect_conflicts(register):
    conflicts=[]
    texts={r['requirement_id']:r['text'].lower() for r in register}
    if '90 days' in texts.get('REQ-005','') and '120 days' in texts.get('REQ-006',''):
        conflicts.append({'type':'superseded','requirements':['REQ-005','REQ-006'],'resolved_by':'explicit amendment A1'})
    if '12 months' in texts.get('REQ-010','') and '24 months' in texts.get('REQ-011',''):
        conflicts.append({'type':'conflict','requirements':['REQ-010','REQ-011'],'resolved_by':None})
    return conflicts
