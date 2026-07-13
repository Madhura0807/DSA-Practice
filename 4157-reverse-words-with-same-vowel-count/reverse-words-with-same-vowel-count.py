class Solution(object):
    def reverseWords(self, s):
        words = s.split(' ')
        vowels = set('aeiou')
        
        def count_vowels(word):
            return sum(1 for char in word if char in vowels)
        
        target_count = count_vowels(words[0])
        
        for i in range(1, len(words)):
            if count_vowels(words[i]) == target_count:
                words[i] = words[i][::-1]
                
        return ' '.join(words)