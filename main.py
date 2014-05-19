#!/usr/bin/env python

import pygtk
pygtk.require('2.0')
import gtk
import scipy as sp
import matplotlib.pyplot as plt

filename=""
def process_file(name):
                    
	print name



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
	    filename=dialog.get_filename()
	    print "filename is " + filename
	
		
            #data = sp.genfromtxt("data/web_traffic.tsv",delimiter="\t")
            data = sp.genfromtxt(filename,delimiter=",")
            x = data[:,0]
            y = data[:,1]
            x = x[~sp.isnan(y)]
            y = y[~sp.isnan(y)]
            plt.scatter(x,y)
            plt.title("Plotting your CSV Data")
            plt.xlabel("X-Axis")
            plt.ylabel("Y-Axis")
            plt.xticks([w*7*24 for w in range(10)],['week %i'%w for w in range(10)])
            plt.autoscale(tight=True)
            plt.grid()
            plt.show()
            def error(f,x,y):
                 return sp.sum((f(x)-y)**2)

            fp1, residuals, rank, sv, rcond = sp.polyfit(x, y, 1, full=True)
















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
    #process_file(filename)
    print filename


