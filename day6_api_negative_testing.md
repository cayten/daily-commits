# Day 6 – API Negative Testing 🛡️

Negative testing helps verify that an API fails **safely and predictably** when given invalid input or used incorrectly.

## ❗Common Negative Scenarios

| Area | Scenario | Expected Result |
|---|---|---|
| Auth | Missing/invalid token | **401 Unauthorized** / error body with code/message |
| Permissions | Valid token, no permission | **403 Forbidden** |
| Resource | Wrong/unknown ID (`/users/999999`) | **404 Not Found** |
| Validation | Required field missing/empty | **400 Bad Request** (field-level errors) |
| Type | Wrong data type (string instead of int) | **400 Bad Request** |
| Size | Exceeds max length / payload too large | **413 Payload Too Large** or **400** |
| Method | Wrong HTTP method on endpoint | **405 Method Not Allowed** (Allow header) |
| Rate limit | Exceed request limits | **429 Too Many Requests** |
| Security | SQL/JS injection payload | Request blocked / **400/403** |
| Idempotency | Duplicate creation with same idempotency key | **409 Conflict** or graceful ignore |

## 🔎 What to Validate
- **Status code** matches spec
- **Response schema** (error envelope, fields)
- **Error codes** are consistent (`code`, `message`, `details`)
- **Headers** (e.g., `Content-Type`, `Retry-After` on 429)
- **No sensitive leakage** (stack traces, SQL errors)

## 🧰 Test Data Tips
- Generate invalid emails: `no-at-symbol.com`, `a@b`
- Strings: boundary values (0, 1, max, max+1)
- Numbers: negative, zero, big numbers
- IDs: non‑existent GUIDs, wrong format (`abc`)

## ✅ Exit Criteria (examples)
- All documented negative scenarios implemented
- Error contract stable & consistent
- No P0/P1 leaks or crashes under malformed input

---

See `day6_negative_test.py` for tiny runnable examples with Python `requests`.
