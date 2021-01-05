""" Your friend is typing his name into a keyboard. Sometimes, when typing a character c, the key might get long pressed, and the character will be typed 1 or more times.

You examine the typed characters of the keyboard. Return True if it is possible that it was your friends name, with some characters (possibly none) being long pressed.

 

Example 1:

Input: name = "alex", typed = "aaleex"
Output: true
Explanation: 'a' and 'e' in 'alex' were long pressed.
Example 2:

Input: name = "saeed", typed = "ssaaedd"
Output: false
Explanation: 'e' must have been pressed twice, but it wasn't in the typed output.
Example 3:

Input: name = "leelee", typed = "lleeelee"
Output: true
Example 4:

Input: name = "laiden", typed = "laiden"
Output: true
Explanation: It's not necessary to long press any character.

 """

def isLongPressedName(name, typed):
    if len(typed) < len(name):
        return False
    p1 = 0
    p2 = 0
    ok = False
    while p1 < len(name) and p2 < len(typed):
        if name[p1] == typed[p2]:
            p2 += 1
            ok = True
        else:
            p1 += 1
            if ok == False:
                return False
            ok = False
    
    return True

print(isLongPressedName('saeed', 'ssaaedd'))
print(isLongPressedName('alex', 'aaleex'))
print(isLongPressedName('laiden', 'laide'))

                
