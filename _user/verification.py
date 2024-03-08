def email_verification(email):
    if '@' not in email:
        return False
    return True


def password_verification(password):
    if len(password) < 6:
        return False
    return True

