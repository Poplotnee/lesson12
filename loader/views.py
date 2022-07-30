from flask import Blueprint, render_template, request
from functions import add_post
import logging
from json import JSONDecodeError

loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder='templates')


@loader_blueprint.route('/post')
def page_post_form():
    return render_template('post_form.html')


@loader_blueprint.route('/post', methods=["POST"])
def page_post_upload():
    content = request.values.get('content')
    picture = request.files.get("picture")
    if not picture or not content:
        return 'Нет картинки или текста '
    if picture.filename.split('.')[-1] not in ['png', 'jpg', 'jpeg']:
        logging.info('Uploaded file is not an image')
        return 'Неверный формат картинки'
    if not picture or not content:
        return 'Нет картинки или текста'
    try:
        filename = picture.filename
        picture.save(fr"uploads/{filename}")
        add_post((fr"uploads/{filename}"), content)
    except FileNotFoundError:
        logging.info('file not found')
        return 'Файл не найден'
    except JSONDecodeError:
        return "Невалидный файл"
    return render_template('post_uploaded.html', picture=picture, content=content, filename=filename)