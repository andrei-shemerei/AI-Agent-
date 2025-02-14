from dotenv import load_dotenv
import os
from llama_index.llms.gemini import Gemini
from llama_index.llms.openllm import OpenLLM

def get_llm():
    load_dotenv()
    
    google_api_key = os.getenv("GOOGLE_API_KEY", "").strip()
    model_api_url = os.getenv("MODEL_API_URL", "").strip()
    model_name = os.getenv("MODEL_NAME", "").strip()

    if google_api_key:
        return Gemini()
    
    if model_api_url and model_name:
        return OpenLLM(
            model=model_name,
            api_base=model_api_url,
            api_key="na",
            use_chat_completions=True,
            max_new_tokens=512,
            do_sample=False,
            return_full_text=True,
            top_k=10,
            num_return_sequences=1,
        )
    
    raise ValueError("Please specify access parameters for either Gemini or a locally hosted model.")