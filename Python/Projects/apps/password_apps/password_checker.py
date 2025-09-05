passward = input("Enter the passward: ")
def check_password_strength(password):
    missing = []
    
    if len(password) < 8:
        missing.append("at least 8 characters")
    if not any(char.isupper() for char in password):
        missing.append("uppercase letter")
    if not any(char.islower() for char in password):
        missing.append("lowercase letter")
    if not any(char.isdigit() for char in password):
        missing.append("digit")
    if not any(not char.isalnum() for char in password):
        missing.append("special character")
    
    if not missing:
        return "Strong password!"
    else:
        return f"Weak password: Missing {', '.join(missing)}"

print(check_password_strength(passward))  