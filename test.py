palindrome_list = []
count = 0
for i in range(100, 999):
    palindrome = (str(i))
    palindrome += palindrome[::-1]
    palindrome_list.append(palindrome)
for num in palindrome_list:
    if int(num) % 9 == 0:
        print(num)
        count += 1
        print(count)