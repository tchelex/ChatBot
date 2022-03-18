import telebot
from paho.mqtt.client import Client

bot = telebot.TeleBot('1485548437:AAEBO5lIHfCgQUiCuS35Hx6OQxNs38ZTX08')
mqtt_message = ''
id = ''
def receive_message(device, userdata, flag, message):
    global mqtt_message
    mqtt_message = message.payload.decode()
    bot.send_message(id, mqtt_message)
@bot.message_handler(commands=['info'])
def info(message):
    bot.send_message(message.chat.id, 'Это бот Александра Борисовича!')
@bot.message_handler(commands=['start'])
def start(message):
    global id
    id = message.chat.id
    bot.send_message(message.chat.id, 'Ваш id сохранен!')
@bot.message_handler(content_types=['text'])
def text(message):
    print(message.chat.id, message.text)
    bot.send_message(message.chat.id, message.text)
    device.publish("___/telega", message.text)
device = Client()
device.username_pw_set("___", "___")
device.connect("mqtt.pi40.ru", 1883)
device.subscribe("___/message")
device.on_message = receive_message
device.loop_start()
bot.polling()
