import globalPluginHandler
import scriptHandler
import random
import ui
import winVersion
class GlobalPlugin(globalPluginHandler.GlobalPlugin):
    @scriptHandler.script(gesture="kb:NVDA+control+D", description="rolls the dice", category="Pax's toolkit")
    def script_dice(self,gesture):
     roll=random.randint(1,6)
     converted=str(roll)
     ui.message(converted)
    @scriptHandler.script(gesture="kb:NVDA+v", description="checks windows version", category="Pax's toolkit")
    def script_getWinVersion(self,gesture):
        v=winVersion.getWinVer()
        ver=str(v)
        ui.message(ver)