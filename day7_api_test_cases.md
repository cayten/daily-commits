# Day 7 – API Test Case Examples 🧪

Here are sample **positive and negative API test cases** for a simple `User API`.  
This format is perfect for quick documentation and interviews 👌

| # | Endpoint | Method | Test Scenario | Input | Expected Output | Status |
|---|----------|--------|---------------|-------|------------------|--------|
| 1 | /users   | GET    | Fetch all users | - | List of users returned | 200 |
| 2 | /users/1 | GET    | Fetch user by ID | 1 | User object with ID=1 | 200 |
| 3 | /users   | POST   | Create new user (valid) | name, email | New user created | 201 |
| 4 | /users   | POST   | Create new user (missing email) | name only | Error message | 400 |
| 5 | /users/999 | GET  | Non-existent user | 999 | Error “not found” | 404 |
| 6 | /users   | PUT    | Invalid method (should be PATCH) | - | Method not allowed | 405 |
| 7 | /auth/login | POST | Wrong password | valid email + wrong pass | Error | 401 |

---

## 🌱 Daily Commit Goal
✅ 7. gün tamamlandı — API + SQL bilgisiyle profiline QA kraliçesi havası kattın 👑✨
