class Solution:
    def isPalindrome(self, x: int) -> bool:
        # 121
        # 123

        # reverse number
        reversed = 0
        while x > reversed:
            reversed = reversed * 10 + x % 10
            x // 10

        return reversed == x

if __name__ == '__main__':
    print(Solution().isPalindrome(123))
