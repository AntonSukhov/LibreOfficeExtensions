import unohelper, modules
from com.sun.star.task import XJobExecutor
from services.messageboxservice import MessageBoxService

class DataLink(unohelper.Base, XJobExecutor):
    implementationName = "vnd.datalink"                   #Имя реализации
    serviceNames = ("com.sun.star.task.Job",)             #Список реализованных служб
    
    def __init__(self, context):
        self.context = context

    def trigger(self, args):                             #args - имя аргумента, определенное в файле Addons.xcu
        dialogCreator = modules.DialogCreator(self.context)
        dialogCreator.CreateConnectionsDialog()

g_ImplementationHelper = unohelper.ImplementationHelper()

g_ImplementationHelper.addImplementation(DataLink, DataLink.implementationName, DataLink.serviceNames,)

