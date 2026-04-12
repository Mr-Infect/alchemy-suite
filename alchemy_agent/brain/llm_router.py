import requests

OLLAMA_URL = "http://localhost:11434/api/generate"


def query_llm(prompt, model="gemma:7b"):
    try:
        res = requests.post(
            OLLAMA_URL,
            json={
                "model": model,
                "prompt": prompt,
                "stream": False
            },
            timeout=60
        )

        data = res.json()

        # Debug visibility
        if "response" in data and data["response"].strip():
            return data["response"].strip()

        return "[LLM returned empty response]"

    except Exception as e:
        return f"[LLM ERROR] {e}"
