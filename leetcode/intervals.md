+ [Non-overlapping Intervals](#non-overlapping-intervals)
+ [Merge Intervals](#merge-intervals)
+ [Insert Interval](#insert-interval)
<!-----solution----->

## Insert Interval

https://leetcode.com/problems/insert-interval/

```python
def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    res = []

    for interval in intervals:
        if newInterval[0] < interval[0]:
            interval, newInterval = newInterval, interval
        if res and interval[0] <= res[-1][1]:
            res[-1][1] = max(res[-1][1], interval[1])
        else:
            res.append(interval)

    if res and newInterval[0] <= res[-1][1]:
        res[-1][1] = max(res[-1][1], newInterval[1])
    else:
        res.append(newInterval)

    return res
```

## Merge Intervals

https://leetcode.com/problems/merge-intervals/

```python
def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    res = []
    for i in sorted(intervals, key=lambda i: i[0]):

        if res and i[0] <= res[-1][1]:
            res[-1][1] = max(i[1],res[-1][1])
        else:
            res += [i]

    return res
```

## Non-overlapping Intervals

https://leetcode.com/problems/non-overlapping-intervals/

```python
def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
    if not intervals:
        return 0
    intervals.sort(key=lambda interval: interval[0])
    count, prev = 0, 0
    for i in range(1, len(intervals)):
        if intervals[prev][1] > intervals[i][0]:
            if intervals[prev][1] > intervals[i][1]:
                prev = i
            count += 1
        else:
            prev = i
    return count
```