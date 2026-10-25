#!/usr/bin/env python3
import os
import sys

def read_rpf(filepath):
    with open(filepath, 'rb') as f:
        magic = f.read(4)
        if magic != b'RPF2':
            print(f'[SAINTS] НЕ RPF2: {filepath}')
            return
        
        f.seek(0)
        data = f.read()
        
        print(f'[SAINTS] ФАЙЛ: {filepath}')
        print(f'[SAINTS] РАЗМЕР: {len(data)} байт')
        print(f'[SAINTS] СИГНАТУРА: {magic}')
        
        # Ищем все строки
        strings_found = []
        current = b''
        for byte in data:
            if 32 <= byte < 127:
                current += bytes([byte])
            else:
                if len(current) >= 4:
                    strings_found.append(current.decode('ascii', errors='ignore'))
                current = b''
        
        print(f'[SAINTS] НАЙДЕНО СТРОК: {len(strings_found)}')
        for s in strings_found[:30]:
            print(f'  {s}')
        
        # Ищем хеши
        import re
        hashes = re.findall(rb'[0-9a-f]{40,}', data)
        print(f'[SAINTS] НАЙДЕНО ХЕШЕЙ: {len(hashes)}')
        for h in hashes[:10]:
            print(f'  {h.decode()}')

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Использование: rpf_extract.py <файл>')
        sys.exit(1)
    
    read_rpf(sys.argv[1])
