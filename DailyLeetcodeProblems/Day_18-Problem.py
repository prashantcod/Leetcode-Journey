#! 3454. Separate Squares II


# You are given a 2D integer array squares. Each squares[i] = [xi, yi, li] represents the coordinates of the bottom-left point and the side length of a square parallel to the x-axis.

# Find the minimum y-coordinate value of a horizontal line such that the total area covered by squares above the line equals the total area covered by squares below the line.

# Answers within 10-5 of the actual answer will be accepted.

# Note: Squares may overlap. Overlapping areas should be counted only once in this version.

 

# Example 1:

# Input: squares = [[0,0,1],[2,2,1]]

# Output: 1.00000

# Explanation:



# Any horizontal line between y = 1 and y = 2 results in an equal split, with 1 square unit above and 1 square unit below. The minimum y-value is 1.

# Example 2:

# Input: squares = [[0,0,2],[1,1,1]]

# Output: 1.00000

# Explanation:



# Since the blue square overlaps with the red square, it will not be counted again. Thus, the line y = 1 splits the squares into two equal parts.

 

# Constraints:

# 1 <= squares.length <= 5 * 104
# squares[i] = [xi, yi, li]
# squares[i].length == 3
# 0 <= xi, yi <= 109
# 1 <= li <= 109
# The total area of all the squares will not exceed 1015.
 





# CODE
class Solution:
    def separateSquares(self, squares):
        # Build sweep events
        events = []
        xs = set()
        for x, y, l in squares:
            events.append((y, 1, x, x + l))
            events.append((y + l, -1, x, x + l))
            xs.add(x)
            xs.add(x + l)

        events.sort()
        xs = sorted(xs)
        x_id = {x: i for i, x in enumerate(xs)}

        n = len(xs) - 1
        cnt = [0] * (4 * n)
        length = [0.0] * (4 * n)

        def push_up(node, l, r):
            if cnt[node] > 0:
                length[node] = xs[r] - xs[l]
            elif l + 1 == r:
                length[node] = 0.0
            else:
                length[node] = length[node * 2] + length[node * 2 + 1]

        def update(node, l, r, ql, qr, val):
            if qr <= l or r <= ql:
                return
            if ql <= l and r <= qr:
                cnt[node] += val
                push_up(node, l, r)
                return
            m = (l + r) // 2
            update(node * 2, l, m, ql, qr, val)
            update(node * 2 + 1, m, r, ql, qr, val)
            push_up(node, l, r)

        prev_y = events[0][0]
        area_slices = []

        i = 0
        while i < len(events):
            y = events[i][0]
            dy = y - prev_y
            if dy > 0 and length[1] > 0:
                area_slices.append((prev_y, y, length[1]))

            while i < len(events) and events[i][0] == y:
                _, typ, x1, x2 = events[i]
                update(1, 0, n, x_id[x1], x_id[x2], typ)
                i += 1

            prev_y = y

        # Total area
        total = sum((y2 - y1) * w for y1, y2, w in area_slices)
        half = total / 2.0

        cur = 0.0
        for y1, y2, w in area_slices:
            area = (y2 - y1) * w
            if cur + area >= half:
                return y1 + (half - cur) / w
            cur += area

        return prev_y
