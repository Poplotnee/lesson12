from flask import Blueprint, render_template, request
from functions import search_post
import logging
from json import JSONDecodeError

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')

logging.basicConfig(filename="basic.log", level=logging.INFO)


@main_blueprint.route('/')
def main_page():
    return render_template('index.html')


@main_blueprint.route('/search')
def search_page():
    key_search = request.args.get("s")
    logging.info('Search in progress')
    try:
        posts = search_post(key_search)
    except FileNotFoundError:
        logging.error(f'{POST_PATH} not found')
        return 'Файл не найден'

    except JSONDecodeError:
        return "Невалидный файл"
    return render_template('post_list.html', posts=posts, key_search=key_search)
