from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        s_color = image[sr][sc]

        if s_color == color:
            return image

        stack = [(sr, sc)]

        while len(stack) > 0:
            r, c = stack.pop()
            image[r][c] = color

            if r-1 >= 0 and image[r-1][c] == s_color:
                stack.append((r-1, c))
            if r+1 < len(image) and image[r+1][c] == s_color:
                stack.append((r+1, c))
            if c-1 >= 0 and image[r][c-1] == s_color:
                stack.append((r, c-1))
            if c+1 < len(image[0]) and image[r][c+1] == s_color:
                stack.append((r, c+1))

        return image

solution = Solution()
image = [[0,0,0],[0,0,0]]; sr = 0; sc = 0; color = 0

print(solution.floodFill(image, sr, sc, color))
