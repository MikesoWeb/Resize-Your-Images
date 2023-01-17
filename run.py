from resize import app_ctx
from resize.routes import index
from resize.settings import is_exists_path_to_images

if __name__ == '__main__':
    is_exists_path_to_images()
    with app_ctx.app_context():
        app_ctx.run(port=5050, debug=True)
    
    
            
# E:\Mass_resize_image_Python\img