from app.services.adapters.base_adapter import BaseAdapter
from app.services.adapters.openai_adapter import OpenAIAdapter
from app.services.adapters.gemini_adapter import GeminiAdapter

class ModelManager:
    """
    Manager for selecting and initializing the appropriate AI model adapter.
    """
    def __init__(self, model_type: str = "openai"):
        self.model_type = model_type
        self.adapter = self._get_adapter()
        
    def _get_adapter(self) -> BaseAdapter:
        """
        Select and initialize the appropriate AI model adapter.
        """
        if self.model_type == "openai":
            return OpenAIAdapter()
        elif self.model_type == "gemini":
            return GeminiAdapter()
        else:
            raise ValueError(f"Invalid model type: {self.model_type}")
    
    def get_adapter(self) -> BaseAdapter:
        """
        Get the initialized adapter.
        """
        return self.adapter