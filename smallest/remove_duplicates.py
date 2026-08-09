def remove_duplicates(str1):
    li = []
    str1 = str1 + ' '
    word = ''
    for i in range(0,len(str1)):
        if str1[i] != ' ' :
            word = word + str1[i]
        else:
            if word !='':
                li.append(word)
            word = ''




    ans = []
    for i in li:
        if i not in ans:
            ans.append(i)
    return ans        

inp = input('Enter a sentence:')
ans = remove_duplicates(inp)
print(ans)
