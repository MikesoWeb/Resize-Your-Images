
import os


BASEDIR = os.path.abspath(os.path.dirname(__file__))
USER_IMAGE_DIRECTORY = 'static/images'


def path_to_user_image():
    return os.path.join(BASEDIR, USER_IMAGE_DIRECTORY)


def is_exists_path_to_images():
    path_to_images = path_to_user_image()

    if not os.path.exists(path_to_images):
        os.mkdir(path_to_images)


RESOLUTIONS_LIST = {'small': (320, 240),
                    'medium': (480, 320),
                    'large': (720, 480)}
