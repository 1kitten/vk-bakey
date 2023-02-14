import os.path
import sqlite3 as sq
from bot_config import ROOT_DIR


def get_products_from_current_section(section: str):
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
