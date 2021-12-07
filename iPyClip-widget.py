#!python3

'''
This widget script shows a grid of shortcut buttons that launch URLs when tapped.

The shortcut titles/URLs and the grid layout can be configured with the SHORTCUTS, COLS, ROWS variables.
'''

import appex, ui
import os
from math import ceil, floor

# NOTE: The ROWS variable determines the number of rows in "compact" mode. In expanded mode, the widget shows all shortcuts.
COLS = 3
ROWS = 2

# Each shortcut should be a dict with at least a 'title' and 'url' key. 'color' and 'icon' are optional. If set, 'icon' should be the name of a built-in image.
SHORTCUTS = [
{'title': 'New Email', 'url': 'mailto:', 'color': '#5e96ff', 'icon': 'iow:email_24'},
{'title': 'New Message', 'url': 'sms://', 'color': '#5ec0ff', 'icon': 'iow:chatbox_24'},
{'title': 'Pythonista', 'url': 'pythonista3://', 'color': '#45d3e8', 'icon': 'iow:chevron_right_24'},
{'title': 'Forum', 'url': 'http://forum.omz-software.com', 'color': '#4dd19d'},
{'title': 'Google', 'url': 'http://google.com', 'color': '#a9de31'},
{'title': 'DuckDuckGo', 'url': 'http://duckduckgo.com', 'color': '#ffd026' },
{'title': 'Amazon', 'url': 'http://amazon.com', 'color': '#ff8e13'},
{'title': 'eBay', 'url': 'http://ebay.com', 'color': '#ff4a09'},
]

class LauncherView (ui.View):
	def __init__(self, shortcuts, *args, **kwargs):
		row_height = 110 / ROWS
		super().__init__(self, frame=(0, 0, 300, ceil(len(shortcuts) / COLS) * row_height), *args, **kwargs)
		self.buttons = []
		for s in shortcuts:
			btn = ui.Button(title=' ' + s['title'], image=ui.Image(s.get('icon', 'iow:compass_24')), name=s['url'], action=self.button_action, bg_color=s.get('color', '#55bcff'), tint_color='#fff', corner_radius=9)
			self.add_subview(btn)
			self.buttons.append(btn)
	
	def layout(self):
		bw = self.width / COLS
		bh = floor(self.height / ROWS) if self.height <= 130 else floor(110 / ROWS)
		for i, btn in enumerate(self.buttons):
			btn.frame = ui.Rect(i%COLS * bw, i//COLS * bh, bw, bh).inset(2, 2)
			btn.alpha = 1 if btn.frame.max_y < self.height else 0
	
	def button_action(self, sender):
		import shortcuts
		shortcuts.open_url(sender.name)

def main():
	widget_name = __file__ + str(os.stat(__file__).st_mtime)
	v = appex.get_widget_view()
	# Optimization: Don't create a new view if the widget already shows the launcher.
	if v is None or v.name != widget_name:
		v = LauncherView(SHORTCUTS)
		v.name = widget_name
		appex.set_widget_view(v)

if __name__ == '__main__':
	main()










#!python3

'''
This widget script simply shows the current contents of the clipboard.
The clipboard can be cleared by tapping the "trash" button.
'''

import appex, ui
import clipboard

def clear_button_tapped(sender):
	clipboard.set('')
	sender.superview['text_label'].text = 'Clipboard:\n'

def main():
	v = ui.View(frame=(0, 0, 320, 220))
	label = ui.Label(frame=(8, 0, 320 - 44 - 8, 220), flex='wh')
	label.name = 'text_label'
	label.font = ('Menlo', 12)
	label.number_of_lines = 0
	v.add_subview(label)
	clear_btn = ui.Button(frame=(320-44, 0, 44, 220), flex='hl')
	clear_btn.image = ui.Image.named('iow:ios7_trash_32')
	clear_btn.action = clear_button_tapped
	v.add_subview(clear_btn)
	appex.set_widget_view(v)
	text = clipboard.get()
	label.text = 'Clipboard:\n' + text
	
if __name__ == '__main__':
	main()
	
