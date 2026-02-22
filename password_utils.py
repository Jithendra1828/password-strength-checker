def load_common_passwords():
    try:
        with open("common_passwords.txt", "r") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []

def check_password_strength(password):
    score = 0
    suggestions = []
    special_characters = "!@#$%^&*"
    common_passwords = load_common_passwords()

    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters.")

    # Uppercase Check
    if any(char.isupper() for char in password):
        score += 1
    else:
        suggestions.append("Add at least one uppercase letter.")

    # Lowercase Check
    if any(char.islower() for char in password):
        score += 1
    else:
        suggestions.append("Add at least one lowercase letter.")

    # Digit Check
    if any(char.isdigit() for char in password):
        score += 1
    else:
        suggestions.append("Add at least one number.")

    # Special Character Check
    if any(char in special_characters for char in password):
        score += 1
    else:
        suggestions.append("Add at least one special character (!@#$%^&*).")

    # Common Password Check
    if password.lower() not in common_passwords:
        score += 1
    else:
        suggestions.append("Avoid common passwords.")

    # Strength Classification
    if score <= 2:
        strength = "Weak 🔴"
    elif score <= 4:
        strength = "Medium 🟡"
    else:
        strength = "Strong 🟢"

    percentage = int((score / 6) * 100)

    return {
        "score": score,
        "strength": strength,
        "percentage": percentage,
        "suggestions": suggestions
    }
