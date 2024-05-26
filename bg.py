#!/usr/local/bin/python3
import pyautogui
import keyboard

# Set the screen coordinates for each action
freeze_coords = (1172, 224)
heropower_coords = (1059, 863)
refresh_coords = (1071, 232)
upgrade_coords = (727,252)
def click_at_coords(coords):
    current_mouse_position = pyautogui.position()  # Store current mouse position
    pyautogui.click(coords[0], coords[1])  # Move to coords and click
    pyautogui.moveTo(current_mouse_position)  # Move back to the original mouse position
    print(f"Clicked at {coords}")

def click_refresh():
    click_at_coords(refresh_coords)

def click_freeze():
    click_at_coords(freeze_coords)

def click_heropower():
    click_at_coords(heropower_coords)


def click_upgrade():
    click_at_coords(upgrade_coords)


# Bind keys to the respective functions
keyboard.add_hotkey('f', click_freeze)
keyboard.add_hotkey('h', click_heropower)
keyboard.add_hotkey('r', click_refresh)
keyboard.add_hotkey('u', click_upgrade)

# Keep the script running
print("Script running. Press 'F' for Freeze, 'H' for Hero Power, r for refresh, u for upgrade Press ESC to stop.")
keyboard.wait('esc')
