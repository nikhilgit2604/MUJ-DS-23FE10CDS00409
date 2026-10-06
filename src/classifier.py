from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score

from src.preprocessing import clean_text


def train_classifier(df):

    X = df["text"].apply(clean_text)
    y = df["category"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    model = Pipeline([
        (
            "tfidf",
            TfidfVectorizer(
                ngram_range=(1, 2),
                stop_words="english",
                sublinear_tf=True
            )
        ),
        (
            "classifier",
            LogisticRegression(
                max_iter=1000,
                class_weight="balanced"
            )
        )
    ])

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)

    print("\nModel Accuracy:")
    print(f"{accuracy:.2%}")

    print("\nClassification Report:")
    print(
        classification_report(
            y_test,
            predictions,
            zero_division=0
        )
    )

    return model


def predict_category(model, text):

    cleaned_text = clean_text(text)

    prediction = model.predict([cleaned_text])[0]

    text_lower = text.lower()

    # Strong domain-specific signals
    delivery_words = [
        "package",
        "parcel",
        "shipment",
        "tracking",
        "delivery",
        "delayed",
        "arrived",
        "not arrived",
        "shipping"
    ]

    billing_words = [
        "charged",
        "payment",
        "invoice",
        "billing",
        "transaction",
        "amount"
    ]

    refund_words = [
        "refund",
        "money back",
        "reimburse"
    ]

    account_words = [
        "login",
        "log in",
        "password",
        "account",
        "sign in"
    ]

    technical_words = [
        "crash",
        "error",
        "bug",
        "not working",
        "application",
        "app"
    ]

    # Give priority to strong complaint domain signals
    if any(word in text_lower for word in delivery_words):
        return "Delivery"

    if any(word in text_lower for word in billing_words):
        return "Billing"

    if any(word in text_lower for word in refund_words):
        return "Refund"

    if any(word in text_lower for word in account_words):
        return "Account"

    if any(word in text_lower for word in technical_words):
        return "Technical"

    return prediction