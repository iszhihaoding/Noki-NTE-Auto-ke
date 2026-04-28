import sys
import os
import importlib.util

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

print("测试Mac兼容性修改...")

def import_module_from_file(file_name, module_name):
    try:
        file_path = os.path.join(os.path.dirname(__file__), file_name)
        spec = importlib.util.spec_from_file_location(module_name, file_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module, None
    except Exception as e:
        return None, str(e)

print("1. 测试 Backend Keyboard and Mouse.py...")
keyboard_mouse_module, error = import_module_from_file("Backend Keyboard and Mouse.py", "keyboard_mouse")
if keyboard_mouse_module:
    print("   ✓ 导入成功 - 键盘和鼠标模块")
else:
    print(f"   ✗ 导入失败: {error}")

print("2. 测试 Emulator ADB operations.py...")
adb_module, error = import_module_from_file("Emulator ADB operations.py", "adb_ops")
if adb_module:
    print("   ✓ 导入成功 - ADB操作模块")
else:
    print(f"   ✗ 导入失败: {error}")

print("3. 测试 Template Matching for Image Detection with OpenCV.py...")
template_module, error = import_module_from_file("Template Matching for Image Detection with OpenCV.py", "template_match")
if template_module:
    print("   ✓ 导入成功 - 模板匹配模块")
else:
    print(f"   ✗ 导入失败: {error}")

print("\n兼容性测试完成！")
print("\n注意事项：")
print("1. 需要安装 pyobjc 库: pip install pyobjc")
print("2. 需要安装 OpenCV: pip install opencv-python")
print("3. 需要安装 PIL: pip install pillow")
print("4. 需要安装 numpy: pip install numpy")
