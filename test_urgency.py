from src.urgency import detect_urgency


complaints = [
    "I have a question about my order.",
    "I need this fixed immediately.",
    "My account is blocked and I cannot access it.",
    "Someone made an unauthorized transaction on my card."
]


for complaint in complaints:

    result = detect_urgency(complaint)

    print("\nComplaint:")
    print(complaint)

    print("Priority:")
    print(result["priority"])

    print("Triggers:")
    print(result["triggers"])

    print("-" * 50)