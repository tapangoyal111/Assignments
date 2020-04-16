#RC4 ALgoRithm

d1={}
for i in range(256):
	p=bin(i)[2:]
	d1[chr(i)]="0"*(8-len(p)) + p

		
		
def wordToKey(w):
	s="0"
	for i in w:
		s+=d1[i]
	return list(s)


def main():
	with open("input.dat","r") as f:
		inp=list(f.readlines())
		word=inp[0].split("\n")[0]
		initialKey=inp[1].split("\n")[0]
		# word=wordToKey(word)
		# initialKey=wordToKey(initialKey)
		initialKey=[ord(initialKey[i]) for i in range(len(initialKey))]
		s=[i for i in range(256)]
		t=[0 for i in range(256)]
		for i in range(256):
			t[i]=initialKey[i%len(initialKey)]
		j=0
		for i in range(256):
			j=(j + s[i] + t[i])%256
			s[i],s[j]=s[j],s[i]
		n=len(word)
		i=0;j=0
		cipherText=""
		key=[]
		while n>0:
			i=(i+1)%256
			j=(j+s[i])%256
			s[i],s[j]=s[j],s[i]
			k=s[i] + s[j]
			key.append(s[k%256])
			n-=1
		n=len(word)
		for i in range(n):
			cipherText+=chr(key[i]^ord(word[i]))
			
		print("cipherText",cipherText)
		decryptText=""
		for i in range(n):
			decryptText+=chr(key[i]^ord(cipherText[i]))
		
		print("decryptText",decryptText)
		
					
				
main()
