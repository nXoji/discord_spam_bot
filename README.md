# 🤖 Spam bot for discord

Спам пользователей по айди в дискорде
> Для работы программы требуеться Python, а также несклоько библиотек указаные в файле requirements.txt
# 📥 Установка
### Linux or Termux 
```sh
apt update && apt upgrade -y
apt install python
apt install git
git clone https://github.com/illia841/discord_spam_bot
cd spam-bot-discord
pip install -r requirements.txt
```
### Windows
Установите релиз на странице проекта.
Также установите [Python(3)](https://www.python.org/downloads/), если он у вас не был установлен. 
После этого откройте командную строку из папки в которую вы скачали проект, и пропишите следующую команду:

```pip insall -r requirements.txt```
# ⌨️ Использование 
### Linux or Termux 
Зайдите в папку в которую устанавливали проект и найдите файл config.py. Затем впишите туда все данные от бота полученные на https://discord.com/developers/applications! А далее введите команды ниже:
```sh
python3 bot.py
```

### Windows
Зайдите в папку в которую устанавливали проект и найдите файл config.py. Затем впишите туда все данные от бота полученные на https://discord.com/developers/applications! А далее введите команды ниже:
```sh
python bot.py
```
