#This program is a simple simulation (Well not a simulation) but yeah it shows how much distance car has covered, 
#the remaining fuel,the remaining distance and it also checks if the fuel is more than its tank.
class Vehicle:
    def check(self):
            if self.fuel>self.amount:
                print(f"Fuel can't be more than {self.amount} L")
                self.fuel=self.amount
    def __init__(self,current_fuel,amount):
        self.fuel=current_fuel
        self.amount=amount
        self.check()
    def drive(self,distance):
        self.distance=distance
    def refuel(self,refuel):
        self.fuel=self.fuel+refuel
        self.check()
class Car(Vehicle):
    def __init__(self,current_fuel,amount,consumption):
        super().__init__(current_fuel,amount)
        self.consumption=consumption#For each km
    def drive(self,distance=None):
            # 1. If a distance is provided, start a new trip
            # 2. If distance=None, resume driving the remaining self.distance
            if distance != None:
                 super().drive(distance)
            self.total_consumption=self.consumption*self.distance
            #Calculates total fuel needed for covering distance
            if self.total_consumption>self.fuel:
                needed=self.total_consumption-self.fuel
                self.covered=self.fuel/self.consumption
                #The above line calculates the distance covered by self.fuel 
                #by dividing self.consumption which is a variable to denote 
                #how much fuel is spend to cover each km.
                self.distance=self.distance-self.covered
                #Remembers the remaining distance and keeps updating
                print("The car needs at least ",needed,"L!!!")
                print("It has covered",self.covered,"km")
                print("Remaining distance to cover",self.distance,"km")
                #Sets back to 0 because all fuel has been spend in covering
                # the distance and it needs more.
                self.fuel=0
            else:
                self.fuel=self.fuel-self.total_consumption
                print(f"The car has covered {self.distance} km and the remaining fuel is {self.fuel} L")
                            
            #print("The distance covered is")
            
car1=Car(14,13,2)
car1.drive(20)
car1.refuel(31)
car1.drive()

