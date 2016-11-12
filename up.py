#@PLUSTM
import telebot
from telebot import types
from telebot import util
import redis as r
import json
import logging
import urllib
import urllib2
import time
import logging
import subprocess
import requests
import os
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
redis = r.StrictRedis(host='localhost', port=6379, db=0,decode_responses=True)
token = "" #YOUR TOKEN
bot = telebot.TeleBot(token)
opizo_email = '' #YOUR EMAIL/GMAIL


@bot.message_handler(regexp='^/start')
def te(m):
 try:
   mer = types.ReplyKeyboardMarkup()
   bac = types.KeyboardButton('Feed Back')
   pm = types.KeyboardButton('Channels')
   mer.add(pm)
   mer.add(bac)
   bot.send_message(m.chat.id,''' Hello \xE2\x9C\x8C \n\nWelcome To SKY UPLOADER bot \xF0\x9F\x98\x8A \nPlease Snd (File/Sticker/Music/Picture And ....) To me And Get Your Link... \nYou Need me?\n\n\xF0\x9F\x91\xA5use buttons\xF0\x9F\x91\xA5 \n
''',parse_mode='markdown',reply_markup=mer)
   name = m.from_user.first_name
   id = m.from_user.id
   redis.sadd('memebers',id)
   print 'User: {} Start the bot!'.format(m.from_user.id)
 except:
   print 'Err'

@bot.message_handler(commands=['feedback'])
def feedback(m):
       try:
          senderid = m.chat.id
          first = m.from_user.first_name
          usr = m.from_user.username
          str = m.text
          txt = str.replace('/feedback', '')
          bot.send_message(senderid, "_Thank Your Msg Send To Yones :|_", parse_mode="Markdown")
          bot.send_message(201704410, "Message : {}\nID : {}\nName : {}\nUsername : @{}".format(txt,senderid,first,usr))
       except:
          bot.send_message(m.chat.id, '*Error!*', parse_mode="Markdown")

@bot.message_handler(regexp='Channels')
def te(m):
   bot.send_message(m.chat.id,' Please Join To \xF0\x9F\x91\xA5Channels\xF0\x9F\x91\xA5\n\n\nhttps://telegram.me/SKYTMS\n\nhttps://telegram.me/PLUSTM')

@bot.message_handler(regexp='Feed Back')
def te(m):
   bot.send_message(m.chat.id,' /feedback [TEXT]\n\n \xE2\x9C\x8Csend your message For YONES\xE2\x9C\x8C')

# Uploader Bot By @plustm

@bot.message_handler(commands=['stats'])
def m(m):
        if m.from_user.id == 201704410:
          file = redis.scard('files')
          msm = redis.scard('memebers')
          em = redis.scard('msgs')
          bot.send_message(m.chat.id,'*Files Uploaded:* _{}_\n*Users:* _{}_\n*All Messages:* _{}_'.format(file,msm,em),parse_mode='Markdown')

# Uploader Bot By @PLUSTM

@bot.message_handler(content_types=['video','photo','sticker','document','audio','voice'])
def all(m):
  try:
            if m.photo :
                fileid = m.photo[1].file_id
            elif m.video :
                fileid = m.video.file_id
            elif m.sticker :
                fileid = m.sticker.file_id
            elif m.document :
                fileid = m.document.file_id
            elif m.audio :
                fileid = m.audio.file_id
            elif m.voice :
                fileid = m.voice.file_id
            e = m.from_user.username
            text = m
            redis.sadd('files',fileid)
            link = urllib2.Request("https://api.pwrtelegram.xyz/bot{}/getFile?file_id={}".format(token,fileid))
            open = urllib2.build_opener()
            f = open.open(link)
            link1 = f.read()
            jdat = json.loads(link1)
            patch = jdat['result']['file_path']
            send = 'https://storage.pwrtelegram.xyz/{}'.format(patch)
            link = urllib2.Request("http://api.gpmod.ir/shorten/?url={}&username={}".format(opizo_email,send))
            opeen = urllib2.build_opener()
            j = opeen.open(link)
            lin1 = j.read()
            bot.send_message(m.chat.id,'Sabr Konid \xE2\x9C\x8C')
         
            bot.send_message(m.chat.id,'<a href="{}">YOUR file Is Here</a>'.format(send),parse_mode='HTML')
  except:
   bot.send_message(m.chat.id,link1)


bot.polling(True)
