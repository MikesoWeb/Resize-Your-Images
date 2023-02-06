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
    
    Для Unix используется os.path.getmtime(path) для получения времени 
    последнего изменения метаданных.
    Добавлено исключение NotImplementedError, которое будет вызываться, 
    если функция вызывается на неподдерживаемой операционной системе.
    """
    
    if platform.system() == 'Windows':
        return os.path.getctime(path)
    elif platform.system() == 'Unix':
        return os.path.getmtime(path)
    else:
        raise NotImplementedError("Функция не реализована для данной операционной системы.")


def lowercase_ext(filename: str) -> str:
    if not filename or '.' not in filename:
        return filename

    _, ext = os.path.splitext(filename)
    return ext.lower()



def random_hex_filename(ext):

    """Функция, которая генерирует случайное имя файла и добавляет к нему расширение"""
    
    # Генерация 16-байтного случайного шестнадцатеричного числа
    random_hex = secrets.token_hex(16)
    # Создание имени файла из случайного шестнадцатеричного числа и расширения
    picture_fn = str(random_hex) + ext
    # Возврат созданного имени файла
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
