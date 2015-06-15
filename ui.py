from calibre.gui2.actions import InterfaceAction
from calibre_plugins.imslp.main import PetrucciDialog

class PetrucciPlugin(InterfaceAction):
    
    name = 'IMSLP Search'
    action_spec = ('IMSLP Search',
                   'images/icon.png',
                   'Search for scores on the Petrucci Music Library',
                   'Ctrl+Shift+I')

    def genesis(self):
        icon = get_icons('images/icon.png')
        self.qaction.setIcon(icon)
        self.qaction.triggered.connect(self.show_dialog)

    def show_dialog(self):
        base_plugin_object = self.interface_action_base_plugin
        d = PetrucciDialog(self.gui, self.qaction.icon())
        d.show()
