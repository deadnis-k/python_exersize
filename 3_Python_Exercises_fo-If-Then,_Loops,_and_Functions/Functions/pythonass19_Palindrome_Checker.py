def is_palindrome(word):
    x=word[len(word)-1] 
    temp_word=x 
    for i in range(2,len(word)+1):
        x = word[-i]
        temp_word=temp_word+x
        print(temp_word)
    if temp_word == word:
        return True
    return False


word=("racecar")
x = is_palindrome(word)
print(x)