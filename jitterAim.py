import time
import win32api
import keyboard

# only jitter while ads
state_left = win32api.GetKeyState(0x01)  # leftButton Up = 0 or 1; Down = -127 or -128
# print("left initial state = {0}".format(state_left))
state_right = win32api.GetKeyState(0x02)  # rightButton Up = 0 or 1; Down = -127 or -128
# print("left initial state = {0}".format(state_right))
# Set the toggle button
flat_toggle = 'Y'
r_smg_toggle = 'U'
car_smg_toggle = 'I'
havoc_toggle = 'O'

# last state for toggle button
last_state_flat = False
last_state_r_smg = False
last_state_car_smg = False
last_state_havoc = False

# Set whether the anti-recoil is enabled by default
enabled_flat = False
enabled_r_smg = False
enabled_car_smg = False
enabled_havoc = False


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
def r_smg(s_left, s_right, x):
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
                    win32api.mouse_event(0x01, 0, 17)  # counter recoil
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
            win32api.mouse_event(0x01, 0, 4)  # counter recoil
            time.sleep(0.01)
            a = win32api.GetKeyState(0x01)  # check button state
            print("left click state = {0}".format(a))


# module for CAR SMG anti recoil
# toggle button = "I"
def car_smg(s_left, s_right, x):
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
                    win32api.mouse_event(0x01, 0, 20)  # counter recoil
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
            win32api.mouse_event(0x01, 0, 5)  # counter recoil
            time.sleep(0.01)
            a = win32api.GetKeyState(0x01)  # check button state
            print("left click state = {0}".format(a))


# module for HAVOC anti recoil
# toggle button = "O"
def havoc(s_left, s_right, x):
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
                    win32api.mouse_event(0x01, 0, 10)  # counter recoil
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
            win32api.mouse_event(0x01, 0, 2)  # counter recoil
            time.sleep(0.01)
            a = win32api.GetKeyState(0x01)  # check button state
            print("left click state = {0}".format(a))


# main part
# print for startup
print("Anti-recoil script started!")

while True:
    b = win32api.GetKeyState(0x02)

    # check state changed for toggle button
    key_down_flat = keyboard.is_pressed(flat_toggle)
    key_down_r_smg = keyboard.is_pressed(r_smg_toggle)
    key_down_car_smg = keyboard.is_pressed(car_smg_toggle)
    key_down_havoc = keyboard.is_pressed(havoc_toggle)

    # FLAT LINE running script
    if key_down_flat != last_state_flat:
        last_state_flat = key_down_flat
        if last_state_flat:
            enabled_flat = not enabled_flat
            if enabled_flat:
                print("Anti-recoil flat line ON")
                # clear state
                last_state_r_smg = False
                enabled_r_smg = False
                last_state_car_smg = False
                enabled_car_smg = False
                last_state_havoc = False
                enabled_havoc = False
            else:
                print("Anti-recoil flat line OFF")

    if enabled_flat:
        flat_line(state_left, state_right, b)

    # R99 running script
    if key_down_r_smg != last_state_r_smg:
        last_state_r_smg = key_down_r_smg
        if last_state_r_smg:
            enabled_r_smg = not enabled_r_smg
            if enabled_r_smg:
                print("Anti-recoil R99 ON")
                # clear state
                last_state_flat = False
                enabled_flat = False
                last_state_car_smg = False
                enabled_car_smg = False
                last_state_havoc = False
                enabled_havoc = False
            else:
                print("Anti-recoil R99 OFF")

    if enabled_r_smg:
        r_smg(state_left, state_right, b)

    # CAR SMG running script
    if key_down_car_smg != last_state_car_smg:
        last_state_car_smg = key_down_car_smg
        if last_state_car_smg:
            enabled_car_smg = not enabled_car_smg
            if enabled_car_smg:
                print("Anti-recoil CAR SMG ON")
                # clear state
                last_state_flat = False
                enabled_flat = False
                last_state_r_smg = False
                enabled_r_smg = False
                last_state_havoc = False
                enabled_havoc = False
            else:
                print("Anti-recoil CAR SMG OFF")

    if enabled_car_smg:
        car_smg(state_left, state_right, b)

    # HAVOC running script
    if key_down_havoc != last_state_havoc:
        last_state_havoc = key_down_havoc
        if last_state_havoc:
            enabled_havoc = not enabled_havoc
            if enabled_havoc:
                print("Anti-recoil HAVOC ON")
                # clear state
                last_state_flat = False
                enabled_flat = False
                last_state_r_smg = False
                enabled_r_smg = False
                last_state_car_smg = False
                enabled_car_smg = False
            else:
                print("Anti-recoil HAVOC OFF")

    if enabled_havoc:
        havoc(state_left, state_right, b)


# module for R301 anti recoil
# toggle button = "P"
