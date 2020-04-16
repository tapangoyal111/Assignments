from BitVector import *

AES_modulus = BitVector(bitstring='100011011')

statearray = [[0 for x in range(4)] for x in range(4)]
plaintext = ['@','b','c','d','e','f','g','h','i','j','k','l','m','n','o',1]
print("Plaintext is: ")
print(plaintext)
print()
for i in range(4):
	for j in range(4):
		if (type(plaintext[i*4 + j]) is str):
			statearray[j][i] = BitVector(textstring=plaintext[i*4 + j])
		else:
			statearray[j][i] = BitVector(intVal=plaintext[i*4 + j],size=8)

'''for i in range(4):
	for j in range(4):
		print(statearray[j][i],end="  ")
	print()'''

def gen_subbytes_table():
    subBytesTable = []
    c = BitVector(bitstring='01100011')
    for i in range(0, 256):
        a = BitVector(intVal = i, size=8).gf_MI(AES_modulus, 8) if i != 0 else BitVector(intVal=0)
        a1,a2,a3,a4 = [a.deep_copy() for x in range(4)]
        a ^= (a1 >> 4) ^ (a2 >> 5) ^ (a3 >> 6) ^ (a4 >> 7) ^ c
        subBytesTable.append(int(a))
    return subBytesTable

def gen_invsubbytes_table():
	invSubBytesTable=[]
	d = BitVector(bitstring='00000101')
	# For the decryption Sbox:
	for i in range(0, 256):
		b = BitVector(intVal = i, size=8)
		# For bit scrambling for the decryption SBox entries:
		b1,b2,b3 = [b.deep_copy() for x in range(3)]
		b = (b1 >> 2) ^ (b2 >> 5) ^ (b3 >> 7) ^ d
		check = b.gf_MI(AES_modulus, 8)
		b = check if isinstance(check, BitVector) else 0
		invSubBytesTable.append(int(b))
	return invSubBytesTable

def gee(keyword, round_constant, byte_sub_table):
    '''
    This is the g() function you see in Figure 4 of Lecture 8.
    '''
    rotated_word = keyword.deep_copy()
    rotated_word << 8
    newword = BitVector(size = 0)
    for i in range(4):
        newword += BitVector(intVal = byte_sub_table[rotated_word[8*i:8*i+8].intValue()], size = 8)
    newword[:8] ^= round_constant
    round_constant = round_constant.gf_multiply_modular(BitVector(intVal = 0x02), AES_modulus, 8)
    return newword, round_constant

def gen_key_schedule_128(key_bv):
    byte_sub_table = gen_subbytes_table()
    #  We need 44 keywords in the key schedule for 128 bit AES.  Each keyword is 32-bits
    #  wide. The 128-bit AES uses the first four keywords to xor the input block with.
    #  Subsequently, each of the 10 rounds uses 4 keywords from the key schedule. We will
    #  store all 44 keywords in the following list:
    key_words = [None for i in range(44)]
    round_constant = BitVector(intVal = 0x01, size=8)
    for i in range(4):
        key_words[i] = key_bv[i*32 : i*32 + 32]
    for i in range(4,44):
        if i%4 == 0:
            kwd, round_constant = gee(key_words[i-1], round_constant, byte_sub_table)
            key_words[i] = key_words[i-4] ^ kwd
        else:
            key_words[i] = key_words[i-4] ^ key_words[i-1]
    return key_words

