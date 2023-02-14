from vkwave.bots.utils.keyboards.keyboard import Keyboard, ButtonColor


def get_go_back_keyboard() -> Keyboard:
    """
    Клавиатура с одной кнопкой "Назад".
    :return: клавиатура (Keyboard)
    """
    back_keyboard = Keyboard(one_time=True)
    back_keyboard.add_text_button(text='назад', color=ButtonColor.NEGATIVE, payload={'button': 'back'})

    return back_keyboard
