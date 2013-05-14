#   Auther      : Heinz Samuelsson
#   Date        : 2013-05-12
#   File        : simulate_car.py
#   Reference   : -
#   Description :  Calculate the distance and final speed. 
#                  A car is defined by its name, acceleration/deacceleration and acceleration time

time_resolution = 0.1 #seconds

class Car:
    def __init__(self,name,acc,deacc,acc_time):
        self.acceleration   = acc       # acceleration m/s^2
        self.deacceleration = deacc     # deacceleration m/s^2
        self.acc_time       = acc_time  # s
        self.v0             = 0.0       # initial velocity
        self.s              = 0.0       # distance
        self.name           = name      # name of car     
        self.my_time        = 0.0       # current time

    def drive(self,log="disabled"):
        # calculate distance and final speed, also keep track of current time
        self.s       = self.acceleration*time_resolution*time_resolution/2 + self.v0 * time_resolution + self.s
        self.v0      = self.acceleration*time_resolution + self.v0
        self.my_time = self.my_time + time_resolution

        if log == "log_enabled":
            print "  Current time:",self.my_time,"s"

        # return distance and speed
        return self.s,self.v0

    def stop(self,log="disabled"):
        self.s       = self.deacceleration*time_resolution*time_resolution/2 + self.v0 * time_resolution + self.s
        self.v0      = self.v0 - self.deacceleration*time_resolution
        self.my_time = self.my_time + time_resolution

        if log == "log_enabled":
            print "  Current time:",self.my_time,"s"

        # just to fix very small values
        if self.v0 < 0.01:
            self.v0 = 0.0
        # return distance and speed
        return self.s,self.v0

    def car_information(self):
        print 30*"-"
        print "Information for:  ",self.name
        print "Acceleration:     ",self.acceleration,"m/s^2"
        print "Deacceleration:   ",self.deacceleration,"m/s^2"
        print "Acceleration time:",self.acc_time,"s"
        print 30*"-"


if __name__ == "__main__":

    car = Car("Volvo",2.0,4.0,10.0)
    sim_time = 11
    car.car_information()

    print "*** drive initated for car ***"
    for i in range(1,sim_time):
        distance,velocity = car.drive("log_enabled")
        print "    Distance:",distance,"m"
        print "    Velocity:",velocity,"m/s"

    print "*** stop initated for car ***"
    while velocity > 0.01:
        distance,velocity = car.stop("log_enabled")
        print "    Distance:",distance,"m"
        print "    Velocity:",velocity,"m/s"

    print "*** car stopped ***"
