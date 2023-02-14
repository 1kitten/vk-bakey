import os
from dataclasses import dataclass
from dotenv import load_dotenv, find_dotenv

if not find_dotenv():
    exit("Переменные окружения не загружены, так как отсутствует файл .env")
else:
    load_dotenv()


@dataclass(frozen=True)
class BotConfig:
    bot_token: str
    group_id: str


bot_configuration: BotConfig = BotConfig(bot_token=os.getenv('BOT_TOKEN'), group_id=os.getenv('GROUP_ID'))

ROOT_DIR: str = os.path.dirname(__file__)
