def is_substring(s1,s2):
    if s1 in s2:
        return s2.index(s1)
    return -1

if __name__ == "__main__":
    s1 = 'Hello'
    s2 = 'Hello World'
    result = is_substring(s1, s2)
    if result != -1:
        print(f"'{s1} is a substring of '{s2}' at index {result}.")
    else :
        print('Not Present')    
