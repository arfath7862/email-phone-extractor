import re

# Step 1: Read text from sample.txt
with open("sample.txt", "r") as file:
    text = file.read()

# Step 2: Define regex patterns
email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
phone_pattern = r'(?:\+91[\-\s]?)?[6-9]\d{9}|\b\d{3}[-.\s]?\d{7,8}\b'

# Step 3: Extract emails and phone numbers
emails = re.findall(email_pattern, text)
phones = [match.group() for match in re.finditer(phone_pattern, text)]

# Step 4: Display the results
print("Emails Found:")
for email in emails:
    print(email)

print("\nPhone Numbers Found:")
for phone in phones:
    print(phone)

# Step 5: Save to output.txt
with open("output.txt", "w") as output_file:
    output_file.write("Emails:\n" + "\n".join(emails) + "\n\n")
    output_file.write("Phone Numbers:\n" + "\n".join(phones))
