#!/usr/bin/env python3
import os
import sys
import struct

def extract_rpf(filepath, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    
    with open(filepath, 'rb') as f:
        data = f.read()
    
    magic = data[:4]
    print(f'[SAINTS] ФАЙЛ: {filepath}')
    print(f'[SAINTS] РАЗМЕР: {len(data)} байт')
    print(f'[SAINTS] СИГНАТУРА: {magic}')
    
    if magic != b'RPF2':
        print('[SAINTS] ЭТО НЕ RPF2')
        return
    
    # Ищем все строки, которые выглядят как имена файлов
    import re
    filenames = re.findall(rb'[a-zA-Z0-9_\-\.]+\.(?:ytd|ytf|yft|ymap|ymt|png|dds|txt|xml|meta|json)', data)
    
    print(f'[SAINTS] НАЙДЕНО ИМЁН ФАЙЛОВ: {len(filenames)}')
    
    for fn in filenames[:50]:
        print(f'  {fn.decode("ascii", errors="ignore")}')
    
    # Ищем PNG-файлы внутри
    png_positions = []
    pos = 0
    while True:
        pos = data.find(b'\x89PNG', pos)
        if pos == -1:
            break
        png_positions.append(pos)
        pos += 1
    
    print(f'[SAINTS] НАЙДЕНО PNG: {len(png_positions)}')
    
    for i, pos in enumerate(png_positions):
        # Ищем конец PNG (IEND)
        end = data.find(b'IEND', pos)
        if end != -1:
            end += 8
            png_data = data[pos:end]
            out_path = os.path.join(output_dir, f'extracted_{i}.png')
            with open(out_path, 'wb') as f:
                f.write(png_data)
            print(f'[SAINTS] ИЗВЛЕЧЁН PNG: {out_path} ({len(png_data)} байт)')

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Использование: rpf_extract_full.py <файл.rpf> <выходная_папка>')
        sys.exit(1)
    
    extract_rpf(sys.argv[1], sys.argv[2])
