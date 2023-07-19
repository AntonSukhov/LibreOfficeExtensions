import uno, unohelper
from com.sun.star.awt import XWindowListener
from com.sun.star.lang import XEventListener
from com.sun.star.awt.PosSize import SIZE as PS_SIZE


#Обработчик событий окна Настройки подключений
class ConnectionsDialogListener(unohelper.Base, XWindowListener):

    """
    Определяет для текущего класса атрибуты и их значения

    Параметры:
    
    self: ссылка на экземпляр текущего класса
    sender: ссылка на экземпляр окна Настрока подключений
    """
    def __init__(self, sender):
        self.sender = sender

    """
    Обработчик события перемещения окна Настройки подключений

    Параметры:
    
    self: ссылка на экземпляр текущего класса
    e: ссылка на экземпляр события окна Настрока подключений
    """
    def windowMoved(self, e):
        self.sender.windowPosX = e.X
        self.sender.windowPosY = e.Y

    """
    Обработчик события изменения размера окна Настройки подключений

    Параметры:
    
    self: ссылка на экземпляр текущего класса
    e: ссылка на экземпляр события окна Настрока подключений
    """
    def windowResized(self, e):
        X = e.Width
        Y = e.Height
        self.sender.windowWidth = X
        self.sender.windowHeight = Y
        self.sender.controlContainer.setPosSize(0, 0, X, Y, PS_SIZE) #PS_SIZE указывает, что при установке внешних границ окна учитываются только значения ширины (третий параметр) и высоты (четвёртый параметр) окна. 
