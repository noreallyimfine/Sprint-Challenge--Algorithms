#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n) -> because as 'n' grows, the amount of operations grow linearly. For n=1, you will do one operation, n=2 will be 2 operations, and so on.


b) O(n log(n)) -> we loop through 'n' so that's the first n. The log(n) comes from j being doubled each time through, so only going through half of 'n' times


c) Also O(n) -> each time the function is called, it does one operation. And the function will be called n times.

## Exercise II

To solve this problem I would use a binary search approach. 

def egg_drop(n)
    # Find the midpoint
    # Drop an egg
    # If it breaks, repeat on lower half
    # If it doesnt break repeat on upper half
    # when n=2, if it breaks, the other one is the highest floor
    # if not, thats the highest floor

Upon further thinking and testing, it might be best to turn the floors into a list so it can be matched better to a traditional binary search

The runtime complexity for this would be O(log(n))