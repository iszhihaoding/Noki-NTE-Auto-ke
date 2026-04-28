import win32gui
import win32con
import time
import threading
import win32api

"""
Virtual key codes for common keys:
Key Code List = [
    0x71,  # F2
    0x51,  # Q
    0x45,  # E
    0x52,  # R
    0x46,  # F
    0x58,  # X
    0x54,  # T
    0x4D,  # M
    0x31,  # 1
    0x32,  # 2
    0x33,  # 3
    0x34,  # 4
    0xA0,  # Left Shift
    0x20,  # Space
    0x04,  # Middle Mouse Button
    0x57,  # W
    0x41,  # A
    0x53,  # S
    0x44,  # D
    0x1B,  # ESC
    0xA4,  # ALT
    0x09,  # TAB
]
"""

def fake_activate_window(hwnd):
    """Activate a background window so that it can receive background keyboard and mouse commands."""
    try:
        win32gui.SendMessage(hwnd, WM_ACTIVATE, WA_ACTIVE, 0)
    except Exception as e:
        print(e)
def simulate_key_press_hold(handle, vk_code, duration):
    """
    Simulates pressing and holding a key for a specified duration

    Args:
        handle: Window handle to send the key event to
        vk_code: Virtual key code of the key to press
        duration: How long to hold the key (in seconds)
    """
    try:
        win32gui.PostMessage(handle, win32con.WM_KEYDOWN, vk_code, 0)
        time.sleep(duration)
        win32gui.PostMessage(handle, win32con.WM_KEYUP, vk_code, 0)
    except Exception as e:
        print(e)
        time.sleep(1)


def simulate_key_down(handle, vk_code):
    """
    Simulates pressing a key down (without releasing)

    Args:
        handle: Window handle to send the key event to
        vk_code: Virtual key code of the key to press down
    """
    try:
        win32gui.PostMessage(handle, win32con.WM_KEYDOWN, vk_code, 0)
    except Exception as e:
        print(e)
        time.sleep(1)


def simulate_key_up(handle, vk_code):
    """
    Simulates releasing a key

    Args:
        handle: Window handle to send the key event to
        vk_code: Virtual key code of the key to release
    """
    try:
        win32gui.PostMessage(handle, win32con.WM_KEYUP, vk_code, 0)
    except Exception as e:
        print(e)
        time.sleep(1)


def MAKELONG(low, high):
    """
    Creates a LONG value from two 16-bit values (used for mouse coordinates)

    Args:
        low: Low-order word (typically X coordinate)
        high: High-order word (typically Y coordinate)

    Returns:
        Combined LONG value
    """
    return (high << 16) | (low & 0xFFFF)


def simulate_mouse_left_click_hold(handle, x, y, duration):
    """
    Simulates pressing and holding the left mouse button for a specified duration

    Args:
        handle: Window handle to send the mouse event to
        x: X coordinate for the mouse event
        y: Y coordinate for the mouse event
        duration: How long to hold the mouse button (in seconds)
    """
    try:
        win32gui.PostMessage(handle, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, MAKELONG(x, y))
        time.sleep(duration)
        win32gui.PostMessage(handle, win32con.WM_LBUTTONUP, 0, MAKELONG(x, y))
    except Exception as e:
        print(e)
        time.sleep(1)


def simulate_mouse_left_down(handle, x, y, delay=0.001):
    """
    Simulates pressing down the left mouse button (without releasing)

    Args:
        handle: Window handle to send the mouse event to
        x: X coordinate for the mouse event
        y: Y coordinate for the mouse event
        delay: Short delay after the action (in seconds)
    """
    try:
        win32gui.PostMessage(handle, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, MAKELONG(x, y))
        time.sleep(delay)
    except Exception:
        pass


def simulate_mouse_left_up(handle, x, y, delay=0.001):
    """
    Simulates releasing the left mouse button

    Args:
        handle: Window handle to send the mouse event to
        x: X coordinate for the mouse event
        y: Y coordinate for the mouse event
        delay: Short delay after the action (in seconds)
    """
    try:
        win32gui.PostMessage(handle, win32con.WM_LBUTTONUP, 0, MAKELONG(x, y))
        time.sleep(delay)
    except Exception:

        pass
import timeimport time
import threading
import sys

if sys.platform ==import time
import threading
import sys

if sys.platform == "darwin":
    import Quartz
    from AppKit import NSWorkspace, NSRunningimport time
import threading
import sys

if sys.platform == "darwin":
    import Quartz
    from AppKit import NSWorkspace, NSRunningApplicationimport time
import threading
import sys

if sys.platform == "darwin":
    import Quartz
    from AppKit import NSWorkspace, NSRunningApplication
else:
    import win32gui
    import win32con
    importimport time
import threading
import sys

if sys.platform == "darwin":
    import Quartz
    from AppKit import NSWorkspace, NSRunningApplication
else:
    import win32gui
    import win32con
    import win32api


