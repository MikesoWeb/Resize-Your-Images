import os

from flask import current_app, flash, redirect, render_template, request, send_from_directory, url_for

from resize import app_ctx
from resize.forms import UploadImgForm
from resize.utils import delete_old_files, image_resize
from resize.settings import path_to_user_image


@app_ctx.errorhandler(413)
def request_entity_too_large(error):
    flash('HTTP 413 Payload Too Large - объект слишком большой')
    return redirect(url_for('index')), 302


@app_ctx.errorhandler(404)
def error_404(error):
    flash('HTTP 404 или Not Found - запрошенный ресурс не существует')
    return redirect(url_for('index')), 302


@app_ctx.errorhandler(403)
def error_403(error):
    flash('HTTP 403 Forbidden - доступ к запрошенному ресурсу запрещен')
    return redirect(url_for('index')), 302


@app_ctx.errorhandler(500)
def error_500(error):
    flash('HTTP 500 (Internal Server Error) - внутренняя проблема сервера')
    return redirect(url_for('index')), 302


@app_ctx.route('/', methods=['GET', 'POST'])
def index():
    form = UploadImgForm()
    delete_old_files()
    if request.method == 'GET':
       return render_template('resize/index.html', form=form) 
    if form.validate_on_submit():
        image_size = form.size_image.data
        image_file = url_for(
            'static', filename=f'images/{image_resize(form.picture.data, image_size)}')
        return render_template('resize/resize.html', form=form, image_file=image_file)
    
    return render_template('resize/index.html', form=form)


@app_ctx.route('/resize')
def resize():
    return render_template('resize/resize.html')


@app_ctx.route('/<string:filename>', methods=['GET'])
def download(filename):
    uploads = os.path.join(current_app.root_path, path_to_user_image())
    return send_from_directory(directory=uploads, path=filename)
