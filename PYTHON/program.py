import rsa

public_key, private_key = rsa.newkeys(2048)

message = "Czkawka Gustawa".encode(encoding="utf-8")

encrypted_message = rsa.encrypt(message, public_key)

print(encrypted_message)