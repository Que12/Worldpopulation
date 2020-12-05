from random import choice

class RandomWalk():
    '''Klasa przeznaczona do generowania błądzenia losowego'''
    def __init__(self, num_points = 5000):
        '''inicjalizowanie atrybutów błądzenia'''
        self.num_points = num_points
        #punkt początkowy ma współrzędne (0,0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        '''wygenerowanie wszystkich punktów dla błądzenia losowego'''

        #Wykonywanie kroków aż do chwili osiągnięcia oczekiwanej liczby punktów 
        while len(self.x_values) < self.num_points: # działa do chwili wygenerowania oczekiwanej liczby punktów 
            #ustalenie kierunku oraz odległości do pokonania w tym kierunku 
            x_direction  = choice([1,-1]) # kierunke w prawo lub w lewo 
            x_distance = choice([0,1,2,3,4]) # odleglosc w danym kierunku 
            x_step = x_direction * x_distance

            y_direction  = choice([1,-1]) # kierunke w góre lub w dół 
            y_distance = choice([0,1,2,3,4])
            y_step = y_direction * y_distance

            #odrzucenie ruchów które prowadzą donikąd
            if x_step == 0 and y_step == 0:
                continue

            #ustalenie następnych wartości X i Y
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)
