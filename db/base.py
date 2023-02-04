import sqlite3
from pathlib import Path

DB_NAME = 'db.sqlite3'
MAIN_PATH = Path(__file__).parent.parent
connection = sqlite3.connect(MAIN_PATH / DB_NAME)
cur = connection.cursor()


def create_tables():
    """
    Для создания таблиц 'Товары'
    и 'Заказы' в БД.
    """

    cur.execute(
        """CREATE TABLE products (
            products_id INTEGER PRIMARY KEY,
            name TEXT,
            descr TEXT,
            price INTEGER,
            photo TEXT
        )"""
    )

    cur.execute(
        """CREATE TABLE IF NOT EXISTS orders(
            order_id INTEGER PRIMARY KEY,
            user_name TEXT,
            address TEXT,
            week_day TEXT,
            product_id INTEGER,
            FOREIGN KEY (product_id)
            REFERENCES products (product_id)
            ON DELETE CASCADE
        )"""
    )


def populate_products():
    """
    Заполняем таблицу товаров
    """
    cur.execute("""INSERT INTO products (
        name,
        descr,
        price,
        photo
    ) VALUES
    ('Книга 1', 'Фантастика', 200, './images/dog.png')
    ('Книга 1', 'Триллер', 300, './images/iphone.jpg')
    """)


def get_products():
    """
    Доставляем товары из таблицы, по страницам
    """
    cur.execute("""
    SELECT * FROM products
    """)


def create_order():
    """
    Создаем заказ
    """
    cur.execute("""INSERT INTO orders (
    user_name,
    address,
    week_day,
    """)


connection.commit()
connection.close()
create_tables()
populate_products()
