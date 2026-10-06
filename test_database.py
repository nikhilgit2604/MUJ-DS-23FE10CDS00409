from src.analyzer import analyze_complaint
from src.database import create_database, save_complaint, get_complaints


# Create database
create_database()

# Test complaint
complaint = """
My package has been delayed for five days.
The tracking information has not been updated
and customer support has not responded.
"""


print("Analyzing complaint...")

result = analyze_complaint(complaint)

print("Analysis completed.")

# Save result
save_complaint(result, complaint)

print("Complaint saved to database.")

# Retrieve records
complaints = get_complaints()

print("\nStored complaints:")
print("-" * 60)

for complaint_record in complaints:
    print("ID:", complaint_record[0])
    print("Complaint:", complaint_record[1])
    print("Category:", complaint_record[2])
    print("Sentiment:", complaint_record[3])
    print("Priority:", complaint_record[5])
    print("Keywords:", complaint_record[6])
    print("Created:", complaint_record[8])
    print("-" * 60)