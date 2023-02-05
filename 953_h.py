class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        flag1 = 0
        flag2 = 0

        for i in range(len(words)-1):

            Min = len(words[i])
            if len(words[i+1]) < Min:
                Min = len(words[i+1])
                flag1 = 1
            
            for j in range(Min):

                if order.index(words[i][j]) > order.index(words[i+1][j]):
                    return False

                elif order.index(words[i][j]) < order.index(words[i+1][j]):
                    flag1 = 0
                    break
                
                else:
                    flag2 = 1
            
            if flag2 == flag1 == 1:
                return False
   
        return True

