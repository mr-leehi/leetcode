class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        flag = 0
        table = []
        for i in order:
            table.append(i)

        for i in range(len(words)-1):
            Min = len(words[i])
            if(Min > len(words[i+1])):
                Min = len(words[i+1])
            for j in range(Min):
                if((table.index(words[i][j])-table.index(words[i+1][j])) > 0):
                    # print("0_0")
                    flag = 0
                    return False
                elif((table.index(words[i][j])-table.index(words[i+1][j])) < 0):
                    # print(words[i])
                    # print(words[i+1])
                    # print(j)
                    # print("1_0")
                    flag = 1
                    break # 這輪pass 往下一輪檢查
                else:
                    flag = 2
            if((flag == 2) and (len(words[i]) > len(words[i+1]))):
                # print("0_1")
                return False # words[i] is longer than words[i+1]
        # print("1_1")
        return True