HIGH_URGENCY_WORDS = [
    "urgent",
    "immediately",
    "asap",
    "emergency",
    "critical",
    "blocked",
    "cannot access",
    "charged twice",
    "fraud",
    "stolen",
    "unauthorized",
    "security"
]


def detect_urgency(text):

    text_lower = text.lower()

    matches = [
        word
        for word in HIGH_URGENCY_WORDS
        if word in text_lower
    ]

    # Critical situations
    critical_words = [
        "fraud",
        "stolen",
        "unauthorized",
        "security"
    ]

    critical_matches = [
        word
        for word in critical_words
        if word in text_lower
    ]

    if critical_matches:
        priority = "Critical"

    elif len(matches) >= 1:
        priority = "High"

    else:
        priority = "Normal"

    return {
        "priority": priority,
        "triggers": matches
    }