VK_CODES = {
    'F2': 0x7import time
import threading
import sys

if sys.platform == "darwin":
    import Quartz
    from AppKit import NSWorkspace, NSRunningApplication
else:
    import win32gui
    import win32con
    import win32api


VK_CODES = {
    'F2': 0x71,
    'Q': 0x51,
    'E': 0import time
import threading
import sys

if sys.platform == "darwin":
    import Quartz
    from AppKit import NSWorkspace, NSRunningApplication
else:
    import win32gui
    import win32con
    import win32api


VK_CODES = {
    'F2': 0x71,
    'Q': 0x51,
    'E': 0x45,
    'R': 0x52,
    'F':import time
import threading
import sys

if sys.platform == "darwin":
    import Quartz
    from AppKit import NSWorkspace, NSRunningApplication
else:
    import win32gui
    import win32con
    import win32api


VK_CODES = {
    'F2': 0x71,
    'Q': 0x51,
    'E': 0x45,
    'R': 0x52,
    'F': 0x46,
    'X': 0x58,
    'import time
import threading
import sys

if sys.platform == "darwin":
    import Quartz
    from AppKit import NSWorkspace, NSRunningApplication
else:
    import win32gui
    import win32con
    import win32api


VK_CODES = {
    'F2': 0x71,
    'Q': 0x51,
    'E': 0x45,
    'R': 0x52,
    'F': 0x46,
    'X': 0x58,
    'T': 0x54,
    'M': 0x4D,
import time
import threading
import sys

if sys.platform == "darwin":
    import Quartz
    from AppKit import NSWorkspace, NSRunningApplication
else:
    import win32gui
    import win32con
    import win32api


VK_CODES = {
    'F2': 0x71,
    'Q': 0x51,
    'E': 0x45,
    'R': 0x52,
    'F': 0x46,
    'X': 0x58,
    'T': 0x54,
    'M': 0x4D,
    '1': 0x31,
    '2': 0x32import time
import threading
import sys

if sys.platform == "darwin":
    import Quartz
    from AppKit import NSWorkspace, NSRunningApplication
else:
    import win32gui
    import win32con
    import win32api


VK_CODES = {
    'F2': 0x71,
    'Q': 0x51,
    'E': 0x45,
    'R': 0x52,
    'F': 0x46,
    'X': 0x58,
    'T': 0x54,
    'M': 0x4D,
    '1': 0x31,
    '2': 0x32,
    '3': 0x33,
    '4': 0ximport time
import threading
import sys

if sys.platform == "darwin":
    import Quartz
    from AppKit import NSWorkspace, NSRunningApplication
else:
    import win32gui
    import win32con
    import win32api


VK_CODES = {
    'F2': 0x71,
    'Q': 0x51,
    'E': 0x45,
    'R': 0x52,
    'F': 0x46,
    'X': 0x58,
    'T': 0x54,
    'M': 0x4D,
    '1': 0x31,
    '2': 0x32,
    '3': 0x33,
    '4': 0x34,
    'LEFT_SHIFT': 0xA0,
    'SPACE': 0x20,
    'MIDDLEimport time
import threading
import sys

if sys.platform == "darwin":
    import Quartz
    from AppKit import NSWorkspace, NSRunningApplication
else:
    import win32gui
    import win32con
    import win32api


VK_CODES = {
    'F2': 0x71,
    'Q': 0x51,
    'E': 0x45,
    'R': 0x52,
    'F': 0x46,
    'X': 0x58,
    'T': 0x54,
    'M': 0x4D,
    '1': 0x31,
    '2': 0x32,
    '3': 0x33,
    '4': 0x34,
    'LEFT_SHIFT': 0xA0,
    'SPACE': 0x20,
    'MIDDLE_MOUSE': 0x04,
    'W': 0x57,import time
import threading
import sys

if sys.platform == "darwin":
    import Quartz
    from AppKit import NSWorkspace, NSRunningApplication
else:
    import win32gui
    import win32con
    import win32api


VK_CODES = {
    'F2': 0x71,
    'Q': 0x51,
    'E': 0x45,
    'R': 0x52,
    'F': 0x46,
    'X': 0x58,
    'T': 0x54,
    'M': 0x4D,
    '1': 0x31,
    '2': 0x32,
    '3': 0x33,
    '4': 0x34,
    'LEFT_SHIFT': 0xA0,
    'SPACE': 0x20,
    'MIDDLE_MOUSE': 0x04,
    'W': 0x57,
    'A': 0x41,import time
import threading
import sys

if sys.platform == "darwin":
    import Quartz
    from AppKit import NSWorkspace, NSRunningApplication
else:
    import win32gui
    import win32con
    import win32api


VK_CODES = {
    'F2': 0x71,
    'Q': 0x51,
    'E': 0x45,
    'R': 0x52,
    'F': 0x46,
    'X': 0x58,
    'T': 0x54,
    'M': 0x4D,
    '1': 0x31,
    '2': 0x32,
    '3': 0x33,
    '4': 0x34,
    'LEFT_SHIFT': 0xA0,
    'SPACE': 0x20,
    'MIDDLE_MOUSE': 0x04,
    'W': 0x57,
    'A': 0x41,
    'S': 0x53,
    'D': 0x4import time
import threading
import sys

if sys.platform == "darwin":
    import Quartz
    from AppKit import NSWorkspace, NSRunningApplication
else:
    import win32gui
    import win32con
    import win32api


VK_CODES = {
    'F2': 0x71,
    'Q': 0x51,
    'E': 0x45,
    'R': 0x52,
    'F': 0x46,
    'X': 0x58,
    'T': 0x54,
    'M': 0x4D,
    '1': 0x31,
    '2': 0x32,
    '3': 0x33,
    '4': 0x34,
    'LEFT_SHIFT': 0xA0,
    'SPACE': 0x20,
    'MIDDLE_MOUSE': 0x04,
    'W': 0x57,
    'A': 0x41,
    'S': 0x53,
    'D': 0x44,
    'ESC': 0x1B,
    'ALT': 0import time
import threading
import sys

if sys.platform == "darwin":
    import Quartz
    from AppKit import NSWorkspace, NSRunningApplication
else:
    import win32gui
    import win32con
    import win32api


VK_CODES = {
    'F2': 0x71,
    'Q': 0x51,
    'E': 0x45,
    'R': 0x52,
    'F': 0x46,
    'X': 0x58,
    'T': 0x54,
    'M': 0x4D,
    '1': 0x31,
    '2': 0x32,
    '3': 0x33,
    '4': 0x34,
    'LEFT_SHIFT': 0xA0,
    'SPACE': 0x20,
    'MIDDLE_MOUSE': 0x04,
    'W': 0x57,
    'A': 0x41,
    'S': 0x53,
    'D': 0x44,
    'ESC': 0x1B,
    'ALT': 0xA4,
    'TAB': 0x09,
}

if sys.platformimport time
import threading
import sys

if sys.platform == "darwin":
    import Quartz
    from AppKit import NSWorkspace, NSRunningApplication
else:
    import win32gui
    import win32con
    import win32api


VK_CODES = {
    'F2': 0x71,
    'Q': 0x51,
    'E': 0x45,
    'R': 0x52,
    'F': 0x46,
    'X': 0x58,
    'T': 0x54,
    'M': 0x4D,
    '1': 0x31,
    '2': 0x32,
    '3': 0x33,
    '4': 0x34,
    'LEFT_SHIFT': 0xA0,
    'SPACE': 0x20,
    'MIDDLE_MOUSE': 0x04,
    'W': 0x57,
    'A': 0x41,
    'S': 0x53,
    'D': 0x44,
    'ESC': 0x1B,
    'ALT': 0xA4,
    'TAB': 0x09,
}

if sys.platform == "darwin":
    MAC_KEY_MAP = {
        0x71:import time
import threading
import sys

if sys.platform == "darwin":
    import Quartz
    from AppKit import NSWorkspace, NSRunningApplication
else:
    import win32gui
    import win32con
    import win32api


VK_CODES = {
    'F2': 0x71,
    'Q': 0x51,
    'E': 0x45,
    'R': 0x52,
    'F': 0x46,
    'X': 0x58,
    'T': 0x54,
    'M': 0x4D,
    '1': 0x31,
    '2': 0x32,
    '3': 0x33,
    '4': 0x34,
    'LEFT_SHIFT': 0xA0,
    'SPACE': 0x20,
    'MIDDLE_MOUSE': 0x04,
    'W': 0x57,
    'A': 0x41,
    'S': 0x53,
    'D': 0x44,
    'ESC': 0x1B,
    'ALT': 0xA4,
    'TAB': 0x09,
}

if sys.platform == "darwin":
    MAC_KEY_MAP = {
        0x71: 120,  
        0x51: 12,   
        0x45: 14,import time
import threading
import sys

if sys.platform == "darwin":
    import Quartz
    from AppKit import NSWorkspace, NSRunningApplication
else:
    import win32gui
    import win32con
    import win32api


VK_CODES = {
    'F2': 0x71,
    'Q': 0x51,
    'E': 0x45,
    'R': 0x52,
    'F': 0x46,
    'X': 0x58,
    'T': 0x54,
    'M': 0x4D,
    '1': 0x31,
    '2': 0x32,
    '3': 0x33,
    '4': 0x34,
    'LEFT_SHIFT': 0xA0,
    'SPACE': 0x20,
    'MIDDLE_MOUSE': 0x04,
    'W': 0x57,
    'A': 0x41,
    'S': 0x53,
    'D': 0x44,
    'ESC': 0x1B,
    'ALT': 0xA4,
    'TAB': 0x09,
}

if sys.platform == "darwin":
    MAC_KEY_MAP = {
        0x71: 120,  
        0x51: 12,   
        0x45: 14,   
        0x52: 15import time
import threading
import sys

if sys.platform == "darwin":
    import Quartz
    from AppKit import NSWorkspace, NSRunningApplication
else:
    import win32gui
    import win32con
    import win32api


VK_CODES = {
    'F2': 0x71,
    'Q': 0x51,
    'E': 0x45,
    'R': 0x52,
    'F': 0x46,
    'X': 0x58,
    'T': 0x54,
    'M': 0x4D,
    '1': 0x31,
    '2': 0x32,
    '3': 0x33,
    '4': 0x34,
    'LEFT_SHIFT': 0xA0,
    'SPACE': 0x20,
    'MIDDLE_MOUSE': 0x04,
    'W': 0x57,
    'A': 0x41,
    'S': 0x53,
    'D': 0x44,
    'ESC': 0x1B,
    'ALT': 0xA4,
    'TAB': 0x09,
}

if sys.platform == "darwin":
    MAC_KEY_MAP = {
        0x71: 120,  
        0x51: 12,   
        0x45: 14,   
        0x52: 15,   
        0x46: 3,    
        0x58:import time
import threading
import sys

if sys.platform == "darwin":
    import Quartz
    from AppKit import NSWorkspace, NSRunningApplication
else:
    import win32gui
    import win32con
    import win32api


VK_CODES = {
    'F2': 0x71,
    'Q': 0x51,
    'E': 0x45,
    'R': 0x52,
    'F': 0x46,
    'X': 0x58,
    'T': 0x54,
    'M': 0x4D,
    '1': 0x31,
    '2': 0x32,
    '3': 0x33,
    '4': 0x34,
    'LEFT_SHIFT': 0xA0,
    'SPACE': 0x20,
    'MIDDLE_MOUSE': 0x04,
    'W': 0x57,
    'A': 0x41,
    'S': 0x53,
    'D': 0x44,
    'ESC': 0x1B,
    'ALT': 0xA4,
    'TAB': 0x09,
}

if sys.platform == "darwin":
    MAC_KEY_MAP = {
        0x71: 120,  
        0x51: 12,   
        0x45: 14,   
        0x52: 15,   
        0x46: 3,    
        0x58: 7,    
        0x54: 17,   
        0ximport time
import threading
import sys

if sys.platform == "darwin":
    import Quartz
    from AppKit import NSWorkspace, NSRunningApplication
else:
    import win32gui
    import win32con
    import win32api


VK_CODES = {
    'F2': 0x71,
    'Q': 0x51,
    'E': 0x45,
    'R': 0x52,
    'F': 0x46,
    'X': 0x58,
    'T': 0x54,
    'M': 0x4D,
    '1': 0x31,
    '2': 0x32,
    '3': 0x33,
    '4': 0x34,
    'LEFT_SHIFT': 0xA0,
    'SPACE': 0x20,
    'MIDDLE_MOUSE': 0x04,
    'W': 0x57,
    'A': 0x41,
    'S': 0x53,
    'D': 0x44,
    'ESC': 0x1B,
    'ALT': 0xA4,
    'TAB': 0x09,
}

if sys.platform == "darwin":
    MAC_KEY_MAP = {
        0x71: 120,  
        0x51: 12,   
        0x45: 14,   
        0x52: 15,   
        0x46: 3,    
        0x58: 7,    
        0x54: 17,   
        0x4D: 46,   
        0x31: 18,   
import time
import threading
import sys

if sys.platform == "darwin":
    import Quartz
    from AppKit import NSWorkspace, NSRunningApplication
else:
    import win32gui
    import win32con
    import win32api


VK_CODES = {
    'F2': 0x71,
    'Q': 0x51,
    'E': 0x45,
    'R': 0x52,
    'F': 0x46,
    'X': 0x58,
    'T': 0x54,
    'M': 0x4D,
    '1': 0x31,
    '2': 0x32,
    '3': 0x33,
    '4': 0x34,
    'LEFT_SHIFT': 0xA0,
    'SPACE': 0x20,
    'MIDDLE_MOUSE': 0x04,
    'W': 0x57,
    'A': 0x41,
    'S': 0x53,
    'D': 0x44,
    'ESC': 0x1B,
    'ALT': 0xA4,
    'TAB': 0x09,
}

if sys.platform == "darwin":
    MAC_KEY_MAP = {
        0x71: 120,  
        0x51: 12,   
        0x45: 14,   
        0x52: 15,   
        0x46: 3,    
        0x58: 7,    
        0x54: 17,   
        0x4D: 46,   
        0x31: 18,   
        0x32: 19,   
        0x33: 20,   
        0x3import time
import threading
import sys

if sys.platform == "darwin":
    import Quartz
    from AppKit import NSWorkspace, NSRunningApplication
else:
    import win32gui
    import win32con
    import win32api


VK_CODES = {
    'F2': 0x71,
    'Q': 0x51,
    'E': 0x45,
    'R': 0x52,
    'F': 0x46,
    'X': 0x58,
    'T': 0x54,
    'M': 0x4D,
    '1': 0x31,
    '2': 0x32,
    '3': 0x33,
    '4': 0x34,
    'LEFT_SHIFT': 0xA0,
    'SPACE': 0x20,
    'MIDDLE_MOUSE': 0x04,
    'W': 0x57,
    'A': 0x41,
    'S': 0x53,
    'D': 0x44,
    'ESC': 0x1B,
    'ALT': 0xA4,
    'TAB': 0x09,
}

if sys.platform == "darwin":
    MAC_KEY_MAP = {
        0x71: 120,  
        0x51: 12,   
        0x45: 14,   
        0x52: 15,   
        0x46: 3,    
        0x58: 7,    
        0x54: 17,   
        0x4D: 46,   
        0x31: 18,   
        0x32: 19,   
        0x33: 20,   
        0x34: 21,   
        0xAimport time
import threading
import sys

if sys.platform == "darwin":
    import Quartz
    from AppKit import NSWorkspace, NSRunningApplication
else:
    import win32gui
    import win32con
    import win32api


VK_CODES = {
    'F2': 0x71,
    'Q': 0x51,
    'E': 0x45,
    'R': 0x52,
    'F': 0x46,
    'X': 0x58,
    'T': 0x54,
    'M': 0x4D,
    '1': 0x31,
    '2': 0x32,
    '3': 0x33,
    '4': 0x34,
    'LEFT_SHIFT': 0xA0,
    'SPACE': 0x20,
    'MIDDLE_MOUSE': 0x04,
    'W': 0x57,
    'A': 0x41,
    'S': 0x53,
    'D': 0x44,
    'ESC': 0x1B,
    'ALT': 0xA4,
    'TAB': 0x09,
}

if sys.platform == "darwin":
    MAC_KEY_MAP = {
        0x71: 120,  
        0x51: 12,   
        0x45: 14,   
        0x52: 15,   
        0x46: 3,    
        0x58: 7,    
        0x54: 17,   
        0x4D: 46,   
        0x31: 18,   
        0x32: 19,   
        0x33: 20,   
        0x34: 21,   
        0xA0: 56,   
        0x20: 49,   
        0x57: 13import time
import threading
import sys

if sys.platform == "darwin":
    import Quartz
    from AppKit import NSWorkspace, NSRunningApplication
else:
    import win32gui
    import win32con
    import win32api


VK_CODES = {
    'F2': 0x71,
    'Q': 0x51,
    'E': 0x45,
    'R': 0x52,
    'F': 0x46,
    'X': 0x58,
    'T': 0x54,
    'M': 0x4D,
    '1': 0x31,
    '2': 0x32,
    '3': 0x33,
    '4': 0x34,
    'LEFT_SHIFT': 0xA0,
    'SPACE': 0x20,
    'MIDDLE_MOUSE': 0x04,
    'W': 0x57,
    'A': 0x41,
    'S': 0x53,
    'D': 0x44,
    'ESC': 0x1B,
    'ALT': 0xA4,
    'TAB': 0x09,
}

if sys.platform == "darwin":
    MAC_KEY_MAP = {
        0x71: 120,  
        0x51: 12,   
        0x45: 14,   
        0x52: 15,   
        0x46: 3,    
        0x58: 7,    
        0x54: 17,   
        0x4D: 46,   
        0x31: 18,   
        0x32: 19,   
        0x33: 20,   
        0x34: 21,   
        0xA0: 56,   
        0x20: 49,   
        0x57: 13,   
        0x41: 0import time
import threading
import sys

if sys.platform == "darwin":
    import Quartz
    from AppKit import NSWorkspace, NSRunningApplication
else:
    import win32gui
    import win32con
    import win32api


VK_CODES = {
    'F2': 0x71,
    'Q': 0x51,
    'E': 0x45,
    'R': 0x52,
    'F': 0x46,
    'X': 0x58,
    'T': 0x54,
    'M': 0x4D,
    '1': 0x31,
    '2': 0x32,
    '3': 0x33,
    '4': 0x34,
    'LEFT_SHIFT': 0xA0,
    'SPACE': 0x20,
    'MIDDLE_MOUSE': 0x04,
    'W': 0x57,
    'A': 0x41,
    'S': 0x53,
    'D': 0x44,
    'ESC': 0x1B,
    'ALT': 0xA4,
    'TAB': 0x09,
}

if sys.platform == "darwin":
    MAC_KEY_MAP = {
        0x71: 120,  
        0x51: 12,   
        0x45: 14,   
        0x52: 15,   
        0x46: 3,    
        0x58: 7,    
        0x54: 17,   
        0x4D: 46,   
        0x31: 18,   
        0x32: 19,   
        0x33: 20,   
        0x34: 21,   
        0xA0: 56,   
        0x20: 49,   
        0x57: 13,   
        0x41: 0,    
        0x53: 1,    
        0x44:import time
import threading
import sys

if sys.platform == "darwin":
    import Quartz
    from AppKit import NSWorkspace, NSRunningApplication
else:
    import win32gui
    import win32con
    import win32api


VK_CODES = {
    'F2': 0x71,
    'Q': 0x51,
    'E': 0x45,
    'R': 0x52,
    'F': 0x46,
    'X': 0x58,
    'T': 0x54,
    'M': 0x4D,
    '1': 0x31,
    '2': 0x32,
    '3': 0x33,
    '4': 0x34,
    'LEFT_SHIFT': 0xA0,
    'SPACE': 0x20,
    'MIDDLE_MOUSE': 0x04,
    'W': 0x57,
    'A': 0x41,
    'S': 0x53,
    'D': 0x44,
    'ESC': 0x1B,
    'ALT': 0xA4,
    'TAB': 0x09,
}

if sys.platform == "darwin":
    MAC_KEY_MAP = {
        0x71: 120,  
        0x51: 12,   
        0x45: 14,   
        0x52: 15,   
        0x46: 3,    
        0x58: 7,    
        0x54: 17,   
        0x4D: 46,   
        0x31: 18,   
        0x32: 19,   
        0x33: 20,   
        0x34: 21,   
        0xA0: 56,   
        0x20: 49,   
        0x57: 13,   
        0x41: 0,    
        0x53: 1,    
        0x44: 2,    
        0x1B: 53,   
        0xAimport time
import threading
import sys

if sys.platform == "darwin":
    import Quartz
    from AppKit import NSWorkspace, NSRunningApplication
else:
    import win32gui
    import win32con
    import win32api


VK_CODES = {
    'F2': 0x71,
    'Q': 0x51,
    'E': 0x45,
    'R': 0x52,
    'F': 0x46,
    'X': 0x58,
    'T': 0x54,
    'M': 0x4D,
    '1': 0x31,
    '2': 0x32,
    '3': 0x33,
    '4': 0x34,
    'LEFT_SHIFT': 0xA0,
    'SPACE': 0x20,
    'MIDDLE_MOUSE': 0x04,
    'W': 0x57,
    'A': 0x41,
    'S': 0x53,
    'D': 0x44,
    'ESC': 0x1B,
    'ALT': 0xA4,
    'TAB': 0x09,
}

if sys.platform == "darwin":
    MAC_KEY_MAP = {
        0x71: 120,  
        0x51: 12,   
        0x45: 14,   
        0x52: 15,   
        0x46: 3,    
        0x58: 7,    
        0x54: 17,   
        0x4D: 46,   
        0x31: 18,   
        0x32: 19,   
        0x33: 20,   
        0x34: 21,   
        0xA0: 56,   
        0x20: 49,   
        0x57: 13,   
        0x41: 0,    
        0x53: 1,    
        0x44: 2,    
        0x1B: 53,   
        0xA4: 58,   
        0import time
import threading
import sys

if sys.platform == "darwin":
    import Quartz
    from AppKit import NSWorkspace, NSRunningApplication
else:
    import win32gui
    import win32con
    import win32api


VK_CODES = {
    'F2': 0x71,
    'Q': 0x51,
    'E': 0x45,
    'R': 0x52,
    'F': 0x46,
    'X': 0x58,
    'T': 0x54,
    'M': 0x4D,
    '1': 0x31,
    '2': 0x32,
    '3': 0x33,
    '4': 0x34,
    'LEFT_SHIFT': 0xA0,
    'SPACE': 0x20,
    'MIDDLE_MOUSE': 0x04,
    'W': 0x57,
    'A': 0x41,
    'S': 0x53,
    'D': 0x44,
    'ESC': 0x1B,
    'ALT': 0xA4,
    'TAB': 0x09,
}

if sys.platform == "darwin":
    MAC_KEY_MAP = {
        0x71: 120,  
        0x51: 12,   
        0x45: 14,   
        0x52: 15,   
        0x46: 3,    
        0x58: 7,    
        0x54: 17,   
        0x4D: 46,   
        0x31: 18,   
        0x32: 19,   
        0x33: 20,   
        0x34: 21,   
        0xA0: 56,   
        0x20: 49,   
        0x57: 13,   
        0x41: 0,    
        0x53: 1,    
        0x44: 2,    
        0x1B: 53,   
        0xA4: 58,   
        0x09: 48,   
    }

    def fake_activate_window(himport time
import threading
import sys

if sys.platform == "darwin":
    import Quartz
    from AppKit import NSWorkspace, NSRunningApplication
else:
    import win32gui
    import win32con
    import win32api


VK_CODES = {
    'F2': 0x71,
    'Q': 0x51,
    'E': 0x45,
    'R': 0x52,
    'F': 0x46,
    'X': 0x58,
    'T': 0x54,
    'M': 0x4D,
    '1': 0x31,
    '2': 0x32,
    '3': 0x33,
    '4': 0x34,
    'LEFT_SHIFT': 0xA0,
    'SPACE': 0x20,
    'MIDDLE_MOUSE': 0x04,
    'W': 0x57,
    'A': 0x41,
    'S': 0x53,
    'D': 0x44,
    'ESC': 0x1B,
    'ALT': 0xA4,
    'TAB': 0x09,
}

if sys.platform == "darwin":
    MAC_KEY_MAP = {
        0x71: 120,  
        0x51: 12,   
        0x45: 14,   
        0x52: 15,   
        0x46: 3,    
        0x58: 7,    
        0x54: 17,   
        0x4D: 46,   
        0x31: 18,   
        0x32: 19,   
        0x33: 20,   
        0x34: 21,   
        0xA0: 56,   
        0x20: 49,   
        0x57: 13,   
        0x41: 0,    
        0x53: 1,    
        0x44: 2,    
        0x1B: 53,   
        0xA4: 58,   
        0x09: 48,   
    }

    def fake_activate_window(hwimport time
import threading
import sys

if sys.platform == "darwin":
    import Quartz
    from AppKit import NSWorkspace, NSRunningApplication
else:
    import win32gui
    import win32con
    import win32api


VK_CODES = {
    'F2': 0x71,
    'Q': 0x51,
    'E': 0x45,
    'R': 0x52,
    'F': 0x46,
    'X': 0x58,
    'T': 0x54,
    'M': 0x4D,
    '1': 0x31,
    '2': 0x32,
    '3': 0x33,
    '4': 0x34,
    'LEFT_SHIFT': 0xA0,
    'SPACE': 0x20,
    'MIDDLE_MOUSE': 0x04,
    'W': 0x57,
    'A': 0x41,
    'S': 0x53,
    'D': 0x44,
    'ESC': 0x1B,
    'ALT': 0xA4,
    'TAB': 0x09,
}

if sys.platform == "darwin":
    MAC_KEY_MAP = {
        0x71: 120,  
        0x51: 12,   
        0x45: 14,   
        0x52: 15,   
        0x46: 3,    
        0x58: 7,    
        0x54: 17,   
        0x4D: 46,   
        0x31: 18,   
        0x32: 19,   
        0x33: 20,   
        0x34: 21,   
        0xA0: 56,   
        0x20: 49,   
        0x57: 13,   
        0x41: 0,    
        0x53: 1,    
        0x44: 2,    
        0x1B: 53,   
        0xA4: 58,   
        0x09: 48,   
    }

    def fake_activate_window(hwnd):
        try:
            ws =import time
import threading
import sys

if sys.platform == "darwin":
    import Quartz
    from AppKit import NSWorkspace, NSRunningApplication
else:
    import win32gui
    import win32con
    import win32api


VK_CODES = {
    'F2': 0x71,
    'Q': 0x51,
    'E': 0x45,
    'R': 0x52,
    'F': 0x46,
    'X': 0x58,
    'T': 0x54,
    'M': 0x4D,
    '1': 0x31,
    '2': 0x32,
    '3': 0x33,
    '4': 0x34,
    'LEFT_SHIFT': 0xA0,
    'SPACE': 0x20,
    'MIDDLE_MOUSE': 0x04,
    'W': 0x57,
    'A': 0x41,
    'S': 0x53,
    'D': 0x44,
    'ESC': 0x1B,
    'ALT': 0xA4,
    'TAB': 0x09,
}

if sys.platform == "darwin":
    MAC_KEY_MAP = {
        0x71: 120,  
        0x51: 12,   
        0x45: 14,   
        0x52: 15,   
        0x46: 3,    
        0x58: 7,    
        0x54: 17,   
        0x4D: 46,   
        0x31: 18,   
        0x32: 19,   
        0x33: 20,   
        0x34: 21,   
        0xA0: 56,   
        0x20: 49,   
        0x57: 13,   
        0x41: 0,    
        0x53: 1,    
        0x44: 2,    
        0x1B: 53,   
        0xA4: 58,   
        0x09: 48,   
    }

    def fake_activate_window(hwnd):
        try:
            ws = NSWorkspace.sharedWorkspace()
            app = NSimport time
import threading
import sys

if sys.platform == "darwin":
    import Quartz
    from AppKit import NSWorkspace, NSRunningApplication
else:
    import win32gui
    import win32con
    import win32api


VK_CODES = {
    'F2': 0x71,
    'Q': 0x51,
    'E': 0x45,
    'R': 0x52,
    'F': 0x46,
    'X': 0x58,
    'T': 0x54,
    'M': 0x4D,
    '1': 0x31,
    '2': 0x32,
    '3': 0x33,
    '4': 0x34,
    'LEFT_SHIFT': 0xA0,
    'SPACE': 0x20,
    'MIDDLE_MOUSE': 0x04,
    'W': 0x57,
    'A': 0x41,
    'S': 0x53,
    'D': 0x44,
    'ESC': 0x1B,
    'ALT': 0xA4,
    'TAB': 0x09,
}

if sys.platform == "darwin":
    MAC_KEY_MAP = {
        0x71: 120,  
        0x51: 12,   
        0x45: 14,   
        0x52: 15,   
        0x46: 3,    
        0x58: 7,    
        0x54: 17,   
        0x4D: 46,   
        0x31: 18,   
        0x32: 19,   
        0x33: 20,   
        0x34: 21,   
        0xA0: 56,   
        0x20: 49,   
        0x57: 13,   
        0x41: 0,    
        0x53: 1,    
        0x44: 2,    
        0x1B: 53,   
        0xA4: 58,   
        0x09: 48,   
    }

    def fake_activate_window(hwnd):
        try:
            ws = NSWorkspace.sharedWorkspace()
            app = NSRunningApplication.runningApplicationWithProcessIdentifier_(hwimport time
import threading
import sys

if sys.platform == "darwin":
    import Quartz
    from AppKit import NSWorkspace, NSRunningApplication
else:
    import win32gui
    import win32con
    import win32api


VK_CODES = {
    'F2': 0x71,
    'Q': 0x51,
    'E': 0x45,
    'R': 0x52,
    'F': 0x46,
    'X': 0x58,
    'T': 0x54,
    'M': 0x4D,
    '1': 0x31,
    '2': 0x32,
    '3': 0x33,
    '4': 0x34,
    'LEFT_SHIFT': 0xA0,
    'SPACE': 0x20,
    'MIDDLE_MOUSE': 0x04,
    'W': 0x57,
    'A': 0x41,
    'S': 0x53,
    'D': 0x44,
    'ESC': 0x1B,
    'ALT': 0xA4,
    'TAB': 0x09,
}

if sys.platform == "darwin":
    MAC_KEY_MAP = {
        0x71: 120,  
        0x51: 12,   
        0x45: 14,   
        0x52: 15,   
        0x46: 3,    
        0x58: 7,    
        0x54: 17,   
        0x4D: 46,   
        0x31: 18,   
        0x32: 19,   
        0x33: 20,   
        0x34: 21,   
        0xA0: 56,   
        0x20: 49,   
        0x57: 13,   
        0x41: 0,    
        0x53: 1,    
        0x44: 2,    
        0x1B: 53,   
        0xA4: 58,   
        0x09: 48,   
    }

    def fake_activate_window(hwnd):
        try:
            ws = NSWorkspace.sharedWorkspace()
            app = NSRunningApplication.runningApplicationWithProcessIdentifier_(hwnd)
            if app:
                wsimport time
import threading
import sys

if sys.platform == "darwin":
    import Quartz
    from AppKit import NSWorkspace, NSRunningApplication
else:
    import win32gui
    import win32con
    import win32api


VK_CODES = {
    'F2': 0x71,
    'Q': 0x51,
    'E': 0x45,
    'R': 0x52,
    'F': 0x46,
    'X': 0x58,
    'T': 0x54,
    'M': 0x4D,
    '1': 0x31,
    '2': 0x32,
    '3': 0x33,
    '4': 0x34,
    'LEFT_SHIFT': 0xA0,
    'SPACE': 0x20,
    'MIDDLE_MOUSE': 0x04,
    'W': 0x57,
    'A': 0x41,
    'S': 0x53,
    'D': 0x44,
    'ESC': 0x1B,
    'ALT': 0xA4,
    'TAB': 0x09,
}

if sys.platform == "darwin":
    MAC_KEY_MAP = {
        0x71: 120,  
        0x51: 12,   
        0x45: 14,   
        0x52: 15,   
        0x46: 3,    
        0x58: 7,    
        0x54: 17,   
        0x4D: 46,   
        0x31: 18,   
        0x32: 19,   
        0x33: 20,   
        0x34: 21,   
        0xA0: 56,   
        0x20: 49,   
        0x57: 13,   
        0x41: 0,    
        0x53: 1,    
        0x44: 2,    
        0x1B: 53,   
        0xA4: 58,   
        0x09: 48,   
    }

    def fake_activate_window(hwnd):
        try:
            ws = NSWorkspace.sharedWorkspace()
            app = NSRunningApplication.runningApplicationWithProcessIdentifier_(hwnd)
            if app:
                ws.launchApplicationWithBundleIdentifier_options_additionalEventimport time
import threading
import sys

if sys.platform == "darwin":
    import Quartz
    from AppKit import NSWorkspace, NSRunningApplication
else:
    import win32gui
    import win32con
    import win32api


VK_CODES = {
    'F2': 0x71,
    'Q': 0x51,
    'E': 0x45,
    'R': 0x52,
    'F': 0x46,
    'X': 0x58,
    'T': 0x54,
    'M': 0x4D,
    '1': 0x31,
    '2': 0x32,
    '3': 0x33,
    '4': 0x34,
    'LEFT_SHIFT': 0xA0,
    'SPACE': 0x20,
    'MIDDLE_MOUSE': 0x04,
    'W': 0x57,
    'A': 0x41,
    'S': 0x53,
    'D': 0x44,
    'ESC': 0x1B,
    'ALT': 0xA4,
    'TAB': 0x09,
}

if sys.platform == "darwin":
    MAC_KEY_MAP = {
        0x71: 120,  
        0x51: 12,   
        0x45: 14,   
        0x52: 15,   
        0x46: 3,    
        0x58: 7,    
        0x54: 17,   
        0x4D: 46,   
        0x31: 18,   
        0x32: 19,   
        0x33: 20,   
        0x34: 21,   
        0xA0: 56,   
        0x20: 49,   
        0x57: 13,   
        0x41: 0,    
        0x53: 1,    
        0x44: 2,    
        0x1B: 53,   
        0xA4: 58,   
        0x09: 48,   
    }

    def fake_activate_window(hwnd):
        try:
            ws = NSWorkspace.sharedWorkspace()
            app = NSRunningApplication.runningApplicationWithProcessIdentifier_(hwnd)
            if app:
                ws.launchApplicationWithBundleIdentifier_options_additionalEventParamDescriptor_launchIdentifier_(
                    app.bundleIdentifier(), 0, None, None)import time
import threading
import sys

if sys.platform == "darwin":
    import Quartz
    from AppKit import NSWorkspace, NSRunningApplication
else:
    import win32gui
    import win32con
    import win32api


VK_CODES = {
    'F2': 0x71,
    'Q': 0x51,
    'E': 0x45,
    'R': 0x52,
    'F': 0x46,
    'X': 0x58,
    'T': 0x54,
    'M': 0x4D,
    '1': 0x31,
    '2': 0x32,
    '3': 0x33,
    '4': 0x34,
    'LEFT_SHIFT': 0xA0,
    'SPACE': 0x20,
    'MIDDLE_MOUSE': 0x04,
    'W': 0x57,
    'A': 0x41,
    'S': 0x53,
    'D': 0x44,
    'ESC': 0x1B,
    'ALT': 0xA4,
    'TAB': 0x09,
}

if sys.platform == "darwin":
    MAC_KEY_MAP = {
        0x71: 120,  
        0x51: 12,   
        0x45: 14,   
        0x52: 15,   
        0x46: 3,    
        0x58: 7,    
        0x54: 17,   
        0x4D: 46,   
        0x31: 18,   
        0x32: 19,   
        0x33: 20,   
        0x34: 21,   
        0xA0: 56,   
        0x20: 49,   
        0x57: 13,   
        0x41: 0,    
        0x53: 1,    
        0x44: 2,    
        0x1B: 53,   
        0xA4: 58,   
        0x09: 48,   
    }

    def fake_activate_window(hwnd):
        try:
            ws = NSWorkspace.sharedWorkspace()
            app = NSRunningApplication.runningApplicationWithProcessIdentifier_(hwnd)
            if app:
                ws.launchApplicationWithBundleIdentifier_options_additionalEventParamDescriptor_launchIdentifier_(
                    app.bundleIdentifier(), 0, None, None)
                return True
        except Exception as e:
            print(e)
        return Falseimport time
import threading
import sys

if sys.platform == "darwin":
    import Quartz
    from AppKit import NSWorkspace, NSRunningApplication
else:
    import win32gui
    import win32con
    import win32api


VK_CODES = {
    'F2': 0x71,
    'Q': 0x51,
    'E': 0x45,
    'R': 0x52,
    'F': 0x46,
    'X': 0x58,
    'T': 0x54,
    'M': 0x4D,
    '1': 0x31,
    '2': 0x32,
    '3': 0x33,
    '4': 0x34,
    'LEFT_SHIFT': 0xA0,
    'SPACE': 0x20,
    'MIDDLE_MOUSE': 0x04,
    'W': 0x57,
    'A': 0x41,
    'S': 0x53,
    'D': 0x44,
    'ESC': 0x1B,
    'ALT': 0xA4,
    'TAB': 0x09,
}

if sys.platform == "darwin":
    MAC_KEY_MAP = {
        0x71: 120,  
        0x51: 12,   
        0x45: 14,   
        0x52: 15,   
        0x46: 3,    
        0x58: 7,    
        0x54: 17,   
        0x4D: 46,   
        0x31: 18,   
        0x32: 19,   
        0x33: 20,   
        0x34: 21,   
        0xA0: 56,   
        0x20: 49,   
        0x57: 13,   
        0x41: 0,    
        0x53: 1,    
        0x44: 2,    
        0x1B: 53,   
        0xA4: 58,   
        0x09: 48,   
    }

    def fake_activate_window(hwnd):
        try:
            ws = NSWorkspace.sharedWorkspace()
            app = NSRunningApplication.runningApplicationWithProcessIdentifier_(hwnd)
            if app:
                ws.launchApplicationWithBundleIdentifier_options_additionalEventParamDescriptor_launchIdentifier_(
                    app.bundleIdentifier(), 0, None, None)
                return True
        except Exception as e:
            print(e)
        return False

    def simulate_key_press_hold(handle, vk_code, duration):
        try:
            mac_key_code = MACimport time
import threading
import sys

if sys.platform == "darwin":
    import Quartz
    from AppKit import NSWorkspace, NSRunningApplication
else:
    import win32gui
    import win32con
    import win32api


VK_CODES = {
    'F2': 0x71,
    'Q': 0x51,
    'E': 0x45,
    'R': 0x52,
    'F': 0x46,
    'X': 0x58,
    'T': 0x54,
    'M': 0x4D,
    '1': 0x31,
    '2': 0x32,
    '3': 0x33,
    '4': 0x34,
    'LEFT_SHIFT': 0xA0,
    'SPACE': 0x20,
    'MIDDLE_MOUSE': 0x04,
    'W': 0x57,
    'A': 0x41,
    'S': 0x53,
    'D': 0x44,
    'ESC': 0x1B,
    'ALT': 0xA4,
    'TAB': 0x09,
}

if sys.platform == "darwin":
    MAC_KEY_MAP = {
        0x71: 120,  
        0x51: 12,   
        0x45: 14,   
        0x52: 15,   
        0x46: 3,    
        0x58: 7,    
        0x54: 17,   
        0x4D: 46,   
        0x31: 18,   
        0x32: 19,   
        0x33: 20,   
        0x34: 21,   
        0xA0: 56,   
        0x20: 49,   
        0x57: 13,   
        0x41: 0,    
        0x53: 1,    
        0x44: 2,    
        0x1B: 53,   
        0xA4: 58,   
        0x09: 48,   
    }

    def fake_activate_window(hwnd):
        try:
            ws = NSWorkspace.sharedWorkspace()
            app = NSRunningApplication.runningApplicationWithProcessIdentifier_(hwnd)
            if app:
                ws.launchApplicationWithBundleIdentifier_options_additionalEventParamDescriptor_launchIdentifier_(
                    app.bundleIdentifier(), 0, None, None)
                return True
        except Exception as e:
            print(e)
        return False

    def simulate_key_press_hold(handle, vk_code, duration):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)import time
import threading
import sys

if sys.platform == "darwin":
    import Quartz
    from AppKit import NSWorkspace, NSRunningApplication
else:
    import win32gui
    import win32con
    import win32api


VK_CODES = {
    'F2': 0x71,
    'Q': 0x51,
    'E': 0x45,
    'R': 0x52,
    'F': 0x46,
    'X': 0x58,
    'T': 0x54,
    'M': 0x4D,
    '1': 0x31,
    '2': 0x32,
    '3': 0x33,
    '4': 0x34,
    'LEFT_SHIFT': 0xA0,
    'SPACE': 0x20,
    'MIDDLE_MOUSE': 0x04,
    'W': 0x57,
    'A': 0x41,
    'S': 0x53,
    'D': 0x44,
    'ESC': 0x1B,
    'ALT': 0xA4,
    'TAB': 0x09,
}

if sys.platform == "darwin":
    MAC_KEY_MAP = {
        0x71: 120,  
        0x51: 12,   
        0x45: 14,   
        0x52: 15,   
        0x46: 3,    
        0x58: 7,    
        0x54: 17,   
        0x4D: 46,   
        0x31: 18,   
        0x32: 19,   
        0x33: 20,   
        0x34: 21,   
        0xA0: 56,   
        0x20: 49,   
        0x57: 13,   
        0x41: 0,    
        0x53: 1,    
        0x44: 2,    
        0x1B: 53,   
        0xA4: 58,   
        0x09: 48,   
    }

    def fake_activate_window(hwnd):
        try:
            ws = NSWorkspace.sharedWorkspace()
            app = NSRunningApplication.runningApplicationWithProcessIdentifier_(hwnd)
            if app:
                ws.launchApplicationWithBundleIdentifier_options_additionalEventParamDescriptor_launchIdentifier_(
                    app.bundleIdentifier(), 0, None, None)
                return True
        except Exception as e:
            print(e)
        return False

    def simulate_key_press_hold(handle, vk_code, duration):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            
            down_event = Quartz.CGEventCreateimport time
import threading
import sys

if sys.platform == "darwin":
    import Quartz
    from AppKit import NSWorkspace, NSRunningApplication
else:
    import win32gui
    import win32con
    import win32api


VK_CODES = {
    'F2': 0x71,
    'Q': 0x51,
    'E': 0x45,
    'R': 0x52,
    'F': 0x46,
    'X': 0x58,
    'T': 0x54,
    'M': 0x4D,
    '1': 0x31,
    '2': 0x32,
    '3': 0x33,
    '4': 0x34,
    'LEFT_SHIFT': 0xA0,
    'SPACE': 0x20,
    'MIDDLE_MOUSE': 0x04,
    'W': 0x57,
    'A': 0x41,
    'S': 0x53,
    'D': 0x44,
    'ESC': 0x1B,
    'ALT': 0xA4,
    'TAB': 0x09,
}

if sys.platform == "darwin":
    MAC_KEY_MAP = {
        0x71: 120,  
        0x51: 12,   
        0x45: 14,   
        0x52: 15,   
        0x46: 3,    
        0x58: 7,    
        0x54: 17,   
        0x4D: 46,   
        0x31: 18,   
        0x32: 19,   
        0x33: 20,   
        0x34: 21,   
        0xA0: 56,   
        0x20: 49,   
        0x57: 13,   
        0x41: 0,    
        0x53: 1,    
        0x44: 2,    
        0x1B: 53,   
        0xA4: 58,   
        0x09: 48,   
    }

    def fake_activate_window(hwnd):
        try:
            ws = NSWorkspace.sharedWorkspace()
            app = NSRunningApplication.runningApplicationWithProcessIdentifier_(hwnd)
            if app:
                ws.launchApplicationWithBundleIdentifier_options_additionalEventParamDescriptor_launchIdentifier_(
                    app.bundleIdentifier(), 0, None, None)
                return True
        except Exception as e:
            print(e)
        return False

    def simulate_key_press_hold(handle, vk_code, duration):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            
            down_event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, True)
            Quartz.CGEventPost(Quimport time
import threading
import sys

if sys.platform == "darwin":
    import Quartz
    from AppKit import NSWorkspace, NSRunningApplication
else:
    import win32gui
    import win32con
    import win32api


VK_CODES = {
    'F2': 0x71,
    'Q': 0x51,
    'E': 0x45,
    'R': 0x52,
    'F': 0x46,
    'X': 0x58,
    'T': 0x54,
    'M': 0x4D,
    '1': 0x31,
    '2': 0x32,
    '3': 0x33,
    '4': 0x34,
    'LEFT_SHIFT': 0xA0,
    'SPACE': 0x20,
    'MIDDLE_MOUSE': 0x04,
    'W': 0x57,
    'A': 0x41,
    'S': 0x53,
    'D': 0x44,
    'ESC': 0x1B,
    'ALT': 0xA4,
    'TAB': 0x09,
}

if sys.platform == "darwin":
    MAC_KEY_MAP = {
        0x71: 120,  
        0x51: 12,   
        0x45: 14,   
        0x52: 15,   
        0x46: 3,    
        0x58: 7,    
        0x54: 17,   
        0x4D: 46,   
        0x31: 18,   
        0x32: 19,   
        0x33: 20,   
        0x34: 21,   
        0xA0: 56,   
        0x20: 49,   
        0x57: 13,   
        0x41: 0,    
        0x53: 1,    
        0x44: 2,    
        0x1B: 53,   
        0xA4: 58,   
        0x09: 48,   
    }

    def fake_activate_window(hwnd):
        try:
            ws = NSWorkspace.sharedWorkspace()
            app = NSRunningApplication.runningApplicationWithProcessIdentifier_(hwnd)
            if app:
                ws.launchApplicationWithBundleIdentifier_options_additionalEventParamDescriptor_launchIdentifier_(
                    app.bundleIdentifier(), 0, None, None)
                return True
        except Exception as e:
            print(e)
        return False

    def simulate_key_press_hold(handle, vk_code, duration):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            
            down_event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, True)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, down_eventimport time
import threading
import sys

if sys.platform == "darwin":
    import Quartz
    from AppKit import NSWorkspace, NSRunningApplication
else:
    import win32gui
    import win32con
    import win32api


VK_CODES = {
    'F2': 0x71,
    'Q': 0x51,
    'E': 0x45,
    'R': 0x52,
    'F': 0x46,
    'X': 0x58,
    'T': 0x54,
    'M': 0x4D,
    '1': 0x31,
    '2': 0x32,
    '3': 0x33,
    '4': 0x34,
    'LEFT_SHIFT': 0xA0,
    'SPACE': 0x20,
    'MIDDLE_MOUSE': 0x04,
    'W': 0x57,
    'A': 0x41,
    'S': 0x53,
    'D': 0x44,
    'ESC': 0x1B,
    'ALT': 0xA4,
    'TAB': 0x09,
}

if sys.platform == "darwin":
    MAC_KEY_MAP = {
        0x71: 120,  
        0x51: 12,   
        0x45: 14,   
        0x52: 15,   
        0x46: 3,    
        0x58: 7,    
        0x54: 17,   
        0x4D: 46,   
        0x31: 18,   
        0x32: 19,   
        0x33: 20,   
        0x34: 21,   
        0xA0: 56,   
        0x20: 49,   
        0x57: 13,   
        0x41: 0,    
        0x53: 1,    
        0x44: 2,    
        0x1B: 53,   
        0xA4: 58,   
        0x09: 48,   
    }

    def fake_activate_window(hwnd):
        try:
            ws = NSWorkspace.sharedWorkspace()
            app = NSRunningApplication.runningApplicationWithProcessIdentifier_(hwnd)
            if app:
                ws.launchApplicationWithBundleIdentifier_options_additionalEventParamDescriptor_launchIdentifier_(
                    app.bundleIdentifier(), 0, None, None)
                return True
        except Exception as e:
            print(e)
        return False

    def simulate_key_press_hold(handle, vk_code, duration):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            
            down_event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, True)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, down_event)
            
            time.sleep(duration)
            
            up_event = Quartz.CGEventCreateKeyboardEventimport time
import threading
import sys

if sys.platform == "darwin":
    import Quartz
    from AppKit import NSWorkspace, NSRunningApplication
else:
    import win32gui
    import win32con
    import win32api


VK_CODES = {
    'F2': 0x71,
    'Q': 0x51,
    'E': 0x45,
    'R': 0x52,
    'F': 0x46,
    'X': 0x58,
    'T': 0x54,
    'M': 0x4D,
    '1': 0x31,
    '2': 0x32,
    '3': 0x33,
    '4': 0x34,
    'LEFT_SHIFT': 0xA0,
    'SPACE': 0x20,
    'MIDDLE_MOUSE': 0x04,
    'W': 0x57,
    'A': 0x41,
    'S': 0x53,
    'D': 0x44,
    'ESC': 0x1B,
    'ALT': 0xA4,
    'TAB': 0x09,
}

if sys.platform == "darwin":
    MAC_KEY_MAP = {
        0x71: 120,  
        0x51: 12,   
        0x45: 14,   
        0x52: 15,   
        0x46: 3,    
        0x58: 7,    
        0x54: 17,   
        0x4D: 46,   
        0x31: 18,   
        0x32: 19,   
        0x33: 20,   
        0x34: 21,   
        0xA0: 56,   
        0x20: 49,   
        0x57: 13,   
        0x41: 0,    
        0x53: 1,    
        0x44: 2,    
        0x1B: 53,   
        0xA4: 58,   
        0x09: 48,   
    }

    def fake_activate_window(hwnd):
        try:
            ws = NSWorkspace.sharedWorkspace()
            app = NSRunningApplication.runningApplicationWithProcessIdentifier_(hwnd)
            if app:
                ws.launchApplicationWithBundleIdentifier_options_additionalEventParamDescriptor_launchIdentifier_(
                    app.bundleIdentifier(), 0, None, None)
                return True
        except Exception as e:
            print(e)
        return False

    def simulate_key_press_hold(handle, vk_code, duration):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            
            down_event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, True)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, down_event)
            
            time.sleep(duration)
            
            up_event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, False)
            Quartz.CGEventPost(Quartz.kimport time
import threading
import sys

if sys.platform == "darwin":
    import Quartz
    from AppKit import NSWorkspace, NSRunningApplication
else:
    import win32gui
    import win32con
    import win32api


VK_CODES = {
    'F2': 0x71,
    'Q': 0x51,
    'E': 0x45,
    'R': 0x52,
    'F': 0x46,
    'X': 0x58,
    'T': 0x54,
    'M': 0x4D,
    '1': 0x31,
    '2': 0x32,
    '3': 0x33,
    '4': 0x34,
    'LEFT_SHIFT': 0xA0,
    'SPACE': 0x20,
    'MIDDLE_MOUSE': 0x04,
    'W': 0x57,
    'A': 0x41,
    'S': 0x53,
    'D': 0x44,
    'ESC': 0x1B,
    'ALT': 0xA4,
    'TAB': 0x09,
}

if sys.platform == "darwin":
    MAC_KEY_MAP = {
        0x71: 120,  
        0x51: 12,   
        0x45: 14,   
        0x52: 15,   
        0x46: 3,    
        0x58: 7,    
        0x54: 17,   
        0x4D: 46,   
        0x31: 18,   
        0x32: 19,   
        0x33: 20,   
        0x34: 21,   
        0xA0: 56,   
        0x20: 49,   
        0x57: 13,   
        0x41: 0,    
        0x53: 1,    
        0x44: 2,    
        0x1B: 53,   
        0xA4: 58,   
        0x09: 48,   
    }

    def fake_activate_window(hwnd):
        try:
            ws = NSWorkspace.sharedWorkspace()
            app = NSRunningApplication.runningApplicationWithProcessIdentifier_(hwnd)
            if app:
                ws.launchApplicationWithBundleIdentifier_options_additionalEventParamDescriptor_launchIdentifier_(
                    app.bundleIdentifier(), 0, None, None)
                return True
        except Exception as e:
            print(e)
        return False

    def simulate_key_press_hold(handle, vk_code, duration):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            
            down_event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, True)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, down_event)
            
            time.sleep(duration)
            
            up_event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, False)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, up_event)
            
        except Exception as e:
            print(eimport time
import threading
import sys

if sys.platform == "darwin":
    import Quartz
    from AppKit import NSWorkspace, NSRunningApplication
else:
    import win32gui
    import win32con
    import win32api


VK_CODES = {
    'F2': 0x71,
    'Q': 0x51,
    'E': 0x45,
    'R': 0x52,
    'F': 0x46,
    'X': 0x58,
    'T': 0x54,
    'M': 0x4D,
    '1': 0x31,
    '2': 0x32,
    '3': 0x33,
    '4': 0x34,
    'LEFT_SHIFT': 0xA0,
    'SPACE': 0x20,
    'MIDDLE_MOUSE': 0x04,
    'W': 0x57,
    'A': 0x41,
    'S': 0x53,
    'D': 0x44,
    'ESC': 0x1B,
    'ALT': 0xA4,
    'TAB': 0x09,
}

if sys.platform == "darwin":
    MAC_KEY_MAP = {
        0x71: 120,  
        0x51: 12,   
        0x45: 14,   
        0x52: 15,   
        0x46: 3,    
        0x58: 7,    
        0x54: 17,   
        0x4D: 46,   
        0x31: 18,   
        0x32: 19,   
        0x33: 20,   
        0x34: 21,   
        0xA0: 56,   
        0x20: 49,   
        0x57: 13,   
        0x41: 0,    
        0x53: 1,    
        0x44: 2,    
        0x1B: 53,   
        0xA4: 58,   
        0x09: 48,   
    }

    def fake_activate_window(hwnd):
        try:
            ws = NSWorkspace.sharedWorkspace()
            app = NSRunningApplication.runningApplicationWithProcessIdentifier_(hwnd)
            if app:
                ws.launchApplicationWithBundleIdentifier_options_additionalEventParamDescriptor_launchIdentifier_(
                    app.bundleIdentifier(), 0, None, None)
                return True
        except Exception as e:
            print(e)
        return False

    def simulate_key_press_hold(handle, vk_code, duration):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            
            down_event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, True)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, down_event)
            
            time.sleep(duration)
            
            up_event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, False)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, up_event)
            
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_key_down(handle, vk_codeimport time
import threading
import sys

if sys.platform == "darwin":
    import Quartz
    from AppKit import NSWorkspace, NSRunningApplication
else:
    import win32gui
    import win32con
    import win32api


VK_CODES = {
    'F2': 0x71,
    'Q': 0x51,
    'E': 0x45,
    'R': 0x52,
    'F': 0x46,
    'X': 0x58,
    'T': 0x54,
    'M': 0x4D,
    '1': 0x31,
    '2': 0x32,
    '3': 0x33,
    '4': 0x34,
    'LEFT_SHIFT': 0xA0,
    'SPACE': 0x20,
    'MIDDLE_MOUSE': 0x04,
    'W': 0x57,
    'A': 0x41,
    'S': 0x53,
    'D': 0x44,
    'ESC': 0x1B,
    'ALT': 0xA4,
    'TAB': 0x09,
}

if sys.platform == "darwin":
    MAC_KEY_MAP = {
        0x71: 120,  
        0x51: 12,   
        0x45: 14,   
        0x52: 15,   
        0x46: 3,    
        0x58: 7,    
        0x54: 17,   
        0x4D: 46,   
        0x31: 18,   
        0x32: 19,   
        0x33: 20,   
        0x34: 21,   
        0xA0: 56,   
        0x20: 49,   
        0x57: 13,   
        0x41: 0,    
        0x53: 1,    
        0x44: 2,    
        0x1B: 53,   
        0xA4: 58,   
        0x09: 48,   
    }

    def fake_activate_window(hwnd):
        try:
            ws = NSWorkspace.sharedWorkspace()
            app = NSRunningApplication.runningApplicationWithProcessIdentifier_(hwnd)
            if app:
                ws.launchApplicationWithBundleIdentifier_options_additionalEventParamDescriptor_launchIdentifier_(
                    app.bundleIdentifier(), 0, None, None)
                return True
        except Exception as e:
            print(e)
        return False

    def simulate_key_press_hold(handle, vk_code, duration):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            
            down_event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, True)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, down_event)
            
            time.sleep(duration)
            
            up_event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, False)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, up_event)
            
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_key_down(handle, vk_code):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vimport time
import threading
import sys

if sys.platform == "darwin":
    import Quartz
    from AppKit import NSWorkspace, NSRunningApplication
else:
    import win32gui
    import win32con
    import win32api


VK_CODES = {
    'F2': 0x71,
    'Q': 0x51,
    'E': 0x45,
    'R': 0x52,
    'F': 0x46,
    'X': 0x58,
    'T': 0x54,
    'M': 0x4D,
    '1': 0x31,
    '2': 0x32,
    '3': 0x33,
    '4': 0x34,
    'LEFT_SHIFT': 0xA0,
    'SPACE': 0x20,
    'MIDDLE_MOUSE': 0x04,
    'W': 0x57,
    'A': 0x41,
    'S': 0x53,
    'D': 0x44,
    'ESC': 0x1B,
    'ALT': 0xA4,
    'TAB': 0x09,
}

if sys.platform == "darwin":
    MAC_KEY_MAP = {
        0x71: 120,  
        0x51: 12,   
        0x45: 14,   
        0x52: 15,   
        0x46: 3,    
        0x58: 7,    
        0x54: 17,   
        0x4D: 46,   
        0x31: 18,   
        0x32: 19,   
        0x33: 20,   
        0x34: 21,   
        0xA0: 56,   
        0x20: 49,   
        0x57: 13,   
        0x41: 0,    
        0x53: 1,    
        0x44: 2,    
        0x1B: 53,   
        0xA4: 58,   
        0x09: 48,   
    }

    def fake_activate_window(hwnd):
        try:
            ws = NSWorkspace.sharedWorkspace()
            app = NSRunningApplication.runningApplicationWithProcessIdentifier_(hwnd)
            if app:
                ws.launchApplicationWithBundleIdentifier_options_additionalEventParamDescriptor_launchIdentifier_(
                    app.bundleIdentifier(), 0, None, None)
                return True
        except Exception as e:
            print(e)
        return False

    def simulate_key_press_hold(handle, vk_code, duration):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            
            down_event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, True)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, down_event)
            
            time.sleep(duration)
            
            up_event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, False)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, up_event)
            
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_key_down(handle, vk_code):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            event = Quartz.CGimport time
import threading
import sys

if sys.platform == "darwin":
    import Quartz
    from AppKit import NSWorkspace, NSRunningApplication
else:
    import win32gui
    import win32con
    import win32api


VK_CODES = {
    'F2': 0x71,
    'Q': 0x51,
    'E': 0x45,
    'R': 0x52,
    'F': 0x46,
    'X': 0x58,
    'T': 0x54,
    'M': 0x4D,
    '1': 0x31,
    '2': 0x32,
    '3': 0x33,
    '4': 0x34,
    'LEFT_SHIFT': 0xA0,
    'SPACE': 0x20,
    'MIDDLE_MOUSE': 0x04,
    'W': 0x57,
    'A': 0x41,
    'S': 0x53,
    'D': 0x44,
    'ESC': 0x1B,
    'ALT': 0xA4,
    'TAB': 0x09,
}

if sys.platform == "darwin":
    MAC_KEY_MAP = {
        0x71: 120,  
        0x51: 12,   
        0x45: 14,   
        0x52: 15,   
        0x46: 3,    
        0x58: 7,    
        0x54: 17,   
        0x4D: 46,   
        0x31: 18,   
        0x32: 19,   
        0x33: 20,   
        0x34: 21,   
        0xA0: 56,   
        0x20: 49,   
        0x57: 13,   
        0x41: 0,    
        0x53: 1,    
        0x44: 2,    
        0x1B: 53,   
        0xA4: 58,   
        0x09: 48,   
    }

    def fake_activate_window(hwnd):
        try:
            ws = NSWorkspace.sharedWorkspace()
            app = NSRunningApplication.runningApplicationWithProcessIdentifier_(hwnd)
            if app:
                ws.launchApplicationWithBundleIdentifier_options_additionalEventParamDescriptor_launchIdentifier_(
                    app.bundleIdentifier(), 0, None, None)
                return True
        except Exception as e:
            print(e)
        return False

    def simulate_key_press_hold(handle, vk_code, duration):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            
            down_event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, True)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, down_event)
            
            time.sleep(duration)
            
            up_event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, False)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, up_event)
            
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_key_down(handle, vk_code):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_codeimport time
import threading
import sys

if sys.platform == "darwin":
    import Quartz
    from AppKit import NSWorkspace, NSRunningApplication
else:
    import win32gui
    import win32con
    import win32api


VK_CODES = {
    'F2': 0x71,
    'Q': 0x51,
    'E': 0x45,
    'R': 0x52,
    'F': 0x46,
    'X': 0x58,
    'T': 0x54,
    'M': 0x4D,
    '1': 0x31,
    '2': 0x32,
    '3': 0x33,
    '4': 0x34,
    'LEFT_SHIFT': 0xA0,
    'SPACE': 0x20,
    'MIDDLE_MOUSE': 0x04,
    'W': 0x57,
    'A': 0x41,
    'S': 0x53,
    'D': 0x44,
    'ESC': 0x1B,
    'ALT': 0xA4,
    'TAB': 0x09,
}

if sys.platform == "darwin":
    MAC_KEY_MAP = {
        0x71: 120,  
        0x51: 12,   
        0x45: 14,   
        0x52: 15,   
        0x46: 3,    
        0x58: 7,    
        0x54: 17,   
        0x4D: 46,   
        0x31: 18,   
        0x32: 19,   
        0x33: 20,   
        0x34: 21,   
        0xA0: 56,   
        0x20: 49,   
        0x57: 13,   
        0x41: 0,    
        0x53: 1,    
        0x44: 2,    
        0x1B: 53,   
        0xA4: 58,   
        0x09: 48,   
    }

    def fake_activate_window(hwnd):
        try:
            ws = NSWorkspace.sharedWorkspace()
            app = NSRunningApplication.runningApplicationWithProcessIdentifier_(hwnd)
            if app:
                ws.launchApplicationWithBundleIdentifier_options_additionalEventParamDescriptor_launchIdentifier_(
                    app.bundleIdentifier(), 0, None, None)
                return True
        except Exception as e:
            print(e)
        return False

    def simulate_key_press_hold(handle, vk_code, duration):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            
            down_event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, True)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, down_event)
            
            time.sleep(duration)
            
            up_event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, False)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, up_event)
            
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_key_down(handle, vk_code):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, True)
            Quartz.CGEventPostimport time
