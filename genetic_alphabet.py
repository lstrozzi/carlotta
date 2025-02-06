STR = "<!START>"
STOP = "<!STOP>"

matrix = [
    [
        [STR, 'A', 'B', 'C'],
        ['D', 'E', 'F', 'G'],
        ['H', 'I', 'J', 'K'],
        ['L', 'M', 'N', 'O']
    ],
    [
        ['P', 'Q', 'R', 'S'],
        ['T', 'U', 'V', 'X'],
        ['Y', 'W', 'Z', '*'],
        [',', ';', ':', '-']
    ],
    [
        [' ', 'a', 'b', 'c'],
        ['d', 'e', 'f', 'g'],
        ['h', 'i', 'j', 'k'],
        ['l', 'm', 'n', 'o']
    ],
    [
        ['p', 'q', 'r', 's'],
        ['t', 'u', 'v', 'x'],
        ['y', 'w', 'z', '+'],
        ['.', '!', '?', STOP]
    ]
]

reverse_matrix = {}
for i in range(0, 3):
    for j in range(0, 3):
        for k in range(0, 3):
            code = i*100 + j * 10 + k
            c = matrix[i][j][k]
            reverse_matrix[c] = code


char = None
while char != STOP:
    char = input('Enter a character: ')
    if char in reverse_matrix:
        print(f'Code for {char}: {reverse_matrix[char]:03d}')
    else:
        print(f'Character {char} not found in matrix.')
    if char == STOP:
        break
    