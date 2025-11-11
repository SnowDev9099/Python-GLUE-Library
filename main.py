from hub import port
import runloop, motor, time, color_sensor

async def main():
    # Example code using the GLUE library.
    print("Hello, World!")
    await GLUE.MotorPairMoveForward(1400, 200) # move using the GLUE library!

    motor.run_to_absolute_position(port.E, 36, 1000) 
    time.sleep_ms(100)







# --------------------------
# GLUE LIBRARY:


# GPL 3.0
# LEGO
# UNIVERSAL
# EXTENSION


# this is a addon to lego robotics to make life easier for anybody just trying to go about their day.

# under the GPL 3.0 license respect that!

# original author: https://github.com/SnowDev9099/Python-GLUE-Library/tree/main

# --------------------------

class GLUE:

    # motor pair is already a function but when you have your drivebase hooked up to it, it tends to "get a bit funky" this aims to solve that
    @staticmethod
    async def MotorPairMoveForward(port_first=port.C, port_second=port.E, DurationInMS=1000, Velocity=200): # port.C and port.E are typically the ones used
        motor.run_for_time(port_first, DurationInMS, Velocity)
        motor.run_for_time(port_second, DurationInMS, -Velocity)


    @staticmethod
    async def MotorPairMoveBackward(port_first=port.C, port_second=port.E, DurationInMS=1000, Velocity=200): # port.C and port.E are typically the ones used
        motor.run_for_time(port_first, DurationInMS, -Velocity)
        motor.run_for_time(port_second, DurationInMS, Velocity)


    @staticmethod
    async def TurnLeft(velocity=-500):
        time.sleep_ms(10)
        motor.run_for_time(port.C, 500, -velocity)


    @staticmethod
    async def TurnRight(velocity=-500):
        time.sleep_ms(10)
        motor.run_for_time(port.E, 500, -velocity)

    @staticmethod
    def GetCurrentColor(port_first=port.A):
        return color_sensor.color(port_first)

    @staticmethod
    async def Calculate(First, Second, Add, Subtract, Multiply, Divide): # good for things you'll need to calcute either being async or easier with a method. you could calculate distance posibly with speed and distance sensor?
        if Add:
            return First + Second
        elif Subtract:
            return First - Second
        elif Multiply:
            return First * Second
        elif Divide:
            if Second == 0:
                print("Divide by zero error!")
            else:
                return First / Second

    @staticmethod
    def MotorPairStop():
        global MotorStop
        MotorStop = True


    @staticmethod
    def MotorPairRun(port_first=port.C, port_second=port.E, Velocity=200):
        global MotorStop
        MotorStop = False
        while not MotorStop:
            motor.run(port_first, Velocity)
            motor.run(port_second, -Velocity)
            time.sleep_ms(50)# prevents code from stopping and overloading the CPU on the Lego Spike robot
        motor.stop(port_first)
        motor.stop(port_second)



runloop.run(main())
