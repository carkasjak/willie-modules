'''
update.py - Module to update modules directory
'''

import sys
import subprocess
import sopel

if sys.version_info >= (2, 7):
    @sopel.module.nickname_commands('updatemodules')
    def update(bot, trigger):
        if not trigger.admin:
            return

        """Pulls the latest versions of all modules from Git"""
        proc = subprocess.Popen('cd /home/bot/.sopel/modules && /usr/bin/git pull',
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE, shell=True)
        bot.reply(proc.communicate()[0])
else:
    @sopel.module.nickname_commands('update')
    def update(bot, trigger):
        bot.say('You need to run me on Python 2.7 to do that.')