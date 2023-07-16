import uno
import unohelper
from com.sun.star.awt.MessageBoxType import MESSAGEBOX
from com.sun.star.awt.MessageBoxButtons import BUTTONS_OK
from com.sun.star.task import XJobExecutor

def MessageBoxShow(captionText, messageText, messageBoxType = MESSAGEBOX):
	context = uno.getComponentContext()
	sManager = context.ServiceManager
	toolkit = sManager.createInstance("com.sun.star.awt.Toolkit")
	msgbox = toolkit.createMessageBox(None, messageBoxType, BUTTONS_OK, captionText, messageText)
	return msgbox.execute()

class DataLink(unohelper.Base, XJobExecutor):
    implementationName = "vnd.datalink"                  #Имя реализации
    serviceNames = ("com.sun.star.task.Job",)             #Список реализованных служб
    
    def __init__(self, context):
        self.context = context

    def trigger(self, args):                             #args - имя аргумента, определенное в файле Addons.xcu
        MessageBoxShow("Info", "Hello World!!! Args: " + args)

g_ImplementationHelper = unohelper.ImplementationHelper()

g_ImplementationHelper.addImplementation(DataLink, DataLink.implementationName, DataLink.serviceNames,)

