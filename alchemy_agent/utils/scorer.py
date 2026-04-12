def score_finding(url, admin_res, user_res, analysis):
    score = 0

    # Status difference
    if admin_res.status_code != user_res.status_code:
        score += 30

    # Content difference
    diff = abs(len(admin_res.text) - len(user_res.text))
    if diff > 50:
        score += 30

    # Sensitive keywords
    sensitive_keywords = ["user", "admin", "account", "auth", "token"]

    if any(k in url.lower() for k in sensitive_keywords):
        score += 20

    # LLM signal boost
    if "idor" in analysis.lower() or "access control" in analysis.lower():
        score += 20

    return score