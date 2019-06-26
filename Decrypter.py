'''1=A
26=Z
27=AA
28=AB
1000=ALL 
proof:
    1000/26=38
    38>26
    38/26=1
        1=A
    38%26=12 
        12=L
    1000%26=12
        12=L
    Thus, 1000=ALL
'''
dic={1:'A',2:'B',3:'C',4:'D',5:'E',6:'F',7:'G',8:'H',9:'I',10:'J',11:'K',12:'L',13:'M',14:'N',15:'O',16:'P',17:'Q',18:'R',19:'S',20:'T',21:'U',22:'V',23:'W',24:'X',25:'Y',26:'Z'}
def split(x):
    if(x<=26):
        print(dic[x])
    else:
        r=x%26
        b=int(x/26)
        if(b>26):
            split(b)
        else:
            print(dic[b])
        print(dic[r])

a=int(float(input("Enter the No to be Decrypted:")))
print("The converted text:")
split(a)
