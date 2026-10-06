from src.llm_service import analyze_with_llm


complaint = """
My payment was charged twice for the same order.
I am very disappointed and need my money back immediately.
"""


result = analyze_with_llm(
    complaint=complaint,
    category="Billing",
    sentiment="Negative",
    priority="High",
    keywords=[
        "payment",
        "charged twice",
        "money",
        "refund"
    ]
)


print("\n")
print("=" * 60)
print("GEMINI ANALYSIS")
print("=" * 60)
print(result)
print("=" * 60)