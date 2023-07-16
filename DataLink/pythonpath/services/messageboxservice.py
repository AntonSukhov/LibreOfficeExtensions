import uno

from com.sun.star.awt.MessageBoxType import INFOBOX
from com.sun.star.awt.MessageBoxButtons import BUTTONS_OK

#Сервис работы с окном сообщения
class MessageBoxService:
    
    """
    Отображает окно сообщения с указанным текстом, заголовком и типом.

    Параметры:

    text: текст сообщения
    caption: заголовок окна сообщения
    type: тип окна сообщения (см. https://www.openoffice.org/api/docs/common/ref/com/sun/star/awt/MessageBoxType.html)
    """
    @staticmethod
    def Show(text, caption, type = INFOBOX):
        context = uno.getComponentContext()
        sManager = context.ServiceManager
        toolkit = sManager.createInstance("com.sun.star.awt.Toolkit")
        msgbox = toolkit.createMessageBox(None, type, BUTTONS_OK, caption, text)
        return msgbox.execute()

