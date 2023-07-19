from . import connectionsdialog

#Создатель окон модулей
class DialogCreator:
    
    """
    Определяет для текущего класса атрибуты и их значения

    Параметры:
    
    self: ссылка на экземпляр текущего класса
    context: контекст текущего класса (соответствует контексту класса DataLink)
    """
    def __init__(self, context):
        self.context = context
        serviceManager = context.getServiceManager()
        desktop = serviceManager.createInstanceWithContext('com.sun.star.frame.Desktop', self.context)
        self.connectionsDialog = connectionsdialog.ConnectionsDialog(self.context, desktop.getCurrentComponent())
    """
    Создаёт окно Настройки подключений

    Параметры:
    
    self: ссылка на экземпляр текущего класса
    """
    def CreateConnectionsDialog(self):
        self.connectionsDialog.CreateWindow()
