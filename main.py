from hub import port, button
import runloop, motor, time, color_sensor,time

async def main():
    # Example code using the GLUE library.
    print("Hello, World!")
    await GLUE.AssignMotorPorts(port.D,port.C)
    await GLUE.MotorPairMoveForward(1500, 400) # move using the GLUE library!


# --------------------------
# GLUE LIBRARY:


# GPL 3.0
# LEGO
# UNIVERSAL
# EXTENSION


# this is a addon to lego robotics to make life easier for anybody just trying to go about their day.

# under the GPL 3.0 license respect that!

# original repo and author: https://github.com/SnowDev9099/Python-GLUE-Library/tree/main

# --------------------------

class GLUE:

    @staticmethod
    async def AssignMotorPorts(Port_ONE, Port_TWO):
        global Port_SECOND
        global Port_FIRST
        Port_SECOND = Port_TWO
        Port_FIRST = Port_ONE



    # motor pair is already a function but when you have your drivebase hooked up to it, it tends to "get a bit funky" this aims to solve that
    @staticmethod
    async def MotorPairMoveForward(DurationInMS=1000, Velocity=200): # port.C and port.E are typically the ones used
        global Port_SECOND
        global Port_FIRST

        motor.run_for_time(Port_SECOND, DurationInMS, -Velocity)
        motor.run_for_time(Port_FIRST, DurationInMS, Velocity)


    @staticmethod
    async def MotorPairMoveBackward(DurationInMS=1000, Velocity=200): # port.C and port.E are typically the ones used
        global Port_SECOND
        global Port_FIRST

        motor.run_for_time(Port_SECOND, DurationInMS, Velocity)
        motor.run_for_time(Port_FIRST, DurationInMS, -Velocity)


    @staticmethod
    async def TurnLeft(time=1000,velocity=-500):
        global Port_FIRST
        Port_FIRST
        motor.run_for_time(Port_FIRST, 800, 500)


    @staticmethod
    async def TurnRight(time=1000,velocity=-500):
        global Port_SECOND
        Port_SECOND
        motor.run_for_time(Port_SECOND, 800, 500)

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
            time.sleep_ms(50) # prevents code from stopping and overloading the CPU on the Lego Spike Hub
        motor.stop(port_first)
        motor.stop(port_second)









runloop.run(main())
