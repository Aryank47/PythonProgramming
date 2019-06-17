# program to check if a string is palindrome or not
print(sys.platform)
print("Enter the strings:")
s1 = input()
s2 = s1[::-1]
if s1 == s2:
    print("Palindrome")
else:
    print("Not Palindrome")
