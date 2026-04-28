import numpy as np
import cv2
import os
from PIL import Image
import time
import logging

logger = logging.getLogger(__name__)


def template_matching_in_region(background_image_data, search_region, template_path, min_similarity):
    if not os.path.exists(template_path):
        error_message = f"模板图片文件不存在: {template_path}"
        print(error_message)
        return False, 0, 0, 0

    background_image = cv2.imdecode(np.frombuffer(background_image_data, dtype=np.uint8), cv2.IMREAD_COLOR)

    try:
        with Image.open(template_path) as img:
            template_image = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
    except Exception as e:
        error_message = f"模板图片加载失败: {template_path}, 错误信息: {e}"
        print(error_message)
        return False, 0, 0, 0

    if background_image is None or template_image is None:
        error_message = f"图片加载失败，可能路径中有问题: {template_path}"
        print(error_message)
        return False, 0, 0, 0

    x, y, width, height = search_region
    region_image = background_image[y:y + height, x:x + width]

    if template_image.shape[0] > region_image.shape[0] or template_image.shape[1] > region_image.shape[1]:
        print(f"警告: 模板尺寸必须小于或等于限定区域尺寸,路径：{str(template_path)}")
        time.sleep(2)
        is_matched, max_val, matched_x, matched_y = (False, 0, 0, 0)
    else:
        match_result = cv2.matchTemplate(region_image, template_image, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(match_result)
        matched_x = max_loc[0] + x
        matched_y = max_loc[1] + y
        is_matched = max_val >= min_similarity

    path_part = str(template_path)
    if "图片" in path_part:
        path_parts = path_part.split("图片")
        extracted_content = path_parts[1] if path_parts else template_path
    else:
        extracted_content = template_path

    if is_matched:
        logger.info(
            f"路径：{extracted_content},模板: {template_image.shape},限定: {region_image.shape},"
            f"匹配: {is_matched},相似: {max_val:.4f},坐标: ({matched_x}, {matched_y})")
    else:
        logger.debug(
            f"路径：{extracted_content},模板: {template_image.shape},限定: {region_image.shape},"
            f"匹配: {is_matched},相似: {max_val:.4f},坐标: ({matched_x}, {matched_y})")

    return is_matched, max_val, matched_x, matched_y
