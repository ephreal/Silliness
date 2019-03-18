import tkinter as tk

from decimal import Decimal
from tkinter import ttk


class Calculator(ttk.Frame):
	def __init__(self, master=tk.Tk()):
		super().__init__(master)
		self.master = master
		self.master.title("tKalculator")
		self.operator = None
		self.prev_num = 0
		self.completed_calculation = False
		self.grid()

		self.create_widgets()
		self.bind_keys()
		self.arrange_widgets()

		self.mainloop()

	def create_widgets(self):
		"""
		Create all calculator buttons
		and widgets
		"""

		self.number_buttons = []

		# Number display
		self.top_display_space = ttk.Label(self, text=" ")
		self.display = tk.Text(self, height=1, width=30, pady=4)
		self.display.insert(1.0, "0")
		self.display["state"] = "disabled"
		self.bottom_display_space = ttk.Label(self, text=" ")

		# Number buttons
		# For some reason, the for loop makes everything send
		# a "9" to the update function
		for num in range(0, 10):
			num = str(num)
			self.number_buttons.append(
				# note to self: The num=num is necessary here
				ttk.Button(self, text=num, command=lambda num=num: self.update(num))
									  )

		self.decimal_button = ttk.Button(self, text=".",
						command=lambda: self.update("."))

		# Special Buttons
		self.clearall_button = ttk.Button(self, text="A/C", command=self.all_clear)
		self.clear_button = ttk.Button(self, text="C", command=self.clear)

		# Math operators
		self.add_button  = ttk.Button(self, text="+", command=lambda: self.math("+"))
		self.sub_button  = ttk.Button(self, text="-", command=lambda: self.math("-"))
		self.mult_button = ttk.Button(self, text="X", command=lambda: self.math("x"))
		self.div_button  = ttk.Button(self, text="/", command=lambda: self.math("/"))
		self.eql_button  = ttk.Button(self, text="=", command=lambda: self.math("="))

	def arrange_widgets(self):
		"""
		Arrange all calculator widgets.
		"""

		# Display
		self.top_display_space.grid(row=0, column=1)
		self.display.grid(row=1, column=0, columnspan=5)
		self.bottom_display_space.grid(row=2, column=2)

		# Number buttons
		row = 3
		column = 1
		for i in range(1, 10):
			self.number_buttons[i].grid(row=row, column=column)
			column += 1
			if column > 3:
				column = 1
				row += 1

		self.number_buttons[0].grid(row=6, column=2)
		self.decimal_button.grid(row=6, column=1)

		# Special Buttons
		self.clearall_button.grid(row=7, column=1)
		self.clear_button.grid(row=6, column=3)

		# Math operator buttons
		self.add_button.grid(row=7, column=2)
		self.sub_button.grid(row=7, column=3)
		self.mult_button.grid(row=8, column=2)
		self.div_button.grid(row=8, column=3)
		self.eql_button.grid(row=8, column=1)

	def bind_keys(self):
		"""
		Binds events to keyboard button presses.
		"""

		# Keys to bind
		keys = "1234567890.caCA+-*x/="
		special_keys = [
						"<KP_1>", "<KP_2>", "<KP_3>",
						"<KP_4>", "<KP_5>", "<KP_6>",
						"<KP_7>", "<KP_8>", "<KP_9>",
						"<KP_0>", "<KP_Decimal>", "<KP_Add>",
						"<KP_Subtract>", "<KP_Multiply>",
						"<KP_Divide>", "<KP_Enter>",
						"<Return>", "<Escape>",
						"<BackSpace>"
					   ]

		# A couple for loops to bind all the keys
		for key in keys:
			self.master.bind(key, self.keypress_handler)

		for key in special_keys:
			self.master.bind(key, self.keypress_handler)

	def backspace(self, event):
		"""
		Remove one character from the display.
		"""

		self.display["state"] = "normal"
		current = self.display.get(1.0, tk.END)
		self.display.delete(1.0, tk.END)
		current = current[:-2]

		# Make sure that the display is never empty
		if current == "":
			current = "0"

		self.display.insert(1.0, current)
		self.display["state"] = "disabled"

	def keypress_handler(self, event):
		"""
		Handles any bound keyboard presses.
		"""

		char_keycode = '01234567890.'
		char_operator = "+-x*/"

		if (event.char in char_keycode):
			self.update(event.char)

		elif event.char in char_operator:
			self.math(event.char)

		elif event.char == "\r" or event.char == "=":
			self.math("=")

		elif event.char == "\x1b":
			self.master.destroy()

		elif event.char == "c" or event.char == "C":
			self.clear()

		elif event.char == "a" or event.char == "A":
			self.all_clear()

	def update(self, character):
		"""
		Handles all updating of the number display.
		"""
		# Allow editing of the display
		self.display["state"] = "normal"

		# Get the current number
		num = self.display.get(1.0, tk.END)
		# clear the display
		self.display.delete(1.0, tk.END)

		# Remove "\n"
		num = num.strip()

		# Clear num provided we're not putting a 
		# decimal after a zero
		if num == "0" and not character == ".":
			num = ""

		num = f"{num}{character}"

		self.display.insert(1.0, f"{num}")
		self.display["state"] = "disabled"

	def all_clear(self):
		"""
		Resets everything for starting a
		new calculation.
		"""
		self.clear()
		self.prev_num = 0
		self.operator = None

	def clear(self):
		"""
		Clears the display by removing
		any current text and setting the
		display to 0
		"""
		self.display["state"] = "normal"
		self.display.delete(1.0, tk.END)
		self.display.insert(1.0, "0")
		self.display["state"] = "disabled"

	def math(self, operator):
		"""
		Handle any actual math.
		"""
		if not self.operator:
			# If an operator doesn't exist, the
			# calculator is waiting for a new 
			# input.
			self.operator = operator
			self.prev_num = self.display.get(1.0, tk.END)
			self.clear()

		else:
			# The calculator is ready to do some math.
			self.prev_num = Decimal(self.prev_num)
			curr_num = self.display.get(1.0, tk.END)
			curr_num = Decimal(curr_num)

			if self.operator == "+":
				self.prev_num += curr_num
			elif self.operator == "-":
				self.prev_num -= curr_num
			elif self.operator == "x" or self.operator == "*":
				self.prev_num *= curr_num
			elif self.operator == "/":
				self.prev_num /= curr_num
			
			self.operator = operator

			if self.operator == "=":
				# It's now time to show the current result
				# of all calculations.
				self.display["state"] = "normal"
				self.display.delete(1.0, tk.END)
				self.display.insert(1.0, str(self.prev_num))
				self.display["state"] = "disabled"
				self.completed_calculation = True
			else:
				# We're ready for another number to
				# perform calculations on
				self.clear()


if __name__ == "__main__":
	calc = Calculator()