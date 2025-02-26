#!/usr/bin/env python3
# ui_manager.py - Simple curses-based UI for NodePhone

import curses

class Menu:
	"""Simple menu implementation using curses"""
	
	def __init__(self, items, title="NodePhone Menu"):
		self.items = items
		self.title = title
		self.selected = 0
	
	def display(self):
		"""Display the menu and handle navigation until selection is made"""
		def _menu_loop(stdscr):
			curses.curs_set(0)  # Hide cursor
			h, w = stdscr.getmaxyx()
			
			# Prepare color pairs
			curses.start_color()
			curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
			
			while True:
				stdscr.clear()
				
				# Draw title
				title_x = max(0, (w - len(self.title)) // 2)
				stdscr.addstr(1, title_x, self.title)
				
				# Draw menu items
				for idx, item in enumerate(self.items):
					y = 3 + idx
					item_str = f" {item} "
					x = max(0, (w - len(item_str)) // 2)
					
					if idx == self.selected:
						stdscr.attron(curses.color_pair(1))
						stdscr.addstr(y, x, item_str)
						stdscr.attroff(curses.color_pair(1))
					else:
						stdscr.addstr(y, x, item_str)
				
				# Draw navigation hint
				hint = "Use ↑/↓ arrows to navigate, Enter to select"
				hint_x = max(0, (w - len(hint)) // 2)
				stdscr.addstr(h-2, hint_x, hint)
				
				stdscr.refresh()
				
				# Handle key presses
				key = stdscr.getch()
				
				if key == curses.KEY_UP:
					self.selected = max(0, self.selected - 1)
				elif key == curses.KEY_DOWN:
					self.selected = min(len(self.items) - 1, self.selected + 1)
				elif key in [curses.KEY_ENTER, ord('\n'), ord(' ')]:
					return self.selected
		
		return curses.wrapper(_menu_loop)


def show_message(message, title="NodePhone"):
	"""Display a simple message box"""
	def _show_message(stdscr):
		stdscr.clear()
		h, w = stdscr.getmaxyx()
		
		# Draw title
		title_x = max(0, (w - len(title)) // 2)
		stdscr.addstr(1, title_x, title)
		
		# Draw message
		msg_lines = message.split('\n')
		for i, line in enumerate(msg_lines):
			y = 3 + i
			x = max(0, (w - len(line)) // 2)
			stdscr.addstr(y, x, line)
		
		# Draw prompt
		prompt = "Press any key to continue..."
		prompt_x = max(0, (w - len(prompt)) // 2)
		stdscr.addstr(h-2, prompt_x, prompt)
		
		stdscr.refresh()
		stdscr.getch()
	
	curses.wrapper(_show_message) 