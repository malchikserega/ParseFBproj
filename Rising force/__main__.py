from app import app
from flask import render_template, request, Response
import db_functions

@app.route('/', methods=["GET", "POST"])
def some():
    """
    Функция возвращает главную страницу
    :rtype: Response
    :return: Главная страница
    """
    return render_template('base.html',
                           title='Main')

@app.route('/target_urls', methods=['GET', 'POST'])
def filtered():
    """
    Если метод GET:
        Функция возвращает страницу с отфильтрованными доменами
    Если метод POST:
        Два поля: Содержимое поля поиска и чекбокс
        Функция обновляет таблицу отфильтрованных доменов и
        возвращает страницу с доменами соответствующими поиску и
        отфильтрованными(которых нет в белом списке доменов) доменами
    :rtype: Response
    :return: Страницы
    """
    if request.method == 'POST':
        db_functions.update_target_urls(request.form['text'])
    return render_template('target_urls.html',
                           title='Цели',
                           target_urls=db_functions.show_targets()
                           )


@app.route('/img/<target>')
def show_photos(target):
    """
    Функция возвращает главную страницу
    :rtype: Response
    :return: Главная страница
    """
    return render_template('photos.html',
                           title='Main',
                           photos=db_functions.show_photos(target)
                           )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
