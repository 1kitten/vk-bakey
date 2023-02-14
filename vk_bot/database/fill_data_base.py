import os.path
import sqlite3 as sq
from bot_config import ROOT_DIR

CREATION_INSERT_SCRIPT: str = """
CREATE TABLE IF NOT EXISTS `sections` (
    name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS `products` (
    name TEXT NOT NULL,
    picture BLOB NOT NULL,
    section_id INTEGER NOT NULL,
    price INTEGER NOT NULL,
    description TEXT NOT NULL DEFAULT ''
);

INSERT INTO `sections` (name)
    VALUES 
        ('Сладкое'),
        ('Зарубежное'),
        ('Пироги'),
        ('Торты и пирожные');

INSERT INTO `products` (name, picture, section_id, price, description) 
    VALUES 
        ('Чизкейк ванильный', 'media/cheese_cake.jpg', 1, 299, 'Чизкейк - один из самых известных и любимых десертов мира.'),
        ('Корзинка миндальная', 'media/korzinka_2.jpg', 1, 150, 'Миндальная песочная корзинка с апельсиново-лимонным кремом, укутанная облаком из белкового крема.'),
        ('Гамбургер норвежский', 'media/hamburger.jpg', 2, 200, 'Блюдо, обычно состоящее из котлеты из измельченного мяса, как правило, говядины, помещенной внутрь нарезанной булочки.'),
        ('Американский хотдог', 'media/hot_dogs.jpg', 2, 300, 'Блюдо, состоящее из жареной или приготовленной на пару сосиски, подаваемой в разрезе булочки.'),
        ('Яблочный пирог', 'media/apple_pie.jpg', 3, 450, 'Один из самых распространённых разновидностей пирога, для начинения которого используются яблоки.'),
        ('Капустный пирог', 'media/kapusta.jpg', 3, 400, 'Пироги с капустой – традиционное угощение для семейного праздника.'),
        ('Красный бархат', 'media/red.jpg', 4, 690, 'Шоколадный торт тёмно-красного, ярко-красного или красно-коричневого цвета. Традиционно готовится как слоёный пирог с глазурью из сливочного сыра. '),
        ('Шоколадный торт', 'media/chocolate.jpg', 4, 900, 'Шоколадный торт или шоколадный гато - это торт, приправленный растопленным шоколадом, какао-порошком или тем и другим.')

"""


def create_and_fill_data_base() -> None:
    """
    Создаём базу данных для хранения информации о разделах и продуктах.
    Если база данных пустая, то наполняем её стартовой информацией.
    """
    with sq.connect(os.path.join(ROOT_DIR, 'bakey.db')) as conn:
        cur = conn.cursor()
        if not _check_if_data_base_empty():
            cur.executescript(CREATION_INSERT_SCRIPT)


def _check_if_data_base_empty() -> bool:
    """
    Проверяем, что база данных пуста.
    Возвращаем False, если она пустая и True, если нет.
    :return: bool
    """
    with sq.connect(os.path.join(ROOT_DIR, 'bakey.db')) as conn:
        cur = conn.cursor()
        try:
            cur.execute(
                """
                SELECT COUNT(*) FROM sections
                """
            )
        except sq.OperationalError:
            return False
        return True
