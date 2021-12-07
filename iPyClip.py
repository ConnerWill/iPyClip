#!python3

'''
This shows a scrolling row or grid of special characters in the Pythonista Keyboard. The view supports both the 'minimized' mode (above the QWERTY keyboard) and the 'expanded' mode with the grid filling most of the keyboard.

Note: This script is designed for the Pythonista Keyboard. You can enable it in the Settings app (under General > Keyboard > Keyboards > Add New Keyboard...). Please check the documentation for more information.
'''

import keyboard
import ui
from configparser import ConfigParser
import ast
import appex
import clipboard
import dialogs

########### cfg parse 

settingsconfig = ConfigParser()
settingsconfig.read('iPyClip-settings.cfg')

clipdbconfig = ConfigParser()
clipdbconfig.read('iPyClip-db.cfg')


# Get new clip
newClip = clipboard.get()






# single variables
slot1 = clipdbconfig.get('clipboarddb','slotdb1')
slot2 = clipdbconfig.get('clipboarddb','slotdb2')
slot3 = clipdbconfig.get('clipboarddb','slotdb3')
slot4 = clipdbconfig.get('clipboarddb','slotdb4')
slot5 = clipdbconfig.get('clipboarddb','slotdb5')
slot6 = clipdbconfig.get('clipboarddb','slotdb6')









bannedclipslist = settingsconfig.get('bannedclips', 'bannedcliplist').split(',')

for bannedclip in bannedclipslist:
	print(bannedclip) 

	
	if newClip.find(bannedclip) != -1:
		print("Found!")
	else:
		print("Not found!")











## Set Clipboard
##########
console.hud_alert("hud alert")
console.input_alert("Set Clipboard")

##########
txt = clipboard.get()
edited_text = dialogs.text_dialog(
    title='View and edit clipboard text',
    text=txt)
if edited_text != txt:
    clipboard.set(edited_text)
#dialogs.share_text(clipboard.get())



def ClearClip():
	empty = ''	
	clipboard.set(empty)
	text = clipboard.get()
	InsertData(text)
	return


# share clip
import , clipboard
dialogs.share_text(clipboard.get())




##### Check if text is selected  if not get saved clips
import keyboard
import ui
import dialogs
import clipboard
import codecs
from urllib.parse import quote
from random import random, choice, randint
import faker

def main():
	# get selected text
	selected_text = keyboard.get_selected_text()
	# check if no text is selected
	if not selected_text:
		# get clipboard
		clipdata = clipboard.get()
		if clipdata == '':
			dialogs.hud_alert('No text in clipboard')
			print('No text in clipboard')
		else:
			# paste clipboard
			keyboard.insert_text(clipdata)
			return
	# Set clipboard to selected text data
	clipboard.set(selected_text)
	dialogs.hud_alert('Copied to clipboard')



if __name__ == '__main__':
	if keyboard.is_keyboard():
		# This keyboard view requires the QWERTY keyboard to be visible,
		# so the view is set in 'minimized' mode.
		main()
		#keyboard.set_view(v, 'minimized')
	else:
		print('hiiii')
		# For debugging in the main app:
#		v.frame = (0, 0, 350, 40)
#		v.name = 'Keyboard Preview'
#		v.present('sheet')
























################## Keyboard ###############

characters = [slot1, slot2, slot3, slot4, slot5, slot6]


class CharsView (ui.View):
	
	def __init__(self, *args, **kwargs):
		super().__init__(self, *args, **kwargs)
		self.background_color = '#333'
		self.scroll_view = ui.ScrollView(frame=self.bounds, flex='WH')
		self.scroll_view.shows_horizontal_scroll_indicator = False
		self.add_subview(self.scroll_view)
		self.buttons = []
		for c in characters:
			button = ui.Button(title=c)
			button.font = ('<System>', 18)
			button.background_color = (1, 1, 1, 0.1)
			button.tint_color = 'white'
			button.corner_radius = 4
			button.action = self.button_action
			self.scroll_view.add_subview(button)
			self.buttons.append(button)
	
	def layout(self):
		rows = max(1, int(self.bounds.h / 36))
		bw = 44
		h = (self.bounds.h / rows) - 4
		x, y = 2, 2
		for button in self.buttons:
			button.frame = (x, y, bw, h)
			y += h + 4
			if y + h > self.bounds.h:
				y = 2
				x += bw + 4
		self.scroll_view.content_size = ((len(self.buttons)/rows + 1) * (bw + 4) + 40, 0)
	
	def button_action(self, sender):
		text = sender.title
		if text == '(?)':
			# Show help
			tv = ui.TextView(name='Help')
			tv.text = 'You can customize this scrollable list of special characters by editing the script in Pythonista (tap and hold the shortcut button, and select "Edit Script").\n\nYou can also remove this Help button, if you like.'
			tv.font = ('<System>', 18)
			tv.editable = False
			tv.selectable = False
			tv.present()
			return
		if keyboard.is_keyboard():
			keyboard.play_input_click()
			keyboard.insert_text(text)
		else:
			print('Keyboard input:', text)


def main():
	v = CharsView(frame = (0, 0, 320, 40))
	if keyboard.is_keyboard():
		keyboard.set_view(v, 'current')
	else:
		# For debugging in the main app:
		v.name = 'Keyboard Preview'
		v.present('sheet')
		
		########### Check if running from keyboard
def main():
	if not appex.is_running_extension():
		print('Running in Pythonista app, using test data...\n')
		text = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'
	else:
		text = appex.get_text()
	if text:
		# TODO: Your own logic here...
		print('Input text: %s' % text)
		out = text.upper()
		print('\nConverted to all-caps: %s' % out)
		clipboard.set(out)
		print('(Copied to clipboard)')
	else:
		print('No input text found.')

		
		


if __name__ == '__main__':
	main()
