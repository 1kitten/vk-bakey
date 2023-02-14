from vkwave.bots.utils.keyboards.keyboard import Keyboard, ButtonColor
from database.get_all_sections import get_sections_from_database


def get_section_keyboard() -> Keyboard:
    """
    Функция для создания клавиатуры.
    Возвращает клавиатуру, где каждая кнопка - это раздел.
    Размер клавиатуры 3x1 (3 кнопки на 1 ряд).
    :return: Клавиатура (Keyboard)
    """
    section_keyboard = Keyboard(one_time=True)

    all_sections = get_sections_from_database()

    buttons_added: int = 0

    for i_section in all_sections:
        if buttons_added != 0 and buttons_added % 3 == 0:
            section_keyboard.add_row()
        section_keyboard.add_text_button(text=i_section[0], color=ButtonColor.POSITIVE)
        buttons_added += 1

    return section_keyboard
