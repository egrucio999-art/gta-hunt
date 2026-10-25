#!/usr/bin/env python3
import os
import sys
import json

def search_hashes(base_dir, hashes):
    results = []
    
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            filepath = os.path.join(root, file)
            filename_lower = file.lower()
            
            for hash_value in hashes:
                if hash_value.lower() in filename_lower:
                    results.append({
                        'file': filepath,
                        'hash': hash_value
                    })
    
    return results

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Использование: hash_search.py <путь> <хеш1,хеш2,...>')
        sys.exit(1)
    
    base_dir = sys.argv[1]
    hashes = sys.argv[2].split(',')
    
    print(f'[SAINTS] ПОИСК ХЕШЕЙ: {hashes}')
    
    results = search_hashes(base_dir, hashes)
    
    for result in results:
        print(f'[+] {result["hash"]}: {result["file"]}')
    
    print(f'[SAINTS] НАЙДЕНО: {len(results)}')
