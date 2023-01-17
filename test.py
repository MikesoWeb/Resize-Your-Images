import os, datetime
import time


def get_timestamp_file(path):
    import platform, os
    if platform.system() == 'Windows':
        return os.path.getctime(path)
    else:
        print('что-то пошло не так')
        
path_to_images = os.getcwd() + '/resize/static/images'        



while True:
    all_files = os.listdir(path_to_images)
    current_time = time.time()
    print()
    print('Ожидаю следующей проверки...')
    print()
    
    for i in (all_files)[:-1]:
        full_path_to_image = path_to_images + '/' + i
        # print(full_path_to_image)
        get_time = get_timestamp_file(full_path_to_image)
        # print(get_time)
        
        if int(str(current_time).split('.')[0]) - (60 * 5) > int(str(get_time).split('.')[0]):
            print(f'Файл {i} устарел, можно удалить')
            os.unlink(full_path_to_image)
        else:
            print(f'Файл {i} был создан менее пяти минут назад')
    
    print()
    time.sleep(10)
# https://www.cy-pr.com/tools/time/

# Файл после скачивания удалять