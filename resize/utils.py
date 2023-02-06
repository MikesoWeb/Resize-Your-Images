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
    elif platform.system() == 'Unix':
        return os.path.getmtime(path)
    else:
        raise NotImplementedError("Функция не реализована для данной операционной системы.")


def lowercase_ext(filename: str) -> str:
    """Разделяет файл на имя и расширение 
    и для приводит расширение к нижнему регистру"""
    if '.' in filename:
        _, ext = os.path.splitext(filename)
        return ext.lower()
    """Если файл нельзя разбить на имя и расширение,
    вернуть входящий файл без изменений"""
    return filename


def random_hex_filename(ext):
    """Генерируем случайно имя для файла и 
    конкатерируем его с расширением"""
    random_hex = secrets.token_hex(16)
    picture_fn = str(random_hex) + ext
    return picture_fn

def image_resize(img: object, image_size: str) -> str:
    """
    Args:
        img (object): Объект изображения с формы загрузки
        image_size (str): Размер изображения в формате строки 

    Returns:
        str: Сгенерированное имя файла
    """
    # lowercase_ext(img)
    # print(lowercase_ext(img))
    
    resolution = RESOLUTIONS_LIST[image_size]
    f_ext = lowercase_ext(img.filename)
    p_name = random_hex_filename(f_ext)
    path = os.path.join(path_to_user_image(), p_name)
    i = Image.open(img)
    i.thumbnail(resolution, Image.ANTIALIAS)
    i.save(path)
    return p_name



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
