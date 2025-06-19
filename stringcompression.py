def python_string(s):
    list=[]
    count=1
    for i in range(1,len(s)):
        if s[i]==s[i-1]:
            count+=1
        else:
            list.append(s[i-1]+str(count))
            count=1
    list.append(s[-1]+str(count))
    result=''.join(list)
    return result if len(result)<len(s) else s
s="aaabbcccccdddd"
hello=python_string(s)
print(hello)
