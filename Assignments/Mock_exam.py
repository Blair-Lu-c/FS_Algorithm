import Vignere
class mock_exam:
    def ispalindorme(self, s):
        i = 0
        j = len(s)-1
        while i < len(s)//2:
            if s[i].lower() == s[j].lower():
                i += 1
                j -= 1
            else:
                return False
        return True
    
    def find_all_palindormic(self, s):
        res = []
        for i in range(len(s)-1):
            for j in range(i,len(s)-1):
                if self.ispalindorme(s[i:j+2]) == True:
                    res.append(s[i:j+2])
        return res
                    
    def all_fibonacci(self, num):
        fibonacci = [0,1]
        i = 0
        while num > fibonacci[i+1]:
            fibonacci.append(fibonacci[i]+fibonacci[i+1])
            i += 1
        if fibonacci[-1] > num:
            fibonacci.pop(-1)
        
        return fibonacci
    
    def is_ascending(self, seq):
        i = 0
        while i < len(seq)-1:
            if seq[i] >= seq[i+1]:
                return False
            i += 1
        return True 
    
    def longest_ascending(self, seq):
        pass
    
    def isAnagram(self, x,y):
        return sorted(x) == sorted(y)
    
    def VC(seld, key):
        pass
    
    def freq(self, seq):
        f = {}
        for s in seq:
            if s in f:
                f[s] += 1
            else:
                f[s] = 1
        return f
    def findAddUp(self, seq, n):
        for i, e in enumerate(seq):
            for j in range(i):
                if seq[i] + seq[j] == n:
                    return seq[i], seq[j]
                    
                
exam = mock_exam()
s = "aabbbaa"
Q1 =  exam.ispalindorme("amanaplanacanalpanama")
Q2 = exam.find_all_palindormic(s)
Q3 = exam.all_fibonacci(11)
Q4 = exam.is_ascending([1,2,23])
Q5 = exam.longest_ascending( [1, 2, 5, 3, 8, 9, 13, 24, 21, 100,1,2],) 
Q6 = exam.isAnagram("anagram", "margana")
Q7 = exam.VC("house")
Q8 = exam.freq(['hi', 'I', 'am', 'Alexa', 'I', 'would', 'just', 'like', 'to', 'say', 'hi'])
Q9 = exam.findAddUp([3, 4, 1, 7 , 9, 17], 8)