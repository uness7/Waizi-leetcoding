class Solution:
    def isAnagram() -> bool:
        return len(s) == len(t) and sorted(s) == sorted(t)

##############################################################

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if (len(s) != len(t)):  
            return False

        counter: int = 0
        
        map_s = dict()
        map_t = dict() 

        for char in s:                                
        
        for char in t:
            map_t[char] = t.count(char)
        
        for char in s:
            if not t.count(char):
                return False

##############################################################
############### My most optimal solution #####################

class Solution:
	def get_char_count(self, s: str):
		char_count = {}
		for char in s:
			if char in char_count:
				char_count[char] += 1	
			else:
				char_count[char] = 1
		return char_count

	def isAnagram(self, s: str, t: str) -> bool:

		if len(s) != len(t):
			return False

		c1 = get_char_count(s)
		c2 =  get_char_count(t)	
		
		return c1 == c2
