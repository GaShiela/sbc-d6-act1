word = input("Enter a word: ").lower().replace(" ", "")
pal = True

for i in range(len(word) // 2):
    if word[i] != word[-i - 1]:
        pal = False
        break

if pal:
    print("Palindrome")
else:
    print("Not Palindrome")