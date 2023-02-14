import os.path
import sqlite3 as sq
from bot_config import ROOT_DIR


def get_products_from_current_section(section: str) -> sq.Cursor.fetchall:
    """
    Функция, которая отправляет запрос в базу данных, ищет все товары в конкретном разделе.
    :param section: str. Наименование раздела.
    :return: sq.Cursor.fetchall. Результат выполнения запроса, кортеж из товаров в разделе.
    """
    with sq.connect(os.path.join(ROOT_DIR, 'bakey.db')) as conn:
        cur = conn.cursor()
        cur.execute(
            """
            SELECT `products`.name, `products`.price, picture, description
            FROM `products`
            JOIN `sections` ON `sections`.ROWID = `products`.section_id
            WHERE `sections`.name = (?)
            """, (section,)
        )
        result = cur.fetchall()
    return result
