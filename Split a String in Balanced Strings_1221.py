def balancedStringSplit( s):
    match = 0
    char = 0
    
    for letter in s:
        if letter == 'R':
            char += 1
        if letter == 'L':
            char -= 1
        if char == 0:
            match += 1
    return match

print(balancedStringSplit("RLRRLLRLLR"))