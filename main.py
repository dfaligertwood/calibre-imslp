from PyQt5.Qt import QDialog
from calibre_plugins.imslp.dialog import Ui_Dialog


class PetrucciDialog(QDialog):
    def __init__(self, gui, icon):
        QDialog.__init__(self, gui)
        self.gui = gui
        self.db = gui.current_db

        # Set up Designer UI
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        
        # Connect signals.
        self.searchButton.clicked.connect(self.doSearch())

    def doSearch(self):
        searchText = self.searchBox.text
        searchResults = self.searchFor(searchText)

