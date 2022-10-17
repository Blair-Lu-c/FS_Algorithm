class Solution(object):
    def intToRoman(self, num):
        a = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        b = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        res = ''
        if num <= 0 or num > 39999:
            print()
        for i, n in enumerate(a):
            while num>=a[i]:
                res+=b[i]
                num-=a[i]
        return res

if __name__ == '__main__':
    num = int(input("Enter integer: "))
    if num <= 0 or num > 3999:
        print('Your input integer should be range from 0 to 3999!')
    else:
        ob1 = Solution()
        print(f'Integer to Roman: {ob1.intToRoman(num)}')