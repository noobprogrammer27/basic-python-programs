#code to find lexicographic minimum in a circular array using python:
def MinRotation(str):
    n=len(str)
    arr=[0]*n
    concat=str+str
    for i in range(n):
        arr[i]=concat[i:n+i]
        print(arr[i])#here we are printing all the lexicograpgic inputs.if you do't need "then remove it"
    arr.sort()
    print(arr[0])
MinRotation("BCABDADAB")

"""i/p:
BCABDADAB
o/p:
BCABDADAB
CABDADABB
ABDADABBC
BDADABBCA
DADABBCAB
ADABBCABD
DABBCABDA
ABBCABDAD
BBCABDADA
ABBCABDAD
"""
