import re
from pdfquery import PDFQuery

# Get the email domain ending from the user
domain_ending = input("Enter the email domain ending (e.g., gmail.com, yahoo.com,etc.): ").strip()

pdf = PDFQuery('doc.pdf')
pdf.load()
text_elements = pdf.pq('LTTextLineHorizontal')
texts = [t.text for t in text_elements]

# Regular expression for email addresses ending with the user-provided domain
email_pattern = re.compile(
    rf'\b[A-Za-z0-9._%+-]+@(?:[A-Za-z0-9-]+\.)*{re.escape(domain_ending)}\b'
)

filtered_emails = []
for text in texts:
    matches = email_pattern.findall(text)
    filtered_emails.extend(matches)

# Save the filtered email addresses to a text file
with open('filtered_emails.txt', 'w', encoding='utf-8') as f:
    for email in filtered_emails:
        f.write(email + '\n')

print(f"Extracted {len(filtered_emails)} email(s) ending with '{domain_ending}'.")
