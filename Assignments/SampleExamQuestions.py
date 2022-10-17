# Q1
# This program will check if a given string is a palindrome
def isPalindrome(x):
    x = x.lower()   # convert all elements of string to lowercase 
    res = x[::-1]   # reverse the string
    return x == res # # check if the string is equal to its reverse, return True or False

# Driver program to test the above function
print(isPalindrome("Anna"))

# Time complexity: O(N), Where N is the length of the given string.

# Q2
# This program will find all palindromic sections of a given string longer than one
def findAllPalindrome(s):
    s = s.lower()   # convert all elements of string to lowercase
    allpalindrome = []  # create an empty list to store all palindromes
    palindrome = "" # create an empty string to store reseltant palindrome
    for i in range(len(s)):   #
        for j in range(i):
            if s[j:i+1] == s[j:i+1][::-1]:
                palindrome = s[j:i+1]
                if len(palindrome) > 1:
                    allpalindrome.append(palindrome)
    return allpalindrome
print(findAllPalindrome("intellect"))


# Q3
def allFibonacci(num):
    lst = [0, 1]
    i = 1
    while num >= lst[i]:
        lst.append(lst[i-1]+lst[i])
        i += 1
    return lst[:i]
print(allFibonacci(11))

# Q4
def isIncreasing(seq):
    i = 0
    while i < len(seq)-1:
        if int(seq[i]) >= int(seq[i+1]):
            return False
        else: 
            i += 1
    return True
print(isIncreasing([1,2,4,5,8,9]))

# Q5
def longestLengthIncreaing(seq):
    l = len(seq)
    n = []
    dp = [1]*l
    for i in range(1,l):
        if seq[i-1] < seq[i]:
            dp[i] = dp[i-1] + 1
    return max(dp)
print(f"'Q5'",longestLengthIncreaing([2,6,4,6,11,8,9,10,89,100,111,11]))

def longestIncreaing(seq):
    i = 0
    start_index = 0
    lst = []
    while i < (len(seq)-1):
        if seq[i] >= seq[i+1]:
            new_list = seq[start_index:i+1]
            print(i+1)
            if len(lst) < len(seq[start_index:i+1]):
                lst = seq[start_index:i+1]
                print(start_index,i+1)
            start_index = i + 1
            print(start_index,i+1)
        i += 1
    return lst

print(longestIncreaing([1,2,5,3,5,19,21,1,2,5,6,23,34,45,100]))
            
            
# Q6
def isAnagram(x,y):
    return sorted(x) == sorted(y)
print(isAnagram("anagram","margana"))

# Q7
#########################Vigenere密码#########################
 
letter_list='ABCDEFGHIJKLMNOPQRSTUVWXYZ'  #字母表
 
#根据输入的key生成key列表
def Get_KeyList(key):
  key_list=[]
  for ch in key:
    key_list.append(ord(ch.upper())-65)
  return key_list
  
#加密函数
def Encrypt(plaintext,key_list):
  ciphertext=""
  
  i=0
  for ch in plaintext:  #遍历明文
    if 0==i%len(key_list):
      i=0
    if ch.isalpha():  #明文是否为字母,如果是,则判断大小写,分别进行加密
      if ch.isupper():  
        ciphertext+=letter_list[(ord(ch)-65+key_list[i]) % 26]
        i+=1
      else:
        ciphertext+=letter_list[(ord(ch)-97+key_list[i]) % 26].lower()
        i+=1
    else: #如果密文不为字母,直接添加到密文字符串里
      ciphertext+=ch
  return ciphertext
  
#解密函数
def Decrypt(ciphertext,key):
  plaintext=""
  
  i=0
  for ch in ciphertext: #遍历密文
    if 0==i%len(key_list):
      i=0
    if ch.isalpha():  #密文为否为字母,如果是,则判断大小写,分别进行解密
      if ch.isupper():
        plaintext+=letter_list[(ord(ch)-65-key_list[i]) % 26]
        i+=1
      else:
        plaintext+=letter_list[(ord(ch)-97-key_list[i]) % 26].lower()
        i+=1
    else: #如果密文不为字母,直接添加到明文字符串里
      plaintext+=ch
  return plaintext
 
if __name__=='__main__':
  print("加密请按D,解密请按E:")
  user_input=input();
  while(user_input!='D' and user_input!='E'):#输入合法性判断
    print("输入有误!请重新输入:")
    user_input=input()
  
  print("请输入密钥:")
  key=input()
  while(False==key.isalpha()):#输入合法性判断
    print("输入有误!密钥为字母,请重新输入:")
    key=input()
  
  key_list=Get_KeyList(key)
  
  if user_input=='D':
    #加密
    print("请输入明文:")
    plaintext=input()
    ciphertext=Encrypt(plaintext,key_list)
    print("密文为:\n%s" % ciphertext)
  else:
    #解密
    print("请输入密文:")
    ciphertext=input()
    plaintext=Decrypt(ciphertext,key_list)
    print("明文为:\n%s" % plaintext)

# Q8
def freq(seq):
    f = {}
    for e in seq:
        if e in f:
            f[e] += 1
        else:
            f[e] = 1
    return f
print(freq(['hi', 'I', 'am', 'Alexa', 'I', 'would', 'just', 'like', 'to', 'say', 'hi']))

# Q9
def findAddUp(seq, n):
    for i, e in enumerate(seq):
        for j in range(i):
            if seq[i] + seq[j] == n:
                return seq[i], seq[j]
print(findAddUp([3,5,1,7,9,17], 8))                    
        
            