import threading
import sys

if sys.platform == "darwin":
    import Quartz
    from AppKit import NSWorkspace, NSRunningApplication
else:
    import win32gui
    import win32con
    import win32api


VK_CODES = {
    'F2': 0x71,
    'Q': 0x51,
    'E': 0x45,
    'R': 0x52,
    'F': 0x46,
    'X': 0x58,
    'T': 0x54,
    'M': 0x4D,
    '1': 0x31,
    '2': 0x32,
    '3': 0x33,
    '4': 0x34,
    'LEFT_SHIFT': 0xA0,
    'SPACE': 0x20,
    'MIDDLE_MOUSE': 0x04,
    'W': 0x57,
    'A': 0x41,
    'S': 0x53,
    'D': 0x44,
    'ESC': 0x1B,
    'ALT': 0xA4,
    'TAB': 0x09,
}

if sys.platform == "darwin":
    MAC_KEY_MAP = {
        0x71: 120,  
        0x51: 12,   
        0x45: 14,   
        0x52: 15,   
        0x46: 3,    
        0x58: 7,    
        0x54: 17,   
        0x4D: 46,   
        0x31: 18,   
        0x32: 19,   
        0x33: 20,   
        0x34: 21,   
        0xA0: 56,   
        0x20: 49,   
        0x57: 13,   
        0x41: 0,    
        0x53: 1,    
        0x44: 2,    
        0x1B: 53,   
        0xA4: 58,   
        0x09: 48,   
    }

    def fake_activate_window(hwnd):
        try:
            ws = NSWorkspace.sharedWorkspace()
            app = NSRunningApplication.runningApplicationWithProcessIdentifier_(hwnd)
            if app:
                ws.launchApplicationWithBundleIdentifier_options_additionalEventParamDescriptor_launchIdentifier_(
                    app.bundleIdentifier(), 0, None, None)
                return True
        except Exception as e:
            print(e)
        return False

    def simulate_key_press_hold(handle, vk_code, duration):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            
            down_event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, True)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, down_event)
            
            time.sleep(duration)
            
            up_event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, False)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, up_event)
            
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_key_down(handle, vk_code):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, True)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap,import time
import threading
import sys

if sys.platform == "darwin":
    import Quartz
    from AppKit import NSWorkspace, NSRunningApplication
else:
    import win32gui
    import win32con
    import win32api


VK_CODES = {
    'F2': 0x71,
    'Q': 0x51,
    'E': 0x45,
    'R': 0x52,
    'F': 0x46,
    'X': 0x58,
    'T': 0x54,
    'M': 0x4D,
    '1': 0x31,
    '2': 0x32,
    '3': 0x33,
    '4': 0x34,
    'LEFT_SHIFT': 0xA0,
    'SPACE': 0x20,
    'MIDDLE_MOUSE': 0x04,
    'W': 0x57,
    'A': 0x41,
    'S': 0x53,
    'D': 0x44,
    'ESC': 0x1B,
    'ALT': 0xA4,
    'TAB': 0x09,
}

if sys.platform == "darwin":
    MAC_KEY_MAP = {
        0x71: 120,  
        0x51: 12,   
        0x45: 14,   
        0x52: 15,   
        0x46: 3,    
        0x58: 7,    
        0x54: 17,   
        0x4D: 46,   
        0x31: 18,   
        0x32: 19,   
        0x33: 20,   
        0x34: 21,   
        0xA0: 56,   
        0x20: 49,   
        0x57: 13,   
        0x41: 0,    
        0x53: 1,    
        0x44: 2,    
        0x1B: 53,   
        0xA4: 58,   
        0x09: 48,   
    }

    def fake_activate_window(hwnd):
        try:
            ws = NSWorkspace.sharedWorkspace()
            app = NSRunningApplication.runningApplicationWithProcessIdentifier_(hwnd)
            if app:
                ws.launchApplicationWithBundleIdentifier_options_additionalEventParamDescriptor_launchIdentifier_(
                    app.bundleIdentifier(), 0, None, None)
                return True
        except Exception as e:
            print(e)
        return False

    def simulate_key_press_hold(handle, vk_code, duration):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            
            down_event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, True)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, down_event)
            
            time.sleep(duration)
            
            up_event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, False)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, up_event)
            
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_key_down(handle, vk_code):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, True)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
        except Exception as e:
            print(e)
            time.sleep(1import time
import threading
import sys

if sys.platform == "darwin":
    import Quartz
    from AppKit import NSWorkspace, NSRunningApplication
else:
    import win32gui
    import win32con
    import win32api


VK_CODES = {
    'F2': 0x71,
    'Q': 0x51,
    'E': 0x45,
    'R': 0x52,
    'F': 0x46,
    'X': 0x58,
    'T': 0x54,
    'M': 0x4D,
    '1': 0x31,
    '2': 0x32,
    '3': 0x33,
    '4': 0x34,
    'LEFT_SHIFT': 0xA0,
    'SPACE': 0x20,
    'MIDDLE_MOUSE': 0x04,
    'W': 0x57,
    'A': 0x41,
    'S': 0x53,
    'D': 0x44,
    'ESC': 0x1B,
    'ALT': 0xA4,
    'TAB': 0x09,
}

if sys.platform == "darwin":
    MAC_KEY_MAP = {
        0x71: 120,  
        0x51: 12,   
        0x45: 14,   
        0x52: 15,   
        0x46: 3,    
        0x58: 7,    
        0x54: 17,   
        0x4D: 46,   
        0x31: 18,   
        0x32: 19,   
        0x33: 20,   
        0x34: 21,   
        0xA0: 56,   
        0x20: 49,   
        0x57: 13,   
        0x41: 0,    
        0x53: 1,    
        0x44: 2,    
        0x1B: 53,   
        0xA4: 58,   
        0x09: 48,   
    }

    def fake_activate_window(hwnd):
        try:
            ws = NSWorkspace.sharedWorkspace()
            app = NSRunningApplication.runningApplicationWithProcessIdentifier_(hwnd)
            if app:
                ws.launchApplicationWithBundleIdentifier_options_additionalEventParamDescriptor_launchIdentifier_(
                    app.bundleIdentifier(), 0, None, None)
                return True
        except Exception as e:
            print(e)
        return False

    def simulate_key_press_hold(handle, vk_code, duration):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            
            down_event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, True)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, down_event)
            
            time.sleep(duration)
            
            up_event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, False)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, up_event)
            
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_key_down(handle, vk_code):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, True)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_key_up(handle, vk_code):
        try:
            mac_key_code = MAC_KEY_MAP.get(vimport time
import threading
import sys

if sys.platform == "darwin":
    import Quartz
    from AppKit import NSWorkspace, NSRunningApplication
else:
    import win32gui
    import win32con
    import win32api


VK_CODES = {
    'F2': 0x71,
    'Q': 0x51,
    'E': 0x45,
    'R': 0x52,
    'F': 0x46,
    'X': 0x58,
    'T': 0x54,
    'M': 0x4D,
    '1': 0x31,
    '2': 0x32,
    '3': 0x33,
    '4': 0x34,
    'LEFT_SHIFT': 0xA0,
    'SPACE': 0x20,
    'MIDDLE_MOUSE': 0x04,
    'W': 0x57,
    'A': 0x41,
    'S': 0x53,
    'D': 0x44,
    'ESC': 0x1B,
    'ALT': 0xA4,
    'TAB': 0x09,
}

if sys.platform == "darwin":
    MAC_KEY_MAP = {
        0x71: 120,  
        0x51: 12,   
        0x45: 14,   
        0x52: 15,   
        0x46: 3,    
        0x58: 7,    
        0x54: 17,   
        0x4D: 46,   
        0x31: 18,   
        0x32: 19,   
        0x33: 20,   
        0x34: 21,   
        0xA0: 56,   
        0x20: 49,   
        0x57: 13,   
        0x41: 0,    
        0x53: 1,    
        0x44: 2,    
        0x1B: 53,   
        0xA4: 58,   
        0x09: 48,   
    }

    def fake_activate_window(hwnd):
        try:
            ws = NSWorkspace.sharedWorkspace()
            app = NSRunningApplication.runningApplicationWithProcessIdentifier_(hwnd)
            if app:
                ws.launchApplicationWithBundleIdentifier_options_additionalEventParamDescriptor_launchIdentifier_(
                    app.bundleIdentifier(), 0, None, None)
                return True
        except Exception as e:
            print(e)
        return False

    def simulate_key_press_hold(handle, vk_code, duration):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            
            down_event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, True)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, down_event)
            
            time.sleep(duration)
            
            up_event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, False)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, up_event)
            
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_key_down(handle, vk_code):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, True)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_key_up(handle, vk_code):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            event =import time
import threading
import sys

if sys.platform == "darwin":
    import Quartz
    from AppKit import NSWorkspace, NSRunningApplication
else:
    import win32gui
    import win32con
    import win32api


VK_CODES = {
    'F2': 0x71,
    'Q': 0x51,
    'E': 0x45,
    'R': 0x52,
    'F': 0x46,
    'X': 0x58,
    'T': 0x54,
    'M': 0x4D,
    '1': 0x31,
    '2': 0x32,
    '3': 0x33,
    '4': 0x34,
    'LEFT_SHIFT': 0xA0,
    'SPACE': 0x20,
    'MIDDLE_MOUSE': 0x04,
    'W': 0x57,
    'A': 0x41,
    'S': 0x53,
    'D': 0x44,
    'ESC': 0x1B,
    'ALT': 0xA4,
    'TAB': 0x09,
}

if sys.platform == "darwin":
    MAC_KEY_MAP = {
        0x71: 120,  
        0x51: 12,   
        0x45: 14,   
        0x52: 15,   
        0x46: 3,    
        0x58: 7,    
        0x54: 17,   
        0x4D: 46,   
        0x31: 18,   
        0x32: 19,   
        0x33: 20,   
        0x34: 21,   
        0xA0: 56,   
        0x20: 49,   
        0x57: 13,   
        0x41: 0,    
        0x53: 1,    
        0x44: 2,    
        0x1B: 53,   
        0xA4: 58,   
        0x09: 48,   
    }

    def fake_activate_window(hwnd):
        try:
            ws = NSWorkspace.sharedWorkspace()
            app = NSRunningApplication.runningApplicationWithProcessIdentifier_(hwnd)
            if app:
                ws.launchApplicationWithBundleIdentifier_options_additionalEventParamDescriptor_launchIdentifier_(
                    app.bundleIdentifier(), 0, None, None)
                return True
        except Exception as e:
            print(e)
        return False

    def simulate_key_press_hold(handle, vk_code, duration):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            
            down_event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, True)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, down_event)
            
            time.sleep(duration)
            
            up_event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, False)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, up_event)
            
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_key_down(handle, vk_code):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, True)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_key_up(handle, vk_code):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, False)
            Quartz.Cimport time
import threading
import sys

if sys.platform == "darwin":
    import Quartz
    from AppKit import NSWorkspace, NSRunningApplication
else:
    import win32gui
    import win32con
    import win32api


VK_CODES = {
    'F2': 0x71,
    'Q': 0x51,
    'E': 0x45,
    'R': 0x52,
    'F': 0x46,
    'X': 0x58,
    'T': 0x54,
    'M': 0x4D,
    '1': 0x31,
    '2': 0x32,
    '3': 0x33,
    '4': 0x34,
    'LEFT_SHIFT': 0xA0,
    'SPACE': 0x20,
    'MIDDLE_MOUSE': 0x04,
    'W': 0x57,
    'A': 0x41,
    'S': 0x53,
    'D': 0x44,
    'ESC': 0x1B,
    'ALT': 0xA4,
    'TAB': 0x09,
}

if sys.platform == "darwin":
    MAC_KEY_MAP = {
        0x71: 120,  
        0x51: 12,   
        0x45: 14,   
        0x52: 15,   
        0x46: 3,    
        0x58: 7,    
        0x54: 17,   
        0x4D: 46,   
        0x31: 18,   
        0x32: 19,   
        0x33: 20,   
        0x34: 21,   
        0xA0: 56,   
        0x20: 49,   
        0x57: 13,   
        0x41: 0,    
        0x53: 1,    
        0x44: 2,    
        0x1B: 53,   
        0xA4: 58,   
        0x09: 48,   
    }

    def fake_activate_window(hwnd):
        try:
            ws = NSWorkspace.sharedWorkspace()
            app = NSRunningApplication.runningApplicationWithProcessIdentifier_(hwnd)
            if app:
                ws.launchApplicationWithBundleIdentifier_options_additionalEventParamDescriptor_launchIdentifier_(
                    app.bundleIdentifier(), 0, None, None)
                return True
        except Exception as e:
            print(e)
        return False

    def simulate_key_press_hold(handle, vk_code, duration):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            
            down_event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, True)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, down_event)
            
            time.sleep(duration)
            
            up_event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, False)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, up_event)
            
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_key_down(handle, vk_code):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, True)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_key_up(handle, vk_code):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, False)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
        except Exception asimport time
import threading
import sys

if sys.platform == "darwin":
    import Quartz
    from AppKit import NSWorkspace, NSRunningApplication
else:
    import win32gui
    import win32con
    import win32api


VK_CODES = {
    'F2': 0x71,
    'Q': 0x51,
    'E': 0x45,
    'R': 0x52,
    'F': 0x46,
    'X': 0x58,
    'T': 0x54,
    'M': 0x4D,
    '1': 0x31,
    '2': 0x32,
    '3': 0x33,
    '4': 0x34,
    'LEFT_SHIFT': 0xA0,
    'SPACE': 0x20,
    'MIDDLE_MOUSE': 0x04,
    'W': 0x57,
    'A': 0x41,
    'S': 0x53,
    'D': 0x44,
    'ESC': 0x1B,
    'ALT': 0xA4,
    'TAB': 0x09,
}

if sys.platform == "darwin":
    MAC_KEY_MAP = {
        0x71: 120,  
        0x51: 12,   
        0x45: 14,   
        0x52: 15,   
        0x46: 3,    
        0x58: 7,    
        0x54: 17,   
        0x4D: 46,   
        0x31: 18,   
        0x32: 19,   
        0x33: 20,   
        0x34: 21,   
        0xA0: 56,   
        0x20: 49,   
        0x57: 13,   
        0x41: 0,    
        0x53: 1,    
        0x44: 2,    
        0x1B: 53,   
        0xA4: 58,   
        0x09: 48,   
    }

    def fake_activate_window(hwnd):
        try:
            ws = NSWorkspace.sharedWorkspace()
            app = NSRunningApplication.runningApplicationWithProcessIdentifier_(hwnd)
            if app:
                ws.launchApplicationWithBundleIdentifier_options_additionalEventParamDescriptor_launchIdentifier_(
                    app.bundleIdentifier(), 0, None, None)
                return True
        except Exception as e:
            print(e)
        return False

    def simulate_key_press_hold(handle, vk_code, duration):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            
            down_event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, True)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, down_event)
            
            time.sleep(duration)
            
            up_event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, False)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, up_event)
            
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_key_down(handle, vk_code):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, True)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_key_up(handle, vk_code):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, False)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
        except Exception as e:
            print(e)
            timeimport time
