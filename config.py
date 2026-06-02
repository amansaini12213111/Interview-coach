from pydantic_settings import BaseSettings
from typing import Literal

class Settings(BaseSettings):
    # API Keys
    # Pydantic Settings will automatically map the google_api_key attribute
    # to the GOOGLE_API_KEY environment variable (case-insensitive)
    google_api_key: str

    # Model settings
    model_name: str = "gemini-2.5-flash"  # Default Gemini model
    temperature: float = 0.7
    max_tokens: int = 1000

    # Interview settings
    max_questions: int = 5
    default_difficulty: Literal["easy", "medium", "hard"] = "medium"

    # RAG settings
    chunk_size: int = 500
    chunk_overlap: int = 50
    retriever_k: int = 3

    class Config:
        env_file = ".env"
        extra = "ignore"  # Ignore other env variables in the system

# Instantiate settings globally
settings = Settings()