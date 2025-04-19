import re
from pdfquery import PDFQuery

pdf = PDFQuery('doc.pdf')
pdf.load()
text_elements = pdf.pq('LTTextLineHorizontal')
texts = [t.text for t in text_elements]

# Regular expression for email addresses ending with ousl.lk
email_pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@(?:[A-Za-z0-9-]+\.)*ousl\.lk\b')

filtered_emails = []
for text in texts:
    matches = email_pattern.findall(text)
    filtered_emails.extend(matches)

# Save the filtered email addresses to a text file
with open('ousl_emails.txt', 'w', encoding='utf-8') as f:
    for email in filtered_emails:
        f.write(email + '\n')

# print(f"Extracted {len(filtered_emails)} email(s) ending with 'ousl.lk'.")
