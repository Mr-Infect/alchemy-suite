from core.crawler.crawler import crawl
from core.session_manager.session import get_sessions
from modules.idor.idor import run_idor
from reporting.report_generator import generate_report


def run(target):
    print(f"[+] Starting scan on {target}")

    sessions = get_sessions(target)

    pages, api_endpoints = crawl(target)

    print(f"[+] Total API endpoints: {len(api_endpoints)}")

    findings = []
    findings += run_idor(api_endpoints, sessions)

    generate_report(findings)
