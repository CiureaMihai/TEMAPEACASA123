import re


def check_password_strength(password):

    if len(password) < 8:
        return False


    if not re.search(r"[A-Z]", password):
        return False


    if not re.search(r"[a-z]", password):
        return False


    if not re.search(r"\d", password):
        return False

    if not re.search(r"[!@#$%^&*]", password):
        return False

    return True


password = input("Enter a password: ")

password_strength = check_password_strength(password)
strength_message = "meets the criteria" if password_strength else "does not meet the criteria"
print(f"Password strength: {password_strength} ({strength_message})")