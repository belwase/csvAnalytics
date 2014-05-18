#!/usr/bin/env python

import pygtk
pygtk.require('2.0')
import gtk

def open_file():
	exit

class HelloWorld:

    def open_file(self, widget, callback_data=None):
		dialog = gtk.FileChooserDialog("Open..",
		                       None,
		                       gtk.FILE_CHOOSER_ACTION_OPEN,
		                       (gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL,
		                        gtk.STOCK_OPEN, gtk.RESPONSE_OK))
		dialog.set_default_response(gtk.RESPONSE_OK)

		filter = gtk.FileFilter()
		filter.set_name("All files")
		filter.add_pattern("*")
		dialog.add_filter(filter)

		filter = gtk.FileFilter()
		filter.set_name("CSV")
		filter.add_mime_type("CSV/csv")
		filter.add_pattern("*.csv")
		dialog.add_filter(filter)

		response = dialog.run()
		if response == gtk.RESPONSE_OK:
		    print dialog.get_filename(), 'selected'
		elif response == gtk.RESPONSE_CANCEL:
		    print 'Closed, no files selected'

    def hello(self, widget, data=None):
        print "Hello World"

    def delete_event(self, widget, event, data=None):
        print "delete event occurred"
        return False

    def destroy(self, widget, data=None):
        print "destroy signal occurred"
        gtk.main_quit()

    def __init__(self):
        # create a new window
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
    	self.window.connect("delete_event", self.delete_event)
        self.window.connect("destroy", self.destroy)
    
        self.window.set_border_width(10)
	self.window.set_default_size(300,300)
	self.window.set_position(gtk.WIN_POS_CENTER_ALWAYS)

	self.frame = gtk.Frame()
	self.frame.set_label("CSV Analytics")
	self.window.add(self.frame)   
	 
	

	self.button = gtk.Button("Open file")
	self.button.set_size_request(100,200)
	#self.button.set_size_request(10,10)
        self.button.connect("clicked", self.open_file)
    	#self.button.connect_object("clicked", gtk.Widget.destroy, self.window)
	
	self.frame.add(self.button)            
	self.frame.show()
        self.button.show()    
        self.window.show()

    
    def main(self):
        gtk.main()


if __name__ == "__main__":
    hello = HelloWorld()
    hello.main()
 


