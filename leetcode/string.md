+ [Valid Anagram](#valid-anagram)
+ [Reverse String](#reverse-string)
+ [Reverse Vowels of a String](#reverse-vowels-of-a-string)
+ [Reverse Words in a String III](#reverse-words-in-a-string-iii)
+ [To Lower Case](#to-lower-case)
<!-----solution----->

## To Lower Case

https://leetcode.com/problems/to-lower-case/

```python
def toLowerCase(self, str: str) -> str:
    alphabet = {'A': 'a', 'B': 'b', 'C': 'c', 'D': 'd', 'E': 'e',
         'F': 'f', 'G': 'g', 'H': 'h', 'I': 'i', 'J': 'j',
         'K': 'k', 'L': 'l', 'M': 'm', 'N': 'n', 'O': 'o',
         'P': 'p', 'Q': 'q', 'R': 'r', 'S': 's', 'T': 't',
         'U': 'u', 'V': 'v', 'X': 'x', 'W': 'w', 'Y': 'y',
         'Z': 'z'}
    for letter in str:
        if letter in alphabet:
            str = str.replace(letter, alphabet[letter])
    return str
```

## Reverse Words in a String III

https://leetcode.com/problems/reverse-words-in-a-string-iii/

```python
def reverseWords(self, s: str) -> str:
    words = s.split()
    for i in range(len(words)):
        words[i] = words[i][::-1]
    return ' '.join(words)
```

## Reverse Vowels of a String

https://leetcode.com/problems/reverse-vowels-of-a-string/

```python
def reverseVowels(self, s: str) -> str:
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    s = list(s)
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] in vowels and s[right] in vowels:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        elif s[left] in vowels and s[right] not in vowels:
            right -= 1
        elif s[left] not in vowels and s[right] in vowels:
            left += 1
        else:
            left += 1
            right -= 1
    return ''.join(s)
```

## Reverse String

https://leetcode.com/problems/reverse-string/

```python
def reverseString(self, s: List[str]) -> None:
    left = 0
    right = len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    return s
```

## Valid Anagram

https://leetcode.com/problems/valid-anagram/

```python
def isAnagram(self, s: str, t: str) -> bool:
    return sorted(s) == sorted(t)
```