import hashlib

password = "admin"
print(hashlib.sha512(password.encode("utf-8")).hexdigest())