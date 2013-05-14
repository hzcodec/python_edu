#   Auther      : Heinz Samuelsson
#   Date        : 2013-05-12
#   File        : traffic.py
#   Reference   : -
#   Description : -

import simulate_car as SimCar

class Traffic:
    def __init__(self,sim_time):
        self.car1 = SimCar.Car("Mazda",1.5,3.0,10.0)
        self.distance1 = 0.0
        self.velocity1 = 0.0

        self.car2 = SimCar.Car("Volvo",2.0,4.0,10.0)
        self.distance2 = 0.0
        self.velocity2 = 0.0

        self.sim_time  = sim_time

    def start(self):

        print "*** drive initated for:",self.car1.name
        for i in range(1,self.sim_time):
            self.distance1,self.velocity1 = self.car1.drive(0.1)
        print "  Distance:",self.distance1,"m"
        print "  Velocity:",self.velocity1,"m/s"

        print "*** drive initated for:",self.car2.name
        for i in range(1,self.sim_time):
            self.distance2,self.velocity2 = self.car2.drive(0.1)
        print "  Distance:",self.distance2,"m"
        print "  Velocity:",self.velocity2,"m/s"


    def check_distance(self):
        pass

if __name__ == "__main__":
   
    sim_time = 11
  
    traffic = Traffic(sim_time)
    traffic.start()
