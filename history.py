#!/usr/bin/env python
'''
today in history
'''

from random import choice
import requests
import willie
from bs4 import BeautifulSoup


@willie.module.commands('history')
def history(bot, input):
    """ returns a random fact of the history for today """

    r = requests.get('http://www.history.com/this-day-in-history')
    if r.status_code == 200:
        soup = BeautifulSoup(r.text)

        soup = soup.find_all('div', class_='cont_box_pie2')[0]
        soup = soup.find_all('div', class_='cont_box_bg2')[0]

        items = soup.find_all('div', recursive=False)
        item = choice(list(items))
        title = item.find_all('h3')[0]
        date = item.find_all('b')[0]

        text = 'Today in history: [%s] %s' % (
            date.string,
            title.string
        )
        bot.say(text)
    else:
        bot.reply('nothing happened today in history')

history.commands = ['history']
history.example = ".history"

if __name__ == '__main__':
    print __doc__.strip()