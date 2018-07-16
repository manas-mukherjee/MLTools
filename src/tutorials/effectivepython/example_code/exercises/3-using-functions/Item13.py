#Item 13
#Know how closures interact with variable scope

numbers = [8,3,1,2,5,4,7,6]
group = {2,3,5,7} # Higher priority

def helper(x):
    if x in group:
        return (0,x)
    return (1,x)

numbers.sort(key=helper)
print(numbers)
