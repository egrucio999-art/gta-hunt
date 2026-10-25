#!/usr/bin/env python3
import os
import sys
import json

def search_files(base_dir, keywords):
    results = []
    
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            filepath = os.path.join(root, file)
            filename_lower = file.lower()
            
            for keyword in keywords:
                if keyword.lower() in filename_lower:
                    results.append({
                        'file': filepath,
                        'keyword': keyword
                    })
    
    return results

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Использование: search.py <путь_к_сборке>')
        sys.exit(1)
    
    base_dir = sys.argv[1]
    keywords = ['easter', 'egg', 'ng_', 'arena', 'cc850', 'maze', 'koenigsegg', 'cube', 'secret', 'hidden']
    
    print(f'[SAINTS] ПОИСК В: {base_dir}')
    print(f'[SAINTS] КЛЮЧЕВЫЕ СЛОВА: {keywords}')
    
    results = search_files(base_dir, keywords)
    
    for result in results:
        print(f'[+] {result["keyword"]}: {result["file"]}')
    
    print(f'[SAINTS] НАЙДЕНО: {len(results)}')
