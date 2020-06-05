# Solved 06/05/2020
# CodeSignal
# https://app.codesignal.com/arcade/intro/level-4/Xfeo7r9SBSpo3Wico

def palindromeRearranging(inputString):
    # a word is a palindrome if its frequency dictionary has only 
    # even counts or only 1 odd count.abs
    # get frequency dictionary
    # loop through frequency dictionary
    # if you find 2 odds return false
    # else return true
    frequency_dictionary = {}
    for char in inputString:
        if frequency_dictionary.__contains__(char):
            frequency_dictionary[char] += 1
        else:
            frequency_dictionary[char] = 1
    
    odds = 0
    for frequency in frequency_dictionary.values():
        if frequency % 2 == 1:
            odds += 1
            if odds == 2:
                return False
    
    return True


palindromeRearranging