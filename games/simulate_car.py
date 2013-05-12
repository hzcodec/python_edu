#   Auther      : Heinz Samuelsson
#   Date        : 2013-05-12
#   File        : simulate_car.py
#   Reference   : -
#   Description :  Calculate the distance: 
#                    s = (at^2)/2 + v0*t 
#                    v = at + v0


class Car:
    def __init__(self):
        self.acceleration = 2.0    # m/s^2
        self.acc_time     = 10.0   # s
        self.v0           = 0.0    # initial velocity
        self.s            = 0.0    # distance

    def drive(self,t):
        print "drive initated for car"
        self.s = self.acceleration*t*t/2 + self.v0 * t + self.s
        self.v0 = self.acceleration*t + self.v0
        return self.s,self.v0

    def stop(self):
        pass

    def car_information(self):
        print "Information for car:"
        print "Acceleration:",self.acceleration
        print 30*"-"


if __name__ == "__main__":

    car = Car()

    car.car_information()
    distance,velocity = car.drive(0.1)
    print "  Distance:",distance,"m"
    print "  Velocity:",velocity,"m/s"

    distance,velocity = car.drive(0.1)
    print "  Distance:",distance,"m"
    print "  Velocity:",velocity,"m/s"

    distance,velocity = car.drive(0.1)
    print "  Distance:",distance,"m"
    print "  Velocity:",velocity,"m/s"

