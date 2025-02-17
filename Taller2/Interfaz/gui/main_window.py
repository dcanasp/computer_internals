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
        MainWindow.resize(1334, 840)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
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
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy1)
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.codeHorizLayout = QHBoxLayout()
        self.codeHorizLayout.setObjectName(u"codeHorizLayout")
        self.layfuent = QVBoxLayout()
        self.layfuent.setObjectName(u"layfuent")
        self.labelProgramaFuente = QLabel(self.centralwidget)
        self.labelProgramaFuente.setObjectName(u"labelProgramaFuente")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.labelProgramaFuente.sizePolicy().hasHeightForWidth())
        self.labelProgramaFuente.setSizePolicy(sizePolicy2)
        self.labelProgramaFuente.setMaximumSize(QSize(16777215, 16777215))

        self.layfuent.addWidget(self.labelProgramaFuente)

        self.textEditCodigoFuente = QTextEdit(self.centralwidget)
        self.textEditCodigoFuente.setObjectName(u"textEditCodigoFuente")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.textEditCodigoFuente.sizePolicy().hasHeightForWidth())
        self.textEditCodigoFuente.setSizePolicy(sizePolicy3)
        self.textEditCodigoFuente.setMinimumSize(QSize(0, 180))
        self.textEditCodigoFuente.setMaximumSize(QSize(16777215, 16777215))
        self.textEditCodigoFuente.setFrameShape(QFrame.Shape.StyledPanel)
        self.textEditCodigoFuente.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)

        self.layfuent.addWidget(self.textEditCodigoFuente)

        self.button_preprocessor = QPushButton(self.centralwidget)
        self.button_preprocessor.setObjectName(u"button_preprocessor")
        sizePolicy2.setHeightForWidth(self.button_preprocessor.sizePolicy().hasHeightForWidth())
        self.button_preprocessor.setSizePolicy(sizePolicy2)
        self.button_preprocessor.setMaximumSize(QSize(16777215, 16777215))

        self.layfuent.addWidget(self.button_preprocessor)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.layfuent.addItem(self.verticalSpacer_3)


        self.codeHorizLayout.addLayout(self.layfuent)

        self.layfuentemod = QVBoxLayout()
        self.layfuentemod.setObjectName(u"layfuentemod")
        self.labelProgramaFuenteModificado = QLabel(self.centralwidget)
        self.labelProgramaFuenteModificado.setObjectName(u"labelProgramaFuenteModificado")
        sizePolicy2.setHeightForWidth(self.labelProgramaFuenteModificado.sizePolicy().hasHeightForWidth())
        self.labelProgramaFuenteModificado.setSizePolicy(sizePolicy2)
        self.labelProgramaFuenteModificado.setMaximumSize(QSize(16777215, 16777215))

        self.layfuentemod.addWidget(self.labelProgramaFuenteModificado)

        self.textEditCodigoFuenteModificado = QTextEdit(self.centralwidget)
        self.textEditCodigoFuenteModificado.setObjectName(u"textEditCodigoFuenteModificado")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.textEditCodigoFuenteModificado.sizePolicy().hasHeightForWidth())
        self.textEditCodigoFuenteModificado.setSizePolicy(sizePolicy4)
        self.textEditCodigoFuenteModificado.setMinimumSize(QSize(0, 180))
        self.textEditCodigoFuenteModificado.setMaximumSize(QSize(16777215, 16777215))
        self.textEditCodigoFuenteModificado.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)

        self.layfuentemod.addWidget(self.textEditCodigoFuenteModificado)

        self.button_compiler = QPushButton(self.centralwidget)
        self.button_compiler.setObjectName(u"button_compiler")
        self.button_compiler.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.button_compiler.sizePolicy().hasHeightForWidth())
        self.button_compiler.setSizePolicy(sizePolicy2)
        self.button_compiler.setMaximumSize(QSize(16777215, 16777215))

        self.layfuentemod.addWidget(self.button_compiler)

        self.button_verTablaSimbolos = QPushButton(self.centralwidget)
        self.button_verTablaSimbolos.setObjectName(u"button_verTablaSimbolos")
        self.button_verTablaSimbolos.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.button_verTablaSimbolos.sizePolicy().hasHeightForWidth())
        self.button_verTablaSimbolos.setSizePolicy(sizePolicy2)
        self.button_verTablaSimbolos.setMaximumSize(QSize(16777215, 32))

        self.layfuentemod.addWidget(self.button_verTablaSimbolos)

        self.verticalSpacer_7 = QSpacerItem(20, 2, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.layfuentemod.addItem(self.verticalSpacer_7)


        self.codeHorizLayout.addLayout(self.layfuentemod)

        self.layasm = QVBoxLayout()
        self.layasm.setObjectName(u"layasm")
        self.labelASM = QLabel(self.centralwidget)
        self.labelASM.setObjectName(u"labelASM")
        sizePolicy2.setHeightForWidth(self.labelASM.sizePolicy().hasHeightForWidth())
        self.labelASM.setSizePolicy(sizePolicy2)

        self.layasm.addWidget(self.labelASM)

        self.textEditCodigoASM = QTextEdit(self.centralwidget)
        self.textEditCodigoASM.setObjectName(u"textEditCodigoASM")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.textEditCodigoASM.sizePolicy().hasHeightForWidth())
        self.textEditCodigoASM.setSizePolicy(sizePolicy5)
        self.textEditCodigoASM.setMinimumSize(QSize(0, 180))
        self.textEditCodigoASM.setMaximumSize(QSize(16777215, 16777215))
        self.textEditCodigoASM.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)

        self.layasm.addWidget(self.textEditCodigoASM)

        self.button_assembler = QPushButton(self.centralwidget)
        self.button_assembler.setObjectName(u"button_assembler")
        self.button_assembler.setEnabled(True)
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.button_assembler.sizePolicy().hasHeightForWidth())
        self.button_assembler.setSizePolicy(sizePolicy6)

        self.layasm.addWidget(self.button_assembler)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.layasm.addItem(self.verticalSpacer_4)


        self.codeHorizLayout.addLayout(self.layasm)

        self.laymaqreloc = QVBoxLayout()
        self.laymaqreloc.setObjectName(u"laymaqreloc")
        self.labelMaquinaRelocalizable = QLabel(self.centralwidget)
        self.labelMaquinaRelocalizable.setObjectName(u"labelMaquinaRelocalizable")
        sizePolicy2.setHeightForWidth(self.labelMaquinaRelocalizable.sizePolicy().hasHeightForWidth())
        self.labelMaquinaRelocalizable.setSizePolicy(sizePolicy2)
        self.labelMaquinaRelocalizable.setMinimumSize(QSize(0, 0))

        self.laymaqreloc.addWidget(self.labelMaquinaRelocalizable)

        self.textEditCodigoReloc = QTextEdit(self.centralwidget)
        self.textEditCodigoReloc.setObjectName(u"textEditCodigoReloc")
        sizePolicy5.setHeightForWidth(self.textEditCodigoReloc.sizePolicy().hasHeightForWidth())
        self.textEditCodigoReloc.setSizePolicy(sizePolicy5)
        self.textEditCodigoReloc.setMinimumSize(QSize(0, 180))
        self.textEditCodigoReloc.setMaximumSize(QSize(16777215, 16777215))
        self.textEditCodigoReloc.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)

        self.laymaqreloc.addWidget(self.textEditCodigoReloc)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        sizePolicy6.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy6)

        self.laymaqreloc.addWidget(self.label_6)

        self.verticalSpacer_5 = QSpacerItem(20, 56, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.laymaqreloc.addItem(self.verticalSpacer_5)


        self.codeHorizLayout.addLayout(self.laymaqreloc)

        self.laylibs = QVBoxLayout()
        self.laylibs.setObjectName(u"laylibs")
        self.labelLibs = QLabel(self.centralwidget)
        self.labelLibs.setObjectName(u"labelLibs")
        sizePolicy2.setHeightForWidth(self.labelLibs.sizePolicy().hasHeightForWidth())
        self.labelLibs.setSizePolicy(sizePolicy2)

        self.laylibs.addWidget(self.labelLibs)

        self.textEditCodigoLib = QTextEdit(self.centralwidget)
        self.textEditCodigoLib.setObjectName(u"textEditCodigoLib")
        sizePolicy5.setHeightForWidth(self.textEditCodigoLib.sizePolicy().hasHeightForWidth())
        self.textEditCodigoLib.setSizePolicy(sizePolicy5)
        self.textEditCodigoLib.setMinimumSize(QSize(0, 180))
        self.textEditCodigoLib.setMaximumSize(QSize(16777215, 16777215))
        self.textEditCodigoLib.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)

        self.laylibs.addWidget(self.textEditCodigoLib)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.spinBox_pos_enlazar = QSpinBox(self.centralwidget)
        self.spinBox_pos_enlazar.setObjectName(u"spinBox_pos_enlazar")
        sizePolicy6.setHeightForWidth(self.spinBox_pos_enlazar.sizePolicy().hasHeightForWidth())
        self.spinBox_pos_enlazar.setSizePolicy(sizePolicy6)
        self.spinBox_pos_enlazar.setMaximumSize(QSize(16777215, 30))
        self.spinBox_pos_enlazar.setMaximum(8192)

        self.horizontalLayout_2.addWidget(self.spinBox_pos_enlazar)

        self.button_linker = QPushButton(self.centralwidget)
        self.button_linker.setObjectName(u"button_linker")
        self.button_linker.setEnabled(True)
        sizePolicy6.setHeightForWidth(self.button_linker.sizePolicy().hasHeightForWidth())
        self.button_linker.setSizePolicy(sizePolicy6)
        self.button_linker.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_2.addWidget(self.button_linker)


        self.laylibs.addLayout(self.horizontalLayout_2)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.laylibs.addItem(self.verticalSpacer_6)


        self.codeHorizLayout.addLayout(self.laylibs)


        self.gridLayout.addLayout(self.codeHorizLayout, 3, 0, 1, 6)

        self.detailshorizlay = QHBoxLayout()
        self.detailshorizlay.setObjectName(u"detailshorizlay")
        self.layram = QVBoxLayout()
        self.layram.setObjectName(u"layram")
        self.layram.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.label_ram = QLabel(self.centralwidget)
        self.label_ram.setObjectName(u"label_ram")
        sizePolicy2.setHeightForWidth(self.label_ram.sizePolicy().hasHeightForWidth())
        self.label_ram.setSizePolicy(sizePolicy2)
        self.label_ram.setMaximumSize(QSize(16777215, 16777215))

        self.layram.addWidget(self.label_ram)

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
        sizePolicy1.setHeightForWidth(self.table_ram.sizePolicy().hasHeightForWidth())
        self.table_ram.setSizePolicy(sizePolicy1)
        self.table_ram.setMinimumSize(QSize(360, 200))
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
        self.table_ram.horizontalHeader().setDefaultSectionSize(293)

        self.layram.addWidget(self.table_ram)


        self.detailshorizlay.addLayout(self.layram)

        self.laydetails = QVBoxLayout()
        self.laydetails.setObjectName(u"laydetails")
        self.laydetails.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.label_registros_2 = QLabel(self.centralwidget)
        self.label_registros_2.setObjectName(u"label_registros_2")
        sizePolicy6.setHeightForWidth(self.label_registros_2.sizePolicy().hasHeightForWidth())
        self.label_registros_2.setSizePolicy(sizePolicy6)
        self.label_registros_2.setMinimumSize(QSize(0, 0))
        self.label_registros_2.setMaximumSize(QSize(16777215, 16777215))
        self.label_registros_2.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.laydetails.addWidget(self.label_registros_2)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.label_registros_reservados = QLabel(self.centralwidget)
        self.label_registros_reservados.setObjectName(u"label_registros_reservados")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.label_registros_reservados.sizePolicy().hasHeightForWidth())
        self.label_registros_reservados.setSizePolicy(sizePolicy7)
        self.label_registros_reservados.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_7.addWidget(self.label_registros_reservados)

        self.table_registros = QTableWidget(self.centralwidget)
        if (self.table_registros.columnCount() < 1):
            self.table_registros.setColumnCount(1)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.table_registros.setHorizontalHeaderItem(0, __qtablewidgetitem13)
        if (self.table_registros.rowCount() < 4):
            self.table_registros.setRowCount(4)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.table_registros.setVerticalHeaderItem(0, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.table_registros.setVerticalHeaderItem(1, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.table_registros.setVerticalHeaderItem(2, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.table_registros.setVerticalHeaderItem(3, __qtablewidgetitem17)
        self.table_registros.setObjectName(u"table_registros")
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.table_registros.sizePolicy().hasHeightForWidth())
        self.table_registros.setSizePolicy(sizePolicy8)
        self.table_registros.setMinimumSize(QSize(0, 120))
        self.table_registros.setMaximumSize(QSize(70, 120))
        self.table_registros.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";")
        self.table_registros.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.table_registros.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.table_registros.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.table_registros.setRowCount(4)
        self.table_registros.horizontalHeader().setVisible(False)
        self.table_registros.horizontalHeader().setDefaultSectionSize(237)
        self.table_registros.horizontalHeader().setHighlightSections(True)

        self.verticalLayout_7.addWidget(self.table_registros)


        self.horizontalLayout_5.addLayout(self.verticalLayout_7)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setSpacing(6)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.label_registros_generales = QLabel(self.centralwidget)
        self.label_registros_generales.setObjectName(u"label_registros_generales")
        sizePolicy9 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy9.setHorizontalStretch(2)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.label_registros_generales.sizePolicy().hasHeightForWidth())
        self.label_registros_generales.setSizePolicy(sizePolicy9)

        self.verticalLayout_10.addWidget(self.label_registros_generales)

        self.table_alu = QTableWidget(self.centralwidget)
        if (self.table_alu.columnCount() < 1):
            self.table_alu.setColumnCount(1)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.table_alu.setHorizontalHeaderItem(0, __qtablewidgetitem18)
        if (self.table_alu.rowCount() < 18):
            self.table_alu.setRowCount(18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.table_alu.setVerticalHeaderItem(0, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.table_alu.setVerticalHeaderItem(1, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.table_alu.setVerticalHeaderItem(2, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.table_alu.setVerticalHeaderItem(3, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.table_alu.setVerticalHeaderItem(4, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.table_alu.setVerticalHeaderItem(5, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.table_alu.setVerticalHeaderItem(6, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.table_alu.setVerticalHeaderItem(7, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.table_alu.setVerticalHeaderItem(8, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.table_alu.setVerticalHeaderItem(9, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.table_alu.setVerticalHeaderItem(10, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.table_alu.setVerticalHeaderItem(11, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.table_alu.setVerticalHeaderItem(12, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.table_alu.setVerticalHeaderItem(13, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.table_alu.setVerticalHeaderItem(14, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.table_alu.setVerticalHeaderItem(15, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.table_alu.setVerticalHeaderItem(16, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.table_alu.setVerticalHeaderItem(17, __qtablewidgetitem36)
        self.table_alu.setObjectName(u"table_alu")
        sizePolicy10 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.table_alu.sizePolicy().hasHeightForWidth())
        self.table_alu.setSizePolicy(sizePolicy10)
        self.table_alu.setMinimumSize(QSize(190, 120))
        self.table_alu.setMaximumSize(QSize(200, 120))
        self.table_alu.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";")
        self.table_alu.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.table_alu.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.table_alu.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.table_alu.setRowCount(18)
        self.table_alu.setColumnCount(1)
        self.table_alu.horizontalHeader().setVisible(False)
        self.table_alu.horizontalHeader().setDefaultSectionSize(153)

        self.verticalLayout_10.addWidget(self.table_alu)


        self.horizontalLayout_5.addLayout(self.verticalLayout_10)


        self.laydetails.addLayout(self.horizontalLayout_5)

        self.label_control = QLabel(self.centralwidget)
        self.label_control.setObjectName(u"label_control")
        sizePolicy7.setHeightForWidth(self.label_control.sizePolicy().hasHeightForWidth())
        self.label_control.setSizePolicy(sizePolicy7)
        self.label_control.setMinimumSize(QSize(0, 26))
        self.label_control.setMaximumSize(QSize(16777215, 16777215))
        self.label_control.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.laydetails.addWidget(self.label_control)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")
        sizePolicy11 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Preferred)
        sizePolicy11.setHorizontalStretch(0)
        sizePolicy11.setVerticalStretch(0)
        sizePolicy11.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy11)
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.label_11, 4, 1, 1, 1)

        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        sizePolicy6.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy6)
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.label_8, 1, 0, 1, 1)

        self.textEdit_ProgramCounter = QTextEdit(self.centralwidget)
        self.textEdit_ProgramCounter.setObjectName(u"textEdit_ProgramCounter")
        self.textEdit_ProgramCounter.setEnabled(False)
        sizePolicy7.setHeightForWidth(self.textEdit_ProgramCounter.sizePolicy().hasHeightForWidth())
        self.textEdit_ProgramCounter.setSizePolicy(sizePolicy7)
        self.textEdit_ProgramCounter.setMinimumSize(QSize(30, 0))
        self.textEdit_ProgramCounter.setMaximumSize(QSize(140, 30))

        self.gridLayout_2.addWidget(self.textEdit_ProgramCounter, 3, 0, 1, 1)

        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        sizePolicy6.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy6)
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.label_10, 4, 0, 1, 1)

        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        sizePolicy6.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy6)
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.label_9, 1, 1, 1, 1)

        self.textEditCurrentInstruction = QTextEdit(self.centralwidget)
        self.textEditCurrentInstruction.setObjectName(u"textEditCurrentInstruction")
        self.textEditCurrentInstruction.setEnabled(False)
        sizePolicy7.setHeightForWidth(self.textEditCurrentInstruction.sizePolicy().hasHeightForWidth())
        self.textEditCurrentInstruction.setSizePolicy(sizePolicy7)
        self.textEditCurrentInstruction.setMaximumSize(QSize(140, 30))
        self.textEditCurrentInstruction.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.gridLayout_2.addWidget(self.textEditCurrentInstruction, 3, 1, 1, 1)

        self.textEditArg2 = QTextEdit(self.centralwidget)
        self.textEditArg2.setObjectName(u"textEditArg2")
        self.textEditArg2.setEnabled(False)
        sizePolicy.setHeightForWidth(self.textEditArg2.sizePolicy().hasHeightForWidth())
        self.textEditArg2.setSizePolicy(sizePolicy)
        self.textEditArg2.setMaximumSize(QSize(140, 30))

        self.gridLayout_2.addWidget(self.textEditArg2, 5, 1, 1, 1)

        self.textEditArg1 = QTextEdit(self.centralwidget)
        self.textEditArg1.setObjectName(u"textEditArg1")
        self.textEditArg1.setEnabled(False)
        sizePolicy7.setHeightForWidth(self.textEditArg1.sizePolicy().hasHeightForWidth())
        self.textEditArg1.setSizePolicy(sizePolicy7)
        self.textEditArg1.setMaximumSize(QSize(140, 30))

        self.gridLayout_2.addWidget(self.textEditArg1, 5, 0, 1, 1)


        self.laydetails.addLayout(self.gridLayout_2)

        self.label_12 = QLabel(self.centralwidget)
        self.label_12.setObjectName(u"label_12")

        self.laydetails.addWidget(self.label_12)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_13 = QLabel(self.centralwidget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_13)

        self.button_sel_ram2dec = QPushButton(self.centralwidget)
        self.button_sel_ram2dec.setObjectName(u"button_sel_ram2dec")

        self.verticalLayout.addWidget(self.button_sel_ram2dec)

        self.button_sel_ram2ascii = QPushButton(self.centralwidget)
        self.button_sel_ram2ascii.setObjectName(u"button_sel_ram2ascii")

        self.verticalLayout.addWidget(self.button_sel_ram2ascii)

        self.button_sel_ram2bin = QPushButton(self.centralwidget)
        self.button_sel_ram2bin.setObjectName(u"button_sel_ram2bin")

        self.verticalLayout.addWidget(self.button_sel_ram2bin)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_14 = QLabel(self.centralwidget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_14)

        self.button_sel_reg2bin = QPushButton(self.centralwidget)
        self.button_sel_reg2bin.setObjectName(u"button_sel_reg2bin")

        self.verticalLayout_2.addWidget(self.button_sel_reg2bin)

        self.button_sel_reg2ascii = QPushButton(self.centralwidget)
        self.button_sel_reg2ascii.setObjectName(u"button_sel_reg2ascii")

        self.verticalLayout_2.addWidget(self.button_sel_reg2ascii)

        self.button_sel_reg2dec = QPushButton(self.centralwidget)
        self.button_sel_reg2dec.setObjectName(u"button_sel_reg2dec")

        self.verticalLayout_2.addWidget(self.button_sel_reg2dec)


        self.horizontalLayout.addLayout(self.verticalLayout_2)


        self.laydetails.addLayout(self.horizontalLayout)


        self.detailshorizlay.addLayout(self.laydetails)

        self.laycredits = QVBoxLayout()
        self.laycredits.setSpacing(10)
        self.laycredits.setObjectName(u"laycredits")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.laycredits.addItem(self.verticalSpacer_2)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        sizePolicy11.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy11)
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.laycredits.addWidget(self.label_4)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.laycredits.addItem(self.verticalSpacer_9)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        sizePolicy11.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy11)

        self.laycredits.addWidget(self.label)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.button_siguiente_instruccion = QPushButton(self.centralwidget)
        self.button_siguiente_instruccion.setObjectName(u"button_siguiente_instruccion")
        sizePolicy6.setHeightForWidth(self.button_siguiente_instruccion.sizePolicy().hasHeightForWidth())
        self.button_siguiente_instruccion.setSizePolicy(sizePolicy6)
        self.button_siguiente_instruccion.setStyleSheet(u"font: 75 12pt \"MS Shell Dlg 2\";")
        self.button_siguiente_instruccion.setAutoDefault(False)
        self.button_siguiente_instruccion.setFlat(False)

        self.verticalLayout_4.addWidget(self.button_siguiente_instruccion)

        self.button_ultima_instruccion = QPushButton(self.centralwidget)
        self.button_ultima_instruccion.setObjectName(u"button_ultima_instruccion")
        sizePolicy6.setHeightForWidth(self.button_ultima_instruccion.sizePolicy().hasHeightForWidth())
        self.button_ultima_instruccion.setSizePolicy(sizePolicy6)
        self.button_ultima_instruccion.setStyleSheet(u"font: 75 12pt \"MS Shell Dlg 2\";")

        self.verticalLayout_4.addWidget(self.button_ultima_instruccion)

        self.button_reiniciar = QPushButton(self.centralwidget)
        self.button_reiniciar.setObjectName(u"button_reiniciar")
        sizePolicy6.setHeightForWidth(self.button_reiniciar.sizePolicy().hasHeightForWidth())
        self.button_reiniciar.setSizePolicy(sizePolicy6)
        self.button_reiniciar.setStyleSheet(u"font: 75 12pt \"MS Shell Dlg 2\";")

        self.verticalLayout_4.addWidget(self.button_reiniciar)


        self.laycredits.addLayout(self.verticalLayout_4)


        self.detailshorizlay.addLayout(self.laycredits)

        self.layio = QVBoxLayout()
        self.layio.setObjectName(u"layio")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy2.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy2)

        self.layio.addWidget(self.label_2)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)

        self.layio.addWidget(self.label_3)

        self.textEditInput = QTextEdit(self.centralwidget)
        self.textEditInput.setObjectName(u"textEditInput")
        sizePolicy3.setHeightForWidth(self.textEditInput.sizePolicy().hasHeightForWidth())
        self.textEditInput.setSizePolicy(sizePolicy3)

        self.layio.addWidget(self.textEditInput)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)

        self.layio.addWidget(self.label_5)

        self.textEditPCOutput = QTextEdit(self.centralwidget)
        self.textEditPCOutput.setObjectName(u"textEditPCOutput")
        sizePolicy3.setHeightForWidth(self.textEditPCOutput.sizePolicy().hasHeightForWidth())
        self.textEditPCOutput.setSizePolicy(sizePolicy3)
        self.textEditPCOutput.setMinimumSize(QSize(0, 0))
        self.textEditPCOutput.setMaximumSize(QSize(16777215, 16777215))

        self.layio.addWidget(self.textEditPCOutput)


        self.detailshorizlay.addLayout(self.layio)

        self.layexm = QVBoxLayout()
        self.layexm.setObjectName(u"layexm")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.layexm.addItem(self.verticalSpacer)

        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")

        self.layexm.addWidget(self.label_7)

        self.button_cargar_ex1 = QPushButton(self.centralwidget)
        self.button_cargar_ex1.setObjectName(u"button_cargar_ex1")

        self.layexm.addWidget(self.button_cargar_ex1)

        self.button_cargar_ex2 = QPushButton(self.centralwidget)
        self.button_cargar_ex2.setObjectName(u"button_cargar_ex2")

        self.layexm.addWidget(self.button_cargar_ex2)

        self.button_cargar_ex3 = QPushButton(self.centralwidget)
        self.button_cargar_ex3.setObjectName(u"button_cargar_ex3")

        self.layexm.addWidget(self.button_cargar_ex3)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.layexm.addItem(self.verticalSpacer_8)


        self.detailshorizlay.addLayout(self.layexm)


        self.gridLayout.addLayout(self.detailshorizlay, 6, 0, 1, 6)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.spinBox_pos_enlazar, self.button_linker)
        QWidget.setTabOrder(self.button_linker, self.table_ram)

        self.retranslateUi(MainWindow)

        self.button_siguiente_instruccion.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Sistema de Procesamiento", None))
        self.labelProgramaFuente.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; color:#2980b9;\">Programa fuente</span></p></body></html>", None))
        self.textEditCodigoFuente.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.button_preprocessor.setText(QCoreApplication.translate("MainWindow", u"Preprocesar", None))
        self.labelProgramaFuenteModificado.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; color:#2980b9;\">Programa fuente modificado</span></p></body></html>", None))
        self.textEditCodigoFuenteModificado.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.button_compiler.setText(QCoreApplication.translate("MainWindow", u"Compilar", None))
        self.button_verTablaSimbolos.setText(QCoreApplication.translate("MainWindow", u"Ver tabla de S\u00edmbolos", None))
        self.labelASM.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; color:#27ae60;\">Programa en Assembler</span></p></body></html>", None))
        self.button_assembler.setText(QCoreApplication.translate("MainWindow", u"Ensamblar", None))
        self.labelMaquinaRelocalizable.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\"><span style=\" font-size:12pt; color:#aa00ff;\">C\u00f3digo m\u00e1quina relocalizable</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\">Posici\u00f3n de memoria inicial:</p></body></html>", None))
        self.labelLibs.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#aa00ff;\">+ Librer\u00edas</span></p></body></html>", None))
        self.button_linker.setText(QCoreApplication.translate("MainWindow", u"Enlazar y Cargar", None))
        self.label_ram.setText(QCoreApplication.translate("MainWindow", u"<html><div align='center'><span style='font-size:14pt; color:#2c3e50;'>RAM</span></div></html>", None))

        __sortingEnabled = self.table_ram.isSortingEnabled()
        self.table_ram.setSortingEnabled(False)
        self.table_ram.setSortingEnabled(__sortingEnabled)

        self.label_registros_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; color:#c0392b;\">Registros</span></p></body></html>", None))
        self.label_registros_reservados.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; color:#c0392b;\">Reservados</span></p></body></html>", None))
        ___qtablewidgetitem = self.table_registros.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Contenido", None));
        ___qtablewidgetitem1 = self.table_registros.verticalHeaderItem(0)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"R0", None));
