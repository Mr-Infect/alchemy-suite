import requests
from brain.llm_router import query_llm
from brain.prompt_engine import build_attack_prompt
from brain.chain_engine import get_next_action
from utils.scorer import score_finding


LOW_VALUE = ["captcha", "assets", "images", "public"]


def parse_llm_output(text):
    method = "GET"
    payload = None
    vuln = "unknown"

    for line in text.split("\n"):
        if "METHOD:" in line:
            method = line.split("METHOD:")[1].strip()

        if "PAYLOAD:" in line:
            payload = line.split("PAYLOAD:")[1].strip()

        if "VULN:" in line:
            vuln = line.split("VULN:")[1].strip().lower()

    return method, payload, vuln


def run_idor(endpoints, sessions):
    findings = []

    print("[+] Running Attack + Validation Engine")

    admin_headers = {"Cookie": sessions.get("admin", "")}
    user_headers = {"Cookie": sessions.get("user", "")}

    for url in endpoints:

        if any(x in url.lower() for x in LOW_VALUE):
            continue

        print(f"\n[>] Target: {url}")

        llm_output = query_llm(build_attack_prompt(url))
        print(f"[LLM Decision]\n{llm_output}\n")

        method, payload, vuln_type = parse_llm_output(llm_output)

        try:
            admin_res = requests.get(url, headers=admin_headers, timeout=5)
            user_res = requests.get(url, headers=user_headers, timeout=5)

            score = score_finding(url, admin_res, user_res, llm_output)

            detected = False
            issue_type = None

            # 🔥 1. LLM-DRIVEN DETECTION (PRIMARY FIX)
            if "sensitive" in vuln_type:
                detected = True
                issue_type = "Sensitive Data Exposure"

            elif "information" in vuln_type:
                detected = True
                issue_type = "Information Disclosure"

            elif "idor" in vuln_type or "access" in vuln_type:
                if admin_res.text != user_res.text:
                    detected = True
                    issue_type = "IDOR / Access Control"

            # 🔥 2. RESPONSE-BASED DETECTION
            if not detected:
                if admin_res.status_code == 200 and user_res.status_code != 200:
                    detected = True
                    issue_type = "Access Control Weakness"

                elif abs(len(admin_res.text) - len(user_res.text)) > 50:
                    detected = True
                    issue_type = "Response Anomaly"

            # 🔥 3. SCORE FALLBACK
            if not detected and score >= 50:
                detected = True
                issue_type = "High-Risk Pattern"

            # ✅ STORE FINDING
            if detected:
                print(f"[!!!] VALIDATED ISSUE ({score}) → {url}")

                findings.append({
                    "type": issue_type,
                    "url": url,
                    "score": score,
                    "evidence": f"Admin({admin_res.status_code}) vs User({user_res.status_code}) | len diff={abs(len(admin_res.text)-len(user_res.text))}",
                    "llm_decision": llm_output
                })

                # 🔥 OPTIONAL CHAINING (no longer blocking)
                chain_input = f"Admin len={len(admin_res.text)}, User len={len(user_res.text)}"
                chain_output = get_next_action(url, chain_input)

                print(f"[CHAIN ATTEMPT]\n{chain_output}\n")

        except Exception as e:
            print(f"[!] Error: {e}")
            continue

    return findings