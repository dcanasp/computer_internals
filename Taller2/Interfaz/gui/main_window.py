# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLayout,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QTableWidget, QTableWidgetItem, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1377, 959)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(0, 0))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        MainWindow.setStyleSheet(u"\n"
"        QMainWindow {\n"
"            background-color: #f0f0f0;\n"
"            font-family: 'Comic Sans MS';\n"
"        }\n"
"        QPushButton {\n"
"            background-color: #4CAF50;\n"
"            color: white;\n"
"            border-radius: 5px;\n"
"            padding: 8px;\n"
"            font-weight: bold;\n"
"        }\n"
"        QPushButton:hover {\n"
"            background-color: #45a049;\n"
"        }\n"
"        QTableWidget {\n"
"            background-color: white;\n"
"            alternate-background-color: #f8f8f8;\n"
"        }\n"
"        QTextEdit {\n"
"            background-color: white;\n"
"        }\n"
"        QLabel {\n"
"            font-weight: bold;\n"
"            color: #2c3e50;\n"
"        }\n"
"      ")
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.labelLibs = QLabel(self.centralwidget)
        self.labelLibs.setObjectName(u"labelLibs")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.labelLibs.sizePolicy().hasHeightForWidth())
        self.labelLibs.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.labelLibs, 1, 12, 1, 1)

        self.textEditCodigoFuente = QTextEdit(self.centralwidget)
        self.textEditCodigoFuente.setObjectName(u"textEditCodigoFuente")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy2.setHorizontalStretch(1)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.textEditCodigoFuente.sizePolicy().hasHeightForWidth())
        self.textEditCodigoFuente.setSizePolicy(sizePolicy2)
        self.textEditCodigoFuente.setMinimumSize(QSize(200, 0))
        self.textEditCodigoFuente.setMaximumSize(QSize(16777215, 16777215))
        self.textEditCodigoFuente.setFrameShape(QFrame.Shape.StyledPanel)
        self.textEditCodigoFuente.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)

        self.gridLayout.addWidget(self.textEditCodigoFuente, 3, 0, 1, 1)

        self.button_verTablaSimbolos = QPushButton(self.centralwidget)
        self.button_verTablaSimbolos.setObjectName(u"button_verTablaSimbolos")
        self.button_verTablaSimbolos.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.button_verTablaSimbolos.sizePolicy().hasHeightForWidth())
        self.button_verTablaSimbolos.setSizePolicy(sizePolicy1)
        self.button_verTablaSimbolos.setMaximumSize(QSize(16777215, 32))

        self.gridLayout.addWidget(self.button_verTablaSimbolos, 5, 1, 1, 1)

        self.button_preprocessor = QPushButton(self.centralwidget)
        self.button_preprocessor.setObjectName(u"button_preprocessor")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.button_preprocessor.sizePolicy().hasHeightForWidth())
        self.button_preprocessor.setSizePolicy(sizePolicy3)

        self.gridLayout.addWidget(self.button_preprocessor, 4, 0, 1, 1)

        self.labelMaquinaRelocalizable = QLabel(self.centralwidget)
        self.labelMaquinaRelocalizable.setObjectName(u"labelMaquinaRelocalizable")
        sizePolicy1.setHeightForWidth(self.labelMaquinaRelocalizable.sizePolicy().hasHeightForWidth())
        self.labelMaquinaRelocalizable.setSizePolicy(sizePolicy1)
        self.labelMaquinaRelocalizable.setMinimumSize(QSize(0, 0))

        self.gridLayout.addWidget(self.labelMaquinaRelocalizable, 1, 4, 1, 1)

        self.button_compiler = QPushButton(self.centralwidget)
        self.button_compiler.setObjectName(u"button_compiler")
        self.button_compiler.setEnabled(True)
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.button_compiler.sizePolicy().hasHeightForWidth())
        self.button_compiler.setSizePolicy(sizePolicy4)

        self.gridLayout.addWidget(self.button_compiler, 4, 1, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy5)
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_4)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.verticalLayout_3.addWidget(self.label)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.button_siguiente_instruccion = QPushButton(self.centralwidget)
        self.button_siguiente_instruccion.setObjectName(u"button_siguiente_instruccion")
        self.button_siguiente_instruccion.setStyleSheet(u"font: 75 12pt \"MS Shell Dlg 2\";")
        self.button_siguiente_instruccion.setAutoDefault(False)
        self.button_siguiente_instruccion.setFlat(False)

        self.verticalLayout_4.addWidget(self.button_siguiente_instruccion)

        self.button_ultima_instruccion = QPushButton(self.centralwidget)
        self.button_ultima_instruccion.setObjectName(u"button_ultima_instruccion")
        self.button_ultima_instruccion.setStyleSheet(u"font: 75 12pt \"MS Shell Dlg 2\";")

        self.verticalLayout_4.addWidget(self.button_ultima_instruccion)

        self.button_reiniciar = QPushButton(self.centralwidget)
        self.button_reiniciar.setObjectName(u"button_reiniciar")
        self.button_reiniciar.setStyleSheet(u"font: 75 12pt \"MS Shell Dlg 2\";")

        self.verticalLayout_4.addWidget(self.button_reiniciar)


        self.verticalLayout_3.addLayout(self.verticalLayout_4)


        self.gridLayout.addLayout(self.verticalLayout_3, 6, 3, 1, 1)

        self.textEditCodigoFuenteModificado = QTextEdit(self.centralwidget)
        self.textEditCodigoFuenteModificado.setObjectName(u"textEditCodigoFuenteModificado")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        sizePolicy6.setHorizontalStretch(1)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.textEditCodigoFuenteModificado.sizePolicy().hasHeightForWidth())
        self.textEditCodigoFuenteModificado.setSizePolicy(sizePolicy6)
        self.textEditCodigoFuenteModificado.setMinimumSize(QSize(200, 0))
        self.textEditCodigoFuenteModificado.setMaximumSize(QSize(16777215, 16777215))
        self.textEditCodigoFuenteModificado.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)

        self.gridLayout.addWidget(self.textEditCodigoFuenteModificado, 3, 1, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.spinBox_pos_enlazar = QSpinBox(self.centralwidget)
        self.spinBox_pos_enlazar.setObjectName(u"spinBox_pos_enlazar")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.spinBox_pos_enlazar.sizePolicy().hasHeightForWidth())
        self.spinBox_pos_enlazar.setSizePolicy(sizePolicy7)
        self.spinBox_pos_enlazar.setMaximumSize(QSize(16777215, 30))
        self.spinBox_pos_enlazar.setMaximum(1024)

        self.horizontalLayout_2.addWidget(self.spinBox_pos_enlazar)

        self.button_linker = QPushButton(self.centralwidget)
        self.button_linker.setObjectName(u"button_linker")
        self.button_linker.setEnabled(True)
        self.button_linker.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_2.addWidget(self.button_linker)


        self.gridLayout.addLayout(self.horizontalLayout_2, 4, 12, 1, 1)

        self.labelProgramaFuente = QLabel(self.centralwidget)
        self.labelProgramaFuente.setObjectName(u"labelProgramaFuente")
        sizePolicy1.setHeightForWidth(self.labelProgramaFuente.sizePolicy().hasHeightForWidth())
        self.labelProgramaFuente.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.labelProgramaFuente, 1, 0, 1, 1)

        self.labelProgramaFuenteModificado = QLabel(self.centralwidget)
        self.labelProgramaFuenteModificado.setObjectName(u"labelProgramaFuenteModificado")
        sizePolicy1.setHeightForWidth(self.labelProgramaFuenteModificado.sizePolicy().hasHeightForWidth())
        self.labelProgramaFuenteModificado.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.labelProgramaFuenteModificado, 1, 1, 1, 1)

        self.textEditCodigoReloc = QTextEdit(self.centralwidget)
        self.textEditCodigoReloc.setObjectName(u"textEditCodigoReloc")
        sizePolicy6.setHeightForWidth(self.textEditCodigoReloc.sizePolicy().hasHeightForWidth())
        self.textEditCodigoReloc.setSizePolicy(sizePolicy6)
        self.textEditCodigoReloc.setMinimumSize(QSize(200, 0))
        self.textEditCodigoReloc.setMaximumSize(QSize(16777215, 16777215))
        self.textEditCodigoReloc.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)

        self.gridLayout.addWidget(self.textEditCodigoReloc, 3, 4, 1, 1)

        self.textEditCodigoASM = QTextEdit(self.centralwidget)
        self.textEditCodigoASM.setObjectName(u"textEditCodigoASM")
        sizePolicy6.setHeightForWidth(self.textEditCodigoASM.sizePolicy().hasHeightForWidth())
        self.textEditCodigoASM.setSizePolicy(sizePolicy6)
        self.textEditCodigoASM.setMinimumSize(QSize(200, 0))
        self.textEditCodigoASM.setMaximumSize(QSize(16777215, 16777215))
        self.textEditCodigoASM.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)

        self.gridLayout.addWidget(self.textEditCodigoASM, 3, 3, 1, 1)

        self.textEditCodigoLib = QTextEdit(self.centralwidget)
        self.textEditCodigoLib.setObjectName(u"textEditCodigoLib")
        sizePolicy6.setHeightForWidth(self.textEditCodigoLib.sizePolicy().hasHeightForWidth())
        self.textEditCodigoLib.setSizePolicy(sizePolicy6)
        self.textEditCodigoLib.setMinimumSize(QSize(200, 0))
        self.textEditCodigoLib.setMaximumSize(QSize(16777215, 16777215))
        self.textEditCodigoLib.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)

        self.gridLayout.addWidget(self.textEditCodigoLib, 3, 12, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.label_ram = QLabel(self.centralwidget)
        self.label_ram.setObjectName(u"label_ram")
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.label_ram.sizePolicy().hasHeightForWidth())
        self.label_ram.setSizePolicy(sizePolicy8)
        self.label_ram.setMaximumSize(QSize(256, 26))

        self.verticalLayout.addWidget(self.label_ram)

        self.table_ram = QTableWidget(self.centralwidget)
        if (self.table_ram.columnCount() < 1):
            self.table_ram.setColumnCount(1)
        font = QFont()
        font.setPointSize(12)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setText(u"Contenido");
        __qtablewidgetitem.setFont(font);
        self.table_ram.setHorizontalHeaderItem(0, __qtablewidgetitem)
        if (self.table_ram.rowCount() < 8192):
            self.table_ram.setRowCount(8192)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_ram.setItem(0, 0, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table_ram.setItem(1, 0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table_ram.setItem(2, 0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.table_ram.setItem(3, 0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.table_ram.setItem(4, 0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.table_ram.setItem(5, 0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.table_ram.setItem(6, 0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.table_ram.setItem(7, 0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.table_ram.setItem(8, 0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.table_ram.setItem(9, 0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.table_ram.setItem(10, 0, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.table_ram.setItem(11, 0, __qtablewidgetitem12)
        self.table_ram.setObjectName(u"table_ram")
        self.table_ram.setEnabled(True)
        sizePolicy9 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.table_ram.sizePolicy().hasHeightForWidth())
        self.table_ram.setSizePolicy(sizePolicy9)
        self.table_ram.setMinimumSize(QSize(0, 300))
        self.table_ram.setMaximumSize(QSize(16777215, 16777215))
#if QT_CONFIG(accessibility)
        self.table_ram.setAccessibleName(u"")
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
        self.table_ram.setAccessibleDescription(u"")
#endif // QT_CONFIG(accessibility)
        self.table_ram.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";")
        self.table_ram.setFrameShape(QFrame.Shape.StyledPanel)
        self.table_ram.setFrameShadow(QFrame.Shadow.Sunken)
        self.table_ram.setLineWidth(1)
        self.table_ram.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.table_ram.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.table_ram.setShowGrid(True)
        self.table_ram.setSortingEnabled(False)
        self.table_ram.setWordWrap(False)
        self.table_ram.setCornerButtonEnabled(False)
        self.table_ram.setRowCount(8192)
        self.table_ram.horizontalHeader().setCascadingSectionResizes(False)
        self.table_ram.horizontalHeader().setDefaultSectionSize(189)

        self.verticalLayout.addWidget(self.table_ram)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.label_registros = QLabel(self.centralwidget)
        self.label_registros.setObjectName(u"label_registros")
        sizePolicy10 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.label_registros.sizePolicy().hasHeightForWidth())
        self.label_registros.setSizePolicy(sizePolicy10)
        self.label_registros.setMaximumSize(QSize(256, 16777215))

        self.verticalLayout_2.addWidget(self.label_registros)

        self.table_registros = QTableWidget(self.centralwidget)
        if (self.table_registros.columnCount() < 2):
            self.table_registros.setColumnCount(2)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.table_registros.setHorizontalHeaderItem(0, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.table_registros.setHorizontalHeaderItem(1, __qtablewidgetitem14)
        if (self.table_registros.rowCount() < 4):
            self.table_registros.setRowCount(4)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.table_registros.setVerticalHeaderItem(0, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.table_registros.setVerticalHeaderItem(1, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.table_registros.setVerticalHeaderItem(2, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.table_registros.setVerticalHeaderItem(3, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.table_registros.setItem(0, 0, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.table_registros.setItem(1, 0, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.table_registros.setItem(2, 0, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.table_registros.setItem(3, 0, __qtablewidgetitem22)
        self.table_registros.setObjectName(u"table_registros")
        sizePolicy11 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        sizePolicy11.setHorizontalStretch(0)
        sizePolicy11.setVerticalStretch(0)
        sizePolicy11.setHeightForWidth(self.table_registros.sizePolicy().hasHeightForWidth())
        self.table_registros.setSizePolicy(sizePolicy11)
        self.table_registros.setMinimumSize(QSize(257, 120))
        self.table_registros.setMaximumSize(QSize(16777215, 120))
        self.table_registros.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";")
        self.table_registros.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.table_registros.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.table_registros.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.table_registros.horizontalHeader().setVisible(False)
        self.table_registros.horizontalHeader().setDefaultSectionSize(117)
        self.table_registros.horizontalHeader().setHighlightSections(True)

        self.verticalLayout_2.addWidget(self.table_registros)

        self.label_unidad_control = QLabel(self.centralwidget)
        self.label_unidad_control.setObjectName(u"label_unidad_control")
        sizePolicy10.setHeightForWidth(self.label_unidad_control.sizePolicy().hasHeightForWidth())
        self.label_unidad_control.setSizePolicy(sizePolicy10)
        self.label_unidad_control.setMinimumSize(QSize(0, 0))
        self.label_unidad_control.setMaximumSize(QSize(256, 30))
        self.label_unidad_control.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.verticalLayout_2.addWidget(self.label_unidad_control)

        self.table_unidad_control = QTableWidget(self.centralwidget)
        if (self.table_unidad_control.columnCount() < 1):
            self.table_unidad_control.setColumnCount(1)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.table_unidad_control.setHorizontalHeaderItem(0, __qtablewidgetitem23)
        if (self.table_unidad_control.rowCount() < 2):
            self.table_unidad_control.setRowCount(2)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.table_unidad_control.setVerticalHeaderItem(0, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.table_unidad_control.setVerticalHeaderItem(1, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.table_unidad_control.setItem(0, 0, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.table_unidad_control.setItem(1, 0, __qtablewidgetitem27)
        self.table_unidad_control.setObjectName(u"table_unidad_control")
        sizePolicy10.setHeightForWidth(self.table_unidad_control.sizePolicy().hasHeightForWidth())
        self.table_unidad_control.setSizePolicy(sizePolicy10)
        self.table_unidad_control.setMinimumSize(QSize(257, 0))
        self.table_unidad_control.setMaximumSize(QSize(16777215, 60))
        self.table_unidad_control.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";")
        self.table_unidad_control.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.table_unidad_control.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.table_unidad_control.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.table_unidad_control.horizontalHeader().setVisible(False)
        self.table_unidad_control.horizontalHeader().setDefaultSectionSize(225)

        self.verticalLayout_2.addWidget(self.table_unidad_control)

        self.label_alu = QLabel(self.centralwidget)
        self.label_alu.setObjectName(u"label_alu")
        sizePolicy10.setHeightForWidth(self.label_alu.sizePolicy().hasHeightForWidth())
        self.label_alu.setSizePolicy(sizePolicy10)
        self.label_alu.setMinimumSize(QSize(0, 26))
        self.label_alu.setMaximumSize(QSize(256, 30))
        self.label_alu.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.verticalLayout_2.addWidget(self.label_alu)

        self.table_alu = QTableWidget(self.centralwidget)
        if (self.table_alu.columnCount() < 2):
            self.table_alu.setColumnCount(2)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.table_alu.setHorizontalHeaderItem(0, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.table_alu.setHorizontalHeaderItem(1, __qtablewidgetitem29)
        if (self.table_alu.rowCount() < 4):
            self.table_alu.setRowCount(4)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.table_alu.setItem(0, 0, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.table_alu.setItem(1, 0, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.table_alu.setItem(2, 0, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.table_alu.setItem(3, 0, __qtablewidgetitem33)
        self.table_alu.setObjectName(u"table_alu")
        sizePolicy10.setHeightForWidth(self.table_alu.sizePolicy().hasHeightForWidth())
        self.table_alu.setSizePolicy(sizePolicy10)
        self.table_alu.setMinimumSize(QSize(257, 120))
        self.table_alu.setMaximumSize(QSize(16777215, 120))
        self.table_alu.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";")
        self.table_alu.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.table_alu.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.table_alu.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.table_alu.horizontalHeader().setVisible(False)
        self.table_alu.horizontalHeader().setDefaultSectionSize(118)

        self.verticalLayout_2.addWidget(self.table_alu)

        self.verticalLayout_2.setStretch(2, 1)
        self.verticalLayout_2.setStretch(3, 1)
        self.verticalLayout_2.setStretch(4, 1)
        self.verticalLayout_2.setStretch(5, 1)

        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.gridLayout.addLayout(self.horizontalLayout, 6, 0, 1, 2)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)

        self.verticalLayout_5.addWidget(self.label_2)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        sizePolicy3.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy3)

        self.verticalLayout_5.addWidget(self.label_3)

        self.textEditInput = QTextEdit(self.centralwidget)
        self.textEditInput.setObjectName(u"textEditInput")
        sizePolicy12 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy12.setHorizontalStretch(0)
        sizePolicy12.setVerticalStretch(0)
        sizePolicy12.setHeightForWidth(self.textEditInput.sizePolicy().hasHeightForWidth())
        self.textEditInput.setSizePolicy(sizePolicy12)

        self.verticalLayout_5.addWidget(self.textEditInput)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        sizePolicy3.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy3)

        self.verticalLayout_5.addWidget(self.label_5)

        self.textEditPCOutput = QTextEdit(self.centralwidget)
        self.textEditPCOutput.setObjectName(u"textEditPCOutput")
        sizePolicy12.setHeightForWidth(self.textEditPCOutput.sizePolicy().hasHeightForWidth())
        self.textEditPCOutput.setSizePolicy(sizePolicy12)
        self.textEditPCOutput.setMinimumSize(QSize(0, 0))
        self.textEditPCOutput.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_5.addWidget(self.textEditPCOutput)


        self.gridLayout.addLayout(self.verticalLayout_5, 6, 4, 1, 1)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer)

        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_6.addWidget(self.label_7)

        self.button_cargar_ex1 = QPushButton(self.centralwidget)
        self.button_cargar_ex1.setObjectName(u"button_cargar_ex1")

        self.verticalLayout_6.addWidget(self.button_cargar_ex1)

        self.button_cargar_ex2 = QPushButton(self.centralwidget)
        self.button_cargar_ex2.setObjectName(u"button_cargar_ex2")

        self.verticalLayout_6.addWidget(self.button_cargar_ex2)

        self.button_cargar_ex3 = QPushButton(self.centralwidget)
        self.button_cargar_ex3.setObjectName(u"button_cargar_ex3")

        self.verticalLayout_6.addWidget(self.button_cargar_ex3)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")

        self.verticalLayout_6.addLayout(self.verticalLayout_7)


        self.gridLayout.addLayout(self.verticalLayout_6, 6, 12, 1, 1)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        sizePolicy4.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy4)

        self.gridLayout.addWidget(self.label_6, 4, 4, 1, 1)

        self.button_assembler = QPushButton(self.centralwidget)
        self.button_assembler.setObjectName(u"button_assembler")
        self.button_assembler.setEnabled(True)
        sizePolicy7.setHeightForWidth(self.button_assembler.sizePolicy().hasHeightForWidth())
        self.button_assembler.setSizePolicy(sizePolicy7)

        self.gridLayout.addWidget(self.button_assembler, 4, 3, 1, 1)

        self.labelASM = QLabel(self.centralwidget)
        self.labelASM.setObjectName(u"labelASM")
        sizePolicy1.setHeightForWidth(self.labelASM.sizePolicy().hasHeightForWidth())
        self.labelASM.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.labelASM, 1, 3, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.textEditCodigoFuente, self.textEditCodigoFuenteModificado)
        QWidget.setTabOrder(self.textEditCodigoFuenteModificado, self.textEditCodigoASM)
        QWidget.setTabOrder(self.textEditCodigoASM, self.textEditCodigoReloc)
        QWidget.setTabOrder(self.textEditCodigoReloc, self.textEditCodigoLib)
        QWidget.setTabOrder(self.textEditCodigoLib, self.button_preprocessor)
        QWidget.setTabOrder(self.button_preprocessor, self.button_compiler)
        QWidget.setTabOrder(self.button_compiler, self.button_verTablaSimbolos)
        QWidget.setTabOrder(self.button_verTablaSimbolos, self.button_assembler)
        QWidget.setTabOrder(self.button_assembler, self.spinBox_pos_enlazar)
        QWidget.setTabOrder(self.spinBox_pos_enlazar, self.button_linker)
        QWidget.setTabOrder(self.button_linker, self.table_ram)
        QWidget.setTabOrder(self.table_ram, self.table_unidad_control)
        QWidget.setTabOrder(self.table_unidad_control, self.table_alu)

        self.retranslateUi(MainWindow)

        self.button_siguiente_instruccion.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Sistema de Procesamiento", None))
        self.labelLibs.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#aa00ff;\">+ Librer\u00edas</span></p></body></html>", None))
        self.textEditCodigoFuente.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.button_verTablaSimbolos.setText(QCoreApplication.translate("MainWindow", u"Ver tabla de S\u00edmbolos", None))
        self.button_preprocessor.setText(QCoreApplication.translate("MainWindow", u"Preprocesar", None))
        self.labelMaquinaRelocalizable.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\"><span style=\" font-size:12pt; color:#aa00ff;\">C\u00f3digo m\u00e1quina relocalizable</span></p></body></html>", None))
        self.button_compiler.setText(QCoreApplication.translate("MainWindow", u"Compilar", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Sistema de procesamiento de lenguaje\n"
" \n"
"David Alfonso Ca\u00f1as Palomino\n"
"Esteban Lopez Barreto\n"
"Santiago Reyes Ochoa\n"
"Juan Esteban Pe\u00f1a Burgos\n"
"Gabriela Guzm\u00e1n Rivera\n"
"Gabriela Gallegos Rubio\n"
"\n"
"Universidad Nacional de Colombia\n"
"Facultad de Ingenier\u00eda\n"
"Lenguajes de programaci\u00f3n (2025966)\n"
"Profesor Jorge Eduardo Ortiz Trivi\u00f1o\n"
"Bogot\u00e1, D.C. Colombia\n"
"2024 - 2S", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; color:#5555ff;\">Control de Ejecuci\u00f3n</span></p></body></html>", None))
        self.button_siguiente_instruccion.setText(QCoreApplication.translate("MainWindow", u"Siguiente instrucci\u00f3n", None))
        self.button_ultima_instruccion.setText(QCoreApplication.translate("MainWindow", u"Saltar al final", None))
        self.button_reiniciar.setText(QCoreApplication.translate("MainWindow", u"Reiniciar Todo", None))
        self.textEditCodigoFuenteModificado.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.button_linker.setText(QCoreApplication.translate("MainWindow", u"Enlazar y Cargar", None))
        self.labelProgramaFuente.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; color:#2980b9;\">Programa fuente</span></p></body></html>", None))
        self.labelProgramaFuenteModificado.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; color:#2980b9;\">Programa fuente modificado</span></p></body></html>", None))
        self.label_ram.setText(QCoreApplication.translate("MainWindow", u"<html><div align='center'><span style='font-size:14pt; color:#2c3e50;'>RAM</span></div></html>", None))

        __sortingEnabled = self.table_ram.isSortingEnabled()
        self.table_ram.setSortingEnabled(False)
        self.table_ram.setSortingEnabled(__sortingEnabled)

        self.label_registros.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; color:#c0392b;\">Registros</span></p></body></html>", None))
        ___qtablewidgetitem = self.table_registros.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"BINARIO", None));
        ___qtablewidgetitem1 = self.table_registros.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"DECIMAL", None));
        ___qtablewidgetitem2 = self.table_registros.verticalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"C", None));
        ___qtablewidgetitem3 = self.table_registros.verticalHeaderItem(1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"P", None));
        ___qtablewidgetitem4 = self.table_registros.verticalHeaderItem(2)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"N", None));
        ___qtablewidgetitem5 = self.table_registros.verticalHeaderItem(3)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"D", None));

        __sortingEnabled1 = self.table_registros.isSortingEnabled()
        self.table_registros.setSortingEnabled(False)
        self.table_registros.setSortingEnabled(__sortingEnabled1)

        self.label_unidad_control.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; color:#2c3e50;\">Unidad de Control</span></p></body></html>", None))
        ___qtablewidgetitem6 = self.table_unidad_control.horizontalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"BINARIO", None));
        ___qtablewidgetitem7 = self.table_unidad_control.verticalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"IC", None));
        ___qtablewidgetitem8 = self.table_unidad_control.verticalHeaderItem(1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"CP", None));

        __sortingEnabled2 = self.table_unidad_control.isSortingEnabled()
        self.table_unidad_control.setSortingEnabled(False)
        self.table_unidad_control.setSortingEnabled(__sortingEnabled2)

        self.label_alu.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; color:#aa00ff;\">Indicadores ALU</span></p></body></html>", None))
        ___qtablewidgetitem9 = self.table_alu.horizontalHeaderItem(0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"BINARIO", None));
        ___qtablewidgetitem10 = self.table_alu.horizontalHeaderItem(1)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"DECIMAL", None));

        __sortingEnabled3 = self.table_alu.isSortingEnabled()
        self.table_alu.setSortingEnabled(False)
        self.table_alu.setSortingEnabled(__sortingEnabled3)

        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; color:#ff0000;\">I/O</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Entrada del computador", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Salida del computador", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; color:#5555ff;\">Ejemplos</span></p></body></html>", None))
        self.button_cargar_ex1.setText(QCoreApplication.translate("MainWindow", u"Cargar Ejemplo 1", None))
        self.button_cargar_ex2.setText(QCoreApplication.translate("MainWindow", u"Cargar Ejemplo 2", None))
        self.button_cargar_ex3.setText(QCoreApplication.translate("MainWindow", u"Cargar Ejemplo 3", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\">Posici\u00f3n de memoria inicial:</p></body></html>", None))
        self.button_assembler.setText(QCoreApplication.translate("MainWindow", u"Ensamblar", None))
        self.labelASM.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; color:#27ae60;\">Programa en Assembler</span></p></body></html>", None))
    # retranslateUi

