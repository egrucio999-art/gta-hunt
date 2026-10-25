# GTA V RPF Archive Reverse Engineering Toolkit

Инструментарий для реверс-инжиниринга проприетарных архивов RPF (Rockstar Package File) из игры Grand Theft Auto V.

## Описание проекта
Архивы RPF — это контейнеры, используемые Rockstar Games для хранения игровых ассетов. Формат закрытый, и для извлечения ресурсов требуется понимание структуры заголовков, работы с хеш-таблицами (Jenkins hash) и смещениями.

## Модули
| Скрипт | Назначение |
|---|---|
| rpf_extract.py | Базовый экстрактор архивов RPF |
| rpf_extract_full.py | Расширенный экстрактор |
| hash_search.py | Поиск файлов по хешам (Jenkins hash) |
| string_search.py | Поиск и извлечение строковых ресурсов |
| search.py | Поиск ассетов по маскам |

## Использование
python rpf_extract.py /path/to/archive.rpf -o /output/dir
