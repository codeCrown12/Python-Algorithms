# An english student named John is currently doing an internship program in a grammar school.
# He has been given a task to document the number of vowels and consonants in a given word. So you have
# been hired by John to help automate the process by writing a program to solve the problem
# Example: countletters("King") -> [vowels: 1, consonants: 3]

def countvowels(word):
    answer = []
    vowelcount = 0
    conscount = 0
    vowels = "aeiou"
    for letter in word:
        if letter in vowels:
            vowelcount += 1
        else:
            conscount += 1
    answer.append(vowelcount)
    answer.append(conscount)
    return answer


val = input("Enter word: ")
ansarr = countvowels(val.lower())
print(f"[vowels: {ansarr[0]}, consonants: {ansarr[1]}]")