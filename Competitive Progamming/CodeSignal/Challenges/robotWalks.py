#Time complexity: O(n*m) : n is length of a, m is the largest element of array
#Space complexity: O(x): x is sum of elements 
def robotWalk(a):

    visited = []
    currentX = currentY = 0
    visited.append((currentX, currentY))
    for key, val in enumerate(a):
        for _ in range(0, val):
            if key % 4 == 0:
                currentY += 1
            elif key % 4 == 1:
                currentX += 1
            elif key % 4 == 2:
                currentY -= 1
                if currentY < 0:
                    currentY = 0
            else:
                currentX -= 1
                if currentX < 0:
                    currentX = 0
            if (currentX, currentY) in visited:
                return True
            visited.append((currentX, currentY))
            # print(visited)
    return False

#Solution 2: Optimized
#Time complexity: O(n)
# Space complexity: O(1)

def robotWalk2(a):
    minX = minY = 0
    maxX = maxY = float('inf')

    for ind, val in enumerate(a):
        if ind % 4 == 0:
            if val >= maxY:
                return True
            maxY = val


if __name__ == "__main__":
    a = [34241, 23434, 2341]
    print(robotWalk2(a))