import threading
import sys

if sys.platform == "darwin":
    import Quartz
    from AppKit import NSWorkspace, NSRunningApplication
else:
    import win32gui
    import win32con
    import win32api


VK_CODES = {
    'F2': 0x71,
    'Q': 0x51,
    'E': 0x45,
    'R': 0x52,
    'F': 0x46,
    'X': 0x58,
    'T': 0x54,
    'M': 0x4D,
    '1': 0x31,
    '2': 0x32,
    '3': 0x33,
    '4': 0x34,
    'LEFT_SHIFT': 0xA0,
    'SPACE': 0x20,
    'MIDDLE_MOUSE': 0x04,
    'W': 0x57,
    'A': 0x41,
    'S': 0x53,
    'D': 0x44,
    'ESC': 0x1B,
    'ALT': 0xA4,
    'TAB': 0x09,
}

if sys.platform == "darwin":
    MAC_KEY_MAP = {
        0x71: 120,  
        0x51: 12,   
        0x45: 14,   
        0x52: 15,   
        0x46: 3,    
        0x58: 7,    
        0x54: 17,   
        0x4D: 46,   
        0x31: 18,   
        0x32: 19,   
        0x33: 20,   
        0x34: 21,   
        0xA0: 56,   
        0x20: 49,   
        0x57: 13,   
        0x41: 0,    
        0x53: 1,    
        0x44: 2,    
        0x1B: 53,   
        0xA4: 58,   
        0x09: 48,   
    }

    def fake_activate_window(hwnd):
        try:
            ws = NSWorkspace.sharedWorkspace()
            app = NSRunningApplication.runningApplicationWithProcessIdentifier_(hwnd)
            if app:
                ws.launchApplicationWithBundleIdentifier_options_additionalEventParamDescriptor_launchIdentifier_(
                    app.bundleIdentifier(), 0, None, None)
                return True
        except Exception as e:
            print(e)
        return False

    def simulate_key_press_hold(handle, vk_code, duration):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            
            down_event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, True)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, down_event)
            
            time.sleep(duration)
            
            up_event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, False)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, up_event)
            
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_key_down(handle, vk_code):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, True)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_key_up(handle, vk_code):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, False)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_mouseimport time
import threading
import sys

if sys.platform == "darwin":
    import Quartz
    from AppKit import NSWorkspace, NSRunningApplication
else:
    import win32gui
    import win32con
    import win32api


VK_CODES = {
    'F2': 0x71,
    'Q': 0x51,
    'E': 0x45,
    'R': 0x52,
    'F': 0x46,
    'X': 0x58,
    'T': 0x54,
    'M': 0x4D,
    '1': 0x31,
    '2': 0x32,
    '3': 0x33,
    '4': 0x34,
    'LEFT_SHIFT': 0xA0,
    'SPACE': 0x20,
    'MIDDLE_MOUSE': 0x04,
    'W': 0x57,
    'A': 0x41,
    'S': 0x53,
    'D': 0x44,
    'ESC': 0x1B,
    'ALT': 0xA4,
    'TAB': 0x09,
}

if sys.platform == "darwin":
    MAC_KEY_MAP = {
        0x71: 120,  
        0x51: 12,   
        0x45: 14,   
        0x52: 15,   
        0x46: 3,    
        0x58: 7,    
        0x54: 17,   
        0x4D: 46,   
        0x31: 18,   
        0x32: 19,   
        0x33: 20,   
        0x34: 21,   
        0xA0: 56,   
        0x20: 49,   
        0x57: 13,   
        0x41: 0,    
        0x53: 1,    
        0x44: 2,    
        0x1B: 53,   
        0xA4: 58,   
        0x09: 48,   
    }

    def fake_activate_window(hwnd):
        try:
            ws = NSWorkspace.sharedWorkspace()
            app = NSRunningApplication.runningApplicationWithProcessIdentifier_(hwnd)
            if app:
                ws.launchApplicationWithBundleIdentifier_options_additionalEventParamDescriptor_launchIdentifier_(
                    app.bundleIdentifier(), 0, None, None)
                return True
        except Exception as e:
            print(e)
        return False

    def simulate_key_press_hold(handle, vk_code, duration):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            
            down_event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, True)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, down_event)
            
            time.sleep(duration)
            
            up_event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, False)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, up_event)
            
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_key_down(handle, vk_code):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, True)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_key_up(handle, vk_code):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, False)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_mouse_left_click_hold(handle, x, y, duration):
        try:
            mouse_down = Quartz.CGEventCreateMouseEventimport time
import threading
import sys

if sys.platform == "darwin":
    import Quartz
    from AppKit import NSWorkspace, NSRunningApplication
else:
    import win32gui
    import win32con
    import win32api


VK_CODES = {
    'F2': 0x71,
    'Q': 0x51,
    'E': 0x45,
    'R': 0x52,
    'F': 0x46,
    'X': 0x58,
    'T': 0x54,
    'M': 0x4D,
    '1': 0x31,
    '2': 0x32,
    '3': 0x33,
    '4': 0x34,
    'LEFT_SHIFT': 0xA0,
    'SPACE': 0x20,
    'MIDDLE_MOUSE': 0x04,
    'W': 0x57,
    'A': 0x41,
    'S': 0x53,
    'D': 0x44,
    'ESC': 0x1B,
    'ALT': 0xA4,
    'TAB': 0x09,
}

if sys.platform == "darwin":
    MAC_KEY_MAP = {
        0x71: 120,  
        0x51: 12,   
        0x45: 14,   
        0x52: 15,   
        0x46: 3,    
        0x58: 7,    
        0x54: 17,   
        0x4D: 46,   
        0x31: 18,   
        0x32: 19,   
        0x33: 20,   
        0x34: 21,   
        0xA0: 56,   
        0x20: 49,   
        0x57: 13,   
        0x41: 0,    
        0x53: 1,    
        0x44: 2,    
        0x1B: 53,   
        0xA4: 58,   
        0x09: 48,   
    }

    def fake_activate_window(hwnd):
        try:
            ws = NSWorkspace.sharedWorkspace()
            app = NSRunningApplication.runningApplicationWithProcessIdentifier_(hwnd)
            if app:
                ws.launchApplicationWithBundleIdentifier_options_additionalEventParamDescriptor_launchIdentifier_(
                    app.bundleIdentifier(), 0, None, None)
                return True
        except Exception as e:
            print(e)
        return False

    def simulate_key_press_hold(handle, vk_code, duration):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            
            down_event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, True)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, down_event)
            
            time.sleep(duration)
            
            up_event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, False)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, up_event)
            
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_key_down(handle, vk_code):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, True)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_key_up(handle, vk_code):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, False)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_mouse_left_click_hold(handle, x, y, duration):
        try:
            mouse_down = Quartz.CGEventCreateMouseEvent(import time
import threading
import sys

if sys.platform == "darwin":
    import Quartz
    from AppKit import NSWorkspace, NSRunningApplication
else:
    import win32gui
    import win32con
    import win32api


VK_CODES = {
    'F2': 0x71,
    'Q': 0x51,
    'E': 0x45,
    'R': 0x52,
    'F': 0x46,
    'X': 0x58,
    'T': 0x54,
    'M': 0x4D,
    '1': 0x31,
    '2': 0x32,
    '3': 0x33,
    '4': 0x34,
    'LEFT_SHIFT': 0xA0,
    'SPACE': 0x20,
    'MIDDLE_MOUSE': 0x04,
    'W': 0x57,
    'A': 0x41,
    'S': 0x53,
    'D': 0x44,
    'ESC': 0x1B,
    'ALT': 0xA4,
    'TAB': 0x09,
}

if sys.platform == "darwin":
    MAC_KEY_MAP = {
        0x71: 120,  
        0x51: 12,   
        0x45: 14,   
        0x52: 15,   
        0x46: 3,    
        0x58: 7,    
        0x54: 17,   
        0x4D: 46,   
        0x31: 18,   
        0x32: 19,   
        0x33: 20,   
        0x34: 21,   
        0xA0: 56,   
        0x20: 49,   
        0x57: 13,   
        0x41: 0,    
        0x53: 1,    
        0x44: 2,    
        0x1B: 53,   
        0xA4: 58,   
        0x09: 48,   
    }

    def fake_activate_window(hwnd):
        try:
            ws = NSWorkspace.sharedWorkspace()
            app = NSRunningApplication.runningApplicationWithProcessIdentifier_(hwnd)
            if app:
                ws.launchApplicationWithBundleIdentifier_options_additionalEventParamDescriptor_launchIdentifier_(
                    app.bundleIdentifier(), 0, None, None)
                return True
        except Exception as e:
            print(e)
        return False

    def simulate_key_press_hold(handle, vk_code, duration):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            
            down_event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, True)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, down_event)
            
            time.sleep(duration)
            
            up_event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, False)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, up_event)
            
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_key_down(handle, vk_code):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, True)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_key_up(handle, vk_code):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, False)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_mouse_left_click_hold(handle, x, y, duration):
        try:
            mouse_down = Quartz.CGEventCreateMouseEvent(
                None, 
                Quartz.kCGEventimport time
import threading
import sys

if sys.platform == "darwin":
    import Quartz
    from AppKit import NSWorkspace, NSRunningApplication
else:
    import win32gui
    import win32con
    import win32api


VK_CODES = {
    'F2': 0x71,
    'Q': 0x51,
    'E': 0x45,
    'R': 0x52,
    'F': 0x46,
    'X': 0x58,
    'T': 0x54,
    'M': 0x4D,
    '1': 0x31,
    '2': 0x32,
    '3': 0x33,
    '4': 0x34,
    'LEFT_SHIFT': 0xA0,
    'SPACE': 0x20,
    'MIDDLE_MOUSE': 0x04,
    'W': 0x57,
    'A': 0x41,
    'S': 0x53,
    'D': 0x44,
    'ESC': 0x1B,
    'ALT': 0xA4,
    'TAB': 0x09,
}

if sys.platform == "darwin":
    MAC_KEY_MAP = {
        0x71: 120,  
        0x51: 12,   
        0x45: 14,   
        0x52: 15,   
        0x46: 3,    
        0x58: 7,    
        0x54: 17,   
        0x4D: 46,   
        0x31: 18,   
        0x32: 19,   
        0x33: 20,   
        0x34: 21,   
        0xA0: 56,   
        0x20: 49,   
        0x57: 13,   
        0x41: 0,    
        0x53: 1,    
        0x44: 2,    
        0x1B: 53,   
        0xA4: 58,   
        0x09: 48,   
    }

    def fake_activate_window(hwnd):
        try:
            ws = NSWorkspace.sharedWorkspace()
            app = NSRunningApplication.runningApplicationWithProcessIdentifier_(hwnd)
            if app:
                ws.launchApplicationWithBundleIdentifier_options_additionalEventParamDescriptor_launchIdentifier_(
                    app.bundleIdentifier(), 0, None, None)
                return True
        except Exception as e:
            print(e)
        return False

    def simulate_key_press_hold(handle, vk_code, duration):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            
            down_event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, True)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, down_event)
            
            time.sleep(duration)
            
            up_event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, False)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, up_event)
            
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_key_down(handle, vk_code):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, True)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_key_up(handle, vk_code):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, False)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_mouse_left_click_hold(handle, x, y, duration):
        try:
            mouse_down = Quartz.CGEventCreateMouseEvent(
                None, 
                Quartz.kCGEventLeftMouseDown, 
                (x, y), 
                Quartz.kCGMouseButtonLeft
import time
import threading
import sys

if sys.platform == "darwin":
    import Quartz
    from AppKit import NSWorkspace, NSRunningApplication
else:
    import win32gui
    import win32con
    import win32api


VK_CODES = {
    'F2': 0x71,
    'Q': 0x51,
    'E': 0x45,
    'R': 0x52,
    'F': 0x46,
    'X': 0x58,
    'T': 0x54,
    'M': 0x4D,
    '1': 0x31,
    '2': 0x32,
    '3': 0x33,
    '4': 0x34,
    'LEFT_SHIFT': 0xA0,
    'SPACE': 0x20,
    'MIDDLE_MOUSE': 0x04,
    'W': 0x57,
    'A': 0x41,
    'S': 0x53,
    'D': 0x44,
    'ESC': 0x1B,
    'ALT': 0xA4,
    'TAB': 0x09,
}

if sys.platform == "darwin":
    MAC_KEY_MAP = {
        0x71: 120,  
        0x51: 12,   
        0x45: 14,   
        0x52: 15,   
        0x46: 3,    
        0x58: 7,    
        0x54: 17,   
        0x4D: 46,   
        0x31: 18,   
        0x32: 19,   
        0x33: 20,   
        0x34: 21,   
        0xA0: 56,   
        0x20: 49,   
        0x57: 13,   
        0x41: 0,    
        0x53: 1,    
        0x44: 2,    
        0x1B: 53,   
        0xA4: 58,   
        0x09: 48,   
    }

    def fake_activate_window(hwnd):
        try:
            ws = NSWorkspace.sharedWorkspace()
            app = NSRunningApplication.runningApplicationWithProcessIdentifier_(hwnd)
            if app:
                ws.launchApplicationWithBundleIdentifier_options_additionalEventParamDescriptor_launchIdentifier_(
                    app.bundleIdentifier(), 0, None, None)
                return True
        except Exception as e:
            print(e)
        return False

    def simulate_key_press_hold(handle, vk_code, duration):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            
            down_event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, True)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, down_event)
            
            time.sleep(duration)
            
            up_event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, False)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, up_event)
            
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_key_down(handle, vk_code):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, True)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_key_up(handle, vk_code):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, False)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_mouse_left_click_hold(handle, x, y, duration):
        try:
            mouse_down = Quartz.CGEventCreateMouseEvent(
                None, 
                Quartz.kCGEventLeftMouseDown, 
                (x, y), 
                Quartz.kCGMouseButtonLeft
            )
            Quartz.CGEventPost(import time
import threading
import sys

if sys.platform == "darwin":
    import Quartz
    from AppKit import NSWorkspace, NSRunningApplication
else:
    import win32gui
    import win32con
    import win32api


VK_CODES = {
    'F2': 0x71,
    'Q': 0x51,
    'E': 0x45,
    'R': 0x52,
    'F': 0x46,
    'X': 0x58,
    'T': 0x54,
    'M': 0x4D,
    '1': 0x31,
    '2': 0x32,
    '3': 0x33,
    '4': 0x34,
    'LEFT_SHIFT': 0xA0,
    'SPACE': 0x20,
    'MIDDLE_MOUSE': 0x04,
    'W': 0x57,
    'A': 0x41,
    'S': 0x53,
    'D': 0x44,
    'ESC': 0x1B,
    'ALT': 0xA4,
    'TAB': 0x09,
}

if sys.platform == "darwin":
    MAC_KEY_MAP = {
        0x71: 120,  
        0x51: 12,   
        0x45: 14,   
        0x52: 15,   
        0x46: 3,    
        0x58: 7,    
        0x54: 17,   
        0x4D: 46,   
        0x31: 18,   
        0x32: 19,   
        0x33: 20,   
        0x34: 21,   
        0xA0: 56,   
        0x20: 49,   
        0x57: 13,   
        0x41: 0,    
        0x53: 1,    
        0x44: 2,    
        0x1B: 53,   
        0xA4: 58,   
        0x09: 48,   
    }

    def fake_activate_window(hwnd):
        try:
            ws = NSWorkspace.sharedWorkspace()
            app = NSRunningApplication.runningApplicationWithProcessIdentifier_(hwnd)
            if app:
                ws.launchApplicationWithBundleIdentifier_options_additionalEventParamDescriptor_launchIdentifier_(
                    app.bundleIdentifier(), 0, None, None)
                return True
        except Exception as e:
            print(e)
        return False

    def simulate_key_press_hold(handle, vk_code, duration):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            
            down_event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, True)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, down_event)
            
            time.sleep(duration)
            
            up_event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, False)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, up_event)
            
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_key_down(handle, vk_code):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, True)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_key_up(handle, vk_code):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, False)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_mouse_left_click_hold(handle, x, y, duration):
        try:
            mouse_down = Quartz.CGEventCreateMouseEvent(
                None, 
                Quartz.kCGEventLeftMouseDown, 
                (x, y), 
                Quartz.kCGMouseButtonLeft
            )
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, mouseimport time
import threading
import sys

if sys.platform == "darwin":
    import Quartz
    from AppKit import NSWorkspace, NSRunningApplication
else:
    import win32gui
    import win32con
    import win32api


VK_CODES = {
    'F2': 0x71,
    'Q': 0x51,
    'E': 0x45,
    'R': 0x52,
    'F': 0x46,
    'X': 0x58,
    'T': 0x54,
    'M': 0x4D,
    '1': 0x31,
    '2': 0x32,
    '3': 0x33,
    '4': 0x34,
    'LEFT_SHIFT': 0xA0,
    'SPACE': 0x20,
    'MIDDLE_MOUSE': 0x04,
    'W': 0x57,
    'A': 0x41,
    'S': 0x53,
    'D': 0x44,
    'ESC': 0x1B,
    'ALT': 0xA4,
    'TAB': 0x09,
}

if sys.platform == "darwin":
    MAC_KEY_MAP = {
        0x71: 120,  
        0x51: 12,   
        0x45: 14,   
        0x52: 15,   
        0x46: 3,    
        0x58: 7,    
        0x54: 17,   
        0x4D: 46,   
        0x31: 18,   
        0x32: 19,   
        0x33: 20,   
        0x34: 21,   
        0xA0: 56,   
        0x20: 49,   
        0x57: 13,   
        0x41: 0,    
        0x53: 1,    
        0x44: 2,    
        0x1B: 53,   
        0xA4: 58,   
        0x09: 48,   
    }

    def fake_activate_window(hwnd):
        try:
            ws = NSWorkspace.sharedWorkspace()
            app = NSRunningApplication.runningApplicationWithProcessIdentifier_(hwnd)
            if app:
                ws.launchApplicationWithBundleIdentifier_options_additionalEventParamDescriptor_launchIdentifier_(
                    app.bundleIdentifier(), 0, None, None)
                return True
        except Exception as e:
            print(e)
        return False

    def simulate_key_press_hold(handle, vk_code, duration):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            
            down_event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, True)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, down_event)
            
            time.sleep(duration)
            
            up_event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, False)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, up_event)
            
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_key_down(handle, vk_code):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, True)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_key_up(handle, vk_code):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, False)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_mouse_left_click_hold(handle, x, y, duration):
        try:
            mouse_down = Quartz.CGEventCreateMouseEvent(
                None, 
                Quartz.kCGEventLeftMouseDown, 
                (x, y), 
                Quartz.kCGMouseButtonLeft
            )
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, mouse_down)
            
            time.sleep(duration)
            
import time
import threading
import sys

if sys.platform == "darwin":
    import Quartz
    from AppKit import NSWorkspace, NSRunningApplication
else:
    import win32gui
    import win32con
    import win32api


VK_CODES = {
    'F2': 0x71,
    'Q': 0x51,
    'E': 0x45,
    'R': 0x52,
    'F': 0x46,
    'X': 0x58,
    'T': 0x54,
    'M': 0x4D,
    '1': 0x31,
    '2': 0x32,
    '3': 0x33,
    '4': 0x34,
    'LEFT_SHIFT': 0xA0,
    'SPACE': 0x20,
    'MIDDLE_MOUSE': 0x04,
    'W': 0x57,
    'A': 0x41,
    'S': 0x53,
    'D': 0x44,
    'ESC': 0x1B,
    'ALT': 0xA4,
    'TAB': 0x09,
}

if sys.platform == "darwin":
    MAC_KEY_MAP = {
        0x71: 120,  
        0x51: 12,   
        0x45: 14,   
        0x52: 15,   
        0x46: 3,    
        0x58: 7,    
        0x54: 17,   
        0x4D: 46,   
        0x31: 18,   
        0x32: 19,   
        0x33: 20,   
        0x34: 21,   
        0xA0: 56,   
        0x20: 49,   
        0x57: 13,   
        0x41: 0,    
        0x53: 1,    
        0x44: 2,    
        0x1B: 53,   
        0xA4: 58,   
        0x09: 48,   
    }

    def fake_activate_window(hwnd):
        try:
            ws = NSWorkspace.sharedWorkspace()
            app = NSRunningApplication.runningApplicationWithProcessIdentifier_(hwnd)
            if app:
                ws.launchApplicationWithBundleIdentifier_options_additionalEventParamDescriptor_launchIdentifier_(
                    app.bundleIdentifier(), 0, None, None)
                return True
        except Exception as e:
            print(e)
        return False

    def simulate_key_press_hold(handle, vk_code, duration):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            
            down_event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, True)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, down_event)
            
            time.sleep(duration)
            
            up_event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, False)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, up_event)
            
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_key_down(handle, vk_code):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, True)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_key_up(handle, vk_code):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, False)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_mouse_left_click_hold(handle, x, y, duration):
        try:
            mouse_down = Quartz.CGEventCreateMouseEvent(
                None, 
                Quartz.kCGEventLeftMouseDown, 
                (x, y), 
                Quartz.kCGMouseButtonLeft
            )
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, mouse_down)
            
            time.sleep(duration)
            
            mouse_up = Quartz.CGEventCreateMouseEventimport time
import threading
import sys

if sys.platform == "darwin":
    import Quartz
    from AppKit import NSWorkspace, NSRunningApplication
else:
    import win32gui
    import win32con
    import win32api


VK_CODES = {
    'F2': 0x71,
    'Q': 0x51,
    'E': 0x45,
    'R': 0x52,
    'F': 0x46,
    'X': 0x58,
    'T': 0x54,
    'M': 0x4D,
    '1': 0x31,
    '2': 0x32,
    '3': 0x33,
    '4': 0x34,
    'LEFT_SHIFT': 0xA0,
    'SPACE': 0x20,
    'MIDDLE_MOUSE': 0x04,
    'W': 0x57,
    'A': 0x41,
    'S': 0x53,
    'D': 0x44,
    'ESC': 0x1B,
    'ALT': 0xA4,
    'TAB': 0x09,
}

if sys.platform == "darwin":
    MAC_KEY_MAP = {
        0x71: 120,  
        0x51: 12,   
        0x45: 14,   
        0x52: 15,   
        0x46: 3,    
        0x58: 7,    
        0x54: 17,   
        0x4D: 46,   
        0x31: 18,   
        0x32: 19,   
        0x33: 20,   
        0x34: 21,   
        0xA0: 56,   
        0x20: 49,   
        0x57: 13,   
        0x41: 0,    
        0x53: 1,    
        0x44: 2,    
        0x1B: 53,   
        0xA4: 58,   
        0x09: 48,   
    }

    def fake_activate_window(hwnd):
        try:
            ws = NSWorkspace.sharedWorkspace()
            app = NSRunningApplication.runningApplicationWithProcessIdentifier_(hwnd)
            if app:
                ws.launchApplicationWithBundleIdentifier_options_additionalEventParamDescriptor_launchIdentifier_(
                    app.bundleIdentifier(), 0, None, None)
                return True
        except Exception as e:
            print(e)
        return False

    def simulate_key_press_hold(handle, vk_code, duration):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            
            down_event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, True)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, down_event)
            
            time.sleep(duration)
            
            up_event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, False)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, up_event)
            
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_key_down(handle, vk_code):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, True)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_key_up(handle, vk_code):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, False)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_mouse_left_click_hold(handle, x, y, duration):
        try:
            mouse_down = Quartz.CGEventCreateMouseEvent(
                None, 
                Quartz.kCGEventLeftMouseDown, 
                (x, y), 
                Quartz.kCGMouseButtonLeft
            )
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, mouse_down)
            
            time.sleep(duration)
            
            mouse_up = Quartz.CGEventCreateMouseEvent(
                None, 
                Quartz.kCGEventLeftMouseUp, 
                (x,import time
import threading
import sys

if sys.platform == "darwin":
    import Quartz
    from AppKit import NSWorkspace, NSRunningApplication
else:
    import win32gui
    import win32con
    import win32api


VK_CODES = {
    'F2': 0x71,
    'Q': 0x51,
    'E': 0x45,
    'R': 0x52,
    'F': 0x46,
    'X': 0x58,
    'T': 0x54,
    'M': 0x4D,
    '1': 0x31,
    '2': 0x32,
    '3': 0x33,
    '4': 0x34,
    'LEFT_SHIFT': 0xA0,
    'SPACE': 0x20,
    'MIDDLE_MOUSE': 0x04,
    'W': 0x57,
    'A': 0x41,
    'S': 0x53,
    'D': 0x44,
    'ESC': 0x1B,
    'ALT': 0xA4,
    'TAB': 0x09,
}

if sys.platform == "darwin":
    MAC_KEY_MAP = {
        0x71: 120,  
        0x51: 12,   
        0x45: 14,   
        0x52: 15,   
        0x46: 3,    
        0x58: 7,    
        0x54: 17,   
        0x4D: 46,   
        0x31: 18,   
        0x32: 19,   
        0x33: 20,   
        0x34: 21,   
        0xA0: 56,   
        0x20: 49,   
        0x57: 13,   
        0x41: 0,    
        0x53: 1,    
        0x44: 2,    
        0x1B: 53,   
        0xA4: 58,   
        0x09: 48,   
    }

    def fake_activate_window(hwnd):
        try:
            ws = NSWorkspace.sharedWorkspace()
            app = NSRunningApplication.runningApplicationWithProcessIdentifier_(hwnd)
            if app:
                ws.launchApplicationWithBundleIdentifier_options_additionalEventParamDescriptor_launchIdentifier_(
                    app.bundleIdentifier(), 0, None, None)
                return True
        except Exception as e:
            print(e)
        return False

    def simulate_key_press_hold(handle, vk_code, duration):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            
            down_event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, True)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, down_event)
            
            time.sleep(duration)
            
            up_event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, False)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, up_event)
            
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_key_down(handle, vk_code):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, True)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_key_up(handle, vk_code):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, False)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_mouse_left_click_hold(handle, x, y, duration):
        try:
            mouse_down = Quartz.CGEventCreateMouseEvent(
                None, 
                Quartz.kCGEventLeftMouseDown, 
                (x, y), 
                Quartz.kCGMouseButtonLeft
            )
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, mouse_down)
            
            time.sleep(duration)
            
            mouse_up = Quartz.CGEventCreateMouseEvent(
                None, 
                Quartz.kCGEventLeftMouseUp, 
                (x, y), 
                Quartz.kCGMouseButtonLeft
            )
            Quartz.CGEventPostimport time
import threading
import sys

if sys.platform == "darwin":
    import Quartz
    from AppKit import NSWorkspace, NSRunningApplication
else:
    import win32gui
    import win32con
    import win32api


