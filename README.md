
# Infinite Lists In Python

Datastructure to imitate infinite lists in Haskell.

## Creating Infinite Lists

### Repeating List of the Same Element

Infinite list of ones:

``` python-console
>>> ones = InfiniteList.repeat(1)
>>> ones
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ...]
```

### Infinite Pattern

All positive integers (by incrementing previous integer):

``` python-console
>>> positive_ints = InfiniteList.pattern(1, lambda x: x + 1)
>>> positive_ints
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...]
```

All even numbers starting from 0:

``` python-console
>>> evens = InfiniteList.pattern(0, lambda x: x + 2)
>>> evens
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, ...]
```

Infinite list where each element is the value of it's index:

``` python-console
>>> nums = InfiniteList.pattern(0, lambda i, x: i)
>>> nums
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, ...]
```

## Math with Infinite Lists

Lists can be combined element-wise with (+, -, \*, /, //, and \*\*):

``` python-console
>>> InfiniteList.repeat(1) + InfiniteList.repeat(2)
[3, 3, 3, 3, 3, 3, 3, 3, 3, 3, ...]
>>> InfiniteList.repeat(5) * InfiniteList.repeat(3)
[15, 15, 15, 15, 15, 15, 15, 15, 15, 15, ...]
>>> 
```

If a list is combined with a scalar, than that scalar will be treated as a
repeating infinite list of that scalar.

``` python-console
>>> InfiniteList.repeat(5) + 8
[13, 13, 13, 13, 13, 13, 13, 13, 13, 13, ...]
>>> 
```

## Filtering and Mapping

Filtering a list of integers to get all even numbers:

``` python-console
>>> naturals = InfiniteList.pattern(0, lambda x: x + 1)
>>> naturals
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, ...]
>>> evens = naturals.filter(lambda x: x % 2 == 0)
>>> evens
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, ...]
```

Mapping an infinite list to multiply all elements by 2:

``` python-console
>>> naturals = InfiniteList.pattern(0, lambda x: x + 1)
>>> naturals
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, ...]
>>> multiplied = naturals.map(lambda x: x * 2)
>>> multiplied
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, ...]
```

