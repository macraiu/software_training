""" 
You are playing the Bulls and Cows game with your friend.

You write down a secret number and ask your friend to guess what the number is. When your friend makes a guess, you provide a hint with the following info:

The number of "bulls", which are digits in the guess that are in the correct position.
The number of "cows", which are digits in the guess that are in your secret number but are located in the wrong position. Specifically, the non-bull digits in the guess that could be rearranged such that they become bulls.
Given the secret number secret and your friend's guess guess, return the hint for your friend's guess.

The hint should be formatted as "xAyB", where x is the number of bulls and y is the number of cows. Note that both secret and guess may contain duplicate digits.

 

Example 1:

Input: secret = "1807", guess = "7810"
Output: "1A3B"
Explanation: Bulls are connected with a '|' and cows are underlined:
"1807"
  |
"7810"
Example 2:

Input: secret = "1123", guess = "0111"
Output: "1A1B"
Explanation: Bulls are connected with a '|' and cows are underlined:
"1123"        "1123"
  |      or     |
"0111"        "0111"
Note that only one of the two unmatched 1s is counted as a cow since the non-bull digits can only be rearranged to allow one 1 to be a bull.
Example 3:

Input: secret = "1", guess = "0"
Output: "0A0B"
Example 4:

Input: secret = "1", guess = "1"
Output: "1A0B"
 """


def getHint2(secret, guess):
    secret_dict = {}
    guess_dict = {}
    for i in range(len(secret)):
        if secret[i] not in secret_dict:
            secret_dict[secret[i]] = [i]
        else:
            secret_dict[secret[i]].append(i)

        if guess[i] not in guess_dict:
            guess_dict[guess[i]] = [i]
        else:
            guess_dict[guess[i]].append(i)


    bulls, cows = 0, 0

    for i in secret_dict:
        if i in guess_dict:
            to_loop = [secret_dict, guess_dict] if len(secret_dict[i]) <= len(guess_dict[i]) else [guess_dict, secret_dict]
            for el in to_loop[0][i]:
                if el in to_loop[1][i]:
                    bulls += 1
                else:
                    cows += 1

    return '{0}A{1}B'.format(bulls, cows)

def getHint3(secret, guess):
    bulls, cows = 0, 0

    slist = list(secret)
    glist = list(guess)

    for i in reversed(range(len(slist))):
        if slist[i] == glist[i]:
            bulls += 1
            slist.pop(i)
            glist.pop(i)

    for i in slist:
        if i in glist:
            cows += 1
            glist.remove(i)


    return '{0}A{1}B'.format(bulls, cows)

def getHint(secret, guess):

    from collections import deque
    bulls, cows = 0, 0

    slist = deque(secret)
    glist = deque(guess)

    for i in reversed(range(len(slist))):
        if slist[i] == glist[i]:
            bulls += 1
            del slist[i]
            del glist[i]

    for i in slist:
        if i in glist:
            cows += 1
            glist.remove(i)


    return '{0}A{1}B'.format(bulls, cows)

print(getHint('1123','0111'))
print(getHint('1','0'))
print(getHint('1807','7810'))
print(getHint('1','1'))
print(getHint('11','10'))


