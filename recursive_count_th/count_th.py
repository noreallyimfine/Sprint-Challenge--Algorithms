'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    # TBC
    total = 0
    if word[0] == 't':
        if word[1] == 'h':
            total += 1
            return total + count_th(word[2:])
    else:
        return total + count_th(word[1:])

