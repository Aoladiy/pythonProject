en_alpha = 'abcdefghijklmnopqrstuvwxyz'
en_alpha_u = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
text = input().split()
text_for_steps = text
for i in range(len(text)):
    text[i] = list(text[i])
#s = ' '.join(text)
r = []

for i in range(len(text_for_steps)):
    step = 0
    for j in range(len(text_for_steps[i])):
        if text_for_steps[i][j].isalpha():
            step += 1
    for z in range(len(text[i])):
        if text[i][z] in en_alpha:
            symbol = en_alpha.find(text[i][z]) + step
            if symbol >= 26:
                symbol -= 26
            text[i][z] = en_alpha[symbol]
        if text[i][z] in en_alpha_u:
            symbol = en_alpha_u.find(text[i][z]) + step
            if symbol >= 26:
                symbol -= 26
            text[i][z] = en_alpha_u[symbol]

for i in range(len(text)):
    text[i] = ''.join(text[i])
print(*text)