#if QT_CONFIG(tooltip)
        ___qtablewidgetitem1.setToolTip(QCoreApplication.translate("MainWindow", u"\u00bfEstamos en una rutina?", None));
#endif // QT_CONFIG(tooltip)
        ___qtablewidgetitem2 = self.table_registros.verticalHeaderItem(1)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"R1", None));
#if QT_CONFIG(tooltip)
        ___qtablewidgetitem2.setToolTip(QCoreApplication.translate("MainWindow", u"Inicio de la rutina", None));
#endif // QT_CONFIG(tooltip)
        ___qtablewidgetitem3 = self.table_registros.verticalHeaderItem(2)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"R2", None));
#if QT_CONFIG(tooltip)
        ___qtablewidgetitem3.setToolTip(QCoreApplication.translate("MainWindow", u"Fin de la rutina", None));
#endif // QT_CONFIG(tooltip)
        ___qtablewidgetitem4 = self.table_registros.verticalHeaderItem(3)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"R3", None));
#if QT_CONFIG(tooltip)
        ___qtablewidgetitem4.setToolTip(QCoreApplication.translate("MainWindow", u"Resultado de la ultima comparaci\u00f3n", None));
#endif // QT_CONFIG(tooltip)
        self.label_registros_generales.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; color:#c0392b;\">Generales</span></p></body></html>", None))
        ___qtablewidgetitem5 = self.table_alu.horizontalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"BINARIO", None));
        ___qtablewidgetitem6 = self.table_alu.verticalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"R4", None));
        ___qtablewidgetitem7 = self.table_alu.verticalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"R5", None));
        ___qtablewidgetitem8 = self.table_alu.verticalHeaderItem(2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"R6", None));
        ___qtablewidgetitem9 = self.table_alu.verticalHeaderItem(3)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"R7", None));
        ___qtablewidgetitem10 = self.table_alu.verticalHeaderItem(4)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"R8", None));
        ___qtablewidgetitem11 = self.table_alu.verticalHeaderItem(5)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"R9", None));
        ___qtablewidgetitem12 = self.table_alu.verticalHeaderItem(6)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"R10", None));
        ___qtablewidgetitem13 = self.table_alu.verticalHeaderItem(7)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"R11", None));
        ___qtablewidgetitem14 = self.table_alu.verticalHeaderItem(8)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"R12", None));
        ___qtablewidgetitem15 = self.table_alu.verticalHeaderItem(9)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"R13", None));
        ___qtablewidgetitem16 = self.table_alu.verticalHeaderItem(10)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"R14", None));
        ___qtablewidgetitem17 = self.table_alu.verticalHeaderItem(11)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"R15", None));
        ___qtablewidgetitem18 = self.table_alu.verticalHeaderItem(12)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"R16", None));
        ___qtablewidgetitem19 = self.table_alu.verticalHeaderItem(13)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"R17", None));
        ___qtablewidgetitem20 = self.table_alu.verticalHeaderItem(14)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"R18", None));
        ___qtablewidgetitem21 = self.table_alu.verticalHeaderItem(15)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"R19", None));
        ___qtablewidgetitem22 = self.table_alu.verticalHeaderItem(16)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"R30", None));
        ___qtablewidgetitem23 = self.table_alu.verticalHeaderItem(17)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"R31", None));
        self.label_control.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; color:#aa00ff;\">Unidad de control</span></p></body></html>", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Argumento 2", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Program Counter", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Argumento 1", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Instrucci\u00f3n", None))
