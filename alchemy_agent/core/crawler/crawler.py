from playwright.sync_api import sync_playwright
from urllib.parse import urljoin, urlparse
from collections import deque


def crawl(target, max_depth=2, max_pages=30):
    visited = set()
    queue = deque([(target, 0)])
    pages = []
    api_endpoints = set()

    domain = urlparse(target).netloc

    print(f"[+] Crawling started (max_depth={max_depth}, max_pages={max_pages})")

    def intercept_response(response):
        try:
            url = response.url
            if any(x in url for x in ["/api/", "/rest/", "/graphql"]):
                api_endpoints.add(url)
        except:
            pass

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)

        while queue and len(visited) < max_pages:
            url, depth = queue.popleft()

            if url in visited or depth > max_depth:
                continue

            context = browser.new_context()
            page = context.new_page()

            page.on("response", intercept_response)

            try:
                print(f"[>] Visiting ({len(visited)+1}): {url}")

                page.goto(url, timeout=10000)
                page.wait_for_timeout(2000)

                visited.add(url)
                pages.append(url)

                links = page.query_selector_all("a")

                for link in links:
                    try:
                        href = link.get_attribute("href")
                        if not href:
                            continue

                        full_url = urljoin(url, href)
                        parsed = urlparse(full_url)

                        if parsed.netloc != domain:
                            continue

                        if full_url not in visited:
                            queue.append((full_url, depth + 1))

                    except:
                        continue

            except Exception as e:
                print(f"[!] Skipped: {url} ({e})")

            finally:
                context.close()

        browser.close()

    print(f"[+] Crawling finished. Total pages: {len(pages)}")
    print(f"[+] Discovered {len(api_endpoints)} API endpoints")

    return pages, list(api_endpoints)
