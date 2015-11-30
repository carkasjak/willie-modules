"""
auth.py - Willie Quakenet Auth Module
"""

from willie.module import commands, example

@commands('auth')
@example('.auth [password]')
def auth(bot, trigger):
	"""Auth to Q. This is owner-only command."""
	# Can only be done in privmsg by the owner
	if trigger.sender.startswith('#'):
		return
	if not trigger.admin:
		return

	if not trigger.group(2):
		bot.reply('You need type type password, ex. .auth password')
	else:
		auth_text = 'auth ' + bot.nick + ' ' + trigger.group(2)
		bot.msg('q@cserve.quakenet.org', auth_text)
		bot.write(('MODE', bot.nick, '+x'))