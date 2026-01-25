import re

text = "Samarth's contact is +91 1234567891 and email is samarth@xo.com. Date: 25/01/2026. Personal email: samarth@gmail.com"

# Searching for 'Samarth' using search()
search_obj = re.search(r"Samarth", text)
if search_obj:
    print(f"Search found: {search_obj.group()} starting at index {search_obj.start()}")

# Since the text starts with 'Samarth', this will succeed else it would return None
match_obj = re.match(r"Samarth", text)
print(f"Match at start: {match_obj.group() if match_obj else 'No match found'}")

# Finding the email address using findall()
emails = re.findall(r"[\w\.-]+@[\w\.-]+", text)
print(f"Emails found: {emails}")

# Replacing the phone number with a placeholder using sub()
censored = re.sub(r"\+91\s\d{10}", "[PHONE HIDDEN]", text)
print(f"Censored Text: {censored}")

# Splitting the text at 'and' using split()
segments = re.split(r"\sand\s", text)
print(f"Split segments: {segments}")

# Finding exactly 10 digits in a row using Quantifiers
phone_digits = re.findall(r"\d{10}", text)
print(f"10-digit sequence: {phone_digits}")

# Finding the date in DD/MM/YYYY format using Matching dates
date_pattern = r"\d{2}/\d{2}/\d{4}"
date_found = re.search(date_pattern, text)
print(f"Date found: {date_found.group() if date_found else 'None'}")

# Extracting alphanumeric characters using Special Characters
after_email_word = re.search(r"email is\s(\w+)", text)
print(f"Word after 'email is': {after_email_word.group(1)}")