VK_CODES = {
    'F2': 0x71,
    'Q': 0x51,
    'E': 0x45,
    'R': 0x52,
    'F': 0x46,
    'X': 0x58,
    'T': 0x54,
    'M': 0x4D,
    '1': 0x31,
    '2': 0x32,
    '3': 0x33,
    '4': 0x34,
    'LEFT_SHIFT': 0xA0,
    'SPACE': 0x20,
    'MIDDLE_MOUSE': 0x04,
    'W': 0x57,
    'A': 0x41,
    'S': 0x53,
    'D': 0x44,
    'ESC': 0x1B,
    'ALT': 0xA4,
    'TAB': 0x09,
}

if sys.platform == "darwin":
    MAC_KEY_MAP = {
        0x71: 120,  
        0x51: 12,   
        0x45: 14,   
        0x52: 15,   
        0x46: 3,    
        0x58: 7,    
        0x54: 17,   
        0x4D: 46,   
        0x31: 18,   
        0x32: 19,   
        0x33: 20,   
        0x34: 21,   
        0xA0: 56,   
        0x20: 49,   
        0x57: 13,   
        0x41: 0,    
        0x53: 1,    
        0x44: 2,    
        0x1B: 53,   
        0xA4: 58,   
        0x09: 48,   
    }

    def fake_activate_window(hwnd):
        try:
            ws = NSWorkspace.sharedWorkspace()
            app = NSRunningApplication.runningApplicationWithProcessIdentifier_(hwnd)
            if app:
                ws.launchApplicationWithBundleIdentifier_options_additionalEventParamDescriptor_launchIdentifier_(
                    app.bundleIdentifier(), 0, None, None)
                return True
        except Exception as e:
            print(e)
        return False

    def simulate_key_press_hold(handle, vk_code, duration):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            
            down_event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, True)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, down_event)
            
            time.sleep(duration)
            
            up_event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, False)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, up_event)
            
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_key_down(handle, vk_code):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, True)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_key_up(handle, vk_code):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, False)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_mouse_left_click_hold(handle, x, y, duration):
        try:
            mouse_down = Quartz.CGEventCreateMouseEvent(
                None, 
                Quartz.kCGEventLeftMouseDown, 
                (x, y), 
                Quartz.kCGMouseButtonLeft
            )
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, mouse_down)
            
            time.sleep(duration)
            
            mouse_up = Quartz.CGEventCreateMouseEvent(
                None, 
                Quartz.kCGEventLeftMouseUp, 
                (x, y), 
                Quartz.kCGMouseButtonLeft
            )
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, mouse_up)
            
        except Exception as e:import time
import threading
import sys

if sys.platform == "darwin":
    import Quartz
    from AppKit import NSWorkspace, NSRunningApplication
else:
    import win32gui
    import win32con
    import win32api


VK_CODES = {
    'F2': 0x71,
    'Q': 0x51,
    'E': 0x45,
    'R': 0x52,
    'F': 0x46,
    'X': 0x58,
    'T': 0x54,
    'M': 0x4D,
    '1': 0x31,
    '2': 0x32,
    '3': 0x33,
    '4': 0x34,
    'LEFT_SHIFT': 0xA0,
    'SPACE': 0x20,
    'MIDDLE_MOUSE': 0x04,
    'W': 0x57,
    'A': 0x41,
    'S': 0x53,
    'D': 0x44,
    'ESC': 0x1B,
    'ALT': 0xA4,
    'TAB': 0x09,
}

if sys.platform == "darwin":
    MAC_KEY_MAP = {
        0x71: 120,  
        0x51: 12,   
        0x45: 14,   
        0x52: 15,   
        0x46: 3,    
        0x58: 7,    
        0x54: 17,   
        0x4D: 46,   
        0x31: 18,   
        0x32: 19,   
        0x33: 20,   
        0x34: 21,   
        0xA0: 56,   
        0x20: 49,   
        0x57: 13,   
        0x41: 0,    
        0x53: 1,    
        0x44: 2,    
        0x1B: 53,   
        0xA4: 58,   
        0x09: 48,   
    }

    def fake_activate_window(hwnd):
        try:
            ws = NSWorkspace.sharedWorkspace()
            app = NSRunningApplication.runningApplicationWithProcessIdentifier_(hwnd)
            if app:
                ws.launchApplicationWithBundleIdentifier_options_additionalEventParamDescriptor_launchIdentifier_(
                    app.bundleIdentifier(), 0, None, None)
                return True
        except Exception as e:
            print(e)
        return False

    def simulate_key_press_hold(handle, vk_code, duration):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            
            down_event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, True)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, down_event)
            
            time.sleep(duration)
            
            up_event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, False)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, up_event)
            
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_key_down(handle, vk_code):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, True)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_key_up(handle, vk_code):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, False)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_mouse_left_click_hold(handle, x, y, duration):
        try:
            mouse_down = Quartz.CGEventCreateMouseEvent(
                None, 
                Quartz.kCGEventLeftMouseDown, 
                (x, y), 
                Quartz.kCGMouseButtonLeft
            )
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, mouse_down)
            
            time.sleep(duration)
            
            mouse_up = Quartz.CGEventCreateMouseEvent(
                None, 
                Quartz.kCGEventLeftMouseUp, 
                (x, y), 
                Quartz.kCGMouseButtonLeft
            )
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, mouse_up)
            
        except Exception as e:
            print(e)
            time.sleep(import time
import threading
import sys

if sys.platform == "darwin":
    import Quartz
    from AppKit import NSWorkspace, NSRunningApplication
else:
    import win32gui
    import win32con
    import win32api


VK_CODES = {
    'F2': 0x71,
    'Q': 0x51,
    'E': 0x45,
    'R': 0x52,
    'F': 0x46,
    'X': 0x58,
    'T': 0x54,
    'M': 0x4D,
    '1': 0x31,
    '2': 0x32,
    '3': 0x33,
    '4': 0x34,
    'LEFT_SHIFT': 0xA0,
    'SPACE': 0x20,
    'MIDDLE_MOUSE': 0x04,
    'W': 0x57,
    'A': 0x41,
    'S': 0x53,
    'D': 0x44,
    'ESC': 0x1B,
    'ALT': 0xA4,
    'TAB': 0x09,
}

if sys.platform == "darwin":
    MAC_KEY_MAP = {
        0x71: 120,  
        0x51: 12,   
        0x45: 14,   
        0x52: 15,   
        0x46: 3,    
        0x58: 7,    
        0x54: 17,   
        0x4D: 46,   
        0x31: 18,   
        0x32: 19,   
        0x33: 20,   
        0x34: 21,   
        0xA0: 56,   
        0x20: 49,   
        0x57: 13,   
        0x41: 0,    
        0x53: 1,    
        0x44: 2,    
        0x1B: 53,   
        0xA4: 58,   
        0x09: 48,   
    }

    def fake_activate_window(hwnd):
        try:
            ws = NSWorkspace.sharedWorkspace()
            app = NSRunningApplication.runningApplicationWithProcessIdentifier_(hwnd)
            if app:
                ws.launchApplicationWithBundleIdentifier_options_additionalEventParamDescriptor_launchIdentifier_(
                    app.bundleIdentifier(), 0, None, None)
                return True
        except Exception as e:
            print(e)
        return False

    def simulate_key_press_hold(handle, vk_code, duration):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            
            down_event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, True)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, down_event)
            
            time.sleep(duration)
            
            up_event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, False)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, up_event)
            
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_key_down(handle, vk_code):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, True)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_key_up(handle, vk_code):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, False)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_mouse_left_click_hold(handle, x, y, duration):
        try:
            mouse_down = Quartz.CGEventCreateMouseEvent(
                None, 
                Quartz.kCGEventLeftMouseDown, 
                (x, y), 
                Quartz.kCGMouseButtonLeft
            )
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, mouse_down)
            
            time.sleep(duration)
            
            mouse_up = Quartz.CGEventCreateMouseEvent(
                None, 
                Quartz.kCGEventLeftMouseUp, 
                (x, y), 
                Quartz.kCGMouseButtonLeft
            )
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, mouse_up)
            
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_mouse_left_downimport time
import threading
import sys

if sys.platform == "darwin":
    import Quartz
    from AppKit import NSWorkspace, NSRunningApplication
else:
    import win32gui
    import win32con
    import win32api


VK_CODES = {
    'F2': 0x71,
    'Q': 0x51,
    'E': 0x45,
    'R': 0x52,
    'F': 0x46,
    'X': 0x58,
    'T': 0x54,
    'M': 0x4D,
    '1': 0x31,
    '2': 0x32,
    '3': 0x33,
    '4': 0x34,
    'LEFT_SHIFT': 0xA0,
    'SPACE': 0x20,
    'MIDDLE_MOUSE': 0x04,
    'W': 0x57,
    'A': 0x41,
    'S': 0x53,
    'D': 0x44,
    'ESC': 0x1B,
    'ALT': 0xA4,
    'TAB': 0x09,
}

if sys.platform == "darwin":
    MAC_KEY_MAP = {
        0x71: 120,  
        0x51: 12,   
        0x45: 14,   
        0x52: 15,   
        0x46: 3,    
        0x58: 7,    
        0x54: 17,   
        0x4D: 46,   
        0x31: 18,   
        0x32: 19,   
        0x33: 20,   
        0x34: 21,   
        0xA0: 56,   
        0x20: 49,   
        0x57: 13,   
        0x41: 0,    
        0x53: 1,    
        0x44: 2,    
        0x1B: 53,   
        0xA4: 58,   
        0x09: 48,   
    }

    def fake_activate_window(hwnd):
        try:
            ws = NSWorkspace.sharedWorkspace()
            app = NSRunningApplication.runningApplicationWithProcessIdentifier_(hwnd)
            if app:
                ws.launchApplicationWithBundleIdentifier_options_additionalEventParamDescriptor_launchIdentifier_(
                    app.bundleIdentifier(), 0, None, None)
                return True
        except Exception as e:
            print(e)
        return False

    def simulate_key_press_hold(handle, vk_code, duration):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            
            down_event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, True)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, down_event)
            
            time.sleep(duration)
            
            up_event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, False)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, up_event)
            
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_key_down(handle, vk_code):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, True)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_key_up(handle, vk_code):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, False)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_mouse_left_click_hold(handle, x, y, duration):
        try:
            mouse_down = Quartz.CGEventCreateMouseEvent(
                None, 
                Quartz.kCGEventLeftMouseDown, 
                (x, y), 
                Quartz.kCGMouseButtonLeft
            )
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, mouse_down)
            
            time.sleep(duration)
            
            mouse_up = Quartz.CGEventCreateMouseEvent(
                None, 
                Quartz.kCGEventLeftMouseUp, 
                (x, y), 
                Quartz.kCGMouseButtonLeft
            )
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, mouse_up)
            
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_mouse_left_down(handle, x, y, delay=0.001):
        try:
import time
import threading
import sys

if sys.platform == "darwin":
    import Quartz
    from AppKit import NSWorkspace, NSRunningApplication
else:
    import win32gui
    import win32con
    import win32api


VK_CODES = {
    'F2': 0x71,
    'Q': 0x51,
    'E': 0x45,
    'R': 0x52,
    'F': 0x46,
    'X': 0x58,
    'T': 0x54,
    'M': 0x4D,
    '1': 0x31,
    '2': 0x32,
    '3': 0x33,
    '4': 0x34,
    'LEFT_SHIFT': 0xA0,
    'SPACE': 0x20,
    'MIDDLE_MOUSE': 0x04,
    'W': 0x57,
    'A': 0x41,
    'S': 0x53,
    'D': 0x44,
    'ESC': 0x1B,
    'ALT': 0xA4,
    'TAB': 0x09,
}

if sys.platform == "darwin":
    MAC_KEY_MAP = {
        0x71: 120,  
        0x51: 12,   
        0x45: 14,   
        0x52: 15,   
        0x46: 3,    
        0x58: 7,    
        0x54: 17,   
        0x4D: 46,   
        0x31: 18,   
        0x32: 19,   
        0x33: 20,   
        0x34: 21,   
        0xA0: 56,   
        0x20: 49,   
        0x57: 13,   
        0x41: 0,    
        0x53: 1,    
        0x44: 2,    
        0x1B: 53,   
        0xA4: 58,   
        0x09: 48,   
    }

    def fake_activate_window(hwnd):
        try:
            ws = NSWorkspace.sharedWorkspace()
            app = NSRunningApplication.runningApplicationWithProcessIdentifier_(hwnd)
            if app:
                ws.launchApplicationWithBundleIdentifier_options_additionalEventParamDescriptor_launchIdentifier_(
                    app.bundleIdentifier(), 0, None, None)
                return True
        except Exception as e:
            print(e)
        return False

    def simulate_key_press_hold(handle, vk_code, duration):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            
            down_event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, True)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, down_event)
            
            time.sleep(duration)
            
            up_event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, False)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, up_event)
            
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_key_down(handle, vk_code):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, True)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_key_up(handle, vk_code):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, False)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_mouse_left_click_hold(handle, x, y, duration):
        try:
            mouse_down = Quartz.CGEventCreateMouseEvent(
                None, 
                Quartz.kCGEventLeftMouseDown, 
                (x, y), 
                Quartz.kCGMouseButtonLeft
            )
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, mouse_down)
            
            time.sleep(duration)
            
            mouse_up = Quartz.CGEventCreateMouseEvent(
                None, 
                Quartz.kCGEventLeftMouseUp, 
                (x, y), 
                Quartz.kCGMouseButtonLeft
            )
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, mouse_up)
            
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_mouse_left_down(handle, x, y, delay=0.001):
        try:
            event = Quartz.CGEventCreateMouseEvent(
                None, 
                Quartz.kCGEventimport time
import threading
import sys

if sys.platform == "darwin":
    import Quartz
    from AppKit import NSWorkspace, NSRunningApplication
else:
    import win32gui
    import win32con
    import win32api


VK_CODES = {
    'F2': 0x71,
    'Q': 0x51,
    'E': 0x45,
    'R': 0x52,
    'F': 0x46,
    'X': 0x58,
    'T': 0x54,
    'M': 0x4D,
    '1': 0x31,
    '2': 0x32,
    '3': 0x33,
    '4': 0x34,
    'LEFT_SHIFT': 0xA0,
    'SPACE': 0x20,
    'MIDDLE_MOUSE': 0x04,
    'W': 0x57,
    'A': 0x41,
    'S': 0x53,
    'D': 0x44,
    'ESC': 0x1B,
    'ALT': 0xA4,
    'TAB': 0x09,
}

if sys.platform == "darwin":
    MAC_KEY_MAP = {
        0x71: 120,  
        0x51: 12,   
        0x45: 14,   
        0x52: 15,   
        0x46: 3,    
        0x58: 7,    
        0x54: 17,   
        0x4D: 46,   
        0x31: 18,   
        0x32: 19,   
        0x33: 20,   
        0x34: 21,   
        0xA0: 56,   
        0x20: 49,   
        0x57: 13,   
        0x41: 0,    
        0x53: 1,    
        0x44: 2,    
        0x1B: 53,   
        0xA4: 58,   
        0x09: 48,   
    }

    def fake_activate_window(hwnd):
        try:
            ws = NSWorkspace.sharedWorkspace()
            app = NSRunningApplication.runningApplicationWithProcessIdentifier_(hwnd)
            if app:
                ws.launchApplicationWithBundleIdentifier_options_additionalEventParamDescriptor_launchIdentifier_(
                    app.bundleIdentifier(), 0, None, None)
                return True
        except Exception as e:
            print(e)
        return False

    def simulate_key_press_hold(handle, vk_code, duration):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            
            down_event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, True)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, down_event)
            
            time.sleep(duration)
            
            up_event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, False)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, up_event)
            
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_key_down(handle, vk_code):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, True)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_key_up(handle, vk_code):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, False)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_mouse_left_click_hold(handle, x, y, duration):
        try:
            mouse_down = Quartz.CGEventCreateMouseEvent(
                None, 
                Quartz.kCGEventLeftMouseDown, 
                (x, y), 
                Quartz.kCGMouseButtonLeft
            )
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, mouse_down)
            
            time.sleep(duration)
            
            mouse_up = Quartz.CGEventCreateMouseEvent(
                None, 
                Quartz.kCGEventLeftMouseUp, 
                (x, y), 
                Quartz.kCGMouseButtonLeft
            )
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, mouse_up)
            
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_mouse_left_down(handle, x, y, delay=0.001):
        try:
            event = Quartz.CGEventCreateMouseEvent(
                None, 
                Quartz.kCGEventLeftMouseDown, 
                (x, y), 
                Quartz.kCGMouseButtonLeft
import time
import threading
import sys

if sys.platform == "darwin":
    import Quartz
    from AppKit import NSWorkspace, NSRunningApplication
else:
    import win32gui
    import win32con
    import win32api


VK_CODES = {
    'F2': 0x71,
    'Q': 0x51,
    'E': 0x45,
    'R': 0x52,
    'F': 0x46,
    'X': 0x58,
    'T': 0x54,
    'M': 0x4D,
    '1': 0x31,
    '2': 0x32,
    '3': 0x33,
    '4': 0x34,
    'LEFT_SHIFT': 0xA0,
    'SPACE': 0x20,
    'MIDDLE_MOUSE': 0x04,
    'W': 0x57,
    'A': 0x41,
    'S': 0x53,
    'D': 0x44,
    'ESC': 0x1B,
    'ALT': 0xA4,
    'TAB': 0x09,
}

if sys.platform == "darwin":
    MAC_KEY_MAP = {
        0x71: 120,  
        0x51: 12,   
        0x45: 14,   
        0x52: 15,   
        0x46: 3,    
        0x58: 7,    
        0x54: 17,   
        0x4D: 46,   
        0x31: 18,   
        0x32: 19,   
        0x33: 20,   
        0x34: 21,   
        0xA0: 56,   
        0x20: 49,   
        0x57: 13,   
        0x41: 0,    
        0x53: 1,    
        0x44: 2,    
        0x1B: 53,   
        0xA4: 58,   
        0x09: 48,   
    }

    def fake_activate_window(hwnd):
        try:
            ws = NSWorkspace.sharedWorkspace()
            app = NSRunningApplication.runningApplicationWithProcessIdentifier_(hwnd)
            if app:
                ws.launchApplicationWithBundleIdentifier_options_additionalEventParamDescriptor_launchIdentifier_(
                    app.bundleIdentifier(), 0, None, None)
                return True
        except Exception as e:
            print(e)
        return False

    def simulate_key_press_hold(handle, vk_code, duration):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            
            down_event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, True)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, down_event)
            
            time.sleep(duration)
            
            up_event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, False)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, up_event)
            
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_key_down(handle, vk_code):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, True)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_key_up(handle, vk_code):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, False)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_mouse_left_click_hold(handle, x, y, duration):
        try:
            mouse_down = Quartz.CGEventCreateMouseEvent(
                None, 
                Quartz.kCGEventLeftMouseDown, 
                (x, y), 
                Quartz.kCGMouseButtonLeft
            )
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, mouse_down)
            
            time.sleep(duration)
            
            mouse_up = Quartz.CGEventCreateMouseEvent(
                None, 
                Quartz.kCGEventLeftMouseUp, 
                (x, y), 
                Quartz.kCGMouseButtonLeft
            )
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, mouse_up)
            
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_mouse_left_down(handle, x, y, delay=0.001):
        try:
            event = Quartz.CGEventCreateMouseEvent(
                None, 
                Quartz.kCGEventLeftMouseDown, 
                (x, y), 
                Quartz.kCGMouseButtonLeft
            )
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, eventimport time
import threading
import sys

if sys.platform == "darwin":
    import Quartz
    from AppKit import NSWorkspace, NSRunningApplication
else:
    import win32gui
    import win32con
    import win32api


VK_CODES = {
    'F2': 0x71,
    'Q': 0x51,
    'E': 0x45,
    'R': 0x52,
    'F': 0x46,
    'X': 0x58,
    'T': 0x54,
    'M': 0x4D,
    '1': 0x31,
    '2': 0x32,
    '3': 0x33,
    '4': 0x34,
    'LEFT_SHIFT': 0xA0,
    'SPACE': 0x20,
    'MIDDLE_MOUSE': 0x04,
    'W': 0x57,
    'A': 0x41,
    'S': 0x53,
    'D': 0x44,
    'ESC': 0x1B,
    'ALT': 0xA4,
    'TAB': 0x09,
}

if sys.platform == "darwin":
    MAC_KEY_MAP = {
        0x71: 120,  
        0x51: 12,   
        0x45: 14,   
        0x52: 15,   
        0x46: 3,    
        0x58: 7,    
        0x54: 17,   
        0x4D: 46,   
        0x31: 18,   
        0x32: 19,   
        0x33: 20,   
        0x34: 21,   
        0xA0: 56,   
        0x20: 49,   
        0x57: 13,   
        0x41: 0,    
        0x53: 1,    
        0x44: 2,    
        0x1B: 53,   
        0xA4: 58,   
        0x09: 48,   
    }

    def fake_activate_window(hwnd):
        try:
            ws = NSWorkspace.sharedWorkspace()
            app = NSRunningApplication.runningApplicationWithProcessIdentifier_(hwnd)
            if app:
                ws.launchApplicationWithBundleIdentifier_options_additionalEventParamDescriptor_launchIdentifier_(
                    app.bundleIdentifier(), 0, None, None)
                return True
        except Exception as e:
            print(e)
        return False

    def simulate_key_press_hold(handle, vk_code, duration):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            
            down_event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, True)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, down_event)
            
            time.sleep(duration)
            
            up_event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, False)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, up_event)
            
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_key_down(handle, vk_code):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, True)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_key_up(handle, vk_code):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, False)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_mouse_left_click_hold(handle, x, y, duration):
        try:
            mouse_down = Quartz.CGEventCreateMouseEvent(
                None, 
                Quartz.kCGEventLeftMouseDown, 
                (x, y), 
                Quartz.kCGMouseButtonLeft
            )
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, mouse_down)
            
            time.sleep(duration)
            
            mouse_up = Quartz.CGEventCreateMouseEvent(
                None, 
                Quartz.kCGEventLeftMouseUp, 
                (x, y), 
                Quartz.kCGMouseButtonLeft
            )
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, mouse_up)
            
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_mouse_left_down(handle, x, y, delay=0.001):
        try:
            event = Quartz.CGEventCreateMouseEvent(
                None, 
                Quartz.kCGEventLeftMouseDown, 
                (x, y), 
                Quartz.kCGMouseButtonLeft
            )
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
            time.sleep(delay)
        except Exception:
            pass

    def simulateimport time
import threading
import sys

if sys.platform == "darwin":
    import Quartz
    from AppKit import NSWorkspace, NSRunningApplication
else:
    import win32gui
    import win32con
    import win32api


VK_CODES = {
    'F2': 0x71,
    'Q': 0x51,
    'E': 0x45,
    'R': 0x52,
    'F': 0x46,
    'X': 0x58,
    'T': 0x54,
    'M': 0x4D,
    '1': 0x31,
    '2': 0x32,
    '3': 0x33,
    '4': 0x34,
    'LEFT_SHIFT': 0xA0,
    'SPACE': 0x20,
    'MIDDLE_MOUSE': 0x04,
    'W': 0x57,
    'A': 0x41,
    'S': 0x53,
    'D': 0x44,
    'ESC': 0x1B,
    'ALT': 0xA4,
    'TAB': 0x09,
}

if sys.platform == "darwin":
    MAC_KEY_MAP = {
        0x71: 120,  
        0x51: 12,   
        0x45: 14,   
        0x52: 15,   
        0x46: 3,    
        0x58: 7,    
        0x54: 17,   
        0x4D: 46,   
        0x31: 18,   
        0x32: 19,   
        0x33: 20,   
        0x34: 21,   
        0xA0: 56,   
        0x20: 49,   
        0x57: 13,   
        0x41: 0,    
        0x53: 1,    
        0x44: 2,    
        0x1B: 53,   
        0xA4: 58,   
        0x09: 48,   
    }

    def fake_activate_window(hwnd):
        try:
            ws = NSWorkspace.sharedWorkspace()
            app = NSRunningApplication.runningApplicationWithProcessIdentifier_(hwnd)
            if app:
                ws.launchApplicationWithBundleIdentifier_options_additionalEventParamDescriptor_launchIdentifier_(
                    app.bundleIdentifier(), 0, None, None)
                return True
        except Exception as e:
            print(e)
        return False

    def simulate_key_press_hold(handle, vk_code, duration):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            
            down_event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, True)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, down_event)
            
            time.sleep(duration)
            
            up_event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, False)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, up_event)
            
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_key_down(handle, vk_code):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, True)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_key_up(handle, vk_code):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, False)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_mouse_left_click_hold(handle, x, y, duration):
        try:
            mouse_down = Quartz.CGEventCreateMouseEvent(
                None, 
                Quartz.kCGEventLeftMouseDown, 
                (x, y), 
                Quartz.kCGMouseButtonLeft
            )
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, mouse_down)
            
            time.sleep(duration)
            
            mouse_up = Quartz.CGEventCreateMouseEvent(
                None, 
                Quartz.kCGEventLeftMouseUp, 
                (x, y), 
                Quartz.kCGMouseButtonLeft
            )
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, mouse_up)
            
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_mouse_left_down(handle, x, y, delay=0.001):
        try:
            event = Quartz.CGEventCreateMouseEvent(
                None, 
                Quartz.kCGEventLeftMouseDown, 
                (x, y), 
                Quartz.kCGMouseButtonLeft
            )
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
            time.sleep(delay)
        except Exception:
            pass

    def simulate_mouse_left_up(handle, x, y, delay=0.001):
import time
import threading
import sys

if sys.platform == "darwin":
    import Quartz
    from AppKit import NSWorkspace, NSRunningApplication
else:
    import win32gui
    import win32con
    import win32api


VK_CODES = {
    'F2': 0x71,
    'Q': 0x51,
    'E': 0x45,
    'R': 0x52,
    'F': 0x46,
    'X': 0x58,
    'T': 0x54,
    'M': 0x4D,
    '1': 0x31,
    '2': 0x32,
    '3': 0x33,
    '4': 0x34,
    'LEFT_SHIFT': 0xA0,
    'SPACE': 0x20,
    'MIDDLE_MOUSE': 0x04,
    'W': 0x57,
    'A': 0x41,
    'S': 0x53,
    'D': 0x44,
    'ESC': 0x1B,
    'ALT': 0xA4,
    'TAB': 0x09,
}

