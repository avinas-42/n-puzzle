from .optParse import optParse

def parsing(argv):
    size = None
    taquin = []
    optlist, argv = optParse(argv)
    try:
        with open(argv[0], 'r') as file:
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
                        try:
                            taquin.append(int(nb.replace('\n', '')))
                        except:
                            return -1, "Le fichier contient des characteres non prevu.", None
                else:
                    try:
                        size = int(tabLine[0].replace('\n', ''))
                    except:
                        pass
    except IOError:
        return -1, "Le fichier ne peut pas etre ouvert.", None
    if size == None:
        return -1, "Le fichier n'indique pas la taille du taquin.", None
    if len(taquin) != size * size:
        return -1, "La taille du taquin ne correspond pas avec le nombre de tuile.", None
    for nb in range(0, size * size):
        if nb in taquin:
            continue
        else:
            return -1, "La valeur d'une tuile du taquin ne correspond pas.", None
    return size, taquin, optlist
