import re

def check_password_strength(password):
    score = 0
    length_criteria = len(password) >= 8
    upper_criteria = re.search(r"[A-Z]", password)
    lower_criteria = re.search(r"[a-z]", password)
    digit_criteria = re.search(r"[0-9]", password)
    special_criteria = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)

    if length_criteria:
        score += 1
    if upper_criteria:
        score += 1
    if lower_criteria:
        score += 1
    if digit_criteria:
        score += 1
    if special_criteria:
        score += 1

    return score

def password_feedback(score):
    if score == 5:
        return "Very Strong"
    elif score == 4:
        return "Strong"
    elif score == 3:
        return "Moderate"
    elif score == 2:
        return "Weak"
    else:
        return "Very Weak"

if __name__ == "__main__":
    password = input("Enter a password to check strength: ")
    score = check_password_strength(password)
    print(f"Password Score: {score}/5")
    print(f"Strength: {password_feedback(score)}")
