def parsing(fileName):
    size = None
    taquin = []
    with open(fileName, 'r') as file:
        for line in file:
            if line[0] == '#':
                continue
            if line.find('#') != -1:
                line = line[:line.find('#')]
            tabLine = line.split(' ')
            if len(tabLine) != 1 and size != None:
                for nb in tabLine:
                    if nb == '':
                        continue
                    taquin.append(int(nb.replace('\n', '')))
            else:
                size = int(tabLine[0].replace('\n', ''))
           
    print(size)
    if len(taquin) != size * size:
        return "error", "La taille du taquin ne correspond pas avec le nombre de tuile."
    for nb in range(0, size * size):
        if nb in taquin:
            continue
        else:
            return "error", "La valeur d'une tuile du taquin ne correspond pas."
    return size, taquin
