"""def compare(s1,s2,s3):
    
    if(s1<s2<s3):
        return s1+s2+s3
    if(s2<s3<s1):
        return s2+s3+s1
    if(s3<s1<s2):
        return s3+s1+s2
    if(s3<s2<s1):
        return s3+s2+s1
    if(s2<s1<s3):
        return s2+s1+s3
    else :
        return s1+s3+s2

print(compare("hack","hacker","hackerrank"))"""
"""def complimentdna(s):
    s=s[::-1]
    compliment=""
    for c in s:
        if(c=="T"):
            compliment+="A"
        if(c == "A"):
            compliment+="T"
        if(c == "C"):
            compliment+="G"
        if(c == "G"):
            compliment+="C"
    return compliment

print(complimentdna("ACCGGGTTTT"))"""

def partionner(k ,numbers) :
    i=0
    partition = [[],[],[]]
    if k > len(numbers):
        return "No1"
    if (len(numbers) % k != 0 ):
        return "No2"
    else:
        n = len(numbers) // k
        for i in range(n):
            partition.append([])
        for i in range(n):
            partition[i] = numbers[i*k:k]
            for j in partition[i]:
               if j in numbers[k:] :
                   return "No3"
        return "Yes"

        

print(partionner(3,[1,2,3,4,3,6]))









