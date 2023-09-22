import re
import sys
input("Enter the text\n:")
text = sys.stdin.read()
email_pattern = r'[\w._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
text_stripped = text.strip()
email_addresses = re.findall(email_pattern, text_stripped, re.MULTILINE)
for email in email_addresses:
    print(email)
