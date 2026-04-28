import time
import threading
from Quartz import CGEventCreateMouseEvent, CGEventPost, CGEventCreateKeyboardEvent
from Quartz import kCGEventMouseDown, kCGEventMouseUp, kCGEventLeftMouseDown, kCGEventLeftMouseUp
from Quartz import kCGEventKeyDown, kCGEventKeyUp, kCGHIDEventTap
from AppKit import NSWorkspace, NSRunningApplication


def get_window_id(app_name):
    """Get the window ID for an application by name."""
    workspace = NSWorkspace.sharedWorkspace()
    apps = workspace.runningApplications()
    for app in apps:
        if app.localizedName() == app_name:
            return app.processIdentifier()
    return None


def fake_activate_window(bundle_identifier):
    """Activate a background application."""
    try:
        workspace = NSWorkspace.sharedWorkspace()
        app = workspace.launchApplicationWithBundleIdentifier_options_additionalEventParamDescriptor_launchIdentifier_(
            bundle_identifier, 0, None, None
        )
        if app:
            app.activateWithOptions_(1)
    except Exception as e:
        print(e)


def simulate_key_press_hold(vk_code, duration):
    """
    Simulates pressing and holding a key for a specified duration

    Args:
        vk_code: Virtual key code of the key to press
        duration: How long to hold the key (in seconds)
    """
    try:
        key_down = CGEventCreateKeyboardEvent(None, vk_code, True)
        CGEventPost(kCGHIDEventTap, key_down)
        time.sleep(duration)
        key_up = CGEventCreateKeyboardEvent(None, vk_code, False)
        CGEventPost(kCGHIDEventTap, key_up)
    except Exception as e:
        print(e)
        time.sleep(1)


def simulate_key_down(vk_code):
    """
    Simulates pressing a key down (without releasing)

    Args:
        vk_code: Virtual key code of the key to press down
    """
    try:
        key_down = CGEventCreateKeyboardEvent(None, vk_code, True)
        CGEventPost(kCGHIDEventTap, key_down)
    except Exception as e:
        print(e)
        time.sleep(1)


def simulate_key_up(vk_code):
    """
    Simulates releasing a key

    Args:
        vk_code: Virtual key code of the key to release
    """
    try:
        key_up = CGEventCreateKeyboardEvent(None, vk_code, False)
        CGEventPost(kCGHIDEventTap, key_up)
    except Exception as e:
        print(e)
        time.sleep(1)


def simulate_mouse_left_click_hold(x, y, duration):
    """
    Simulates pressing and holding the left mouse button for a specified duration

    Args:
        x: X coordinate for the mouse event
        y: Y coordinate for the mouse event
        duration: How long to hold the mouse button (in seconds)
    """
    try:
        mouse_down = CGEventCreateMouseEvent(None, kCGEventLeftMouseDown, (x, y), 0)
        CGEventPost(kCGHIDEventTap, mouse_down)
        time.sleep(duration)
        mouse_up = CGEventCreateMouseEvent(None, kCGEventLeftMouseUp, (x, y), 0)
        CGEventPost(kCGHIDEventTap, mouse_up)
    except Exception as e:
        print(e)
        time.sleep(1)


def simulate_mouse_left_down(x, y, delay=0.001):
    """
    Simulates pressing down the left mouse button (without releasing)

    Args:
        x: X coordinate for the mouse event
        y: Y coordinate for the mouse event
        delay: Short delay after the action (in seconds)
    """
    try:
        mouse_down = CGEventCreateMouseEvent(None, kCGEventLeftMouseDown, (x, y), 0)
        CGEventPost(kCGHIDEventTap, mouse_down)
        time.sleep(delay)
    except Exception:
        pass


def simulate_mouse_left_up(x, y, delay=0.001):
    """
    Simulates releasing the left mouse button

    Args:
        x: X coordinate for the mouse event
        y: Y coordinate for the mouse event
        delay: Short delay after the action (in seconds)
    """
    try:
        mouse_up = CGEventCreateMouseEvent(None, kCGEventLeftMouseUp, (x, y), 0)
        CGEventPost(kCGHIDEventTap, mouse_up)
        time.sleep(delay)
    except Exception:
        pass