if sys.platform == "darwin":
    MAC_KEY_MAP = {
        0x71: 120,  
        0x51: 12,   
        0x45: 14,   
        0x52: 15,   
        0x46: 3,    
        0x58: 7,    
        0x54: 17,   
        0x4D: 46,   
        0x31: 18,   
        0x32: 19,   
        0x33: 20,   
        0x34: 21,   
        0xA0: 56,   
        0x20: 49,   
        0x57: 13,   
        0x41: 0,    
        0x53: 1,    
        0x44: 2,    
        0x1B: 53,   
        0xA4: 58,   
        0x09: 48,   
    }

    def fake_activate_window(hwnd):
        try:
            ws = NSWorkspace.sharedWorkspace()
            app = NSRunningApplication.runningApplicationWithProcessIdentifier_(hwnd)
            if app:
                ws.launchApplicationWithBundleIdentifier_options_additionalEventParamDescriptor_launchIdentifier_(
                    app.bundleIdentifier(), 0, None, None)
                return True
        except Exception as e:
            print(e)
        return False

    def simulate_key_press_hold(handle, vk_code, duration):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            
            down_event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, True)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, down_event)
            
            time.sleep(duration)
            
            up_event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, False)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, up_event)
            
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_key_down(handle, vk_code):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, True)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_key_up(handle, vk_code):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, False)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_mouse_left_click_hold(handle, x, y, duration):
        try:
            mouse_down = Quartz.CGEventCreateMouseEvent(
                None, 
                Quartz.kCGEventLeftMouseDown, 
                (x, y), 
                Quartz.kCGMouseButtonLeft
            )
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, mouse_down)
            
            time.sleep(duration)
            
            mouse_up = Quartz.CGEventCreateMouseEvent(
                None, 
                Quartz.kCGEventLeftMouseUp, 
                (x, y), 
                Quartz.kCGMouseButtonLeft
            )
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, mouse_up)
            
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_mouse_left_down(handle, x, y, delay=0.001):
        try:
            event = Quartz.CGEventCreateMouseEvent(
                None, 
                Quartz.kCGEventLeftMouseDown, 
                (x, y), 
                Quartz.kCGMouseButtonLeft
            )
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
            time.sleep(delay)
        except Exception:
            pass

    def simulate_mouse_left_up(handle, x, y, delay=0.001):
        try:
            event = Quartz.CGEventCreateMouseEvent(
                None, 
                Quartz.kCGEventLeftMouseUp, 
import time
import threading
import sys

if sys.platform == "darwin":
    import Quartz
    from AppKit import NSWorkspace, NSRunningApplication
else:
    import win32gui
    import win32con
    import win32api


VK_CODES = {
    'F2': 0x71,
    'Q': 0x51,
    'E': 0x45,
    'R': 0x52,
    'F': 0x46,
    'X': 0x58,
    'T': 0x54,
    'M': 0x4D,
    '1': 0x31,
    '2': 0x32,
    '3': 0x33,
    '4': 0x34,
    'LEFT_SHIFT': 0xA0,
    'SPACE': 0x20,
    'MIDDLE_MOUSE': 0x04,
    'W': 0x57,
    'A': 0x41,
    'S': 0x53,
    'D': 0x44,
    'ESC': 0x1B,
    'ALT': 0xA4,
    'TAB': 0x09,
}

if sys.platform == "darwin":
    MAC_KEY_MAP = {
        0x71: 120,  
        0x51: 12,   
        0x45: 14,   
        0x52: 15,   
        0x46: 3,    
        0x58: 7,    
        0x54: 17,   
        0x4D: 46,   
        0x31: 18,   
        0x32: 19,   
        0x33: 20,   
        0x34: 21,   
        0xA0: 56,   
        0x20: 49,   
        0x57: 13,   
        0x41: 0,    
        0x53: 1,    
        0x44: 2,    
        0x1B: 53,   
        0xA4: 58,   
        0x09: 48,   
    }

    def fake_activate_window(hwnd):
        try:
            ws = NSWorkspace.sharedWorkspace()
            app = NSRunningApplication.runningApplicationWithProcessIdentifier_(hwnd)
            if app:
                ws.launchApplicationWithBundleIdentifier_options_additionalEventParamDescriptor_launchIdentifier_(
                    app.bundleIdentifier(), 0, None, None)
                return True
        except Exception as e:
            print(e)
        return False

    def simulate_key_press_hold(handle, vk_code, duration):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            
            down_event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, True)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, down_event)
            
            time.sleep(duration)
            
            up_event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, False)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, up_event)
            
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_key_down(handle, vk_code):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, True)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_key_up(handle, vk_code):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, False)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_mouse_left_click_hold(handle, x, y, duration):
        try:
            mouse_down = Quartz.CGEventCreateMouseEvent(
                None, 
                Quartz.kCGEventLeftMouseDown, 
                (x, y), 
                Quartz.kCGMouseButtonLeft
            )
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, mouse_down)
            
            time.sleep(duration)
            
            mouse_up = Quartz.CGEventCreateMouseEvent(
                None, 
                Quartz.kCGEventLeftMouseUp, 
                (x, y), 
                Quartz.kCGMouseButtonLeft
            )
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, mouse_up)
            
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_mouse_left_down(handle, x, y, delay=0.001):
        try:
            event = Quartz.CGEventCreateMouseEvent(
                None, 
                Quartz.kCGEventLeftMouseDown, 
                (x, y), 
                Quartz.kCGMouseButtonLeft
            )
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
            time.sleep(delay)
        except Exception:
            pass

    def simulate_mouse_left_up(handle, x, y, delay=0.001):
        try:
            event = Quartz.CGEventCreateMouseEvent(
                None, 
                Quartz.kCGEventLeftMouseUp, 
                (x, y), 
                Quartz.kCGimport time
import threading
import sys

if sys.platform == "darwin":
    import Quartz
    from AppKit import NSWorkspace, NSRunningApplication
else:
    import win32gui
    import win32con
    import win32api


VK_CODES = {
    'F2': 0x71,
    'Q': 0x51,
    'E': 0x45,
    'R': 0x52,
    'F': 0x46,
    'X': 0x58,
    'T': 0x54,
    'M': 0x4D,
    '1': 0x31,
    '2': 0x32,
    '3': 0x33,
    '4': 0x34,
    'LEFT_SHIFT': 0xA0,
    'SPACE': 0x20,
    'MIDDLE_MOUSE': 0x04,
    'W': 0x57,
    'A': 0x41,
    'S': 0x53,
    'D': 0x44,
    'ESC': 0x1B,
    'ALT': 0xA4,
    'TAB': 0x09,
}

if sys.platform == "darwin":
    MAC_KEY_MAP = {
        0x71: 120,  
        0x51: 12,   
        0x45: 14,   
        0x52: 15,   
        0x46: 3,    
        0x58: 7,    
        0x54: 17,   
        0x4D: 46,   
        0x31: 18,   
        0x32: 19,   
        0x33: 20,   
        0x34: 21,   
        0xA0: 56,   
        0x20: 49,   
        0x57: 13,   
        0x41: 0,    
        0x53: 1,    
        0x44: 2,    
        0x1B: 53,   
        0xA4: 58,   
        0x09: 48,   
    }

    def fake_activate_window(hwnd):
        try:
            ws = NSWorkspace.sharedWorkspace()
            app = NSRunningApplication.runningApplicationWithProcessIdentifier_(hwnd)
            if app:
                ws.launchApplicationWithBundleIdentifier_options_additionalEventParamDescriptor_launchIdentifier_(
                    app.bundleIdentifier(), 0, None, None)
                return True
        except Exception as e:
            print(e)
        return False

    def simulate_key_press_hold(handle, vk_code, duration):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            
            down_event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, True)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, down_event)
            
            time.sleep(duration)
            
            up_event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, False)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, up_event)
            
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_key_down(handle, vk_code):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, True)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_key_up(handle, vk_code):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, False)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_mouse_left_click_hold(handle, x, y, duration):
        try:
            mouse_down = Quartz.CGEventCreateMouseEvent(
                None, 
                Quartz.kCGEventLeftMouseDown, 
                (x, y), 
                Quartz.kCGMouseButtonLeft
            )
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, mouse_down)
            
            time.sleep(duration)
            
            mouse_up = Quartz.CGEventCreateMouseEvent(
                None, 
                Quartz.kCGEventLeftMouseUp, 
                (x, y), 
                Quartz.kCGMouseButtonLeft
            )
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, mouse_up)
            
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_mouse_left_down(handle, x, y, delay=0.001):
        try:
            event = Quartz.CGEventCreateMouseEvent(
                None, 
                Quartz.kCGEventLeftMouseDown, 
                (x, y), 
                Quartz.kCGMouseButtonLeft
            )
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
            time.sleep(delay)
        except Exception:
            pass

    def simulate_mouse_left_up(handle, x, y, delay=0.001):
        try:
            event = Quartz.CGEventCreateMouseEvent(
                None, 
                Quartz.kCGEventLeftMouseUp, 
                (x, y), 
                Quartz.kCGMouseButtonLeft
            )
            Quartz.CGEventPost(Quartz.kCGHIDimport time
import threading
import sys

if sys.platform == "darwin":
    import Quartz
    from AppKit import NSWorkspace, NSRunningApplication
else:
    import win32gui
    import win32con
    import win32api


VK_CODES = {
    'F2': 0x71,
    'Q': 0x51,
    'E': 0x45,
    'R': 0x52,
    'F': 0x46,
    'X': 0x58,
    'T': 0x54,
    'M': 0x4D,
    '1': 0x31,
    '2': 0x32,
    '3': 0x33,
    '4': 0x34,
    'LEFT_SHIFT': 0xA0,
    'SPACE': 0x20,
    'MIDDLE_MOUSE': 0x04,
    'W': 0x57,
    'A': 0x41,
    'S': 0x53,
    'D': 0x44,
    'ESC': 0x1B,
    'ALT': 0xA4,
    'TAB': 0x09,
}

if sys.platform == "darwin":
    MAC_KEY_MAP = {
        0x71: 120,  
        0x51: 12,   
        0x45: 14,   
        0x52: 15,   
        0x46: 3,    
        0x58: 7,    
        0x54: 17,   
        0x4D: 46,   
        0x31: 18,   
        0x32: 19,   
        0x33: 20,   
        0x34: 21,   
        0xA0: 56,   
        0x20: 49,   
        0x57: 13,   
        0x41: 0,    
        0x53: 1,    
        0x44: 2,    
        0x1B: 53,   
        0xA4: 58,   
        0x09: 48,   
    }

    def fake_activate_window(hwnd):
        try:
            ws = NSWorkspace.sharedWorkspace()
            app = NSRunningApplication.runningApplicationWithProcessIdentifier_(hwnd)
            if app:
                ws.launchApplicationWithBundleIdentifier_options_additionalEventParamDescriptor_launchIdentifier_(
                    app.bundleIdentifier(), 0, None, None)
                return True
        except Exception as e:
            print(e)
        return False

    def simulate_key_press_hold(handle, vk_code, duration):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            
            down_event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, True)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, down_event)
            
            time.sleep(duration)
            
            up_event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, False)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, up_event)
            
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_key_down(handle, vk_code):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, True)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_key_up(handle, vk_code):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, False)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_mouse_left_click_hold(handle, x, y, duration):
        try:
            mouse_down = Quartz.CGEventCreateMouseEvent(
                None, 
                Quartz.kCGEventLeftMouseDown, 
                (x, y), 
                Quartz.kCGMouseButtonLeft
            )
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, mouse_down)
            
            time.sleep(duration)
            
            mouse_up = Quartz.CGEventCreateMouseEvent(
                None, 
                Quartz.kCGEventLeftMouseUp, 
                (x, y), 
                Quartz.kCGMouseButtonLeft
            )
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, mouse_up)
            
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_mouse_left_down(handle, x, y, delay=0.001):
        try:
            event = Quartz.CGEventCreateMouseEvent(
                None, 
                Quartz.kCGEventLeftMouseDown, 
                (x, y), 
                Quartz.kCGMouseButtonLeft
            )
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
            time.sleep(delay)
        except Exception:
            pass

    def simulate_mouse_left_up(handle, x, y, delay=0.001):
        try:
            event = Quartz.CGEventCreateMouseEvent(
                None, 
                Quartz.kCGEventLeftMouseUp, 
                (x, y), 
                Quartz.kCGMouseButtonLeft
            )
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
            time.sleep(delay)
        except Exception:
            passimport time
import threading
import sys

if sys.platform == "darwin":
    import Quartz
    from AppKit import NSWorkspace, NSRunningApplication
else:
    import win32gui
    import win32con
    import win32api


VK_CODES = {
    'F2': 0x71,
    'Q': 0x51,
    'E': 0x45,
    'R': 0x52,
    'F': 0x46,
    'X': 0x58,
    'T': 0x54,
    'M': 0x4D,
    '1': 0x31,
    '2': 0x32,
    '3': 0x33,
    '4': 0x34,
    'LEFT_SHIFT': 0xA0,
    'SPACE': 0x20,
    'MIDDLE_MOUSE': 0x04,
    'W': 0x57,
    'A': 0x41,
    'S': 0x53,
    'D': 0x44,
    'ESC': 0x1B,
    'ALT': 0xA4,
    'TAB': 0x09,
}

if sys.platform == "darwin":
    MAC_KEY_MAP = {
        0x71: 120,  
        0x51: 12,   
        0x45: 14,   
        0x52: 15,   
        0x46: 3,    
        0x58: 7,    
        0x54: 17,   
        0x4D: 46,   
        0x31: 18,   
        0x32: 19,   
        0x33: 20,   
        0x34: 21,   
        0xA0: 56,   
        0x20: 49,   
        0x57: 13,   
        0x41: 0,    
        0x53: 1,    
        0x44: 2,    
        0x1B: 53,   
        0xA4: 58,   
        0x09: 48,   
    }

    def fake_activate_window(hwnd):
        try:
            ws = NSWorkspace.sharedWorkspace()
            app = NSRunningApplication.runningApplicationWithProcessIdentifier_(hwnd)
            if app:
                ws.launchApplicationWithBundleIdentifier_options_additionalEventParamDescriptor_launchIdentifier_(
                    app.bundleIdentifier(), 0, None, None)
                return True
        except Exception as e:
            print(e)
        return False

    def simulate_key_press_hold(handle, vk_code, duration):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            
            down_event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, True)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, down_event)
            
            time.sleep(duration)
            
            up_event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, False)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, up_event)
            
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_key_down(handle, vk_code):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, True)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_key_up(handle, vk_code):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, False)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_mouse_left_click_hold(handle, x, y, duration):
        try:
            mouse_down = Quartz.CGEventCreateMouseEvent(
                None, 
                Quartz.kCGEventLeftMouseDown, 
                (x, y), 
                Quartz.kCGMouseButtonLeft
            )
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, mouse_down)
            
            time.sleep(duration)
            
            mouse_up = Quartz.CGEventCreateMouseEvent(
                None, 
                Quartz.kCGEventLeftMouseUp, 
                (x, y), 
                Quartz.kCGMouseButtonLeft
            )
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, mouse_up)
            
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_mouse_left_down(handle, x, y, delay=0.001):
        try:
            event = Quartz.CGEventCreateMouseEvent(
                None, 
                Quartz.kCGEventLeftMouseDown, 
                (x, y), 
                Quartz.kCGMouseButtonLeft
            )
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
            time.sleep(delay)
        except Exception:
            pass

    def simulate_mouse_left_up(handle, x, y, delay=0.001):
        try:
            event = Quartz.CGEventCreateMouseEvent(
                None, 
                Quartz.kCGEventLeftMouseUp, 
                (x, y), 
                Quartz.kCGMouseButtonLeft
            )
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
            time.sleep(delay)
        except Exception:
            pass

else:
    def fake_activate_window(hwnd):
        try:
            win32gui.SendMessage(hwndimport time
import threading
import sys

if sys.platform == "darwin":
    import Quartz
    from AppKit import NSWorkspace, NSRunningApplication
else:
    import win32gui
    import win32con
    import win32api


VK_CODES = {
    'F2': 0x71,
    'Q': 0x51,
    'E': 0x45,
    'R': 0x52,
    'F': 0x46,
    'X': 0x58,
    'T': 0x54,
    'M': 0x4D,
    '1': 0x31,
    '2': 0x32,
    '3': 0x33,
    '4': 0x34,
    'LEFT_SHIFT': 0xA0,
    'SPACE': 0x20,
    'MIDDLE_MOUSE': 0x04,
    'W': 0x57,
    'A': 0x41,
    'S': 0x53,
    'D': 0x44,
    'ESC': 0x1B,
    'ALT': 0xA4,
    'TAB': 0x09,
}

if sys.platform == "darwin":
    MAC_KEY_MAP = {
        0x71: 120,  
        0x51: 12,   
        0x45: 14,   
        0x52: 15,   
        0x46: 3,    
        0x58: 7,    
        0x54: 17,   
        0x4D: 46,   
        0x31: 18,   
        0x32: 19,   
        0x33: 20,   
        0x34: 21,   
        0xA0: 56,   
        0x20: 49,   
        0x57: 13,   
        0x41: 0,    
        0x53: 1,    
        0x44: 2,    
        0x1B: 53,   
        0xA4: 58,   
        0x09: 48,   
    }

    def fake_activate_window(hwnd):
        try:
            ws = NSWorkspace.sharedWorkspace()
            app = NSRunningApplication.runningApplicationWithProcessIdentifier_(hwnd)
            if app:
                ws.launchApplicationWithBundleIdentifier_options_additionalEventParamDescriptor_launchIdentifier_(
                    app.bundleIdentifier(), 0, None, None)
                return True
        except Exception as e:
            print(e)
        return False

    def simulate_key_press_hold(handle, vk_code, duration):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            
            down_event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, True)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, down_event)
            
            time.sleep(duration)
            
            up_event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, False)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, up_event)
            
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_key_down(handle, vk_code):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, True)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_key_up(handle, vk_code):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, False)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_mouse_left_click_hold(handle, x, y, duration):
        try:
            mouse_down = Quartz.CGEventCreateMouseEvent(
                None, 
                Quartz.kCGEventLeftMouseDown, 
                (x, y), 
                Quartz.kCGMouseButtonLeft
            )
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, mouse_down)
            
            time.sleep(duration)
            
            mouse_up = Quartz.CGEventCreateMouseEvent(
                None, 
                Quartz.kCGEventLeftMouseUp, 
                (x, y), 
                Quartz.kCGMouseButtonLeft
            )
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, mouse_up)
            
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_mouse_left_down(handle, x, y, delay=0.001):
        try:
            event = Quartz.CGEventCreateMouseEvent(
                None, 
                Quartz.kCGEventLeftMouseDown, 
                (x, y), 
                Quartz.kCGMouseButtonLeft
            )
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
            time.sleep(delay)
        except Exception:
            pass

    def simulate_mouse_left_up(handle, x, y, delay=0.001):
        try:
            event = Quartz.CGEventCreateMouseEvent(
                None, 
                Quartz.kCGEventLeftMouseUp, 
                (x, y), 
                Quartz.kCGMouseButtonLeft
            )
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
            time.sleep(delay)
        except Exception:
            pass

else:
    def fake_activate_window(hwnd):
        try:
            win32gui.SendMessage(hwnd, win32con.WM_ACTIVATE, winimport time
import threading
import sys

if sys.platform == "darwin":
    import Quartz
    from AppKit import NSWorkspace, NSRunningApplication
else:
    import win32gui
    import win32con
    import win32api


VK_CODES = {
    'F2': 0x71,
    'Q': 0x51,
    'E': 0x45,
    'R': 0x52,
    'F': 0x46,
    'X': 0x58,
    'T': 0x54,
    'M': 0x4D,
    '1': 0x31,
    '2': 0x32,
    '3': 0x33,
    '4': 0x34,
    'LEFT_SHIFT': 0xA0,
    'SPACE': 0x20,
    'MIDDLE_MOUSE': 0x04,
    'W': 0x57,
    'A': 0x41,
    'S': 0x53,
    'D': 0x44,
    'ESC': 0x1B,
    'ALT': 0xA4,
    'TAB': 0x09,
}

if sys.platform == "darwin":
    MAC_KEY_MAP = {
        0x71: 120,  
        0x51: 12,   
        0x45: 14,   
        0x52: 15,   
        0x46: 3,    
        0x58: 7,    
        0x54: 17,   
        0x4D: 46,   
        0x31: 18,   
        0x32: 19,   
        0x33: 20,   
        0x34: 21,   
        0xA0: 56,   
        0x20: 49,   
        0x57: 13,   
        0x41: 0,    
        0x53: 1,    
        0x44: 2,    
        0x1B: 53,   
        0xA4: 58,   
        0x09: 48,   
    }

    def fake_activate_window(hwnd):
        try:
            ws = NSWorkspace.sharedWorkspace()
            app = NSRunningApplication.runningApplicationWithProcessIdentifier_(hwnd)
            if app:
                ws.launchApplicationWithBundleIdentifier_options_additionalEventParamDescriptor_launchIdentifier_(
                    app.bundleIdentifier(), 0, None, None)
                return True
        except Exception as e:
            print(e)
        return False

    def simulate_key_press_hold(handle, vk_code, duration):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            
            down_event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, True)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, down_event)
            
            time.sleep(duration)
            
            up_event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, False)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, up_event)
            
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_key_down(handle, vk_code):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, True)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_key_up(handle, vk_code):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, False)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_mouse_left_click_hold(handle, x, y, duration):
        try:
            mouse_down = Quartz.CGEventCreateMouseEvent(
                None, 
                Quartz.kCGEventLeftMouseDown, 
                (x, y), 
                Quartz.kCGMouseButtonLeft
            )
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, mouse_down)
            
            time.sleep(duration)
            
            mouse_up = Quartz.CGEventCreateMouseEvent(
                None, 
                Quartz.kCGEventLeftMouseUp, 
                (x, y), 
                Quartz.kCGMouseButtonLeft
            )
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, mouse_up)
            
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_mouse_left_down(handle, x, y, delay=0.001):
        try:
            event = Quartz.CGEventCreateMouseEvent(
                None, 
                Quartz.kCGEventLeftMouseDown, 
                (x, y), 
                Quartz.kCGMouseButtonLeft
            )
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
            time.sleep(delay)
        except Exception:
            pass

    def simulate_mouse_left_up(handle, x, y, delay=0.001):
        try:
            event = Quartz.CGEventCreateMouseEvent(
                None, 
                Quartz.kCGEventLeftMouseUp, 
                (x, y), 
                Quartz.kCGMouseButtonLeft
            )
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
            time.sleep(delay)
        except Exception:
            pass

else:
    def fake_activate_window(hwnd):
        try:
            win32gui.SendMessage(hwnd, win32con.WM_ACTIVATE, win32con.WA_ACTIVE, 0)
        except Exception as e:
            print(e)

    def simulate_key_pimport time
import threading
import sys

if sys.platform == "darwin":
    import Quartz
    from AppKit import NSWorkspace, NSRunningApplication
else:
    import win32gui
    import win32con
    import win32api


VK_CODES = {
    'F2': 0x71,
    'Q': 0x51,
    'E': 0x45,
    'R': 0x52,
    'F': 0x46,
    'X': 0x58,
    'T': 0x54,
    'M': 0x4D,
    '1': 0x31,
    '2': 0x32,
    '3': 0x33,
    '4': 0x34,
    'LEFT_SHIFT': 0xA0,
    'SPACE': 0x20,
    'MIDDLE_MOUSE': 0x04,
    'W': 0x57,
    'A': 0x41,
    'S': 0x53,
    'D': 0x44,
    'ESC': 0x1B,
    'ALT': 0xA4,
    'TAB': 0x09,
}

if sys.platform == "darwin":
    MAC_KEY_MAP = {
        0x71: 120,  
        0x51: 12,   
        0x45: 14,   
        0x52: 15,   
        0x46: 3,    
        0x58: 7,    
        0x54: 17,   
        0x4D: 46,   
        0x31: 18,   
        0x32: 19,   
        0x33: 20,   
        0x34: 21,   
        0xA0: 56,   
        0x20: 49,   
        0x57: 13,   
        0x41: 0,    
        0x53: 1,    
        0x44: 2,    
        0x1B: 53,   
        0xA4: 58,   
        0x09: 48,   
    }

    def fake_activate_window(hwnd):
        try:
            ws = NSWorkspace.sharedWorkspace()
            app = NSRunningApplication.runningApplicationWithProcessIdentifier_(hwnd)
            if app:
                ws.launchApplicationWithBundleIdentifier_options_additionalEventParamDescriptor_launchIdentifier_(
                    app.bundleIdentifier(), 0, None, None)
                return True
        except Exception as e:
            print(e)
        return False

    def simulate_key_press_hold(handle, vk_code, duration):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            
            down_event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, True)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, down_event)
            
            time.sleep(duration)
            
            up_event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, False)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, up_event)
            
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_key_down(handle, vk_code):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, True)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_key_up(handle, vk_code):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, False)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_mouse_left_click_hold(handle, x, y, duration):
        try:
            mouse_down = Quartz.CGEventCreateMouseEvent(
                None, 
                Quartz.kCGEventLeftMouseDown, 
                (x, y), 
                Quartz.kCGMouseButtonLeft
            )
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, mouse_down)
            
            time.sleep(duration)
            
            mouse_up = Quartz.CGEventCreateMouseEvent(
                None, 
                Quartz.kCGEventLeftMouseUp, 
                (x, y), 
                Quartz.kCGMouseButtonLeft
            )
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, mouse_up)
            
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_mouse_left_down(handle, x, y, delay=0.001):
        try:
            event = Quartz.CGEventCreateMouseEvent(
                None, 
                Quartz.kCGEventLeftMouseDown, 
                (x, y), 
                Quartz.kCGMouseButtonLeft
            )
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
            time.sleep(delay)
        except Exception:
            pass

    def simulate_mouse_left_up(handle, x, y, delay=0.001):
        try:
            event = Quartz.CGEventCreateMouseEvent(
                None, 
                Quartz.kCGEventLeftMouseUp, 
                (x, y), 
                Quartz.kCGMouseButtonLeft
            )
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
            time.sleep(delay)
        except Exception:
            pass

else:
    def fake_activate_window(hwnd):
        try:
            win32gui.SendMessage(hwnd, win32con.WM_ACTIVATE, win32con.WA_ACTIVE, 0)
        except Exception as e:
            print(e)

    def simulate_key_press_hold(handle, vk_code, durationimport time
import threading
import sys

if sys.platform == "darwin":
    import Quartz
    from AppKit import NSWorkspace, NSRunningApplication
else:
    import win32gui
    import win32con
    import win32api


VK_CODES = {
    'F2': 0x71,
    'Q': 0x51,
    'E': 0x45,
    'R': 0x52,
    'F': 0x46,
    'X': 0x58,
    'T': 0x54,
    'M': 0x4D,
    '1': 0x31,
    '2': 0x32,
    '3': 0x33,
    '4': 0x34,
    'LEFT_SHIFT': 0xA0,
    'SPACE': 0x20,
    'MIDDLE_MOUSE': 0x04,
    'W': 0x57,
    'A': 0x41,
    'S': 0x53,
    'D': 0x44,
    'ESC': 0x1B,
    'ALT': 0xA4,
    'TAB': 0x09,
}

if sys.platform == "darwin":
    MAC_KEY_MAP = {
        0x71: 120,  
        0x51: 12,   
        0x45: 14,   
        0x52: 15,   
        0x46: 3,    
        0x58: 7,    
        0x54: 17,   
        0x4D: 46,   
        0x31: 18,   
        0x32: 19,   
        0x33: 20,   
        0x34: 21,   
        0xA0: 56,   
        0x20: 49,   
        0x57: 13,   
        0x41: 0,    
        0x53: 1,    
        0x44: 2,    
        0x1B: 53,   
        0xA4: 58,   
        0x09: 48,   
    }

    def fake_activate_window(hwnd):
        try:
            ws = NSWorkspace.sharedWorkspace()
            app = NSRunningApplication.runningApplicationWithProcessIdentifier_(hwnd)
            if app:
                ws.launchApplicationWithBundleIdentifier_options_additionalEventParamDescriptor_launchIdentifier_(
                    app.bundleIdentifier(), 0, None, None)
                return True
        except Exception as e:
            print(e)
        return False

    def simulate_key_press_hold(handle, vk_code, duration):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            
            down_event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, True)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, down_event)
            
            time.sleep(duration)
            
            up_event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, False)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, up_event)
            
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_key_down(handle, vk_code):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, True)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_key_up(handle, vk_code):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, False)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_mouse_left_click_hold(handle, x, y, duration):
        try:
            mouse_down = Quartz.CGEventCreateMouseEvent(
                None, 
                Quartz.kCGEventLeftMouseDown, 
                (x, y), 
                Quartz.kCGMouseButtonLeft
            )
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, mouse_down)
            
            time.sleep(duration)
            
            mouse_up = Quartz.CGEventCreateMouseEvent(
                None, 
                Quartz.kCGEventLeftMouseUp, 
                (x, y), 
                Quartz.kCGMouseButtonLeft
            )
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, mouse_up)
            
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_mouse_left_down(handle, x, y, delay=0.001):
        try:
            event = Quartz.CGEventCreateMouseEvent(
                None, 
                Quartz.kCGEventLeftMouseDown, 
                (x, y), 
                Quartz.kCGMouseButtonLeft
            )
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
            time.sleep(delay)
        except Exception:
            pass

    def simulate_mouse_left_up(handle, x, y, delay=0.001):
        try:
            event = Quartz.CGEventCreateMouseEvent(
                None, 
                Quartz.kCGEventLeftMouseUp, 
                (x, y), 
                Quartz.kCGMouseButtonLeft
            )
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
            time.sleep(delay)
        except Exception:
            pass

