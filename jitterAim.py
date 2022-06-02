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
enabled_flat = False
enabled_r_smg = False


# module session
# module for FLAT LINE anti recoil
# toggle button = "Y"
def flat_line(s_left, s_right, x):
    if x != s_right:  # jitter aim while ads
        while x < 0:
            a = win32api.GetKeyState(0x01)  # always check the state of right click
            if a != s_left:
                while a < 0:
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
                    a = win32api.GetKeyState(0x01)  # check button state
                    print("left click state = {0}".format(a))
            x = win32api.GetKeyState(0x02)  # check right button state
            print("right click state = {0}".format(x))

    a = win32api.GetKeyState(0x01)
    if a != s_left:
        while a < 0:
            print('Left Button Pressed')
            win32api.mouse_event(0x01, 0, 1)  # counter recoil
            time.sleep(0.01)
            a = win32api.GetKeyState(0x01)  # check button state
            print("left click state = {0}".format(a))


# module for R99 anti recoil
# toggle button = "U"


# print for startup
print("Anti-recoil script started!")

while True:
    b = win32api.GetKeyState(0x02)
    key_down_flat = keyboard.is_pressed(flat_toggle)  # check state changed for toggle button
    key_down_r_smg = keyboard.is_pressed(r_smg_toggle)

    if key_down_flat != last_state:
        last_state = key_down_flat
        if last_state:
            enabled_flat = not enabled_flat
            if enabled_flat:
                print("Anti-recoil flat line ON")
            else:
                print("Anti-recoil flat line OFF")

    if enabled_flat:
        flat_line(state_left, state_right, b)


# module for CAR SMG anti recoil
# toggle button = "I"

# module for HAVOC anti recoil
# toggle button = "O"

# module for R301 anti recoil
# toggle button = "P"
