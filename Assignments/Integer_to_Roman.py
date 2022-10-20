class integer_to_roman:
    def intToRoman(self, num):
        """
        Function to convert decimal to Roman Numerals
        """
        a = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        b = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        res = ''
        if num <= 0 or num > 3999:
            print()
        for i, n in enumerate(a):
            while num >= a[i]:
                res += b[i]
                num -= a[i]
        return res

# Diver Code
if __name__ == '__main__':
    num = int(input("Enter integer: "))
    if num <= 0 or num > 3999:
        print('Your input integer should be range from 0 to 3999!')
    else:
        roman = integer_to_roman()
        print(f'Integer to Roman: {roman.intToRoman(num)}')