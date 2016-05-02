'''
channelmodule for #pony.ql
'''
import willie
from random import choice
import datetime
import requests
import re
import urllib.request as urllib2
'''import urllib2'''
import random

@willie.module.commands('quakecon')
def quakecon(bot, trigger):
   now = datetime.datetime.now()     
   qcon = datetime.datetime(2016, 8, 4, 10)
   delta = qcon - now
   if delta.days < 6:
      hours, remainder = divmod(delta.seconds, 3600)
      minutes, seconds = divmod(remainder, 60) 
      output = "{days} days, {hours} hours, {minutes} minutes, and {seconds} seconds until QuakeCon!".format(days=delta.days, hours=hours, minutes=minutes, seconds=seconds)
   else:
      output = "%s days until QuakeCon!" % delta.days
   bot.say(output)

@willie.module.commands('blizzcon')
def blizzcon(bot, trigger):
   now = datetime.datetime.now()
   target = datetime.datetime(2015, 11, 6, 0)
   delta = target - now
   if delta.days < 7:
      hours, remainder = divmod(delta.seconds, 3600)
      minutes, seconds = divmod(remainder, 60)
      output = "{days} days, {hours} hours, {minutes} minutes, and {seconds} seconds until BlizzCon!".format(days=delta.days, hours=hours, minutes=minutes, seconds=seconds)
   else:
      output = "%s days until BlizzCon!" % delta.days
   bot.say(output)

@willie.module.commands('zen')
def zen(bot, trigger):
   bot.say(requests.get("https://api.github.com/zen").text)
   
@willie.module.commands('whatgameisthayacurrentlyplaying')
def whatgameisthayacurrentlyplaying(bot, trigger):
   bot.say("not playing, just botting.")

@willie.module.commands('nfact')
def nfact(bot, trigger):
   bot.say(requests.get("http://numbersapi.com/random").text)

@willie.module.commands('42')
def fourtytwo(bot, trigger):
   bot.say(requests.get("http://numbersapi.com/42").text)

@willie.module.commands('tfact')
def today(bot, trigger):
   month = datetime.datetime.now().month
   day = datetime.datetime.now().day
   bot.say(requests.get("http://numbersapi.com/%s/%s/date" % (month, day)).text)

@willie.module.commands('askreddit', 'asscredit')
def ask(bot, trigger):
  header =  {"User-Agent": "Willie the bot"}
  bot.say(choice(requests.get("http://www.reddit.com/r/askreddit.json?limit=100", headers=header).json()["data"]["children"])["data"]["title"])

@willie.module.commands('shower')
def shower(bot, trigger):
  header =  {"User-Agent": "Willie the bot"}
  bot.say(choice(requests.get("http://www.reddit.com/r/showerthoughts.json?limit=100", headers=header).json()["data"]["children"])["data"]["title"])

@willie.module.commands('5050')
def fifty(bot, trigger):
  header =  {"User-Agent": "Willie the bot"}
  pick = choice(requests.get("http://www.reddit.com/r/fiftyfifty.json?limit=100", headers=header).json()["data"]["children"])["data"]
  bot.say("%s - %s" % (pick["title"], pick["url"]))

@willie.module.commands('til')
def til(bot, trigger):
  header =  {"User-Agent": "Willie the bot"}
  pick = choice(requests.get("http://www.reddit.com/r/todayilearned.json?limit=100", headers=header).json()["data"]["children"])["data"]
  bot.say("%s" % (pick["title"]))

@willie.module.commands('beat')
def beat(bot, trigger):
  header =  {"User-Agent": "Willie the bot"}
  pick = choice(requests.get("http://www.reddit.com/r/beatheads.json?limit=100", headers=header).json()["data"]["children"])["data"]
  bot.say("%s" % (pick["url"]))
  
@willie.module.commands('kadse', 'kazachstan', 'c@')
def kadse(bot, trigger):
  header =  {"User-Agent": "Willie the bot"}
  pick = choice(requests.get("http://www.reddit.com/r/catgifs.json?limit=100", headers=header).json()["data"]["children"])["data"]
  bot.say("%s" % (pick["url"]))

@willie.module.commands('newbeat','latest')
def newbeat(bot, trigger):
  header =  {"User-Agent": "Willie the bot"}
  pick = choice(requests.get("http://www.reddit.com/r/beatheads/new.json?limit=1", headers=header).json()["data"]["children"])["data"]
  bot.say("%s" % (pick["url"]))

@willie.module.commands('tifu')
def tifu(bot, trigger):
  header =  {"User-Agent": "Willie the bot"}
  pick = choice(requests.get("http://www.reddit.com/r/tifu.json?limit=100", headers=header).json()["data"]["children"])["data"]
  bot.say("%s - %s" % (pick["title"], pick["url"]))

@willie.module.commands('rather')
def rather(bot, trigger):
  header =  {"User-Agent": "Willie the bot"}
  bot.say(choice(requests.get("http://www.reddit.com/r/wouldyourather.json?limit=100", headers=header).json()["data"]["children"])["data"]["title"])

@willie.module.commands('youporn', 'yp')
def youporn(bot, trigger):
  foundComment = False
  opener = urllib2.build_opener()
  opener.addheaders.append(('Cookie', 'age_verified=1'))

  for x in range(7):
    f = opener.open("http://www.youporn.com/random/video/")
    htmlSource = f.read()
    f.close()
    comments = re.findall(b'<div class="commentContent">((?:.|\\n)*?)</p>', htmlSource)
    if len(comments) == 0:
        continue
    randomcomment = random.choice(comments).replace(b"<p>", b"")
    bot.say(randomcomment, max_messages=2)
    foundComment = True
    break
  if not foundComment:
    bot.say("No comment found, please retry")

@willie.module.commands('jpg','jpeg')
def jpg(bot, trigger):
   bot.say("Do I look like I know what a JPEG is? https://youtu.be/QEzhxP-pdos")

@willie.module.commands('fap','fapathon')
def fap(bot, trigger):
   bot.say("https://i.imgur.com/9ciSNye.gifv")

@willie.module.commands('rd')
def reverseDict(bot, trigger):
  word = trigger.group(2)
  if not word:
    bot.say("syntx: .rd <definition/description>")
  else:
    result = requests.get("http://api.datamuse.com/words", params={"rd": word}).json()
    if result:
      reply = "Possible words matching '%s': %s" % (word, ", ".join(w["word"] for w in result[0:5]))
      bot.say(reply)
      
@willie.module.commands("lenny")
def lenny(bot, trigger):
  bot.say(u"( ͡° ͜ʖ ͡°)")

@willie.module.commands("shrug1")
def shrug1(bot, trigger):
  bot.say(u"¯\_(ツ)_/¯")
  
@willie.module.commands("shrug2")
def shrug2(bot, trigger):
  bot.say(u"¯\(º_o)/¯")

@willie.module.commands("shrug3")
def shrug3(bot, trigger):
  bot.say(u"┐(ツ)┌")
  
@willie.module.commands("wowalert")
def wowalert(bot, trigger):
  bot.say("http://launcher.worldofwarcraft.com/alert (US); http://status.wow-europe.com/en/alert (EU)")
