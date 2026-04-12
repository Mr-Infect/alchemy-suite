from playwright.sync_api import sync_playwright


def login_and_get_cookie(page, email, password):
    page.goto("http://localhost:3000/#/login")
    page.wait_for_timeout(2000)

    try:
        page.click('button[aria-label="Close Welcome Banner"]', timeout=2000)
    except:
        pass

    page.fill('input[name="email"]', email)
    page.fill('input[name="password"]', password)

    page.locator('button[type="submit"]').click(force=True)
    page.wait_for_timeout(3000)

    cookies = page.context.cookies()
    return "; ".join([f"{c['name']}={c['value']}" for c in cookies])


def get_sessions(target):
    print("[+] Creating multiple sessions...")

    sessions = {}

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)

        context1 = browser.new_context()
        page1 = context1.new_page()

        context2 = browser.new_context()
        page2 = context2.new_page()

        try:
            # Admin session
            sessions["admin"] = login_and_get_cookie(
                page1,
                "admin@juice-sh.op",
                "admin123"
            )

            # Normal user (create manually in UI if needed)
            sessions["user"] = login_and_get_cookie(
                page2,
                "test@user.com",
                "test123"
            )

            print("[+] Multi-session ready")

        except Exception as e:
            print(f"[!] Session error: {e}")

        finally:
            browser.close()

    return sessions
