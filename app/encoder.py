#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File  : encoder.py
# Author: DaShenHan&道长-----先苦后甜，任凭晚风拂柳颜------
# Date  : 2024/5/29

import gzip
import base64
import os
from pathlib import Path
import shutil


def compress_and_encode(data):
    # 压缩数据
    compressed_data = gzip.compress(data.encode('utf-8'))
    # 对压缩数据进行Base64编码
    encoded_data = base64.b64encode(compressed_data).decode('utf-8')
    return encoded_data


def decode_and_decompress(encoded_data):
    # 解码Base64数据
    decoded_data = base64.b64decode(encoded_data.encode('utf-8'))
    # 解压缩数据
    decompressed_data = gzip.decompress(decoded_data).decode('utf-8')
    return decompressed_data


def main():
    base_dir = './t4/files/drpy_js'
    files = [Path(os.path.join(base_dir, file)).as_posix() for file in os.listdir(base_dir)]
    print('=================获取待加密文件=========================')
    print(f'数量: {len(files)}')
    print(files)
    print('=================加密前准备目录=========================')
    out_dir = './dist/drpy_js'
    if os.path.exists(out_dir):
        print(f'=================删除已存在的目录: {out_dir}=========================')
        shutil.rmtree(out_dir)
    print(f'=================创建目录: {out_dir}=========================')
    os.makedirs(out_dir, exist_ok=True)
    print('=================开始加密=========================')
    for file in files:
        file_out_path = os.path.join(out_dir, os.path.basename(file))
        file_out_path = Path(file_out_path).as_posix()
        print('输出加密后的文件:', file_out_path)
        with open(file, encoding='utf-8') as f:
            file_content = f.read()
        with open(file_out_path, mode='w+', encoding='utf-8') as f:
            f.write(compress_and_encode(file_content))


if __name__ == '__main__':
    # 使用例子
    # original_data = "这是需要被加密的文本"
    # encoded_data = compress_and_encode(original_data)
    # print("加密后的数据:", encoded_data)
    #
    # decoded_data = decode_and_decompress(encoded_data)
    # print("解密后的数据:", decoded_data)
    #
    # encoded_data = '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'
    # decoded_data = decode_and_decompress(encoded_data)
    # print("解密后的筛选:", decoded_data)

    main()