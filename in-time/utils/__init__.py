from hashlib import md5


def md5_hex(string):
    return md5(string.encode('utf-8')).hexdigest()
