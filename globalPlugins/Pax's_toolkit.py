import globalPluginHandler
import gui
import scriptHandler
import random
import ui
class GlobalPlugin(globalPluginHandler.GlobalPlugin):
    @scriptHandler.script(gesture="kb:NVDA+control+D", description="rolls the dice", category="pax's toolkit")
    def script_dice(self,gesture):
     roll=random.randint(1,6)
     converted=str(roll)
     ui.message(converted)