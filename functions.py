import json


def load_posts_from_json():
    with open('posts.json', 'r', encoding='utf-8') as file:
        posts = json.load(file)
        return posts


def search_post(key_search):
    posts = load_posts_from_json()
    find_list_posts = []
    for post in posts:
        if key_search in post['content']:
            find_list_posts.append(post)
    return find_list_posts


def add_post(pic, cont):
    try:
        with open('posts.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        data.append({'pic': pic, 'content': cont})
        with open('posts.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False)
    except FileNotFoundError:
        # Будет выполнено, если файл не найден
        print("Файл не найден")
    except JSONDecodeError:
        # Будет выполнено, если файл найден, но не превращается из JSON
        print("Файл не удается преобразовать")
