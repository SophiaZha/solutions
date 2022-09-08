class Solution:
    def encode(self, strs):
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, str):
        res, i = [], 0
        while i < len(str):
            j = i
            while str[j] != "#":
                j +=1
            length = int(str[i:j])
            res.append(str[j+1:j+1 +length])
            i = j + 1 + length
        return res
strs = ["lint","code","love","you"]
so = Solution()
str = so.encode(strs)
result = so.decode(str)
print(result)


"""
https://www.lintcode.com/problem/659/
271 · Encode and Decode Strings
659 · Encode and Decode Strings
Algorithms
Medium
Accepted Rate
63%
Description
Solution
Notes
Discuss
Leaderboard
Record
Description
Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

Please implement encode and decode

Contact me on wechat to get Amazon、Google requent Interview questions . (wechat id : jiuzhang0607)


Example
Example1

Input: ["lint","code","love","you"]
Output: ["lint","code","love","you"]
Explanation:
One possible encode method is: "lint:;code:;love:;you"
Example2

Input: ["we", "say", ":", "yes"]
Output: ["we", "say", ":", "yes"]
Explanation:
One possible encode method is: "we:;say:;:::;yes"
Tags
Company

"""