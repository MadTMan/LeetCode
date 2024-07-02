class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word1_len = len(word1)
        word2_len = len(word2)
        merged = ''

        if(word1_len > word2_len):
            remainder = word1_len-word2_len
            min_len = word2_len
        elif(word2_len > word1_len):
            remainder = word2_len-word1_len
            min_len = word1_len
        else:
            remainder = word1_len-word2_len
            min_len = word2_len

        for i in range(min_len):
            merged += word1[i]
            merged += word2[i]
        for i in range(remainder):
            if(word1_len > word2_len):
                merged += word1[word2_len+i]
            if(word2_len > word1_len):
                merged += word2[word1_len+i]


        return merged