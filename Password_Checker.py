import re

def assess_password_strength(password):
    # Check password length
    length_score = min(2, len(password) // 4)

    # Check for presence of uppercase letters
    uppercase_score = 2 if re.search(r'[A-Z]', password) else 0

    # Check for presence of lowercase letters
    lowercase_score = 2 if re.search(r'[a-z]', password) else 0

    # Check for presence of numbers
    numbers_score = 2 if re.search(r'\d', password) else 0

    # Check for presence of special characters
    special_characters_score = 2 if re.search(r'[!@#$%^&*(),.?":{}|<>]', password) else 0

    # Calculate total score
    total_score = length_score + uppercase_score + lowercase_score + numbers_score + special_characters_score

    # Provide feedback on password strength
    if total_score < 5:
        return "Weak password"
    elif total_score <= 8:
        return "Moderate password"
    else:
        return "Strong password"

# Example usage
password = input("Enter your password: ")
result = assess_password_strength(password)
print(result)