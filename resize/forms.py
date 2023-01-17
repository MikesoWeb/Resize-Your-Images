from flask_uploads import IMAGES
from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from wtforms import FileField, SelectField, SubmitField
from resize.settings import RESOLUTIONS_LIST


class UploadImgForm(FlaskForm):
    picture = FileField('', validators=[
        FileAllowed(IMAGES, message=f'Только изображения формата {IMAGES}'),
        ])
    size_image = SelectField('', choices=[i for i in RESOLUTIONS_LIST])
    submit = SubmitField('Загрузить')
