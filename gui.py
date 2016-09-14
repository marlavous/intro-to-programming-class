from tkinter import *



root_widget = Tk()
var_label_text = StringVar()
entry_text = Entry()
entry_text2 = Entry()


def main():

	root_widget.geometry("300x300")
	root_widget.title("Enter Your Name")

	var_label_text.set("This is a simple GUI.")
	lbl_hello = Label(root_widget, textvariable=var_label_text)
	lbl_hello.pack()

	entry_text.insert(0, "Type your first name.")
	entry_text.pack()

	entry_text2.insert(1, "Type your last name.")
	entry_text2.pack()

	btn_ok = Button(text='Ok', command=lambda: var_label_text.set("My name is" + " " + entry_text.get() + " " + entry_text2.get()))
	btn_ok.pack()


	root_widget.mainloop()


if __name__ == '__main__':
	main()