else:
    def fake_activate_window(hwnd):
        try:
            win32gui.SendMessage(hwnd, win32con.WM_ACTIVATE, win32con.WA_ACTIVE, 0)
        except Exception as e:
            print(e)

    def simulate_key_press_hold(handle, vk_code, duration):
        try:
            win32gui.PostMessage(handle, win32conimport time
import threading
import sys

if sys.platform == "darwin":
    import Quartz
    from AppKit import NSWorkspace, NSRunningApplication
else:
    import win32gui
    import win32con
    import win32api


VK_CODES = {
    'F2': 0x71,
    'Q': 0x51,
    'E': 0x45,
    'R': 0x52,
    'F': 0x46,
    'X': 0x58,
    'T': 0x54,
    'M': 0x4D,
    '1': 0x31,
    '2': 0x32,
    '3': 0x33,
    '4': 0x34,
    'LEFT_SHIFT': 0xA0,
    'SPACE': 0x20,
    'MIDDLE_MOUSE': 0x04,
    'W': 0x57,
    'A': 0x41,
    'S': 0x53,
    'D': 0x44,
    'ESC': 0x1B,
    'ALT': 0xA4,
    'TAB': 0x09,
}

if sys.platform == "darwin":
    MAC_KEY_MAP = {
        0x71: 120,  
        0x51: 12,   
        0x45: 14,   
        0x52: 15,   
        0x46: 3,    
        0x58: 7,    
        0x54: 17,   
        0x4D: 46,   
        0x31: 18,   
        0x32: 19,   
        0x33: 20,   
        0x34: 21,   
        0xA0: 56,   
        0x20: 49,   
        0x57: 13,   
        0x41: 0,    
        0x53: 1,    
        0x44: 2,    
        0x1B: 53,   
        0xA4: 58,   
        0x09: 48,   
    }

    def fake_activate_window(hwnd):
        try:
            ws = NSWorkspace.sharedWorkspace()
            app = NSRunningApplication.runningApplicationWithProcessIdentifier_(hwnd)
            if app:
                ws.launchApplicationWithBundleIdentifier_options_additionalEventParamDescriptor_launchIdentifier_(
                    app.bundleIdentifier(), 0, None, None)
                return True
        except Exception as e:
            print(e)
        return False

    def simulate_key_press_hold(handle, vk_code, duration):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            
            down_event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, True)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, down_event)
            
            time.sleep(duration)
            
            up_event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, False)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, up_event)
            
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_key_down(handle, vk_code):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, True)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_key_up(handle, vk_code):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, False)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_mouse_left_click_hold(handle, x, y, duration):
        try:
            mouse_down = Quartz.CGEventCreateMouseEvent(
                None, 
                Quartz.kCGEventLeftMouseDown, 
                (x, y), 
                Quartz.kCGMouseButtonLeft
            )
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, mouse_down)
            
            time.sleep(duration)
            
            mouse_up = Quartz.CGEventCreateMouseEvent(
                None, 
                Quartz.kCGEventLeftMouseUp, 
                (x, y), 
                Quartz.kCGMouseButtonLeft
            )
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, mouse_up)
            
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_mouse_left_down(handle, x, y, delay=0.001):
        try:
            event = Quartz.CGEventCreateMouseEvent(
                None, 
                Quartz.kCGEventLeftMouseDown, 
                (x, y), 
                Quartz.kCGMouseButtonLeft
            )
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
            time.sleep(delay)
        except Exception:
            pass

    def simulate_mouse_left_up(handle, x, y, delay=0.001):
        try:
            event = Quartz.CGEventCreateMouseEvent(
                None, 
                Quartz.kCGEventLeftMouseUp, 
                (x, y), 
                Quartz.kCGMouseButtonLeft
            )
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
            time.sleep(delay)
        except Exception:
            pass

else:
    def fake_activate_window(hwnd):
        try:
            win32gui.SendMessage(hwnd, win32con.WM_ACTIVATE, win32con.WA_ACTIVE, 0)
        except Exception as e:
            print(e)

    def simulate_key_press_hold(handle, vk_code, duration):
        try:
            win32gui.PostMessage(handle, win32con.WM_KEYDOWN, vk_code, 0)
            time.sleep(duration)
import time
import threading
import sys

if sys.platform == "darwin":
    import Quartz
    from AppKit import NSWorkspace, NSRunningApplication
else:
    import win32gui
    import win32con
    import win32api


VK_CODES = {
    'F2': 0x71,
    'Q': 0x51,
    'E': 0x45,
    'R': 0x52,
    'F': 0x46,
    'X': 0x58,
    'T': 0x54,
    'M': 0x4D,
    '1': 0x31,
    '2': 0x32,
    '3': 0x33,
    '4': 0x34,
    'LEFT_SHIFT': 0xA0,
    'SPACE': 0x20,
    'MIDDLE_MOUSE': 0x04,
    'W': 0x57,
    'A': 0x41,
    'S': 0x53,
    'D': 0x44,
    'ESC': 0x1B,
    'ALT': 0xA4,
    'TAB': 0x09,
}

if sys.platform == "darwin":
    MAC_KEY_MAP = {
        0x71: 120,  
        0x51: 12,   
        0x45: 14,   
        0x52: 15,   
        0x46: 3,    
        0x58: 7,    
        0x54: 17,   
        0x4D: 46,   
        0x31: 18,   
        0x32: 19,   
        0x33: 20,   
        0x34: 21,   
        0xA0: 56,   
        0x20: 49,   
        0x57: 13,   
        0x41: 0,    
        0x53: 1,    
        0x44: 2,    
        0x1B: 53,   
        0xA4: 58,   
        0x09: 48,   
    }

    def fake_activate_window(hwnd):
        try:
            ws = NSWorkspace.sharedWorkspace()
            app = NSRunningApplication.runningApplicationWithProcessIdentifier_(hwnd)
            if app:
                ws.launchApplicationWithBundleIdentifier_options_additionalEventParamDescriptor_launchIdentifier_(
                    app.bundleIdentifier(), 0, None, None)
                return True
        except Exception as e:
            print(e)
        return False

    def simulate_key_press_hold(handle, vk_code, duration):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            
            down_event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, True)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, down_event)
            
            time.sleep(duration)
            
            up_event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, False)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, up_event)
            
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_key_down(handle, vk_code):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, True)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_key_up(handle, vk_code):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, False)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_mouse_left_click_hold(handle, x, y, duration):
        try:
            mouse_down = Quartz.CGEventCreateMouseEvent(
                None, 
                Quartz.kCGEventLeftMouseDown, 
                (x, y), 
                Quartz.kCGMouseButtonLeft
            )
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, mouse_down)
            
            time.sleep(duration)
            
            mouse_up = Quartz.CGEventCreateMouseEvent(
                None, 
                Quartz.kCGEventLeftMouseUp, 
                (x, y), 
                Quartz.kCGMouseButtonLeft
            )
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, mouse_up)
            
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_mouse_left_down(handle, x, y, delay=0.001):
        try:
            event = Quartz.CGEventCreateMouseEvent(
                None, 
                Quartz.kCGEventLeftMouseDown, 
                (x, y), 
                Quartz.kCGMouseButtonLeft
            )
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
            time.sleep(delay)
        except Exception:
            pass

    def simulate_mouse_left_up(handle, x, y, delay=0.001):
        try:
            event = Quartz.CGEventCreateMouseEvent(
                None, 
                Quartz.kCGEventLeftMouseUp, 
                (x, y), 
                Quartz.kCGMouseButtonLeft
            )
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
            time.sleep(delay)
        except Exception:
            pass

else:
    def fake_activate_window(hwnd):
        try:
            win32gui.SendMessage(hwnd, win32con.WM_ACTIVATE, win32con.WA_ACTIVE, 0)
        except Exception as e:
            print(e)

    def simulate_key_press_hold(handle, vk_code, duration):
        try:
            win32gui.PostMessage(handle, win32con.WM_KEYDOWN, vk_code, 0)
            time.sleep(duration)
            win32gui.PostMessage(handle, win32con.WM_KEYUP, vimport time
import threading
import sys

if sys.platform == "darwin":
    import Quartz
    from AppKit import NSWorkspace, NSRunningApplication
else:
    import win32gui
    import win32con
    import win32api


VK_CODES = {
    'F2': 0x71,
    'Q': 0x51,
    'E': 0x45,
    'R': 0x52,
    'F': 0x46,
    'X': 0x58,
    'T': 0x54,
    'M': 0x4D,
    '1': 0x31,
    '2': 0x32,
    '3': 0x33,
    '4': 0x34,
    'LEFT_SHIFT': 0xA0,
    'SPACE': 0x20,
    'MIDDLE_MOUSE': 0x04,
    'W': 0x57,
    'A': 0x41,
    'S': 0x53,
    'D': 0x44,
    'ESC': 0x1B,
    'ALT': 0xA4,
    'TAB': 0x09,
}

if sys.platform == "darwin":
    MAC_KEY_MAP = {
        0x71: 120,  
        0x51: 12,   
        0x45: 14,   
        0x52: 15,   
        0x46: 3,    
        0x58: 7,    
        0x54: 17,   
        0x4D: 46,   
        0x31: 18,   
        0x32: 19,   
        0x33: 20,   
        0x34: 21,   
        0xA0: 56,   
        0x20: 49,   
        0x57: 13,   
        0x41: 0,    
        0x53: 1,    
        0x44: 2,    
        0x1B: 53,   
        0xA4: 58,   
        0x09: 48,   
    }

    def fake_activate_window(hwnd):
        try:
            ws = NSWorkspace.sharedWorkspace()
            app = NSRunningApplication.runningApplicationWithProcessIdentifier_(hwnd)
            if app:
                ws.launchApplicationWithBundleIdentifier_options_additionalEventParamDescriptor_launchIdentifier_(
                    app.bundleIdentifier(), 0, None, None)
                return True
        except Exception as e:
            print(e)
        return False

    def simulate_key_press_hold(handle, vk_code, duration):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            
            down_event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, True)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, down_event)
            
            time.sleep(duration)
            
            up_event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, False)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, up_event)
            
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_key_down(handle, vk_code):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, True)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_key_up(handle, vk_code):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, False)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_mouse_left_click_hold(handle, x, y, duration):
        try:
            mouse_down = Quartz.CGEventCreateMouseEvent(
                None, 
                Quartz.kCGEventLeftMouseDown, 
                (x, y), 
                Quartz.kCGMouseButtonLeft
            )
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, mouse_down)
            
            time.sleep(duration)
            
            mouse_up = Quartz.CGEventCreateMouseEvent(
                None, 
                Quartz.kCGEventLeftMouseUp, 
                (x, y), 
                Quartz.kCGMouseButtonLeft
            )
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, mouse_up)
            
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_mouse_left_down(handle, x, y, delay=0.001):
        try:
            event = Quartz.CGEventCreateMouseEvent(
                None, 
                Quartz.kCGEventLeftMouseDown, 
                (x, y), 
                Quartz.kCGMouseButtonLeft
            )
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
            time.sleep(delay)
        except Exception:
            pass

    def simulate_mouse_left_up(handle, x, y, delay=0.001):
        try:
            event = Quartz.CGEventCreateMouseEvent(
                None, 
                Quartz.kCGEventLeftMouseUp, 
                (x, y), 
                Quartz.kCGMouseButtonLeft
            )
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
            time.sleep(delay)
        except Exception:
            pass

else:
    def fake_activate_window(hwnd):
        try:
            win32gui.SendMessage(hwnd, win32con.WM_ACTIVATE, win32con.WA_ACTIVE, 0)
        except Exception as e:
            print(e)

    def simulate_key_press_hold(handle, vk_code, duration):
        try:
            win32gui.PostMessage(handle, win32con.WM_KEYDOWN, vk_code, 0)
            time.sleep(duration)
            win32gui.PostMessage(handle, win32con.WM_KEYUP, vk_code, 0)
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulateimport time
import threading
import sys

if sys.platform == "darwin":
    import Quartz
    from AppKit import NSWorkspace, NSRunningApplication
else:
    import win32gui
    import win32con
    import win32api


VK_CODES = {
    'F2': 0x71,
    'Q': 0x51,
    'E': 0x45,
    'R': 0x52,
    'F': 0x46,
    'X': 0x58,
    'T': 0x54,
    'M': 0x4D,
    '1': 0x31,
    '2': 0x32,
    '3': 0x33,
    '4': 0x34,
    'LEFT_SHIFT': 0xA0,
    'SPACE': 0x20,
    'MIDDLE_MOUSE': 0x04,
    'W': 0x57,
    'A': 0x41,
    'S': 0x53,
    'D': 0x44,
    'ESC': 0x1B,
    'ALT': 0xA4,
    'TAB': 0x09,
}

if sys.platform == "darwin":
    MAC_KEY_MAP = {
        0x71: 120,  
        0x51: 12,   
        0x45: 14,   
        0x52: 15,   
        0x46: 3,    
        0x58: 7,    
        0x54: 17,   
        0x4D: 46,   
        0x31: 18,   
        0x32: 19,   
        0x33: 20,   
        0x34: 21,   
        0xA0: 56,   
        0x20: 49,   
        0x57: 13,   
        0x41: 0,    
        0x53: 1,    
        0x44: 2,    
        0x1B: 53,   
        0xA4: 58,   
        0x09: 48,   
    }

    def fake_activate_window(hwnd):
        try:
            ws = NSWorkspace.sharedWorkspace()
            app = NSRunningApplication.runningApplicationWithProcessIdentifier_(hwnd)
            if app:
                ws.launchApplicationWithBundleIdentifier_options_additionalEventParamDescriptor_launchIdentifier_(
                    app.bundleIdentifier(), 0, None, None)
                return True
        except Exception as e:
            print(e)
        return False

    def simulate_key_press_hold(handle, vk_code, duration):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            
            down_event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, True)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, down_event)
            
            time.sleep(duration)
            
            up_event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, False)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, up_event)
            
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_key_down(handle, vk_code):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, True)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_key_up(handle, vk_code):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, False)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_mouse_left_click_hold(handle, x, y, duration):
        try:
            mouse_down = Quartz.CGEventCreateMouseEvent(
                None, 
                Quartz.kCGEventLeftMouseDown, 
                (x, y), 
                Quartz.kCGMouseButtonLeft
            )
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, mouse_down)
            
            time.sleep(duration)
            
            mouse_up = Quartz.CGEventCreateMouseEvent(
                None, 
                Quartz.kCGEventLeftMouseUp, 
                (x, y), 
                Quartz.kCGMouseButtonLeft
            )
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, mouse_up)
            
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_mouse_left_down(handle, x, y, delay=0.001):
        try:
            event = Quartz.CGEventCreateMouseEvent(
                None, 
                Quartz.kCGEventLeftMouseDown, 
                (x, y), 
                Quartz.kCGMouseButtonLeft
            )
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
            time.sleep(delay)
        except Exception:
            pass

    def simulate_mouse_left_up(handle, x, y, delay=0.001):
        try:
            event = Quartz.CGEventCreateMouseEvent(
                None, 
                Quartz.kCGEventLeftMouseUp, 
                (x, y), 
                Quartz.kCGMouseButtonLeft
            )
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
            time.sleep(delay)
        except Exception:
            pass

else:
    def fake_activate_window(hwnd):
        try:
            win32gui.SendMessage(hwnd, win32con.WM_ACTIVATE, win32con.WA_ACTIVE, 0)
        except Exception as e:
            print(e)

    def simulate_key_press_hold(handle, vk_code, duration):
        try:
            win32gui.PostMessage(handle, win32con.WM_KEYDOWN, vk_code, 0)
            time.sleep(duration)
            win32gui.PostMessage(handle, win32con.WM_KEYUP, vk_code, 0)
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_key_down(handle, vk_code):
        try:
            win32gui.Postimport time
import threading
import sys

if sys.platform == "darwin":
    import Quartz
    from AppKit import NSWorkspace, NSRunningApplication
else:
    import win32gui
    import win32con
    import win32api


VK_CODES = {
    'F2': 0x71,
    'Q': 0x51,
    'E': 0x45,
    'R': 0x52,
    'F': 0x46,
    'X': 0x58,
    'T': 0x54,
    'M': 0x4D,
    '1': 0x31,
    '2': 0x32,
    '3': 0x33,
    '4': 0x34,
    'LEFT_SHIFT': 0xA0,
    'SPACE': 0x20,
    'MIDDLE_MOUSE': 0x04,
    'W': 0x57,
    'A': 0x41,
    'S': 0x53,
    'D': 0x44,
    'ESC': 0x1B,
    'ALT': 0xA4,
    'TAB': 0x09,
}

if sys.platform == "darwin":
    MAC_KEY_MAP = {
        0x71: 120,  
        0x51: 12,   
        0x45: 14,   
        0x52: 15,   
        0x46: 3,    
        0x58: 7,    
        0x54: 17,   
        0x4D: 46,   
        0x31: 18,   
        0x32: 19,   
        0x33: 20,   
        0x34: 21,   
        0xA0: 56,   
        0x20: 49,   
        0x57: 13,   
        0x41: 0,    
        0x53: 1,    
        0x44: 2,    
        0x1B: 53,   
        0xA4: 58,   
        0x09: 48,   
    }

    def fake_activate_window(hwnd):
        try:
            ws = NSWorkspace.sharedWorkspace()
            app = NSRunningApplication.runningApplicationWithProcessIdentifier_(hwnd)
            if app:
                ws.launchApplicationWithBundleIdentifier_options_additionalEventParamDescriptor_launchIdentifier_(
                    app.bundleIdentifier(), 0, None, None)
                return True
        except Exception as e:
            print(e)
        return False

    def simulate_key_press_hold(handle, vk_code, duration):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            
            down_event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, True)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, down_event)
            
            time.sleep(duration)
            
            up_event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, False)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, up_event)
            
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_key_down(handle, vk_code):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, True)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_key_up(handle, vk_code):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, False)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_mouse_left_click_hold(handle, x, y, duration):
        try:
            mouse_down = Quartz.CGEventCreateMouseEvent(
                None, 
                Quartz.kCGEventLeftMouseDown, 
                (x, y), 
                Quartz.kCGMouseButtonLeft
            )
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, mouse_down)
            
            time.sleep(duration)
            
            mouse_up = Quartz.CGEventCreateMouseEvent(
                None, 
                Quartz.kCGEventLeftMouseUp, 
                (x, y), 
                Quartz.kCGMouseButtonLeft
            )
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, mouse_up)
            
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_mouse_left_down(handle, x, y, delay=0.001):
        try:
            event = Quartz.CGEventCreateMouseEvent(
                None, 
                Quartz.kCGEventLeftMouseDown, 
                (x, y), 
                Quartz.kCGMouseButtonLeft
            )
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
            time.sleep(delay)
        except Exception:
            pass

    def simulate_mouse_left_up(handle, x, y, delay=0.001):
        try:
            event = Quartz.CGEventCreateMouseEvent(
                None, 
                Quartz.kCGEventLeftMouseUp, 
                (x, y), 
                Quartz.kCGMouseButtonLeft
            )
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
            time.sleep(delay)
        except Exception:
            pass

else:
    def fake_activate_window(hwnd):
        try:
            win32gui.SendMessage(hwnd, win32con.WM_ACTIVATE, win32con.WA_ACTIVE, 0)
        except Exception as e:
            print(e)

    def simulate_key_press_hold(handle, vk_code, duration):
        try:
            win32gui.PostMessage(handle, win32con.WM_KEYDOWN, vk_code, 0)
            time.sleep(duration)
            win32gui.PostMessage(handle, win32con.WM_KEYUP, vk_code, 0)
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_key_down(handle, vk_code):
        try:
            win32gui.PostMessage(handle, win32con.WM_KEYimport time
import threading
import sys

if sys.platform == "darwin":
    import Quartz
    from AppKit import NSWorkspace, NSRunningApplication
else:
    import win32gui
    import win32con
    import win32api


VK_CODES = {
    'F2': 0x71,
    'Q': 0x51,
    'E': 0x45,
    'R': 0x52,
    'F': 0x46,
    'X': 0x58,
    'T': 0x54,
    'M': 0x4D,
    '1': 0x31,
    '2': 0x32,
    '3': 0x33,
    '4': 0x34,
    'LEFT_SHIFT': 0xA0,
    'SPACE': 0x20,
    'MIDDLE_MOUSE': 0x04,
    'W': 0x57,
    'A': 0x41,
    'S': 0x53,
    'D': 0x44,
    'ESC': 0x1B,
    'ALT': 0xA4,
    'TAB': 0x09,
}

if sys.platform == "darwin":
    MAC_KEY_MAP = {
        0x71: 120,  
        0x51: 12,   
        0x45: 14,   
        0x52: 15,   
        0x46: 3,    
        0x58: 7,    
        0x54: 17,   
        0x4D: 46,   
        0x31: 18,   
        0x32: 19,   
        0x33: 20,   
        0x34: 21,   
        0xA0: 56,   
        0x20: 49,   
        0x57: 13,   
        0x41: 0,    
        0x53: 1,    
        0x44: 2,    
        0x1B: 53,   
        0xA4: 58,   
        0x09: 48,   
    }

    def fake_activate_window(hwnd):
        try:
            ws = NSWorkspace.sharedWorkspace()
            app = NSRunningApplication.runningApplicationWithProcessIdentifier_(hwnd)
            if app:
                ws.launchApplicationWithBundleIdentifier_options_additionalEventParamDescriptor_launchIdentifier_(
                    app.bundleIdentifier(), 0, None, None)
                return True
        except Exception as e:
            print(e)
        return False

    def simulate_key_press_hold(handle, vk_code, duration):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            
            down_event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, True)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, down_event)
            
            time.sleep(duration)
            
            up_event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, False)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, up_event)
            
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_key_down(handle, vk_code):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, True)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_key_up(handle, vk_code):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, False)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_mouse_left_click_hold(handle, x, y, duration):
        try:
            mouse_down = Quartz.CGEventCreateMouseEvent(
                None, 
                Quartz.kCGEventLeftMouseDown, 
                (x, y), 
                Quartz.kCGMouseButtonLeft
            )
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, mouse_down)
            
            time.sleep(duration)
            
            mouse_up = Quartz.CGEventCreateMouseEvent(
                None, 
                Quartz.kCGEventLeftMouseUp, 
                (x, y), 
                Quartz.kCGMouseButtonLeft
            )
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, mouse_up)
            
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_mouse_left_down(handle, x, y, delay=0.001):
        try:
            event = Quartz.CGEventCreateMouseEvent(
                None, 
                Quartz.kCGEventLeftMouseDown, 
                (x, y), 
                Quartz.kCGMouseButtonLeft
            )
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
            time.sleep(delay)
        except Exception:
            pass

    def simulate_mouse_left_up(handle, x, y, delay=0.001):
        try:
            event = Quartz.CGEventCreateMouseEvent(
                None, 
                Quartz.kCGEventLeftMouseUp, 
                (x, y), 
                Quartz.kCGMouseButtonLeft
            )
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
            time.sleep(delay)
        except Exception:
            pass

else:
    def fake_activate_window(hwnd):
        try:
            win32gui.SendMessage(hwnd, win32con.WM_ACTIVATE, win32con.WA_ACTIVE, 0)
        except Exception as e:
            print(e)

    def simulate_key_press_hold(handle, vk_code, duration):
        try:
            win32gui.PostMessage(handle, win32con.WM_KEYDOWN, vk_code, 0)
            time.sleep(duration)
            win32gui.PostMessage(handle, win32con.WM_KEYUP, vk_code, 0)
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_key_down(handle, vk_code):
        try:
            win32gui.PostMessage(handle, win32con.WM_KEYDOWN, vk_code, 0)
        except Exception as e:
            print(eimport time
import threading
import sys

if sys.platform == "darwin":
    import Quartz
    from AppKit import NSWorkspace, NSRunningApplication
else:
    import win32gui
    import win32con
    import win32api


VK_CODES = {
    'F2': 0x71,
    'Q': 0x51,
    'E': 0x45,
    'R': 0x52,
    'F': 0x46,
    'X': 0x58,
    'T': 0x54,
    'M': 0x4D,
    '1': 0x31,
    '2': 0x32,
    '3': 0x33,
    '4': 0x34,
    'LEFT_SHIFT': 0xA0,
    'SPACE': 0x20,
    'MIDDLE_MOUSE': 0x04,
    'W': 0x57,
    'A': 0x41,
    'S': 0x53,
    'D': 0x44,
    'ESC': 0x1B,
    'ALT': 0xA4,
    'TAB': 0x09,
}

if sys.platform == "darwin":
    MAC_KEY_MAP = {
        0x71: 120,  
        0x51: 12,   
        0x45: 14,   
        0x52: 15,   
        0x46: 3,    
        0x58: 7,    
        0x54: 17,   
        0x4D: 46,   
        0x31: 18,   
        0x32: 19,   
        0x33: 20,   
        0x34: 21,   
        0xA0: 56,   
        0x20: 49,   
        0x57: 13,   
        0x41: 0,    
        0x53: 1,    
        0x44: 2,    
        0x1B: 53,   
        0xA4: 58,   
        0x09: 48,   
    }

    def fake_activate_window(hwnd):
        try:
            ws = NSWorkspace.sharedWorkspace()
            app = NSRunningApplication.runningApplicationWithProcessIdentifier_(hwnd)
            if app:
                ws.launchApplicationWithBundleIdentifier_options_additionalEventParamDescriptor_launchIdentifier_(
                    app.bundleIdentifier(), 0, None, None)
                return True
        except Exception as e:
            print(e)
        return False

    def simulate_key_press_hold(handle, vk_code, duration):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            
            down_event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, True)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, down_event)
            
            time.sleep(duration)
            
            up_event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, False)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, up_event)
            
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_key_down(handle, vk_code):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, True)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_key_up(handle, vk_code):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, False)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_mouse_left_click_hold(handle, x, y, duration):
        try:
            mouse_down = Quartz.CGEventCreateMouseEvent(
                None, 
                Quartz.kCGEventLeftMouseDown, 
                (x, y), 
                Quartz.kCGMouseButtonLeft
            )
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, mouse_down)
            
            time.sleep(duration)
            
            mouse_up = Quartz.CGEventCreateMouseEvent(
                None, 
                Quartz.kCGEventLeftMouseUp, 
                (x, y), 
                Quartz.kCGMouseButtonLeft
            )
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, mouse_up)
            
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_mouse_left_down(handle, x, y, delay=0.001):
        try:
            event = Quartz.CGEventCreateMouseEvent(
                None, 
                Quartz.kCGEventLeftMouseDown, 
                (x, y), 
                Quartz.kCGMouseButtonLeft
            )
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
            time.sleep(delay)
        except Exception:
            pass

    def simulate_mouse_left_up(handle, x, y, delay=0.001):
        try:
            event = Quartz.CGEventCreateMouseEvent(
                None, 
                Quartz.kCGEventLeftMouseUp, 
                (x, y), 
                Quartz.kCGMouseButtonLeft
            )
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
            time.sleep(delay)
        except Exception:
            pass

