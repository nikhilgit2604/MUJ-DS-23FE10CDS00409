from src.keywords import extract_keywords


complaint = """
My package has been delayed for five days.
The tracking information has not been updated
and customer support has not responded.
"""


keywords = extract_keywords(complaint)

print("Extracted Keywords:")
print(keywords)