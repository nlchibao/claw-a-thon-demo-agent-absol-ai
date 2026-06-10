import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


class LLMService:

    def __init__(self):

        self.client = OpenAI(
            api_key=os.getenv(
                "AI_PLATFORM_API_KEY"
            ),
            base_url=os.getenv(
                "AI_PLATFORM_BASE_URL"
            )
        )

        self.model_name = os.getenv(
            "MODEL_NAME"
        )

    def generate(
        self,
        prompt: str
    ):

        print("Calling model...")

        response = (
            self.client.chat.completions.create(
                model=self.model_name,
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )
        )

        print("Response received")

        return (
            response
            .choices[0]
            .message
            .content
        )