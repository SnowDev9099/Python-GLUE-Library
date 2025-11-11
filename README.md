# GLUE Library

**GPL 3.0 Licensed LEGO Universal Extension**

A simplified addon library for LEGO robotics that makes motor control and drivebase operations easier and more reliable.

---

## Overview

GLUE (GPL 3.0 LEGO Universal Extension) is a Python library designed to simplify common LEGO robotics operations, particularly addressing the quirks that arise when working with motor pairs and drivebase configurations.

## Features

- **Simplified Motor Pair Control** - Fixed implementation for forward/backward movement that handles the "funky" behavior of standard motor pair functions when using a standardized drivebase
- **Easy Turning Operations** - Dedicated left and right turn methods
- **Async/Await Support** - Built with modern Python async patterns
- **Standard Port Defaults** - Pre-configured for typical LEGO robotics setups (ports C and E)

## Installation

Simply copy the GLUE class into your LEGO robotics project file.

## Usage
```python
from hub import port
import runloop, motor, time

async def main():
    # Basic example
    print("Hello, World!")
    
    # Move forward for 1400ms at velocity 200
    await GLUE.MotorPairMoveForward(1400, 200)
    
    # Move backward
    await GLUE.MotorPairMoveBackward(1000, 200)
    
    # Turn left
    await GLUE.TurnLeft(500)
    
    # Turn right
    await GLUE.TurnRight(500)

runloop.run(main())
```

## API Reference

### `MotorPairMoveForward(port_first, port_second, DurationInMS, Velocity)`

Moves the robot forward using a motor pair.

**Parameters:**
- `port_first` (default: `port.C`) - First motor port
- `port_second` (default: `port.E`) - Second motor port
- `DurationInMS` (default: `1000`) - Duration in milliseconds
- `Velocity` (default: `200`) - Motor velocity

### `MotorPairMoveBackward(port_first, port_second, DurationInMS, Velocity)`

Moves the robot backward using a motor pair.

**Parameters:**
- Same as `MotorPairMoveForward`

### `TurnLeft(velocity)`

Executes a left turn.

**Parameters:**
- `velocity` - Turn velocity (defaults to -500 if 0 is provided)

### `TurnRight(velocity)`

Executes a right turn.

**Parameters:**
- `velocity` - Turn velocity (defaults to 500 if 0 is provided)

## Default Configuration

The library is pre-configured for standard LEGO robotics setups though in code you can change this when calling a method:
- **Primary motor ports:** C and E
- **Default velocity:** 200
- **Default duration:** 1000ms

## License

This project is licensed under the GPL 3.0 License - see the LICENSE file for details.

## Author

Original Author: [SnowDev9099](https://github.com/SnowDev9099)

## Contributing

Contributions, issues, feature requests, and pull requests are welcome! Please respect the GPL 3.0 license terms.

## Important Notes

- This library specifically addresses the inconsistent behavior that can occur with LEGO's built-in motor pair functions when used with drivebase configurations. this also aims to add other functions that help and add more functionality
- All methods are async and should be called with `await` or `runloop.run(yourmethodhere())` currently all are async and i am trying to keep it this way. some may not be in future releases!
- Designed for use with LEGO SPIKE Prime/Robot Inventor hubs

---

*Making LEGO robotics easier, one motor at a time!*
