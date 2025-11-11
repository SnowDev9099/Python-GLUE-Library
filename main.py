from hub import port
import runloop, motor, time

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
    async def MotorPairMoveForward(port_first=port.C, port_second=port.E, DurationInMS=1000, Velocity=200): # port.C and port.E are typically the ones used.
        motor.run_for_time(port_first, DurationInMS, Velocity)
        motor.run_for_time(port_second, DurationInMS, -Velocity)


    @staticmethod
    async def MotorPairMoveBackward(port_first=port.C, port_second=port.E, DurationInMS=1000, Velocity=200): # port.C and port.E are typically the ones used.
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


runloop.run(main())
