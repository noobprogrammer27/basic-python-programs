#Find the position from where the parenthesis is not balanced??

string=input()
lst=[]
lst1=['{','(','[']
lst2=['}',')',']']
a=b=c=0
Dict={'}':'{',')':'(',']':'['}
if string[0] in lst2:
    print(1)
else:
    for i in range(len(string)):
        if string[i] in lst1:
            lst.append(string[i])
            k=i+2 
        else:
            if len(lst)==0 and (string[i] in lst2):
                print(i+1)
                c=1 
                break
            else:
                if Dict[string[i]]==lst[len(lst)-1]:
                    lst.pop()
                else:
                    print(i+1)
                    a=1 
                    break
    if len(lst)==0 and c==0:
        print(0)
        b=1 
    if(a==0 and b==0  and c==0):
        print(k)


"""input:
{}{}}
output:
5"""
