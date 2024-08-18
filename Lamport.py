import secrets
import hashlib

class Lamport:

    def GenerateKey(key_length):
        
        private_key = [[],[]]
        public_key = [[],[]]
        for _ in range(key_length):
            random_number1 = secrets.token_bytes(key_length//8)
            random_number2 = secrets.token_bytes(key_length//8)
            private_key[0].append(random_number1)
            private_key[1].append(random_number2)
        #public key creation
        for i in range(len(private_key)):
            for priv_num in private_key[i]:
                public_key[i].append(hashlib.sha256(priv_num).hexdigest())
        return public_key, private_key
    

    def Sign(message, private_key):

        encoded_message = message.encode("utf-8")
        hashed_message = hashlib.sha256(encoded_message).hexdigest()
        byte_array = bytearray.fromhex(hashed_message)

        # Convert each byte to a binary string (8 bits per byte)
        bit_string = ''.join(f'{b:08b}' for b in byte_array)

        signature = []
        newprivkey = []
        for i,j in zip(bit_string, range(len(bit_string))):
            signature.append(private_key[int(i)][j])
    
        return signature
    

    def Verify(message, public_key, signature):
        encoded_message = message.encode("utf-8")
        hashed_message = hashlib.sha256(encoded_message).hexdigest()
        byte_array = bytearray.fromhex(hashed_message)

        # Convert each byte to a binary string (8 bits per byte)
        bit_string = ''.join(f'{b:08b}' for b in byte_array)
        chosen_number = []
        newprivkey = []
        hashed_signature = []
        for i,j,z in zip(bit_string,signature ,range(len(bit_string))):
            hash1 = public_key[int(i)][z]
            hash2 = hashlib.sha256(j).hexdigest()
            chosen_number.append(hash1)
            hashed_signature.append(hash2)
        if chosen_number == hashed_signature:
         print("Verified!")
         return "Verified!"
        else:
          print("Not Verified!")
          return "Not Verified"
       
    
public_key, private_key = Lamport.GenerateKey(256)
message = "Farida Mohamed Abdelazeez"
signature= Lamport.Sign(message, private_key)
Lamport.Verify(message, public_key, signature)  