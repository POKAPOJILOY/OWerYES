def remove_palindroms(spells):
    l = []
    for i in range(len(spells) - 1):
        if spells[i] == spells[i][::-1]:
            l.append(i)
    for i in range(len(l)):
        spells.pop(l[i])