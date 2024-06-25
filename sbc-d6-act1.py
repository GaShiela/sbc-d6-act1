pal = input("ENTER ANY WORD: ")
cleaned_pal = pal.replace(" ", "").upper()

is_palindrome = True

for i in range(len(cleaned_pal) // 2):
    if cleaned_pal[i] != cleaned_pal[-(i + 1)]:
        is_palindrome = False
        break

if is_palindrome:
    print("Palindrome")
else:
    print("Not a palindrome")