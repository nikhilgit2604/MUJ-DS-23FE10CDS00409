from src.analyzer import analyze_complaint


complaint = """
My package was supposed to arrive five days ago,
but it has still not arrived. The tracking information
has not been updated and customer support has not
responded to my messages. I am extremely frustrated.
"""


result = analyze_complaint(complaint)


print("\n")
print("=" * 70)
print("INTELLIREsolve - COMPLETE COMPLAINT ANALYSIS")
print("=" * 70)

print("\nCUSTOMER COMPLAINT:")
print(complaint)

print("\nCATEGORY:")
print(result["category"])

print("\nSENTIMENT:")
print(result["sentiment"]["sentiment"])

print("\nSENTIMENT SCORE:")
print(result["sentiment"]["score"])

print("\nPRIORITY:")
print(result["urgency"]["priority"])

print("\nURGENCY TRIGGERS:")
print(result["urgency"]["triggers"])

print("\nKEYWORDS:")
print(", ".join(result["keywords"]))

print("\n" + "=" * 70)
print("GEMINI AI ANALYSIS")
print("=" * 70)

print(result["llm_analysis"])

print("\n" + "=" * 70)