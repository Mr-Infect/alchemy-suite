from brain.llm_router import query_llm


def build_chain_prompt(url, previous_result):
    return f"""
You are an expert penetration tester.

Target endpoint:
{url}

Previous observation:
{previous_result}

Decide next step:
1. What should be tested next?
2. Provide exact payload or request modification

Format:

NEXT_STEP: <action>
PAYLOAD: <payload>
"""
    

def get_next_action(url, previous_result):
    prompt = build_chain_prompt(url, previous_result)
    return query_llm(prompt)
