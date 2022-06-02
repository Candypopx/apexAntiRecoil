import time
import win32api
import keyboard

# only jitter while ads
state_left = win32api.GetKeyState(0x01)  # leftButton Up = 0 or 1; Down = -127 or -128
# print("left initial state = {0}".format(state_left))
state_right = win32api.GetKeyState(0x02)  # rightButton Up = 0 or 1; Down = -127 or -128
# print("left initial state = {0}".format(state_right))
# Set the toggle button
toggle_button = 'num lock'
last_state = False  # last state for toggle button
# Set whether the anti-recoil is enabled by default
enabled = False

# print for startup
print("Anti-recoil script started!")
if enabled:
    print("Currently ON")
else:
    print("Currently OFF")

    while True:
        b = win32api.GetKeyState(0x02)
        key_down = keyboard.is_pressed(toggle_button)  # check state changed for toggle button
        if key_down != last_state:
            last_state = key_down
            if last_state:
                enabled = not enabled
                if enabled:
                    print("Anti-recoil ON")
                else:
                    print("Anti-recoil OFF")

        if enabled:  # Button state changed
            if b != state_right:    # jitter aim while ads
                while b < 0:
                    a = win32api.GetKeyState(0x01)  # always check the state of right click
                    if a != state_left:
                        while a < 0:
                            print('Left Button Pressed with Right button')
                            win32api.mouse_event(0x01, 10, 0)    # move left
                            time.sleep(0.001)
                            win32api.mouse_event(0x01, -10, 0)   # move right back
                            time.sleep(0.001)
                            win32api.mouse_event(0x01, 0, 6)   # counter recoil
                            time.sleep(0.001)
                            win32api.mouse_event(0x01, -10, 0)    # move right
                            time.sleep(0.001)
                            win32api.mouse_event(0x01, 10, 0)    # move back left to center
                            time.sleep(0.001)
                            a = win32api.GetKeyState(0x01)  # check button state
                            print("left click state = {0}".format(a))
                    b = win32api.GetKeyState(0x02)  # check right button state
                    print("right click state = {0}".format(b))

            a = win32api.GetKeyState(0x01)
            if a != state_left:
                while a < 0:
                    print('Left Button Pressed')
                    win32api.mouse_event(0x01, 0, 1)  # counter recoil
                    time.sleep(0.01)
                    a = win32api.GetKeyState(0x01)  # check button state
                    print("left click state = {0}".format(a))

# module for FLATLINE anti recoil
def flatline():

# module for R99 anti recoil

# module for CAR SMG anti recoil

# module for HAVOC anti recoil

# module for R301 anti recoil
