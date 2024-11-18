import os
from dotenv import load_dotenv, find_dotenv

# Load environment variables from @.env file
dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

# # Add __all__ to explicitly declare what should be exported
# __all__ = ['Config']

class Config:
    # API Keys
    class APIKeys:
        OPENAI = os.getenv("OPENAI_API_KEY")
        ANTHROPIC = os.getenv("ANTHROPIC_API_KEY")
        GROQ = os.getenv("GROQ_API_KEY")
        GOOGLE = os.getenv("GOOGLE_API_KEY")

    class Helicone:
        API_KEY = os.getenv("HELIECONE_API_KEY")

# Usage example:
if __name__ == "__main__":
    print(f"OpenAI API Key: {Config.APIKeys.OPENAI}")
    print(f"Helicone API Key: {Config.Helicone.API_KEY}")