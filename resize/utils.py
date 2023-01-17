import os
import secrets
import time
import platform
from PIL import Image

from resize.settings import path_to_user_image, RESOLUTIONS_LIST


def get_timestamp_file(path: str) -> float:
    
    """ 
    Функция getctime() модуля os.path возвращает системное время ctime,
    которое в некоторых системах, например Unix, 
    является временем последнего изменения метаданных, 
    а в Windows - временем создания файла или каталога, 
    указанномого в path. Возвращаемое значение представляет 
    собой число с плавающей запятой, указывающее количество
    секунд с начала эпохи Unix
    """
    
    if platform.system() == 'Windows':
        return os.path.getctime(path)
    else:
        print('что-то пошло не так')


def image_resize(img:object, image_size:str) -> str:
    """
    Args:
        img (object): Объект изображения с формы загрузки
        image_size (str): Размер изображения в формате строки 

    Returns:
        str: Сгенерированное имя файла
    """
    resolution = RESOLUTIONS_LIST[image_size]
    random_hex = secrets.token_hex(16)
    _, f_ext = os.path.splitext(img.filename)
    picture_fn = str(random_hex) + f_ext

    path = os.path.join(path_to_user_image(), picture_fn)
    i = Image.open(img)
    i.thumbnail(resolution, Image.ANTIALIAS)
    i.save(path)
    return picture_fn



def delete_old_files():
    """ Удаляет старые файлы, дата создания которых более 5-ти минут

    Returns:
        _type_: _description_
    """
    while True:
        all_files = os.listdir(path_to_user_image())
        current_time = time.time()
        print()
        print('Ожидаю следующей проверки...')
        print()

        for i in (all_files)[:-1]:
            full_path_to_image = path_to_user_image() + '/' + i
            get_time = get_timestamp_file(full_path_to_image)
            if int(str(current_time).split('.')[0]) - (60 * 5) > int(str(get_time).split('.')[0]):
                print(f'Файл {i} устарел, можно удалить')
                os.unlink(full_path_to_image)
            else:
                print(f'Файл {i} был создан менее пяти минут назад')

        print()
        time.sleep(0.1)
        return 'Удалён'
# https://www.cy-pr.com/tools/time/
