import os
import sys
import logging
import argparse

LOG_FORMAT = '%(asctime)s - %(message)s'
logging.basicConfig(filename="file_data.txt", level=logging.INFO,format=LOG_FORMAT, encoding="UTF-8")


def get_file_date(path):
    file_dates =[]
    for parents_dir, dirs, files in os.walk(path):
        parent_directory = os.path.basename(os.path.normpath(parents_dir))
        for i in dirs + files:
            full_path = os.path.join(parents_dir, i)
            this_directory = os.path.isdir(full_path)
            file_name, extension = os.path.splitext(i)
        
            logging.info(f"Имя: {file_name}, расширение: {extension if not this_directory else 'папка'}, флаг каталога: {this_directory}, родительская директоря: {parent_directory}" )
    return file_dates
        

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Directory path')
    parser.add_argument('path', type=str, help='Path to the directory')
    args = parser.parse_args()
    logging.info('Программа запущена!')

    if os.path.isdir(args.path):
        files_info = get_file_date(args.path)
        for file_info in files_info:
            print(file_info)  

    else:
        print('Путь не найден')
        logging.warning('Путь не найден')
        
    logging.info('Завершение работы!\n_________________________')

    


# parser = argparse.ArgumentParser(description='Find date')
# parser.add_argument('-date', metavar='date', type=str, nargs='*', help='Enter a number of weekday in month')


# # Введите ваше решение ниже
# import json
# import csv
# import pickle
# import os

# def traverse_directory(directory):
#     result = []
#     for root, dirs, files in os.walk(directory):
#         for name in files:
#             path = os.path.join(root,name)
#             size = os.path.getsize(path)
#             result.append({'Path': path, 'Type': 'File', 'Size' : size})
#         for name in dirs:
#             path = os.path.join(root,name)
#             result.append({'Path': path, 'Type': 'Directory'})
#     return result




