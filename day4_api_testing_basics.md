# Day 4 – API Testing Basics 📡

Today’s daily commit dives into the fundamentals of **API Testing**, a crucial skill for any modern QA Engineer. 🧪

## 🌐 What is an API?
API (Application Programming Interface) is a set of rules that allows different software components to communicate with each other.  
In testing, we focus on verifying:
- Functionality
- Reliability
- Performance
- Security

---

## 📬 Common HTTP Methods

| Method | Description                          | Example Use Case                        |
|--------|---------------------------------------|-------------------------------------------|
| GET    | Retrieve data                        | Fetch user details                       |
| POST   | Send data to create a resource       | Create a new user                        |
| PUT    | Update an existing resource          | Update user profile                      |
| PATCH  | Partially update a resource          | Update a single user field               |
| DELETE | Remove a resource                    | Delete a user                            |

---

## 📊 Important Status Codes

| Code | Meaning               | Description                                                       |
|------|-------------------------|-------------------------------------------------------------------|
| 200  | OK                     | Request succeeded                                                 |
| 201  | Created                | New resource successfully created                                 |
| 400  | Bad Request            | Client-side error (e.g. missing fields)                           |
| 401  | Unauthorized           | Authentication is required                                       |
| 403  | Forbidden              | Authenticated but not allowed                                    |
| 404  | Not Found              | Resource doesn’t exist                                          |
| 500  | Internal Server Error  | Server-side failure                                              |

---

## 🧰 Tools for API Testing

- **Postman** – Great for manual testing & scripting collections  
- **Swagger** – For API documentation & quick tryouts  
- **cURL** – Command-line API testing  
- **REST Assured / Requests** – For automated testing

---

## 📝 QA Pro Tips
- Always validate both **status code** and **response body**.  
- Test **negative scenarios** (e.g., missing auth, invalid data).  
- Save & organize your test collections.  
- Automate repetitive checks for regression coverage.

---

## 🌱 Daily Commit Goal
Another green box added to the contribution graph ✅  
And one step closer to becoming an unstoppable QA legend 👑
