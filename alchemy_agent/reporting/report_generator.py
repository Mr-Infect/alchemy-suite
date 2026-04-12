def generate_report(findings):
    print("\n=== FINAL REPORT ===\n")

    if not findings:
        print("[+] No validated exploits found\n")
        return

    findings = sorted(findings, key=lambda x: x["score"], reverse=True)

    for f in findings:
        print(f"[!!!] {f['type']} (Score: {f['score']})")
        print(f"Target URL: {f['url']}")

        # ✅ SAFE ACCESS (NO CRASH)
        if "exploit" in f:
            print(f"Exploit URL: {f['exploit']}")

        if "evidence" in f:
            print(f"Evidence: {f['evidence']}")

        print(f"\n[LLM Analysis]\n{f['llm_decision']}\n")