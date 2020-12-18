+ [Max Consecutive Ones](#max-consecutive-ones)
+ [Reshape the Matrix](#reshape-the-matrix)
+ [Image Smoother](#image-smoother)
+ [Flipping an Image](#flipping-an-image)
+ [Transpose Matrix](#transpose-matrix)
+ [Move Zeroes](#move-zeroes)
+ [Squares of a Sorted Array](#squares-of-a-sorted-array)
<!-----solution----->

## Squares of a Sorted Array

https://leetcode.com/problems/squares-of-a-sorted-array/

```python
def sortedSquares(self, nums: List[int]) -> List[int]:
    sq_nums = []
    for num in nums:
        sq_nums.append(num ** 2)

    return sorted(sq_nums)
```

## Move Zeroes

https://leetcode.com/problems/move-zeroes/

```python
def moveZeroes(self, nums: List[int]) -> None:
    nums.sort(key=lambda x: 0 if x else 1)
```

## Transpose Matrix

https://leetcode.com/problems/transpose-matrix/

```python
def transpose(self, A: List[List[int]]) -> List[List[int]]:
    tr_A = []

    for i in range(len(A[0])):
        tr = []
        for j in range(len(A)):
            tr.append(A[j][i])
        tr_A.append(tr)
    return tr_A
```

## Flipping an Image

https://leetcode.com/problems/flipping-an-image/

```python
def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
    for i in range(len(A)):
        row = A[i]
        A[i]=row[::-1]

    for i in range(len(A)):
        for j in range(len(A[0])):
            A[i][j]=0 if A[i][j]==1 else 1

    return A
```

## Image Smoother

https://leetcode.com/problems/image-smoother/

```python
def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
    height = len(M)
    width = len(M[0])

    for i in range(height):
        prev = -1
        for j in range(width):
            next_prev = M[i][j]
            M[i][j] += (0 if prev == -1 else prev) + (0 if j == width-1 else M[i][j+1])
            prev = next_prev

    for j in range(width):
        prev = -1
        for i in range(height):
            next_prev = M[i][j]
            M[i][j] += (0 if prev == -1 else prev) + (0 if i == height-1 else M[i+1][j])
            prev = next_prev

    for i in range(height):
        for j in range(width):
            count = (0 if j == 0 else 1) + 1 + (0 if j == width-1 else 1)
            divisor = (0 if i == 0 else count) + count + (0 if i == height-1 else count)
            M[i][j] //= divisor

    return M
```

## Reshape the Matrix

https://leetcode.com/problems/reshape-the-matrix/

```python
def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
    if len(nums) * len(nums[0]) != r * c:
        return nums
    matrix = []
    for i in range(len(nums)):
        for j in range(len(nums[0])):
            matrix.append(nums[i][j])
    re_matrix = []
    for i in range(0,len(matrix),c):
        re_matrix.append(matrix[i:i+c])
    return re_matrix
```

## Max Consecutive Ones

https://leetcode.com/problems/max-consecutive-ones/

```python
def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
    count = 0
    max_count = 0
    for i in nums:
        if i == 1:
            count += 1
        else:
            max_count = max(count, max_count)
            count = 0
    max_count = max(count, max_count)
    return max_count
```