#Write a function that takes a string and returns the count of vowels and consonants. For example, for the input "hello world", the output should be {'vowels': 3, 'consonants': 7}.

def count_vowels_and_consonants(s):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    consonant_count = 0
    
    for char in s:
        if char.isalpha(): 
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
    
    return {'vowels': vowel_count, 'consonants': consonant_count}

    result = count_vowels_and_consonants("hello world")
    print(result)
