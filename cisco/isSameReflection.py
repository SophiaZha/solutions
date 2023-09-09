class Solution:
    def isSameReflection(self, str1, str2):
        if len(str1) != len(str2):
            return False
        str1 += str1

        for i in range(len(str1)):
            if str1[i] == str2[0]:
                matching = True
                for j in range(len(str2)):
                    if str1[ (i+j ) % len(str1) ] != str2[j]:
                        matching = False
                        break
                if matching:
                    return True
        return False

so = Solution()
print(so.isSameReflection("abcdefgh", "efghabcd"))
print(so.isSameReflection("abcdefgh", "efghaxcd"))
print(so.isSameReflection("sample", "plesam"))

#sample
#plesam
#esampl