keysize = int(input("Enter the length of Key(128, 192 or 256 only): "))
Nk = keysize // 32 #Number of 32-bit words in the key
Nr = Nk + 6  #Number of rounds
key = input("\nEnter key (any number of chars): ")
key = key.strip()
key += '0' * (keysize//8 - len(key)) if len(key) < keysize//8 else key[:keysize//8] 
key_bv = BitVector( textstring = key )
key_words = gen_key_schedule_128(key_bv)

round_keys = [None for i in range(Nr+1)]
for i in range(Nr+1):
    round_keys[i] = (key_words[i*4] + key_words[i*4+1] + key_words[i*4+2] + key_words[i*4+3])
#print("\n\nRound keys in hex (first key for input block):\n")
#for round_key in round_keys:
    #print(round_key)

#Function to Add round key
def AddRoundKey(round):
	round_key=round_keys[round]
	for i in range(4):
		for j in range(4):
			statearray[j][i] ^= round_key[i*32 + j*8 : i*32 + (j+1)*8]

#Function for substitution bytes
s_box = gen_subbytes_table()
def SubBytes(s):
    for i in range(4):
        for j in range(4):
            s[i][j] = BitVector(intVal=s_box[int(s[i][j])],size=8)

invs_box = gen_invsubbytes_table()
def InvSubBytes(s):
    for i in range(4):
        for j in range(4):
            s[i][j] = BitVector(intVal=invs_box[int(s[i][j])],size=8)

#Function for shift rows
def ShiftRows(s):
    s[1][0], s[1][1], s[1][2], s[1][3] = s[1][1], s[1][2], s[1][3], s[1][0]
    s[2][0], s[2][1], s[2][2], s[2][3] = s[2][2], s[2][3], s[2][0], s[2][1]
    s[3][0], s[3][1], s[3][2], s[3][3] = s[3][3], s[3][0], s[3][1], s[3][2]

def InvShiftRows(s):
    s[1][0], s[1][1], s[1][2], s[1][3] = s[1][3], s[1][0], s[1][1], s[1][2]
    s[2][0], s[2][1], s[2][2], s[2][3] = s[2][2], s[2][3], s[2][0], s[2][1]
    s[3][0], s[3][1], s[3][2], s[3][3] = s[3][1], s[3][2], s[3][3], s[3][0]

def Multiply(x,y):
	return x.gf_multiply_modular(BitVector(intVal = y), AES_modulus, 8)

#Function for mixing columns
def MixColumns(s):
    for i in range(4):
        a=s[0][i]
        b=s[1][i]
        c=s[2][i]
        d=s[3][i]

        s[0][i] = Multiply(a, 0x02) ^ Multiply(b, 0x03) ^ Multiply(c, 0x01) ^ Multiply(d, 0x01)
        s[1][i] = Multiply(a, 0x01) ^ Multiply(b, 0x02) ^ Multiply(c, 0x03) ^ Multiply(d, 0x01)
        s[2][i] = Multiply(a, 0x01) ^ Multiply(b, 0x01) ^ Multiply(c, 0x02) ^ Multiply(d, 0x03)
        s[3][i] = Multiply(a, 0x03) ^ Multiply(b, 0x01) ^ Multiply(c, 0x01) ^ Multiply(d, 0x02)

def InvMixColumns(s):
    for i in range(4):
        a=s[0][i]
        b=s[1][i]
        c=s[2][i]
        d=s[3][i]

        s[0][i] = Multiply(a, 0x0E) ^ Multiply(b, 0x0B) ^ Multiply(c, 0x0D) ^ Multiply(d, 0x09)
        s[1][i] = Multiply(a, 0x09) ^ Multiply(b, 0x0E) ^ Multiply(c, 0x0B) ^ Multiply(d, 0x0D)
        s[2][i] = Multiply(a, 0x0D) ^ Multiply(b, 0x09) ^ Multiply(c, 0x0E) ^ Multiply(d, 0x0B)
        s[3][i] = Multiply(a, 0x0B) ^ Multiply(b, 0x0D) ^ Multiply(c, 0x09) ^ Multiply(d, 0x0E)

def Cipher():
	AddRoundKey(0)
	for round in range(1,Nr):
		SubBytes(statearray)
		ShiftRows(statearray)
		MixColumns(statearray)
		AddRoundKey(round)
	SubBytes(statearray)
	ShiftRows(statearray)
	AddRoundKey(Nr)
	ciphertext=[None for x in range(16)]
	for i in range(4):
		for j in range(4):
			ciphertext[i*4 + j] = int(statearray[j][i])
	return ciphertext

def InvCipher():
	AddRoundKey(Nr)
	for round in range(Nr-1,0,-1):
		InvShiftRows(statearray)
		InvSubBytes(statearray)
		AddRoundKey(round)
		InvMixColumns(statearray)
	InvShiftRows(statearray)
	InvSubBytes(statearray)
	AddRoundKey(0)
	ciphertext=[None for x in range(16)]
	for i in range(4):
		for j in range(4):
			ciphertext[i*4 + j] = int(statearray[j][i])
	return ciphertext
	
	
ciphertext=Cipher()
ptext = InvCipher()

print("\nCiphertext after encryption: ")
print(ciphertext)

print("\nPlaintext after decryption: ")
print(ptext)

with open("output.txt","w+") as f:
	mess=""
	cip=""
	dec=""
	for i in plaintext:
		mess+=str(i)
	for i in ciphertext:
		if i<10:
			cip+=str(i)
		else:
			cip+=chr(i)
				
	for i in ptext:
		if i<10:
			dec+=str(i)
		else:
			dec+=chr(i)
		
	f.write("Message : " + mess + '\n')
	f.write("Encrypted Message : " + cip + '\n')
	f.write("Decrypted Message : " + dec + '\n')
	f.close()

print("\nCiphertext after encryption: ")
print(cip)

print("\nPlaintext after decryption: ")
print(dec)
