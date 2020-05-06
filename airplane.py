class Airplane:
    make = 'boing'
    model = 747
    year = 1997
    max_speed = 933
    odometr = 0
    is_flying = False
    
    def take_off(self):
        Airplane.is_flying = True
        Airplane.land = False

    def fly(self, path):
        Airplane.odometr += path 

    def land(self):
        is_flying = False


boing = Airplane()
boing.take_off()
boing.fly(800)
boing.land()