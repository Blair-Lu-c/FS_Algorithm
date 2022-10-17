class Vigenere:
    """
    Develop the class to encrypt and decrypt using the cipher developed by Vigenere.
    """
    # define a Alphabet list
    letter_list = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    
    # create key list
    def __init__(self, key):
        self.key_list=[]    # an empty list to store key list
        self.key = key
        # convert each character of key to number
        for ch in key:
            self.key_list.append(ord(ch.upper())-65)
    
    # create Encrypt function
    def encrypt(self, plaintext):
        ciphertext = "" # an empty string to store encrypt result
        i = 0   # initialize an index of plaintext to 0
        while i < len(plaintext):
            for ch in plaintext:    # each character of plaintext
                if ch.isupper():    
                    ciphertext += self.letter_list[(ord(ch) - 65 + self.key_list[i % len(self.key_list)]) % 26]        
                    i += 1
                else:
                    ciphertext += self.letter_list[(ord(ch) - 97 + self.key_list[i % len(self.key_list)]) % 26].lower()
                    i += 1
        return ciphertext
        
        
    def decrypt(self, ciphertext):
        plaintext = ""  # an empty string to store decrypt result
        i = 0   # initialize an index of ciphertext to 0
        while i < len(ciphertext):
            for ch in ciphertext:   # each character of ciphertext
                if ch.isupper():
                    plaintext += self.letter_list[(ord(ch) - 65 - self.key_list[i % len(self.key_list)] + 26) % 26]
                    i += 1
                else:
                    plaintext += self.letter_list[(ord(ch) - 97 - self.key_list[i % len(self.key_list)] + 26) % 26].lower()
                    i += 1
        return plaintext
    
v = Vigenere("house")
cipher_text = v.encrypt("Algorithm")
message = v.decrypt("Hzagvphbe")
assert (message == "Algorithm"), "encrypt, decrypt did not result in same message"

if __name__ == '__main__':
    user_input = input("Press E to encrypt, press D to decrypt: ")
    while(user_input!='D' and user_input!='E'):
        print("Input error, please enter again! Press E to encrypt, press D to decrypt:")
        user_input=input()
        
    key = input("Please enter a key: ")
    while(False==key.isalpha()):
        key=input("Input error, the key should be alphabet, please enter again!: ")
    
    v = Vigenere(key)
    
    if user_input == "E":
        plaintext = input("Please input plaintext: ")
        print(v.encrypt(plaintext))
        
    if user_input == "D":
        ciphertext = input("Please input ciphertext: ")
        print(v.decrypt(ciphertext))    
    