import gtk

class Application():
	def __init__(self):
		self.string = ""
		self.window = gtk.Window()
		self.window.set_title("Calculator")
		self.create_widgets()
		self.connect_signals()
		self.window.show_all()
		gtk.main()

	def create_widgets(self):
		self.vbox = gtk.VBox(spacing = 5)
		self.hbox2 = gtk.HBox(spacing = 5)
		self.hbox = gtk.HBox(spacing = 5)
		self.hbox1 =gtk.HBox(spacing = 5)
		self.hbox4 = gtk.HBox(spacing =5)
		self.hbox5 = gtk.HBox(spacing = 5)
		
		self.entry = gtk.Entry()
		self.hbox2.pack_start(self.entry)

		self.label1 = gtk.Button("1")
		self.label2 = gtk.Button("2")
		self.label3 = gtk.Button("3")
		self.addition = gtk.Button("+")
		self.hbox.pack_start(self.label1)
		self.hbox.pack_start(self.label2)
		self.hbox.pack_start(self.label3)
		self.hbox.pack_start(self.addition)

		self.label4 = gtk.Button("4")
		self.label5 = gtk.Button("5")
		self.label6 = gtk.Button("6")
		self.subration = gtk.Button("-")
		self.hbox1.pack_start(self.label4)
		self.hbox1.pack_start(self.label5)
		self.hbox1.pack_start(self.label6)
		self.hbox1.pack_start(self.subration)

		self.label7 = gtk.Button("7")
		self.label8 = gtk.Button("8")
		self.label9 = gtk.Button("9")
		self.multiplication = gtk.Button("*")
		self.hbox4.pack_start(self.label7)
		self.hbox4.pack_start(self.label8)
		self.hbox4.pack_start(self.label9)
		self.hbox4.pack_start(self.multiplication)


		self.calculate = gtk.Button("Enter")
		self.hbox5.pack_start(self.calculate)

		self.vbox.pack_start(self.hbox2)
		self.vbox.pack_start(self.hbox)
		self.vbox.pack_start(self.hbox1)
		self.vbox.pack_start(self.hbox4)
		self.vbox.pack_start(self.hbox5)

		self.window.add(self.vbox)
		self.window.connect('destroy',self.exit)
	
	def connect_signals(self):
		self.label1.connect('clicked',self.display,1)
		self.label2.connect('clicked',self.display,2)
		self.label3.connect('clicked',self.display,3)
		self.label4.connect('clicked',self.display,4)
		self.label5.connect('clicked',self.display,5)
		self.label6.connect('clicked',self.display,6)
		self.label7.connect('clicked',self.display,7)
		self.label8.connect('clicked',self.display,8)
		self.label9.connect('clicked',self.display,9)
		
		self.addition.connect('clicked',self.display,'+')
		self.subration.connect('clicked',self.display,'-')
		self.multiplication.connect('clicked',self.display,'*')		

		self.calculate.connect('clicked',self.calc)

	def display(self,widget,i ):
		self.string = self.string + str(i)
		self.entry.set_text(self.string)


	def calc(self,widget):
		self.entry.set_text(str(eval(self.entry.get_text())))  ## Eval is a really powerful tool... 
		
	def exit(self,widget,callback_data=None):
		print "Good Bye"
		gtk.main_quit()
app = Application()
