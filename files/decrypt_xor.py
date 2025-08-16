with open("encrypted_memo.dat", "rb") as f:
    data = f.read()

key = 0x42  
decrypted = ''.join([chr(b ^ key) for b in data])
print("Flag:", decrypted)
