import time
import win32api
import keyboard

# only jitter while ads
state_left = win32api.GetKeyState(0x01)  # leftButton Up = 0 or 1; Down = -127 or -128
# print("left initial state = {0}".format(state_left))
state_right = win32api.GetKeyState(0x02)  # rightButton Up = 0 or 1; Down = -127 or -128
# print("left initial state = {0}".format(state_right))
# Set the toggle button
flat_toggle = 'num lock'
r_smg_toggle = 'y'
last_state = False  # last state for toggle button
# Set whether the anti-recoil is enabled by default
enabled = False


# module session
# module for FLATLINE anti recoil
# toggle button = "Y"
def flat_line(s_left, s_right, k_down, l_state, started, x):
    if k_down != l_state:
        l_state = k_down
        if l_state:
            started = not started
            if started:
                print("Anti-recoil Flat line ON")
            else:
                print("Anti-recoil Flat line OFF")

    if started:  # Button state changed
        if x != s_right:  # jitter aim while ads
            while x < 0:
                y = win32api.GetKeyState(0x01)  # always check the state of right click
                if y != s_left:
                    while y < 0:
                        print('Left Button Pressed with Right button')
                        win32api.mouse_event(0x01, 10, 0)  # move left
                        time.sleep(0.001)
                        win32api.mouse_event(0x01, -10, 0)  # move right back
                        time.sleep(0.001)
                        win32api.mouse_event(0x01, 0, 6)  # counter recoil
                        time.sleep(0.001)
                        win32api.mouse_event(0x01, -10, 0)  # move right
                        time.sleep(0.001)
                        win32api.mouse_event(0x01, 10, 0)  # move back left to center
                        time.sleep(0.001)
                        y = win32api.GetKeyState(0x01)  # check button state
                        print("left click state = {0}".format(y))
                x = win32api.GetKeyState(0x02)  # check right button state
                print("right click state = {0}".format(x))

        y = win32api.GetKeyState(0x01)
        if y != s_left:
            while y < 0:
                print('Left Button Pressed')
                win32api.mouse_event(0x01, 0, 1)  # counter recoil
                time.sleep(0.01)
                y = win32api.GetKeyState(0x01)  # check button state
                print("left click state = {0}".format(y))

    return [l_state, started]  # return the state of the toggle button and the enabled changes state


# module for R99 anti recoil
# toggle button = "U"
def r_smg(s_left, s_right, k_down, l_state, started, x):
    if k_down != l_state:
        l_state = k_down
        if l_state:
            started = not started
            if started:
                print("Anti-recoil R99 ON")
            else:
                print("Anti-recoil R99 OFF")

    if started:  # Button state changed
        if x != s_right:  # jitter aim while ads
            while x < 0:
                y = win32api.GetKeyState(0x01)  # always check the state of right click
                if y != s_left:
                    while y < 0:
                        print('Left Button Pressed with Right button')
                        win32api.mouse_event(0x01, 10, 0)  # move left
                        time.sleep(0.001)
                        win32api.mouse_event(0x01, -10, 0)  # move right back
                        time.sleep(0.001)
                        win32api.mouse_event(0x01, 0, 6)  # counter recoil
                        time.sleep(0.001)
                        win32api.mouse_event(0x01, -10, 0)  # move right
                        time.sleep(0.001)
                        win32api.mouse_event(0x01, 10, 0)  # move back left to center
                        time.sleep(0.001)
                        y = win32api.GetKeyState(0x01)  # check button state
                        print("left click state = {0}".format(y))
                x = win32api.GetKeyState(0x02)  # check right button state
                print("right click state = {0}".format(x))

        y = win32api.GetKeyState(0x01)
        if y != s_left:
            while y < 0:
                print('Left Button Pressed')
                win32api.mouse_event(0x01, 0, 1)  # counter recoil
                time.sleep(0.01)
                y = win32api.GetKeyState(0x01)  # check button state
                print("left click state = {0}".format(y))

    return [l_state, started]  # return the state of the toggle button and the enabled changes state


# print for startup
print("Anti-recoil script started!")
if enabled:
    print("Currently ON")
else:
    print("Currently OFF")

    while True:
        b = win32api.GetKeyState(0x02)
        key_down = keyboard.is_pressed(flat_toggle)  # check state changed for toggle button
        key_down2 = keyboard.is_pressed(r_smg_toggle)
        [last_state, enabled] = flat_line(state_left, state_right, key_down, last_state, enabled, b)
        [last_state, enabled] = r_smg(state_left, state_right, key_down2, last_state, enabled, b)


# module for CAR SMG anti recoil
# toggle button = "I"

# module for HAVOC anti recoil
# toggle button = "O"

# module for R301 anti recoil
# toggle button = "P"
