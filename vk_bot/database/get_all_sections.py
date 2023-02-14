import logging
import os
import sqlite3 as sq

from bot_config import ROOT_DIR

logger: logging.Logger = logging.getLogger('sections_log')


def get_sections_from_database() -> sq.Cursor.fetchall:
    """
    Функция которая отправлять запрос в базу данных, берёт всё имена разделов
    из таблицы sections.
    :return: sqlite3.Cursor.fetchall. Результат выполнения запроса
    """
    logger.info('Getting all the sections from database.')
    with sq.connect(os.path.join(ROOT_DIR, 'bakey.db')) as conn:
        cur: conn.cursor = conn.cursor()
        cur.execute(
            """
            SELECT name FROM `sections`
            """
        )
        result: cur.fetchall = cur.fetchall()
    return result
