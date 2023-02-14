import sqlite3 as sq
import os
from bot_config import ROOT_DIR


def get_sections_from_database():
    with sq.connect(os.path.join(ROOT_DIR, 'bakey.db')) as conn:
        cur = conn.cursor()
        cur.execute(
            """
            SELECT name FROM `sections`
            """
        )
        result = cur.fetchall()
    return result
