def main():
	with open("input.dat","r") as f:
		inp=list(f.readlines())
		word=inp[0].split("\n")[0]
		key=inp[1].split("\n")[0]
		
		mat=[[0 for i in range(5)] for j in range(5)]
		dickey={}
		count=0
		for i in key:
			if i not in dickey:
				dickey[i]=count
				mat[count//5][count%5]=i
				count+=1
		for i in range(26):
			if chr(ord('a')+ i)!="j":
				if chr(ord('a')+ i) not in dickey:
					dickey[chr(ord('a')+ i)]=count
					mat[count//5][count%5]=chr(ord('a')+ i)
					count+=1
		enc=""
		dec=""			
		if len(word)%2:
			word+='z'
		for i in range(len(word)//2):
			x=word[2*i]
			y=word[2*i  + 1]
			rowx=dickey[x]//5
			colx=dickey[x]%5
			rowy=dickey[y]//5
			coly=dickey[y]%5
			
			if rowx==rowy:
				enc+=mat[rowx][(colx + 1)%5]
				enc+=mat[rowy][(coly + 1)%5]
			elif colx==coly:
				enc+=mat[(rowx + 1)%5][(colx )]
				enc+=mat[(rowy + 1)%5][(coly )]
			else:
				enc+=mat[rowx][coly]
				enc+=mat[rowy][colx]
		
		
		for i in range(len(enc)//2):
			x=enc[2*i]
			y=enc[2*i  + 1]
			rowx=dickey[x]//5
			colx=dickey[x]%5
			rowy=dickey[y]//5
			coly=dickey[y]%5
			
			if rowx==rowy:
				dec+=mat[rowx][(colx - 1)%5]
				dec+=mat[rowy][(coly - 1)%5]
			elif colx==coly:
				dec+=mat[(rowx - 1)%5][(colx )]
				dec+=mat[(rowy - 1)%5][(coly )]
			else:
				dec+=mat[rowx][coly]
				dec+=mat[rowy][colx]
		
		print(enc,dec)
							
		
	f.close()
	
	with open("PlayFair.txt","w+") as f:
		f.write("Message : " + "".join(word) + '\n')
		f.write("Encrypted Message : " + "".join(enc) + '\n')
		f.write("Decrypted Message : " + "".join(dec) + '\n')
		
	f.close()
		
		
main()		

