def evaluate(extracted, reference):
    e={r['requirement_id'] for r in extracted}; g={r['requirement_id'] for r in reference}
    tp=len(e & g); fp=len(e-g); fn=len(g-e)
    precision=tp/(tp+fp) if tp+fp else 0.0; recall=tp/(tp+fn) if tp+fn else 0.0
    return {'tp':tp,'fp':fp,'fn':fn,'precision':precision,'recall':recall,'duplicates':len(extracted)-len(e),'omissions':fn,'wrong_values':0,'unsupported_inferences':0}
