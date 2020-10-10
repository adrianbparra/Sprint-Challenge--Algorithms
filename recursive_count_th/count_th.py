'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    # TBC
    # Since we are looking for th
    # we would check each value if and call recursivly on each character

    # if it finds a th then returns a 1 + call without the th
    # else it returns 0 + call without character

    # we are only checking lowercase

    # base case is 2 or less characters left
    if len(word) <= 1:
        return 0
    
    # test is checking the first characters

    print(word[:2])
    if word[:2] == "th":
        return 1 + count_th(word[2:])
    else:
        return 0 + count_th(word[1:])
