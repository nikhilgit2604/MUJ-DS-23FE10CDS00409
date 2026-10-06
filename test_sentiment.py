from src.sentiment import analyze_sentiment


complaints = [
    "I am extremely disappointed with your service.",
    "The product is okay.",
    "Thank you for solving my problem quickly.",
    "My payment was charged twice and I am very angry.",
    "I have not received my package yet."
]


for complaint in complaints:

    result = analyze_sentiment(complaint)

    print("\nComplaint:")
    print(complaint)

    print("Sentiment:")
    print(result["sentiment"])

    print("Score:")
    print(result["score"])

    print("-" * 50)