from com.sun.star.awt import Rectangle, WindowDescriptor
from com.sun.star.awt.WindowClass import MODALTOP as WC_MODALTOP
from com.sun.star.awt.WindowAttribute import BORDER as WA_BORDER, SHOW as WA_SHOW, SIZEABLE as WA_SIZEABLE, MOVEABLE as WA_MOVEABLE, CLOSEABLE as WA_CLOSEABLE
from com.sun.star.awt.PosSize import POSSIZE as PS_POSSIZE

#Окно Настройки подключений
class ConnectionsDialog:

    """
    Определяет для текущего класса атрибуты и их значения

    Параметры:
    
    self: ссылка на экземпляр текущего класса
    context: контекст текущего класса (соответствует контексту класса DataLink)
    desktopComponent: текущий компонент рабочего стола
    """
    def __init__(self, context, desktopComponent):
        self.context = context
        self.serviceManager = context.getServiceManager()
        self.desktopComponent = desktopComponent
        self.controlContainer = None
        self.windowHeight = 190
        self.windowWidth = 260
        self.windowPosX = 800
        self.windowPosY = 100
      
    """
    Создаёт окно Настройки подключений

    Параметры:
    
    self: ссылка на экземпляр текущего класса
    """
    def CreateWindow(self):
        containerWindow = self.desktopComponent.getCurrentController().Frame.ContainerWindow
        containerWindowToolkit = containerWindow.getToolkit()
        frame = self.serviceManager.createInstanceWithContext('com.sun.star.frame.Frame', self.context)
        bounds = Rectangle(self.windowPosX, self.windowPosY, self.windowWidth, self.windowHeight) #Задаёт положение и размер окна
        windowDescriptor = WindowDescriptor(WC_MODALTOP, 'floatingwindow', containerWindow, -1, bounds, WA_BORDER + WA_SHOW + WA_SIZEABLE + WA_MOVEABLE + WA_CLOSEABLE) #Значение -1 означает рабочий стол
        window = containerWindowToolkit.createWindow(windowDescriptor)
        frame.initialize(window) #Вызывается для инициализации фрейма внутри окна - окна контейнера. 
        controlContainer = self.serviceManager.createInstanceWithContext('com.sun.star.awt.UnoControlContainer', self.context)
        self.controlContainer = controlContainer
        controlContainerModel = self.serviceManager.createInstanceWithContext('com.sun.star.awt.UnoControlContainerModel', self.context)
        controlContainer.setModel(controlContainerModel)
        controlContainer.createPeer(containerWindowToolkit, window)
        controlContainer.setPosSize(0, 0, self.WindowWidth, self.WindowHeight, PS_POSSIZE)
        controlContainerModel.BackgroundColor = window.getAccessibleContext().Background #0xFAFAFA
        frame.setComponent(self.controlContainer, None)
        window.setVisible(True) #Показать окно