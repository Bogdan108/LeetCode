def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1

        while left < right:
            if s[left] != s[right]:
                print(s[left:right-1])
                print(s[left+1:right])
                if self.isPalindrome(s[left:right]) or self.isPalindrome(s[left+1:right+1]):
                    return True
                else:
                    return False
            left += 1
            right -= 1
            return True