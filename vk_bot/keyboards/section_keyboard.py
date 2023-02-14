from vkwave.bots.utils.keyboards.keyboard import Keyboard, ButtonColor
from database.get_all_sections import get_sections_from_database


def get_section_keyboard() -> Keyboard:
    """
    Функция для создания клавиатуры.
    Возвращает клавиатуру, где каждая кнопка - это раздел.
    :return: Клавиатура (Keyboard)
    """
    section_keyboard = Keyboard(one_time=True)

    all_sections = get_sections_from_database()

    for i_section in all_sections:
        if i_section == all_sections[-1]:
            section_keyboard.add_text_button(text=i_section[0], color=ButtonColor.POSITIVE)
        else:
            section_keyboard.add_text_button(text=i_section[0], color=ButtonColor.POSITIVE)
            section_keyboard.add_row()

    return section_keyboard
