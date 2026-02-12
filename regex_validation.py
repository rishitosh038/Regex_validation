import re 

# Email Validation Function
def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not email:
        return "Email cannot be empty."
    if re.fullmatch(pattern, email):
        return "Valid Email"
    return "Invalid Email"

# Indian Mobile Validation Function
def validate_phone(phone):
    pattern = r'^(?:\+91|91)?[6-9]\d{9}$'
    if not phone:
        return "Phone number cannot be empty."
    if re.fullmatch(pattern, phone):
        return "Valid Indian Mobile Number"
    return "Invalid Indian Mobile Number"

# Password Validation Function
def validate_password(password):
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
    if not password:
        return "Password cannot be empty."
    if re.fullmatch(pattern, password):
        return "Strong Password"
    return """Invalid Password
Requirments:
- Minimum 8 characters
- At least one uppercase letter
- At least one Lowercase letter
- At least one digit
- At least one special character (@$!%*?&)
"""

# Main Program
def main():
    print("=== REGEX VALIDATION PROGRAM ===")

    email = input("Enter the Email: ")
    print(validate_email(email))

    phone = input("Enter Indian Mobile Number: ")
    print(validate_phone(phone))

    password = input("Enter Password: ")
    print(validate_password(password))

if __name__ == "__main__":
    main()