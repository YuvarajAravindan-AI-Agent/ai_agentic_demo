"""List the models your Gemini API key can see.

Usage:
    export GEMINI_API_KEY="your-key"
    python list_gemini_models.py

Note: this reflects what the API key can call. It does NOT show what your
Google AI Pro subscription includes in the Gemini app (those are separate).
"""
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request

# Endpoint from memory of the Gemini API REST reference (models.list);
# verify against the current docs at https://ai.google.dev/api/models
URL = "https://generativelanguage.googleapis.com/v1beta/models"


def fetch_page(api_key, page_token=None):
    params = {"pageSize": "100"}
    if page_token:
        params["pageToken"] = page_token
    req = urllib.request.Request(
        f"{URL}?{urllib.parse.urlencode(params)}",
        headers={"x-goog-api-key": api_key},
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.load(resp)


def main():
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        sys.exit("Set GEMINI_API_KEY first.")

    models, token = [], None
    try:
        while True:
            page = fetch_page(api_key, token)
            models.extend(page.get("models", []))
            token = page.get("nextPageToken")
            if not token:
                break
    except urllib.error.HTTPError as e:
        sys.exit(f"HTTP {e.code}: {e.read().decode(errors='replace')}")
    except urllib.error.URLError as e:
        sys.exit(f"Network error: {e.reason}")

    for m in sorted(models, key=lambda m: m.get("name", "")):
        methods = ", ".join(m.get("supportedGenerationMethods", []))
        print(f"{m.get('name', '?'):55} {m.get('displayName', '')}  [{methods}]")
    print(f"\n{len(models)} models")


if __name__ == "__main__":
    main()
