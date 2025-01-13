# AI-Stream
Twitch бот, блокирующий токсичный контент на стримах.

## О проекте
Twitch бот, который имеет множество настроек по фильтрации токсичного контента. Стример сам может решать, какие сообщения
в чате он считает токсичными, а какие нет, а также как на них реагировать 

## Архитектура
Простая схема работы чатбота
![architecture](artifacts/simple_schema.png)

## установка окружения
python3 -m venv myenv ИЛИ  python -m venv myenv 
myenv\Scripts\activate
pip install -r requirements.txt
deactivate

conda create --name myenv
conda activate myenv

virtualenv myenv