else:
    def fake_activate_window(hwnd):
        try:
            win32gui.SendMessage(hwnd, win32con.WM_ACTIVATE, win32con.WA_ACTIVE, 0)
        except Exception as e:
            print(e)

    def simulate_key_press_hold(handle, vk_code, duration):
        try:
            win32gui.PostMessage(handle, win32con.WM_KEYDOWN, vk_code, 0)
            time.sleep(duration)
            win32gui.PostMessage(handle, win32con.WM_KEYUP, vk_code, 0)
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_key_down(handle, vk_code):
        try:
            win32gui.PostMessage(handle, win32con.WM_KEYDOWN, vk_code, 0)
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_key_up(handle, vk_codeimport time
import threading
import sys

if sys.platform == "darwin":
    import Quartz
    from AppKit import NSWorkspace, NSRunningApplication
else:
    import win32gui
    import win32con
    import win32api


VK_CODES = {
    'F2': 0x71,
    'Q': 0x51,
    'E': 0x45,
    'R': 0x52,
    'F': 0x46,
    'X': 0x58,
    'T': 0x54,
    'M': 0x4D,
    '1': 0x31,
    '2': 0x32,
    '3': 0x33,
    '4': 0x34,
    'LEFT_SHIFT': 0xA0,
    'SPACE': 0x20,
    'MIDDLE_MOUSE': 0x04,
    'W': 0x57,
    'A': 0x41,
    'S': 0x53,
    'D': 0x44,
    'ESC': 0x1B,
    'ALT': 0xA4,
    'TAB': 0x09,
}

if sys.platform == "darwin":
    MAC_KEY_MAP = {
        0x71: 120,  
        0x51: 12,   
        0x45: 14,   
        0x52: 15,   
        0x46: 3,    
        0x58: 7,    
        0x54: 17,   
        0x4D: 46,   
        0x31: 18,   
        0x32: 19,   
        0x33: 20,   
        0x34: 21,   
        0xA0: 56,   
        0x20: 49,   
        0x57: 13,   
        0x41: 0,    
        0x53: 1,    
        0x44: 2,    
        0x1B: 53,   
        0xA4: 58,   
        0x09: 48,   
    }

    def fake_activate_window(hwnd):
        try:
            ws = NSWorkspace.sharedWorkspace()
            app = NSRunningApplication.runningApplicationWithProcessIdentifier_(hwnd)
            if app:
                ws.launchApplicationWithBundleIdentifier_options_additionalEventParamDescriptor_launchIdentifier_(
                    app.bundleIdentifier(), 0, None, None)
                return True
        except Exception as e:
            print(e)
        return False

    def simulate_key_press_hold(handle, vk_code, duration):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            
            down_event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, True)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, down_event)
            
            time.sleep(duration)
            
            up_event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, False)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, up_event)
            
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_key_down(handle, vk_code):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, True)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_key_up(handle, vk_code):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, False)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_mouse_left_click_hold(handle, x, y, duration):
        try:
            mouse_down = Quartz.CGEventCreateMouseEvent(
                None, 
                Quartz.kCGEventLeftMouseDown, 
                (x, y), 
                Quartz.kCGMouseButtonLeft
            )
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, mouse_down)
            
            time.sleep(duration)
            
            mouse_up = Quartz.CGEventCreateMouseEvent(
                None, 
                Quartz.kCGEventLeftMouseUp, 
                (x, y), 
                Quartz.kCGMouseButtonLeft
            )
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, mouse_up)
            
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_mouse_left_down(handle, x, y, delay=0.001):
        try:
            event = Quartz.CGEventCreateMouseEvent(
                None, 
                Quartz.kCGEventLeftMouseDown, 
                (x, y), 
                Quartz.kCGMouseButtonLeft
            )
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
            time.sleep(delay)
        except Exception:
            pass

    def simulate_mouse_left_up(handle, x, y, delay=0.001):
        try:
            event = Quartz.CGEventCreateMouseEvent(
                None, 
                Quartz.kCGEventLeftMouseUp, 
                (x, y), 
                Quartz.kCGMouseButtonLeft
            )
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
            time.sleep(delay)
        except Exception:
            pass

else:
    def fake_activate_window(hwnd):
        try:
            win32gui.SendMessage(hwnd, win32con.WM_ACTIVATE, win32con.WA_ACTIVE, 0)
        except Exception as e:
            print(e)

    def simulate_key_press_hold(handle, vk_code, duration):
        try:
            win32gui.PostMessage(handle, win32con.WM_KEYDOWN, vk_code, 0)
            time.sleep(duration)
            win32gui.PostMessage(handle, win32con.WM_KEYUP, vk_code, 0)
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_key_down(handle, vk_code):
        try:
            win32gui.PostMessage(handle, win32con.WM_KEYDOWN, vk_code, 0)
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_key_up(handle, vk_code):
        try:
            win32gui.PostMessage(handle, win32conimport time
import threading
import sys

if sys.platform == "darwin":
    import Quartz
    from AppKit import NSWorkspace, NSRunningApplication
else:
    import win32gui
    import win32con
    import win32api


VK_CODES = {
    'F2': 0x71,
    'Q': 0x51,
    'E': 0x45,
    'R': 0x52,
    'F': 0x46,
    'X': 0x58,
    'T': 0x54,
    'M': 0x4D,
    '1': 0x31,
    '2': 0x32,
    '3': 0x33,
    '4': 0x34,
    'LEFT_SHIFT': 0xA0,
    'SPACE': 0x20,
    'MIDDLE_MOUSE': 0x04,
    'W': 0x57,
    'A': 0x41,
    'S': 0x53,
    'D': 0x44,
    'ESC': 0x1B,
    'ALT': 0xA4,
    'TAB': 0x09,
}

if sys.platform == "darwin":
    MAC_KEY_MAP = {
        0x71: 120,  
        0x51: 12,   
        0x45: 14,   
        0x52: 15,   
        0x46: 3,    
        0x58: 7,    
        0x54: 17,   
        0x4D: 46,   
        0x31: 18,   
        0x32: 19,   
        0x33: 20,   
        0x34: 21,   
        0xA0: 56,   
        0x20: 49,   
        0x57: 13,   
        0x41: 0,    
        0x53: 1,    
        0x44: 2,    
        0x1B: 53,   
        0xA4: 58,   
        0x09: 48,   
    }

    def fake_activate_window(hwnd):
        try:
            ws = NSWorkspace.sharedWorkspace()
            app = NSRunningApplication.runningApplicationWithProcessIdentifier_(hwnd)
            if app:
                ws.launchApplicationWithBundleIdentifier_options_additionalEventParamDescriptor_launchIdentifier_(
                    app.bundleIdentifier(), 0, None, None)
                return True
        except Exception as e:
            print(e)
        return False

    def simulate_key_press_hold(handle, vk_code, duration):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            
            down_event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, True)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, down_event)
            
            time.sleep(duration)
            
            up_event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, False)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, up_event)
            
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_key_down(handle, vk_code):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, True)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_key_up(handle, vk_code):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, False)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_mouse_left_click_hold(handle, x, y, duration):
        try:
            mouse_down = Quartz.CGEventCreateMouseEvent(
                None, 
                Quartz.kCGEventLeftMouseDown, 
                (x, y), 
                Quartz.kCGMouseButtonLeft
            )
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, mouse_down)
            
            time.sleep(duration)
            
            mouse_up = Quartz.CGEventCreateMouseEvent(
                None, 
                Quartz.kCGEventLeftMouseUp, 
                (x, y), 
                Quartz.kCGMouseButtonLeft
            )
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, mouse_up)
            
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_mouse_left_down(handle, x, y, delay=0.001):
        try:
            event = Quartz.CGEventCreateMouseEvent(
                None, 
                Quartz.kCGEventLeftMouseDown, 
                (x, y), 
                Quartz.kCGMouseButtonLeft
            )
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
            time.sleep(delay)
        except Exception:
            pass

    def simulate_mouse_left_up(handle, x, y, delay=0.001):
        try:
            event = Quartz.CGEventCreateMouseEvent(
                None, 
                Quartz.kCGEventLeftMouseUp, 
                (x, y), 
                Quartz.kCGMouseButtonLeft
            )
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
            time.sleep(delay)
        except Exception:
            pass

else:
    def fake_activate_window(hwnd):
        try:
            win32gui.SendMessage(hwnd, win32con.WM_ACTIVATE, win32con.WA_ACTIVE, 0)
        except Exception as e:
            print(e)

    def simulate_key_press_hold(handle, vk_code, duration):
        try:
            win32gui.PostMessage(handle, win32con.WM_KEYDOWN, vk_code, 0)
            time.sleep(duration)
            win32gui.PostMessage(handle, win32con.WM_KEYUP, vk_code, 0)
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_key_down(handle, vk_code):
        try:
            win32gui.PostMessage(handle, win32con.WM_KEYDOWN, vk_code, 0)
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_key_up(handle, vk_code):
        try:
            win32gui.PostMessage(handle, win32con.WM_KEYUP, vk_code, 0)
        except Exception as e:
import time
import threading
import sys

if sys.platform == "darwin":
    import Quartz
    from AppKit import NSWorkspace, NSRunningApplication
else:
    import win32gui
    import win32con
    import win32api


VK_CODES = {
    'F2': 0x71,
    'Q': 0x51,
    'E': 0x45,
    'R': 0x52,
    'F': 0x46,
    'X': 0x58,
    'T': 0x54,
    'M': 0x4D,
    '1': 0x31,
    '2': 0x32,
    '3': 0x33,
    '4': 0x34,
    'LEFT_SHIFT': 0xA0,
    'SPACE': 0x20,
    'MIDDLE_MOUSE': 0x04,
    'W': 0x57,
    'A': 0x41,
    'S': 0x53,
    'D': 0x44,
    'ESC': 0x1B,
    'ALT': 0xA4,
    'TAB': 0x09,
}

if sys.platform == "darwin":
    MAC_KEY_MAP = {
        0x71: 120,  
        0x51: 12,   
        0x45: 14,   
        0x52: 15,   
        0x46: 3,    
        0x58: 7,    
        0x54: 17,   
        0x4D: 46,   
        0x31: 18,   
        0x32: 19,   
        0x33: 20,   
        0x34: 21,   
        0xA0: 56,   
        0x20: 49,   
        0x57: 13,   
        0x41: 0,    
        0x53: 1,    
        0x44: 2,    
        0x1B: 53,   
        0xA4: 58,   
        0x09: 48,   
    }

    def fake_activate_window(hwnd):
        try:
            ws = NSWorkspace.sharedWorkspace()
            app = NSRunningApplication.runningApplicationWithProcessIdentifier_(hwnd)
            if app:
                ws.launchApplicationWithBundleIdentifier_options_additionalEventParamDescriptor_launchIdentifier_(
                    app.bundleIdentifier(), 0, None, None)
                return True
        except Exception as e:
            print(e)
        return False

    def simulate_key_press_hold(handle, vk_code, duration):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            
            down_event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, True)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, down_event)
            
            time.sleep(duration)
            
            up_event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, False)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, up_event)
            
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_key_down(handle, vk_code):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, True)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_key_up(handle, vk_code):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, False)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_mouse_left_click_hold(handle, x, y, duration):
        try:
            mouse_down = Quartz.CGEventCreateMouseEvent(
                None, 
                Quartz.kCGEventLeftMouseDown, 
                (x, y), 
                Quartz.kCGMouseButtonLeft
            )
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, mouse_down)
            
            time.sleep(duration)
            
            mouse_up = Quartz.CGEventCreateMouseEvent(
                None, 
                Quartz.kCGEventLeftMouseUp, 
                (x, y), 
                Quartz.kCGMouseButtonLeft
            )
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, mouse_up)
            
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_mouse_left_down(handle, x, y, delay=0.001):
        try:
            event = Quartz.CGEventCreateMouseEvent(
                None, 
                Quartz.kCGEventLeftMouseDown, 
                (x, y), 
                Quartz.kCGMouseButtonLeft
            )
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
            time.sleep(delay)
        except Exception:
            pass

    def simulate_mouse_left_up(handle, x, y, delay=0.001):
        try:
            event = Quartz.CGEventCreateMouseEvent(
                None, 
                Quartz.kCGEventLeftMouseUp, 
                (x, y), 
                Quartz.kCGMouseButtonLeft
            )
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
            time.sleep(delay)
        except Exception:
            pass

else:
    def fake_activate_window(hwnd):
        try:
            win32gui.SendMessage(hwnd, win32con.WM_ACTIVATE, win32con.WA_ACTIVE, 0)
        except Exception as e:
            print(e)

    def simulate_key_press_hold(handle, vk_code, duration):
        try:
            win32gui.PostMessage(handle, win32con.WM_KEYDOWN, vk_code, 0)
            time.sleep(duration)
            win32gui.PostMessage(handle, win32con.WM_KEYUP, vk_code, 0)
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_key_down(handle, vk_code):
        try:
            win32gui.PostMessage(handle, win32con.WM_KEYDOWN, vk_code, 0)
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_key_up(handle, vk_code):
        try:
            win32gui.PostMessage(handle, win32con.WM_KEYUP, vk_code, 0)
        except Exception as e:
            print(e)
            time.sleep(1)

    def MAKELONG(lowimport time
import threading
import sys

if sys.platform == "darwin":
    import Quartz
    from AppKit import NSWorkspace, NSRunningApplication
else:
    import win32gui
    import win32con
    import win32api


VK_CODES = {
    'F2': 0x71,
    'Q': 0x51,
    'E': 0x45,
    'R': 0x52,
    'F': 0x46,
    'X': 0x58,
    'T': 0x54,
    'M': 0x4D,
    '1': 0x31,
    '2': 0x32,
    '3': 0x33,
    '4': 0x34,
    'LEFT_SHIFT': 0xA0,
    'SPACE': 0x20,
    'MIDDLE_MOUSE': 0x04,
    'W': 0x57,
    'A': 0x41,
    'S': 0x53,
    'D': 0x44,
    'ESC': 0x1B,
    'ALT': 0xA4,
    'TAB': 0x09,
}

if sys.platform == "darwin":
    MAC_KEY_MAP = {
        0x71: 120,  
        0x51: 12,   
        0x45: 14,   
        0x52: 15,   
        0x46: 3,    
        0x58: 7,    
        0x54: 17,   
        0x4D: 46,   
        0x31: 18,   
        0x32: 19,   
        0x33: 20,   
        0x34: 21,   
        0xA0: 56,   
        0x20: 49,   
        0x57: 13,   
        0x41: 0,    
        0x53: 1,    
        0x44: 2,    
        0x1B: 53,   
        0xA4: 58,   
        0x09: 48,   
    }

    def fake_activate_window(hwnd):
        try:
            ws = NSWorkspace.sharedWorkspace()
            app = NSRunningApplication.runningApplicationWithProcessIdentifier_(hwnd)
            if app:
                ws.launchApplicationWithBundleIdentifier_options_additionalEventParamDescriptor_launchIdentifier_(
                    app.bundleIdentifier(), 0, None, None)
                return True
        except Exception as e:
            print(e)
        return False

    def simulate_key_press_hold(handle, vk_code, duration):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            
            down_event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, True)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, down_event)
            
            time.sleep(duration)
            
            up_event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, False)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, up_event)
            
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_key_down(handle, vk_code):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, True)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_key_up(handle, vk_code):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, False)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_mouse_left_click_hold(handle, x, y, duration):
        try:
            mouse_down = Quartz.CGEventCreateMouseEvent(
                None, 
                Quartz.kCGEventLeftMouseDown, 
                (x, y), 
                Quartz.kCGMouseButtonLeft
            )
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, mouse_down)
            
            time.sleep(duration)
            
            mouse_up = Quartz.CGEventCreateMouseEvent(
                None, 
                Quartz.kCGEventLeftMouseUp, 
                (x, y), 
                Quartz.kCGMouseButtonLeft
            )
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, mouse_up)
            
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_mouse_left_down(handle, x, y, delay=0.001):
        try:
            event = Quartz.CGEventCreateMouseEvent(
                None, 
                Quartz.kCGEventLeftMouseDown, 
                (x, y), 
                Quartz.kCGMouseButtonLeft
            )
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
            time.sleep(delay)
        except Exception:
            pass

    def simulate_mouse_left_up(handle, x, y, delay=0.001):
        try:
            event = Quartz.CGEventCreateMouseEvent(
                None, 
                Quartz.kCGEventLeftMouseUp, 
                (x, y), 
                Quartz.kCGMouseButtonLeft
            )
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
            time.sleep(delay)
        except Exception:
            pass

else:
    def fake_activate_window(hwnd):
        try:
            win32gui.SendMessage(hwnd, win32con.WM_ACTIVATE, win32con.WA_ACTIVE, 0)
        except Exception as e:
            print(e)

    def simulate_key_press_hold(handle, vk_code, duration):
        try:
            win32gui.PostMessage(handle, win32con.WM_KEYDOWN, vk_code, 0)
            time.sleep(duration)
            win32gui.PostMessage(handle, win32con.WM_KEYUP, vk_code, 0)
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_key_down(handle, vk_code):
        try:
            win32gui.PostMessage(handle, win32con.WM_KEYDOWN, vk_code, 0)
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_key_up(handle, vk_code):
        try:
            win32gui.PostMessage(handle, win32con.WM_KEYUP, vk_code, 0)
        except Exception as e:
            print(e)
            time.sleep(1)

    def MAKELONG(low, high):
        return (high << 16) | (low & 0ximport time
import threading
import sys

if sys.platform == "darwin":
    import Quartz
    from AppKit import NSWorkspace, NSRunningApplication
else:
    import win32gui
    import win32con
    import win32api


VK_CODES = {
    'F2': 0x71,
    'Q': 0x51,
    'E': 0x45,
    'R': 0x52,
    'F': 0x46,
    'X': 0x58,
    'T': 0x54,
    'M': 0x4D,
    '1': 0x31,
    '2': 0x32,
    '3': 0x33,
    '4': 0x34,
    'LEFT_SHIFT': 0xA0,
    'SPACE': 0x20,
    'MIDDLE_MOUSE': 0x04,
    'W': 0x57,
    'A': 0x41,
    'S': 0x53,
    'D': 0x44,
    'ESC': 0x1B,
    'ALT': 0xA4,
    'TAB': 0x09,
}

if sys.platform == "darwin":
    MAC_KEY_MAP = {
        0x71: 120,  
        0x51: 12,   
        0x45: 14,   
        0x52: 15,   
        0x46: 3,    
        0x58: 7,    
        0x54: 17,   
        0x4D: 46,   
        0x31: 18,   
        0x32: 19,   
        0x33: 20,   
        0x34: 21,   
        0xA0: 56,   
        0x20: 49,   
        0x57: 13,   
        0x41: 0,    
        0x53: 1,    
        0x44: 2,    
        0x1B: 53,   
        0xA4: 58,   
        0x09: 48,   
    }

    def fake_activate_window(hwnd):
        try:
            ws = NSWorkspace.sharedWorkspace()
            app = NSRunningApplication.runningApplicationWithProcessIdentifier_(hwnd)
            if app:
                ws.launchApplicationWithBundleIdentifier_options_additionalEventParamDescriptor_launchIdentifier_(
                    app.bundleIdentifier(), 0, None, None)
                return True
        except Exception as e:
            print(e)
        return False

    def simulate_key_press_hold(handle, vk_code, duration):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            
            down_event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, True)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, down_event)
            
            time.sleep(duration)
            
            up_event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, False)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, up_event)
            
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_key_down(handle, vk_code):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, True)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_key_up(handle, vk_code):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, False)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_mouse_left_click_hold(handle, x, y, duration):
        try:
            mouse_down = Quartz.CGEventCreateMouseEvent(
                None, 
                Quartz.kCGEventLeftMouseDown, 
                (x, y), 
                Quartz.kCGMouseButtonLeft
            )
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, mouse_down)
            
            time.sleep(duration)
            
            mouse_up = Quartz.CGEventCreateMouseEvent(
                None, 
                Quartz.kCGEventLeftMouseUp, 
                (x, y), 
                Quartz.kCGMouseButtonLeft
            )
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, mouse_up)
            
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_mouse_left_down(handle, x, y, delay=0.001):
        try:
            event = Quartz.CGEventCreateMouseEvent(
                None, 
                Quartz.kCGEventLeftMouseDown, 
                (x, y), 
                Quartz.kCGMouseButtonLeft
            )
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
            time.sleep(delay)
        except Exception:
            pass

    def simulate_mouse_left_up(handle, x, y, delay=0.001):
        try:
            event = Quartz.CGEventCreateMouseEvent(
                None, 
                Quartz.kCGEventLeftMouseUp, 
                (x, y), 
                Quartz.kCGMouseButtonLeft
            )
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
            time.sleep(delay)
        except Exception:
            pass

else:
    def fake_activate_window(hwnd):
        try:
            win32gui.SendMessage(hwnd, win32con.WM_ACTIVATE, win32con.WA_ACTIVE, 0)
        except Exception as e:
            print(e)

    def simulate_key_press_hold(handle, vk_code, duration):
        try:
            win32gui.PostMessage(handle, win32con.WM_KEYDOWN, vk_code, 0)
            time.sleep(duration)
            win32gui.PostMessage(handle, win32con.WM_KEYUP, vk_code, 0)
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_key_down(handle, vk_code):
        try:
            win32gui.PostMessage(handle, win32con.WM_KEYDOWN, vk_code, 0)
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_key_up(handle, vk_code):
        try:
            win32gui.PostMessage(handle, win32con.WM_KEYUP, vk_code, 0)
        except Exception as e:
            print(e)
            time.sleep(1)

    def MAKELONG(low, high):
        return (high << 16) | (low & 0xFFFF)

    def simulate_mouse_left_click_hold(handle, x, y,import time
import threading
import sys

if sys.platform == "darwin":
    import Quartz
    from AppKit import NSWorkspace, NSRunningApplication
else:
    import win32gui
    import win32con
    import win32api


VK_CODES = {
    'F2': 0x71,
    'Q': 0x51,
    'E': 0x45,
    'R': 0x52,
    'F': 0x46,
    'X': 0x58,
    'T': 0x54,
    'M': 0x4D,
    '1': 0x31,
    '2': 0x32,
    '3': 0x33,
    '4': 0x34,
    'LEFT_SHIFT': 0xA0,
    'SPACE': 0x20,
    'MIDDLE_MOUSE': 0x04,
    'W': 0x57,
    'A': 0x41,
    'S': 0x53,
    'D': 0x44,
    'ESC': 0x1B,
    'ALT': 0xA4,
    'TAB': 0x09,
}

if sys.platform == "darwin":
    MAC_KEY_MAP = {
        0x71: 120,  
        0x51: 12,   
        0x45: 14,   
        0x52: 15,   
        0x46: 3,    
        0x58: 7,    
        0x54: 17,   
        0x4D: 46,   
        0x31: 18,   
        0x32: 19,   
        0x33: 20,   
        0x34: 21,   
        0xA0: 56,   
        0x20: 49,   
        0x57: 13,   
        0x41: 0,    
        0x53: 1,    
        0x44: 2,    
        0x1B: 53,   
        0xA4: 58,   
        0x09: 48,   
    }

    def fake_activate_window(hwnd):
        try:
            ws = NSWorkspace.sharedWorkspace()
            app = NSRunningApplication.runningApplicationWithProcessIdentifier_(hwnd)
            if app:
                ws.launchApplicationWithBundleIdentifier_options_additionalEventParamDescriptor_launchIdentifier_(
                    app.bundleIdentifier(), 0, None, None)
                return True
        except Exception as e:
            print(e)
        return False

    def simulate_key_press_hold(handle, vk_code, duration):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            
            down_event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, True)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, down_event)
            
            time.sleep(duration)
            
            up_event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, False)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, up_event)
            
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_key_down(handle, vk_code):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, True)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_key_up(handle, vk_code):
        try:
            mac_key_code = MAC_KEY_MAP.get(vk_code, vk_code)
            event = Quartz.CGEventCreateKeyboardEvent(None, mac_key_code, False)
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_mouse_left_click_hold(handle, x, y, duration):
        try:
            mouse_down = Quartz.CGEventCreateMouseEvent(
                None, 
                Quartz.kCGEventLeftMouseDown, 
                (x, y), 
                Quartz.kCGMouseButtonLeft
            )
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, mouse_down)
            
            time.sleep(duration)
            
            mouse_up = Quartz.CGEventCreateMouseEvent(
                None, 
                Quartz.kCGEventLeftMouseUp, 
                (x, y), 
                Quartz.kCGMouseButtonLeft
            )
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, mouse_up)
            
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_mouse_left_down(handle, x, y, delay=0.001):
        try:
            event = Quartz.CGEventCreateMouseEvent(
                None, 
                Quartz.kCGEventLeftMouseDown, 
                (x, y), 
                Quartz.kCGMouseButtonLeft
            )
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
            time.sleep(delay)
        except Exception:
            pass

    def simulate_mouse_left_up(handle, x, y, delay=0.001):
        try:
            event = Quartz.CGEventCreateMouseEvent(
                None, 
                Quartz.kCGEventLeftMouseUp, 
                (x, y), 
                Quartz.kCGMouseButtonLeft
            )
            Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
            time.sleep(delay)
        except Exception:
            pass

else:
    def fake_activate_window(hwnd):
        try:
            win32gui.SendMessage(hwnd, win32con.WM_ACTIVATE, win32con.WA_ACTIVE, 0)
        except Exception as e:
            print(e)

    def simulate_key_press_hold(handle, vk_code, duration):
        try:
            win32gui.PostMessage(handle, win32con.WM_KEYDOWN, vk_code, 0)
            time.sleep(duration)
            win32gui.PostMessage(handle, win32con.WM_KEYUP, vk_code, 0)
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_key_down(handle, vk_code):
        try:
            win32gui.PostMessage(handle, win32con.WM_KEYDOWN, vk_code, 0)
        except Exception as e:
            print(e)
            time.sleep(1)

    def simulate_key_up(handle, vk_code):
        try:
            win32gui.PostMessage(handle, win32con.WM_KEYUP, vk_code, 0)
        except Exception as e:
            print(e)
            time.sleep(1)

    def MAKELONG(low, high):
        return (high << 16) | (low & 0xFFFF)

    def simulate_mouse_left_click_hold(handle, x, y, duration):
        try:
            win3