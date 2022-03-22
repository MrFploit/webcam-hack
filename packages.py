#LinuxArmy
#MrFploit
import os
packages = ['pytelegrambotapi']
os.system(f'pip3 uninstall telebot -y')
os.system(f'pip3 uninstall pytelegrambotapi -y')
os.system('pip install -U git+https://github.com/eternnoir/pyTelegramBotAPI.git')
