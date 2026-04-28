import sys
import os
import time
import logging

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)


def main():
    print("=" * 50)
    print("         Noki-NTE-Auto Mac版")
    print("=" * 50)
    print("\n功能列表:")
    print("  1. 自动钓鱼")
    print("  2. 自动钢琴")
    print("  3. 退出")
    print("\n请输入选择: ", end="")

    try:
        choice = int(input())
        
        if choice == 1:
            logger.info("启动自动钓鱼功能...")
            start_fishing()
        elif choice == 2:
            logger.info("启动自动钢琴功能...")
            start_piano()
        elif choice == 3:
            logger.info("退出程序")
            sys.exit(0)
        else:
            print("无效选择，请输入1-3")
            main()
    except ValueError:
        print("请输入有效的数字")
        main()


def start_fishing():
    try:
        from Backend_Keyboard_and_Mouse import (
            simulate_key_press_hold,
            simulate_mouse_left_click_hold,
            simulate_mouse_left_down,
            simulate_mouse_left_up
        )
        from Template_Matching_for_Image_Detection_with_OpenCV import (
            template_matching_in_region
        )
        from Emulator_ADB_operations import (
            long_press,
            swipe,
            connect_emulator,
            get_all_device_ports
        )

        logger.info("自动钓鱼功能已启动")
        logger.info("按 Ctrl+C 停止")
        
        while True:
            time.sleep(1)
            logger.debug("钓鱼循环中...")
            
    except KeyboardInterrupt:
        logger.info("自动钓鱼已停止")


def start_piano():
    try:
        from Backend_Keyboard_and_Mouse import (
            simulate_key_press_hold
        )

        logger.info("自动钢琴功能已启动")
        logger.info("按 Ctrl+C 停止")
        
        while True:
            time.sleep(1)
            logger.debug("钢琴循环中...")
            
    except KeyboardInterrupt:
        logger.info("自动钢琴已停止")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logger.info("程序已退出")
        sys.exit(0)
