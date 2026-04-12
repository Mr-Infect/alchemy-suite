import re
import requests
from urllib.parse import urljoin

def extract_js_endpoints(base_url):
    endpoints = set()

    try:
        r = requests.get(base_url, timeout=5)

        # Extract JS files
        js_files = re.findall(r'src="(.*?\.js)"', r.text)

        for js in js_files:
            full_js_url = urljoin(base_url, js)

            try:
                js_content = requests.get(full_js_url, timeout=5).text

                # Extract API-like patterns
                found = re.findall(r'["\'](\/api\/.*?|\/rest\/.*?|\/graphql.*?)["\']', js_content)

                for ep in found:
                    endpoints.add(urljoin(base_url, ep))

            except:
                continue

    except:
        pass

    return list(endpoints)
