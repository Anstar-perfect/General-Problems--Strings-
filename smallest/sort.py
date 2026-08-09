def sort(s):
    li = []
    ans = ''
    for i in range(26):
        li.append(0)
    for i in range((len(s))):
        ind = ord(s[i])-ord('a')
        li[ind] += 1
    for i in range(26):
        if li[i] >= 1:
            for j in range(li[i]):
                ans += chr(i+ord('a'))
    return ans

print(sort('hello')) 
           