import matplotlib.pyplot as plt 
from random_walk import RandomWalk

while True:
    rw = RandomWalk(50000)
    rw.fill_walk()

    #określenie wielkości okna wykresu
    plt.figure(dpi=128, figsize=(10, 6))  # figrzsize podaje w calach wielkosc obrazu 



    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c = point_numbers, cmap = plt.cm.Blues, edgecolor = 'none', s = 1)
    #podkreslenie pierwszego i ostatniego punktu błądzenia losowego
    plt.scatter(0,0, c = 'green', edgecolor = 'none', s = 100) # wyswietlenie punktu początkowego
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c = 'yellow', edgecolor = 'none', s = 100) # wyswietlenie punktu ostatniego 
    
    #ukrywanie osi 
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()
    keep_running = input("Utowrzyć kolejne błądzenie losowe? (t/n)" )
    if keep_running == 'n':
        break
