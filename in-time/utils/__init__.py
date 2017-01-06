from hashlib import md5


def password_md5(password):
    return md5(password.encode('utf-8')).hexdigest()
