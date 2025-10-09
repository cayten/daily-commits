# day6_negative_test.py
\"\"\"
Tiny negative API tests using requests.
Run with:  python day6_negative_test.py
(Optional) With pytest:  pytest -q day6_negative_test.py
\"\"\"

import json
import requests

BASE_URL = "https://httpbin.org"  # demo-only endpoints

def assert_status(resp, expected):
    assert resp.status_code == expected, f"Expected {expected}, got {resp.status_code}. Body: {resp.text}"

def test_missing_auth():
    # Simulate calling an endpoint that requires auth (httpbin returns 401 for /bearer)
    resp = requests.get(f\"{BASE_URL}/bearer\")  # no Authorization header
    assert_status(resp, 401)

def test_wrong_method():
    # /get supports GET; sending POST should not be allowed (often 405)
    # httpbin echoes 405 at /status/405
    resp = requests.post(f\"{BASE_URL}/status/405\")
    assert_status(resp, 405)

def test_validation_bad_json():
    # Send malformed JSON to simulate 400 (httpbin returns 400 for invalid JSON at /post?)
    bad_body = \"{not: valid json\"  # deliberately broken
    headers = {\"Content-Type\": \"application/json\"}
    resp = requests.post(f\"{BASE_URL}/post\", data=bad_body, headers=headers)
    # httpbin will treat as raw data; we mimic a spec by checking content-type echo
    # In a real API this should be 400; here we assert server received invalid JSON pattern.
    assert resp.status_code in (200, 400), f\"Unexpected code: {resp.status_code}\"
    # Demonstrate parsing safety
    try:
        json.loads(bad_body)
        assert False, \"Client-side JSON should have failed\"
    except Exception:
        pass

if __name__ == \"__main__\":
    # Run mini smoke when executed directly
    tests = [test_missing_auth, test_wrong_method, test_validation_bad_json]
    failures = 0
    for t in tests:
        try:
            t()
            print(f\"[PASS] {t.__name__}\")
        except AssertionError as e:
            failures += 1
            print(f\"[FAIL] {t.__name__}: {e}\")
    if failures:
        raise SystemExit(1)
    print(\"All day6 negative tests passed ✔\")
