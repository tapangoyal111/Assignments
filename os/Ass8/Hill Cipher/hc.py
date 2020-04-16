
# Hill Cipher

import random
import numpy

def inverse_mod_n(a,m):
	
	a=a%m
	for i in range(1,m):
		if((a*i)%m == 1):
			return(i)
	return(1)

def gcd(a,b):
	if(b==0):
		return(a)
	else:
		return(gcd(b,a%b))

def inverse(mat,mod):
	m = len(mat)
	n = len(mat[0])
	mat1 = [[0 for i in range(n)] for j in range(m)]
	for i in range(m):
		for j in range(n):
			temp_mat = []
			for k in range(m):
				x = []
				for l in range(n):
					if(k!=i and l!=j):
						x.append(mat[k][l])
				if(len(x)!=0):
					temp_mat.append(x)
			temp_det = numpy.linalg.det(temp_mat)
			mat1[i][j] = ((-1)**(i+j))*int(round(temp_det))
	
	for i in range(m):
		for j in range(i):
			mat1[i][j],mat1[j][i] = mat1[j][i],mat1[i][j]
	
	det_mat = int(round(numpy.linalg.det(mat)))
	if(gcd(det_mat,mod)!=1):
		return(-1)
	det_inv_mod = inverse_mod_n(det_mat,mod)
	for i in range(m):
		for j in range(n):
			mat1[i][j] = (mat1[i][j]*det_inv_mod)%mod
	
	return(mat1)


def matrix_mult(a,b,mod):
	res = [[0 for i in range(len(b[0]))] for j in range(len(a))]
	for i in range(len(res)):
		for j in range(len(res[0])):
			for k in range(len(a[0])):
				res[i][j] += a[i][k]*b[k][j]
			res[i][j] = res[i][j]%mod
	return(res)

def hill_cipher_encrypt(encrypt_mat,plaintext):
	# length of encryption matrix
	n = len(encrypt_mat)
	# length of plaintext
	n1 = len(plaintext)
	# padding if necessary
	if(n1%n!=0):
		for i in range(n-n1%n):
			plaintext += 'x'
	n1 = len(plaintext)
	# plaintext matrix
	p = [[0 for i in range(n1//n)] for j in range(n)]
	ct=0
	# plaintext matrix generation
	for i in range(n1//n):
		for j in range(n):
			temp = ord(plaintext[ct])
			if(temp<97):
				p[j][i] = ord(plaintext[ct])-48+26
			else:
				p[j][i] = ord(plaintext[ct])-97
			ct+=1

	# get cipher text matrix
	cipher_mat = matrix_mult(encrypt_mat,p,36)

	# get cipher text from cipher matrix
	cipher_text= ''
	for i in range(len(cipher_mat[0])):
		for j in range(len(cipher_mat)):
			if(cipher_mat[j][i]>25):
				cipher_text += chr(cipher_mat[j][i]+48-26)
			else:
				cipher_text += chr(cipher_mat[j][i]+97)
	return(cipher_text)

def hill_cipher_decrypt(decrypt_mat,cipher_text):
	# length of decryption matrix
	n = len(decrypt_mat)
	#length of cipher text
	n1 = len(cipher_text)

	# get cipher text matrix form cipher text
	p = [[0 for i in range(n1//n)] for j in range(n)]
	ct=0
	for i in range(n1//n):
		for j in range(n):
			temp = ord(cipher_text[ct])
			if(temp<97):
				p[j][i] = ord(cipher_text[ct])-48+26
			else:
				p[j][i] = ord(cipher_text[ct])-97
			ct+=1
	
	# get plain text matrix
	plain_mat = matrix_mult(decrypt_mat,p,36)
	
	# get plain text from plain text matrix
	plaintext= ''
	for i in range(len(plain_mat[0])):
		for j in range(len(plain_mat)):
			if(plain_mat[j][i]>25):
				plaintext += chr(int(round(plain_mat[j][i]))+48-26)
			else:
				plaintext += chr(int(round(plain_mat[j][i]))+97)
	
	return(plaintext)


def main():
	file = open('input.dat','r')
	lines = file.readlines()
	plaintext = lines[0].strip()
	print("Hill cipher: ")
	# get encryption matrix
	encrypt_mat = []
	for i in range(1,len(lines)):
		encrypt_mat.append(list(map(int,lines[i].strip().split())))
	# encrypt plaintext to cipher text
	cipher_text = hill_cipher_encrypt(encrypt_mat,plaintext)
	f = open('output.txt','w')
	f.write("Message : " + plaintext + '\n')
	f.write("Encrypted Message : " + cipher_text + '\n')
	print("Cipher text: ",cipher_text)

	# get decryption matrix by inversing encryption matrix
	decrypt_mat = inverse(encrypt_mat,36)

	# decrypt the message
	dec_mess=hill_cipher_decrypt(decrypt_mat,cipher_text)
	f.write("Decrypted Message : " + dec_mess + '\n')
	print(dec_mess)
	f.close()
		
main()
