"""
Run once: py build_I360.py
Generates I-360_Wizard.html -- a fully self-contained file you can
double-click to open. No server, no Python needed after this.
"""
import base64, os

PDF_PATH = r'C:\Users\johnh\uscis_forms\I-360.pdf'
OUT_PATH = r'C:\Users\johnh\immigration\I-360_Wizard.html'

with open(PDF_PATH, 'rb') as f:
    pdf_b64 = base64.b64encode(f.read()).decode('ascii')

states = ['AL','AK','AZ','AR','CA','CO','CT','DE','DC','FL','GA','HI','ID','IL','IN',
          'IA','KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH',
          'NJ','NM','NY','NC','ND','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT',
          'VT','VA','WA','WV','WI','WY']
state_opts = '<option value="">-- Select --</option>' + ''.join(f'<option>{s}</option>' for s in states)

tmpl_path = os.path.join(os.path.dirname(__file__), 'I-360_wizard_template.html')
with open(tmpl_path, 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace('__PDF_BASE64__', pdf_b64)
html = html.replace('<?= STATE_OPTIONS ?>', state_opts)

with open(OUT_PATH, 'w', encoding='utf-8') as f:
    f.write(html)

size_kb = os.path.getsize(OUT_PATH) / 1024
print(f'Built: {OUT_PATH}  ({size_kb:.0f} KB)')
