def build_attack_prompt(endpoint):
    return f"""
You are an expert penetration tester.

Target endpoint:
{endpoint}

Decide:
1. HTTP method to use (GET, POST, PUT, DELETE)
2. Possible vulnerability type
3. Example payload (JSON or params)

Respond STRICTLY in this format:

METHOD: <method>
VULN: <type>
PAYLOAD: <payload>
"""