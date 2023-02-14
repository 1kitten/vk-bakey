from vkwave.bots import SimpleLongPollBot, SimpleBotEvent, PhotoUploader
from vkwave.bots.fsm import ForWhat
import logging.config
from logging_config import LOGGING
from bot_config import bot_configuration
from database.fill_data_base import create_and_fill_data_base
from database.get_products_in_sections import get_products_from_current_section
from keyboards.go_back_keyboard import get_go_back_keyboard
from keyboards.section_keyboard import get_section_keyboard
from states.user_state import UserState, user_state_machine

bot = SimpleLongPollBot(tokens=bot_configuration.bot_token, group_id=int(bot_configuration.group_id))
uploader = PhotoUploader(bot.api_context)


@bot.message_handler(bot.regex_filter('(?i)(начать|старт)'))
async def greetings(event: SimpleBotEvent) -> SimpleBotEvent.answer:
    """
    Хендлер который отлавливает сообщение пользователя - старт/начать.
    Регистр сообщения не важен.
    Выводит пользователю меню с доступными разделами.
    """
    logger.info(f'User: {event.user_id} starts conversation with the bot.')
    await user_state_machine.set_state(event=event, state=UserState.section, for_what=ForWhat.FOR_USER)
    await event.answer(
        message=
        """
        Для просмотра ассортимента выбери необходимый раздел ❤️
        """,
        keyboard=get_section_keyboard().get_keyboard()
    )


@bot.message_handler(bot.state_filter(fsm=user_state_machine, state=UserState.section, for_what=ForWhat.FOR_USER))
async def get_section(event: SimpleBotEvent) -> SimpleBotEvent.answer:
    """
    Хендлер который отлавливает состояние пользователя.
    Выбранная секция добавляется в машину состояния.
    После чего по данной секции будут выведены все товары.
    """
    await user_state_machine.add_data(
        event=event,
        for_what=ForWhat.FOR_USER,
        state_data={'section': event.object.object.message.text}
    )
    user_data = await user_state_machine.get_data(event=event, for_what=ForWhat.FOR_USER)
    user_chosen_section = user_data.get('section')

    logger.info(f'User: {event.user_id} asked for items in {user_chosen_section} section.')

    await user_state_machine.finish(event=event, for_what=ForWhat.FOR_USER)

    await event.answer(
        message=f'🕖 Ищу товары в секции \"{user_chosen_section}\"'
    )

    products = get_products_from_current_section(user_chosen_section)

    for i_product in products:
        photo = await uploader.get_attachment_from_path(file_path=f"{i_product[2]}", peer_id=event.peer_id)
        await event.answer(
            message=f"""
            🍰 Название: {i_product[0]}
            📝 Описание: {i_product[3]}
            
            💸 Цена: {i_product[1]} руб.
            """,
            attachment=photo
        )

    await event.answer(
        message='Всё что нашёл в данной секции 😀',
        keyboard=get_go_back_keyboard().get_keyboard()
    )


@bot.message_handler(bot.payload_contains_filter('button'))
async def get_payload(event: SimpleBotEvent) -> SimpleBotEvent.answer:
    """
    Хендлер который отлавливает payload от кнопки "назад".
    Вызывает функцию greetings по нажатию.
    """
    await greetings(event)


if __name__ == '__main__':
    logger: logging.Logger = logging.getLogger('bot_logger')
    logging.config.dictConfig(LOGGING)

    create_and_fill_data_base()

    logger.info('Bot starts working.')

    bot.run_forever()
