def pre_process(msg,round_key):
    data=dict()
    a=list(round_key)
    a.sort()
    # print(a)
    round_num={}
    cc=0
    for ele in enumerate(a):
        t=ele[1]
        try:
            if t in round_num.keys():
                raise TypeError()
            round_num[t]=ele[0]+1
        except :
            raise TypeError("Duplicate Character Key is not Allowed")
            
    # print(round_num)
    for s in round_key:
        data[s]=round_num[s]
    print(data)  

    import math
    row=math.ceil(len(msg)/len(round_key))

    row=row+1
    column=len(round_key)
    print("Rowsize : ",row)


    #populate matrix of size row*column
    table=[["$"]*column for i in range(row)]
    idx=0
    val=list(data.values())
    # print(val)
    while idx<len(val):
        table[0][idx]=val[idx]
        idx=idx+1

    print("Initial Table")
    printTable(table)
    return table,data

def printTable(table):
    for i in range(row):
        for j in range(column):
            print(table[i][j],end=' ')
        print(" ")

def encrypt(msg,round_key):
    msg=msg.upper().replace(" ","")
    idx=0
    table,data=pre_process(msg,round_key)
    row=len(table)
    column=len(table[0])
    print("MSG LEN: ",len(msg))
    #Arrange the msg row-wise
    for i in range(1,row):
        flag=False
        for j in range(column):
    #         print(i,j,idx)
            table[i][j]=msg[idx]
            idx=idx+1
            if idx==len(msg):
                flag=True
                break           
        if flag:
            break

    printTable(table)
    #creating the cipher by reading column-wise
    cipher_text=""
    for ele in range(len(round_key)):
        ele=ele+1
        idx=0
        for i in range(column):
            if table[0][i]==ele:
                idx=i
                break
    #     print(idx)
    #     print(row)
        for j in range(1,row):
    #         print(j)
            tt=table[j][idx]
            cipher_text=cipher_text+tt
    print("Cipher Text: ",cipher_text)
    return cipher_text

def decrypt(msg,round_key):
    table,data=pre_process(msg,round_key)
    row=len(table)
    column=len(table[0])
    print("Encrypted MSG LEN: ",len(msg))
    idx_c=0
    #Insert Column wise
    for ele in range(len(round_key)):
        ele=ele+1
        idx=0
        for i in range(column):
            if table[0][i]==ele:
                idx=i
                break
        for j in range(1,row):
            table[j][idx]=msg[idx_c]
            idx_c+=1
    print(table)
    
    decipher_text=""
    #Read Row wise
    for i in range(1,row):
        for j in range(column):
            decipher_text+=table[i][j]
    print("Decipher Text: ",decipher_text)
    return decipher_text
        from itertools import permutations 
def findPermutation(str):
    alist=list(permutations(str))
    permutationList=list()
#     print(permutationList)
    for p in alist:
        permutationList.append("".join(p))
    print(permutationList)
    return permutationList
for perm in findPermutation("ABC"):
    dec1=decrypt(cipher,perm)
    print(dec1)

round_key1="COMPUTER" #ALWAYS USE SAME KEY SIZE FOR BOTH ROUNDS
round_key2="RAKSHITM"
msg="We are living in beautiful world"
encrypted_text1=encrypt(msg,round_key1)
encrypted_text2=encrypt(encrypted_text1,round_key2)
decrypted_text2=decrypt(encrypted_text2,round_key2)
decrypted_text1=decrypt(decrypted_text2,round_key1)

print("PLAIN TEXT: ",msg)
print("ENCRYPTED 1: ",encrypted_text1)
print("ENCRYPTED 2: ",encrypted_text2)
print("DECRYPTED 2: ",decrypted_text2)
print("DECRYPTED 1: ",decrypted_text1)

OUTPUT:
PLAIN TEXT:  We are living in beautiful world
ENCRYPTED 1:  WIURIEW$AGIDENTLRIF$VAO$LBL$ENU$
ENCRYPTED 2:  IGIBIEVEENANUIFL$L$$WARLRD$$WTOU
DECRYPTED 2:  WIURIEW$AGIDENTLRIF$VAO$LBL$ENU$
DECRYPTED 1:  WEARELIVINGINBEAUTIFULWORLD$$$$$
