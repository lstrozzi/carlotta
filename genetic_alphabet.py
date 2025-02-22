import msvcrt

def get_key():
    return msvcrt.getch().decode('utf-8')

STR = "<!START>"
STOP = "<!STOP>"
CTRL_A = '\x01'

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
for i in range(0, 4):
    for j in range(0, 4):
        for k in range(0, 4):
            code = (i+1)*100 + (j+1) * 10 + (k+1)
            c = matrix[i][j][k]
            reverse_matrix[c] = code

print('Enter a character (CTRL-A to stop): ', end='', flush=True)

char = None

while char != CTRL_A:
    char = get_key()
    if char in reverse_matrix:
        print(f"{reverse_matrix[char]:03d} ", end="", flush=True)
    elif char != CTRL_A:
        print(f'\nCharacter {char} not found in matrix.')

print("\nBye!")