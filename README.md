# Regular Expressions for Data Validation

## Project Overview

This project demonstrates how to use Python Regular Expressions (`re` module) to validate user input in real-world applications.

The script validates:

- Email Addresses  
- Indian Mobile Numbers  
- Password Strength  

This project is useful for backend validation, login systems, form validation, and interview preparation.

---

## Tools Used

- Python 3.x
- re module (built-in)
- VS Code / Jupyter Notebook / PyCharm Community Edition

---

## Project Structure

regex_validation.py  
README.md  

---

## How to Run the Project

1. Install Python (if not already installed)
2. Open terminal in the project folder
3. Run:

   python regex_validation.py

4. Enter the required inputs when prompted.

---

## Email Validation

### Rules:
- Must contain @
- Must contain a valid domain (example: .com, .in, .org)
- Username may include letters, digits, ., _, %, +, -

### Regex Pattern:

^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$

### Valid Examples:
- test@gmail.com
- user.name@company.in

### Invalid Examples:
- test@
- user.com

---

## Indian Mobile Number Validation

### Rules:
- Must be 10 digits
- Must start with 6, 7, 8, or 9
- May optionally start with +91 or 91

### Regex Pattern:

^(?:\+91|91)?[6-9]\d{9}$

### Valid Examples:
- 9876543210
- +919876543210
- 919876543210

### Invalid Examples:
- 1234567890
- 98765

---

## Password Validation

### Rules:
- Minimum 8 characters
- At least one uppercase letter
- At least one lowercase letter
- At least one digit
- At least one special character (@$!%*?&)

### Regex Pattern:

^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$

### Valid Example:
- Pass@123
- Strong1@Pass

### Invalid Example:
- password
- Password1
- PASS@123

---

## Concepts Covered

- Regular Expressions (Regex)
- Pattern Matching
- Lookahead Assertions (?=)
- re.fullmatch() vs re.match()
- Input Validation
- Edge Case Handling
- Function-based Code Organization

---

## Learning Outcome

After completing this project, you will be able to:

- Validate user input in real-world applications
- Write reusable regex-based validation functions
- Handle edge cases effectively
- Build login/signup input validation logic
- Explain regex concepts confidently in interviews

---
