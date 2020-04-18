s = input('Выберите действие: актеры или фильмы ').lower()
if s == 'фильмы':
    film1 = str(input())
    film2 = str(input())
    films = {}
    with open('input') as inp_file:
        for line in inp_file:
            film, *cast = line.split()
            films[film] = cast
    act1 = set(films[film1])
    act2 = set(films[film2])
    act12 = act1 & act2
    act = act1 - act2

    print('общий актерский состав: ', act2)
    print('актеры, снимавшиеся и в первом, и во втором фильме:', act12)
    print('актеры, участвующие в съемках первого, но не участвующие в съемках второго', act)
else:
    print('None')