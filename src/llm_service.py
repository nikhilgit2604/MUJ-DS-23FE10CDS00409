import os
import time

from dotenv import load_dotenv
from google import genai

from src.prompt_loader import load_prompts


# Load environment variables
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError(
        "GEMINI_API_KEY was not found in the .env file."
    )


# Create Gemini client
client = genai.Client(api_key=api_key)

# Load prompts
prompts = load_prompts()


def analyze_with_llm(
    complaint,
    category,
    sentiment,
    priority,
    keywords
):
    system_prompt = prompts[
        "complaint_analysis"
    ]["system"]

    user_prompt = prompts[
        "complaint_analysis"
    ]["user"]

    user_prompt = user_prompt.format(
        complaint=complaint,
        category=category,
        sentiment=sentiment,
        priority=priority,
        keywords=", ".join(keywords)
    )

    final_prompt = (
        system_prompt
        + "\n\n"
        + user_prompt
    )

    # Retry if Gemini is temporarily unavailable
    max_retries = 3

    for attempt in range(max_retries):
        try:
            response = client.models.generate_content(
                model="gemini-3.8-flash",
                contents=final_prompt
            )

            return response.text

        except Exception as error:

            error_message = str(error)

            # Retry temporary server / availability errors
            if (
                "503" in error_message
                or "UNAVAILABLE" in error_message
                or "high demand" in error_message
            ):
                if attempt < max_retries - 1:
                    wait_time = 2 ** attempt

                    print(
                        f"Gemini temporarily unavailable. "
                        f"Retrying in {wait_time} seconds..."
                    )

                    time.sleep(wait_time)
                else:
                    raise RuntimeError(
                        "Gemini is temporarily unavailable "
                        "after multiple attempts. "
                        "Please try again later."
                    )

            else:
                # Do not retry authentication,
                # invalid request, etc.
                raise error