#if QT_CONFIG(tooltip)
        self.label_12.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Cambiar celdas seleccionadas al formato del bot\u00f3n</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; color:#aaaa00;\">Cambio de formato</span></p></body></html>", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Ram seleccionada", None))
        self.button_sel_ram2dec.setText(QCoreApplication.translate("MainWindow", u"Decimal", None))
        self.button_sel_ram2ascii.setText(QCoreApplication.translate("MainWindow", u"ASCII", None))
        self.button_sel_ram2bin.setText(QCoreApplication.translate("MainWindow", u"Reiniciar", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Registros Seleccionados", None))
        self.button_sel_reg2bin.setText(QCoreApplication.translate("MainWindow", u"Binario", None))
        self.button_sel_reg2ascii.setText(QCoreApplication.translate("MainWindow", u"ASCII", None))
        self.button_sel_reg2dec.setText(QCoreApplication.translate("MainWindow", u"Reiniciar", None))
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
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; color:#ff0000;\">I/O</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Entrada del computador", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Salida del computador", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; color:#5555ff;\">Ejemplos</span></p></body></html>", None))
        self.button_cargar_ex1.setText(QCoreApplication.translate("MainWindow", u"Cargar Ejemplo 1", None))
        self.button_cargar_ex2.setText(QCoreApplication.translate("MainWindow", u"Cargar Ejemplo 2", None))
        self.button_cargar_ex3.setText(QCoreApplication.translate("MainWindow", u"Cargar Ejemplo 3", None))
    # retranslateUi

