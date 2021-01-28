from Crypto.PublicKey import DSA
from Crypto.Signature import DSS
from Crypto.Hash import SHA256
import time

# Create a new DSA key
start=time.time()
key = DSA.generate(2048)
print(time.time() - start)

f = open("public_key.pem", "wb")
print(type(key.publickey().export_key()))
f.write(key.publickey().export_key())
f.close()
# Sign a message
message = b"Hello"
hash_obj = SHA256.new(message)


signer = DSS.new(key, 'fips-186-3')
signature = signer.sign(hash_obj)



# Load the public key
f = open("public_key.pem", "r")
hash_obj = SHA256.new(message)
pub_key = DSA.import_key(f.read())
verifier = DSS.new(pub_key, 'fips-186-3')
# Verify the authenticity of the message
try:
    verifier.verify(hash_obj, signature)
    print("The message is authentic.")
except ValueError:
    print("The message is not authent")