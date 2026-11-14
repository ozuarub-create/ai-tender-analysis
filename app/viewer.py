def render_html(register):
    rows=''.join(f"<tr><td>{r['requirement_id']}</td><td>{r['text']}</td><td>{r.get('mandatory')}</td><td>{r['source']['document']} p.{r['source'].get('page','')}</td></tr>" for r in register)
    return f"<html><body><h1>Tender Requirement Register</h1><table border=1><tr><th>ID</th><th>Requirement</th><th>Mandatory</th><th>Source</th></tr>{rows}</table></body></html>"
