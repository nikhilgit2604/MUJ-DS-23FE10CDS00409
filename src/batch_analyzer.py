import pandas as pd
import joblib

from src.preprocessing import clean_text
from src.classifier import predict_category
from src.sentiment import analyze_sentiment
from src.urgency import detect_urgency
from src.keywords import extract_keywords
from src.llm_service import analyze_with_llm


# Load trained model
MODEL_PATH = "models/complaint_classifier.pkl"
model = joblib.load(MODEL_PATH)


def process_batch(df):
    """
    Process multiple complaints.

    NLP analysis is performed first.
    Gemini analysis is attempted separately so that
    temporary Gemini failures do not destroy the NLP results.
    """

    # -----------------------------------------
    # Identify complaint column
    # -----------------------------------------

    if "text" in df.columns:
        complaint_column = "text"

    elif "complaint" in df.columns:
        complaint_column = "complaint"

    else:
        raise ValueError(
            "CSV must contain a 'text' or 'complaint' column."
        )

    results = []

    total = len(df)

    for index, complaint in enumerate(
        df[complaint_column],
        start=1
    ):

        if pd.isna(complaint):
            continue

        complaint = str(complaint).strip()

        if not complaint:
            continue

        print(
            f"Processing complaint {index}/{total}..."
        )

        # -----------------------------------------
        # Traditional NLP
        # -----------------------------------------

        try:

            cleaned_text = clean_text(
                complaint
            )

            category = predict_category(
                model,
                complaint
            )

            sentiment_result = analyze_sentiment(
                complaint
            )

            urgency_result = detect_urgency(
                complaint
            )

            keywords = extract_keywords(
                complaint
            )

        except Exception as error:

            results.append({
                "complaint": complaint,
                "category": "Unknown",
                "sentiment": "Unknown",
                "sentiment_score": 0,
                "priority": "Unknown",
                "keywords": "",
                "ai_analysis": "",
                "status": f"NLP Error: {error}"
            })

            continue

        # -----------------------------------------
        # Gemini
        # -----------------------------------------

        try:

            llm_result = analyze_with_llm(
                complaint=complaint,
                category=category,
                sentiment=sentiment_result["sentiment"],
                priority=urgency_result["priority"],
                keywords=keywords
            )

            ai_status = "Success"

        except Exception as error:

            llm_result = (
                "Gemini AI analysis was temporarily "
                "unavailable. Traditional NLP analysis "
                "was completed successfully."
            )

            ai_status = (
                f"NLP Success / LLM Error: {error}"
            )

        # -----------------------------------------
        # Store result
        # -----------------------------------------

        results.append({

            "complaint": complaint,

            "category": category,

            "sentiment":
                sentiment_result["sentiment"],

            "sentiment_score":
                sentiment_result["score"],

            "priority":
                urgency_result["priority"],

            "keywords":
                ", ".join(keywords),

            "ai_analysis":
                llm_result,

            "status":
                ai_status
        })

    return pd.DataFrame(results)