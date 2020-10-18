+ [Reverse Integer](#reverse-integer)
+ [Palindrome Number](#palindrome-number)
+ [Fizz Buzz](#fizz-buzz)
+ [Base 7](#base-7)
+ [Fibonacci Number](#fibonacci-number)
+ [Largest Perimeter Triangle](#largest-perimeter-triangle)
+ [Sqrt(x)](#sqrtx)
<!-----solution----->

## Sqrt(x)

https://leetcode.com/problems/sqrtx/

```python
def mySqrt(self, x: int) -> int:
    sqrt = x
    while sqrt * sqrt > x:
        sqrt = (sqrt + x // sqrt) // 2
    return sqrt
```

## Largest Perimeter Triangle

https://leetcode.com/problems/largest-perimeter-triangle/

```python
def largestPerimeter(self, A: List[int]) -> int:
    A.sort(reverse = True)
    for i in range(len(A) - 2):
        if A[i+1] + A[i+2] > A[i]:
            return A[i] + A[i+1] + A[i+2]
    return 0
```

## Fibonacci Number

https://leetcode.com/problems/fibonacci-number/

```python
def fib(self, N: int) -> int:
    if N == 0:
        return 0
    if N == 1:
        return 1
    return self.fib(N - 1) + self.fib(N - 2)
```

## Base 7

https://leetcode.com/problems/base-7/

```python
def convertToBase7(self, num: int) -> str:
    base_seven = []
    minus_sign = False
    if num == 0:
        return '0'
    if num < 0:
        minus_sign = True
        num = -num
    while num > 0:
        base_seven.append(str(num % 7))
        num //= 7
    if minus_sign:
        return '-' + ''.join(base_seven[::-1])
    return ''.join(base_seven[::-1])
```

## Fizz Buzz

https://leetcode.com/problems/fizz-buzz/

```python
def fizzBuzz(self, n: int) -> List[str]:
    list = []
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 != 0:
            list.append('Fizz')
        elif i % 5 == 0 and i % 3 != 0:
            list.append('Buzz')
        elif i % 3 == 0 and i % 5 == 0:
            list.append('FizzBuzz')
        else:
            list.append(str(i))
    return list
```

## Palindrome Number

https://leetcode.com/problems/palindrome-number/

```python
def isPalindrome(self, x: int) -> bool:
    if x < 0 or (x % 10 == 0 and x != 0):
        return False
    x_reverse = 0
    while x > x_reverse:
        x_reverse = x_reverse * 10 + x % 10
        x //= 10
    return x == x_reverse or x == x_reverse // 10
```

## Reverse Integer

https://leetcode.com/problems/reverse-integer/

```python
def reverse(self, x: int) -> int:
    x_str = str(x)
    if x >= 0:
        x_reverse = x_str[::-1]
    else:
        x_no_sign = x_str[1::]
        x_reverse = "-" + x_no_sign[::-1]
    if int(x_reverse) <= -2**31 or int(x_reverse) >= 2**31-1:
        return 0
    else:
        return int(x_reverse)
```