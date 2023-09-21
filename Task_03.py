import re

text = """Hi there,
        I hope this email finds you well. I wanted to share my contact information with you:
        My email addresses are:
        - john.doe@example.com
        - alice.smith12345@gmail.com
        - support@mywebsite.org
        - user(at)example(dot)com
        Please feel free to reach out to me anytime.
        Best regards,
        [Your Name]"""
email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
email_addresses = re.findall(email_pattern, text)
for email in email_addresses:
    print(email)
