class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        def isAnagram(str1, str2):
            if len(str1) != len(str2):
                return False

            ref1, ref2 = {}, {}
            for i in range(len(str1)):
                ref1[str1[i]] = ref1.get(str1[i], 0) + 1
                ref2[str2[i]] = ref2.get(str2[i], 0) + 1
            return ref1 == ref2
        
        result = []
        for string in strs:
            isAna = False
            for i in range(len(result)):
                if isAnagram(string, result[i][0]):
                    isAna = True
                    result[i].append(string)
            if not isAna:
                result.append([string])
        return result

            