def longcomm(l):

    prefix = ""
    for letter_number in range(len(l[0])):
        for string_index in range(len(l) - 1):
            if l[string_index][letter_number] != l[string_index + 1][letter_number]:
                return prefix
                
        prefix += l[0][letter_number]
    
    return prefix

print(longcomm(["flower","fl","flight"]))