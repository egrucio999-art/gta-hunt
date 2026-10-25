#!/usr/bin/env python3
import os
import sys

def search_strings(base_dir, search_text):
    results = []
    
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            filepath = os.path.join(root, file)
            
            try:
                with open(filepath, 'rb') as f:
                    data = f.read()
                
                if search_text.encode() in data:
                    results.append(filepath)
            except:
                pass
    
    return results

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Использование: string_search.py <путь> <текст>')
        sys.exit(1)
    
    base_dir = sys.argv[1]
    search_text = sys.argv[2]
    
    print(f'[SAINTS] ПОИСК ТЕКСТА: {search_text}')
    
    results = search_strings(base_dir, search_text)
    
    for result in results:
        print(f'[+] {result}')
    
    print(f'[SAINTS] НАЙДЕНО: {len(results)}')
