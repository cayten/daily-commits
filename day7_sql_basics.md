# Day 7 – SQL Basics for Testers 🧠💾

As a QA Engineer, knowing how to write **basic SQL queries** is essential for verifying backend data, checking test results, and debugging production issues efficiently.

---

## 🧭 SELECT & WHERE

```sql
-- Get all users from the "users" table
SELECT * FROM users;

-- Get active users only
SELECT id, name, email FROM users
WHERE status = 'active';
```

---

## 📊 ORDER BY & LIMIT

```sql
-- Get the 5 newest users by created_at timestamp
SELECT id, name, created_at FROM users
ORDER BY created_at DESC
LIMIT 5;
```

---

## 🔗 Simple JOIN Example

```sql
-- List users and their corresponding orders
SELECT u.id, u.name, o.id AS order_id, o.total
FROM users u
JOIN orders o ON u.id = o.user_id;
```

---

## 🧪 QA Tester Use Cases

| Scenario | Query | What to Check |
|----------|-------|---------------|
| Verify new user is stored correctly | `SELECT * FROM users WHERE email='test@example.com';` | User data matches UI input |
| Validate order total after checkout | Join `orders` and `order_items` | Totals calculated correctly |
| Check data consistency | Count users/orders | UI counts match DB counts |

---

## 📝 Mini SQL Challenges (Try It!)
1. List all users whose names start with **“A”**.  
2. Find orders where the **total is greater than 100**.  
3. Count how many users are **inactive**.

---

✨ **Pro Tip**: Keep a personal `.sql` snippets file for commonly used queries. It saves you tons of time during testing 🕓⚡
