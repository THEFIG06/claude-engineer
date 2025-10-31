from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    ANTHROPIC_API_KEY = os.getenv('ANTHROPIC_API_KEY')

    # Available Anthropic Models (as of January 2025):
    # - claude-3-5-sonnet-20241022: Latest Sonnet (best balance of intelligence/speed)
    # - claude-3-5-haiku-20241022: Latest Haiku (fastest, most cost-effective)
    # - claude-3-opus-20240229: Claude 3 Opus (most capable, slower)
    MODEL = "claude-3-5-sonnet-20241022"

    MAX_TOKENS = 8000
    MAX_CONVERSATION_TOKENS = 200000  # Maximum tokens per conversation

    # Paths
    BASE_DIR = Path(__file__).parent
    TOOLS_DIR = BASE_DIR / "tools"
    PROMPTS_DIR = BASE_DIR / "prompts"

    # Assistant Configuration
    ENABLE_THINKING = True
    SHOW_TOOL_USAGE = True
    DEFAULT_TEMPERATURE = 0.7
