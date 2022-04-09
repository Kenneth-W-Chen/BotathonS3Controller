# BotathonS3Controller
## What is this?
A python script designed to parse inputs from Xbox controllers and send it to a websocket server. Along with input information, it sends the team number and amount of inputs that the program has sent since it began running.

## JSON Output
This script sends the information in a JSON format. An example of what is sent is below:
```
{
     'teamNumber': 123,
     'sequenceNumber': 456,
     'eventType': "XBOX",
     'input':
     {
          'type': "AXIS",
          'key': "R-X",
          'value': -0.78910
     }
}
```

* `teamNumber` is the team's assigned team number. This is processed via a command-line argument.
* `sequenceNumber` is the number of inputs that has been sent since the program's start.
* `eventType` is the type of controller used
* `type` is either a button input, D-Pad input, or trigger/joystick input. Valid names are `AXIS`, `BUTTON`, and `DPAD`
* `key` is the key, joystick, trigger, or D-Pad input that is being parsed. Input names are
     * For `type: AXIS`:
          * `L-Y` for the left joystick's Y-axis
          * `L-X` for the left joystick's X-axis
          * `R-Y` for the right joystick's Y-axis
          * `R-X` for the right joystick's X-axis
          * `LEFT_TRIGGER` for the left trigger (sometimes called L2)
          * `RIGHT_TRIGGER` for the right trigger (sometimes called R2)
     * For `type: BUTTON`: 
          * `A_BUTTON`
          * `B_BUTTON`
          * `X_BUTTON`
          * `Y_BUTTON`
          * `LEFT_BUMPER`
          * `RIGHT_BUMPER`
          * `VIEW_BUTTON`
          * `MENU_BUTTON`
          * `L_JOY_PRESS`
          * `R_JOY_PRESS`
          * `XBOX_BUTTON`
          * `HOME_BUTTON`
     * For `type: DPAD`:
          * `DPAD1` 
* `value` is as follows:
     * For `AXIS`, the value is a float between `-1.0` and `1.0`.
          *  For the X-axis, left is negative and right is positive.
          *  For the Y-axis, down is negative and up is positive.
          *  For the triggers, released is negative and depressed is positive.
     *  For `BUTTON`:
          *   Button down is `True`.
          *   Button up is `False`.
     * For `DPAD`:
          *   Two nested JSON objects named `x` and `y`.
          *   Left or Down is `-1`
          *   Right or Up is `1`
          *   Neutral position is `0`
_Note: Input is never sent continuously. They are only sent if the value changes._

## Required Packages
This script uses the `asyncio`, `pygame`, and `websockets` libraries. They are on PyPI for installation using `pip install` or can be downloaded from their Gits.

[asyncio](https://github.com/python/cpython/tree/3.10/Lib/asyncio/)

[pygame](https://github.com/pygame/pygame)

[websockets](https://github.com/aaugustin/websockets)

## Compilation
_Note:_ Compilation tested with python 3.7.8
With the required packages installed, use `pyinstaller` to compile the program for use on machines without python installed.

Install pyinstaller using
```
pip install pyinstaller
```
or compile it from [the source](https://github.com/pyinstaller/pyinstaller)

#### Using pyinstaller
_[pyinstaller manual](https://pyinstaller.readthedocs.io/en/latest/usage.html)_

The command is
```
pyinstaller [options] script
```
Use option `-F` or `--onefile` to make the resulting output be one file.

Note that pyinstaller will create multiple files and folders while compiling.

__Additionally, pyinstaller cannot compile for any other platform except the platform you are currently using; you can only compile a MacOS app on a machine running MacOS, and you can only compile a Windows app on a machine running Windows.__
