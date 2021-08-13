from Utility import Utility
from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore
import threading
import sys


from numpy import uint
from ui_Raid import Ui_MainWindow
from level_functions import Level_Function
import images_rc

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.level = Level_Function()
       
        #PAGE CHANGE
        self.ui.level_Btn.clicked.connect(lambda: self.ui.main_Stack.setCurrentWidget(self.ui.level_Page))
        self.ui.dungeon_Btn.clicked.connect(lambda: self.ui.main_Stack.setCurrentWidget(self.ui.dungeon_Page))
        self.ui.auto_Btn.clicked.connect(lambda: self.ui.main_Stack.setCurrentWidget(self.ui.other_Page))
        self.ui.cal_Btn.clicked.connect(lambda: self.ui.main_Stack.setCurrentWidget(self.ui.cal_Page))
        self.ui.info_Btn.clicked.connect(lambda: self.ui.main_Stack.setCurrentWidget(self.ui.info_Page))
        self.ui.dragon_Btn.clicked.connect(lambda: self.ui.dungeon_Stack.setCurrentWidget(self.ui.dragon_Page))
        self.ui.golem_Btn.clicked.connect(lambda: self.ui.dungeon_Stack.setCurrentWidget(self.ui.golem_Page))
        self.ui.knight_Btn.clicked.connect(lambda: self.ui.dungeon_Stack.setCurrentWidget(self.ui.knight_Page))

        #Info page
        self.ui.prank_Btn.clicked.connect(lambda: self.ui.prank_lbl.setText("Ihr seit auch so dumm, dass ihr mir vertraut!"))
        
        #Level page
        self.ui.start_level.clicked.connect(self.level_func)
        self.ui.stop_level.clicked.connect(lambda: self.level.set_finish(True))

        #Other stuff page
        self.ui.resize_Btn.clicked.connect(lambda: Utility.resize_window())

        self.show()

    def level_func(self):
        if(not self.level.is_finish()):
            pass
        else:
            self.level.set_finish(False)
            if(self.ui.level1_Radio.isChecked()):
                counter = 2
            if(self.ui.level2_Radio.isChecked()):
                counter = 8
            if(self.ui.level3_Radio.isChecked()):
                counter = 20
            if(self.ui.level4_Radio.isChecked()):
                counter = 47
            threading.Thread(target=self.level.run,args=(self.ui.counter_level_lbl,self.ui.status_level_lbl,counter,),daemon=True).start()
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())