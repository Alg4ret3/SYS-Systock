# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\PagoCredito.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PagoCredito(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1417, 1002)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.gridLayout_2 = QtWidgets.QGridLayout(Form)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.Contenedor = QtWidgets.QWidget(Form)
        self.Contenedor.setStyleSheet("\n"
"QPushButton {\n"
"    background-color: black; /* Fondo blanco */\n"
"    border: none; /* Sin borde ni decoración inicial */\n"
"    color:  white; /* Color del texto */\n"
"    border-radius: 15px; /* Bordes circulares */\n"
"    padding: 5px 10px; /* Espaciado interno para mejor apariencia */\n"
"    height: 40px; /* Altura del botón */\n"
"    text-align: center; /* Alinea el texto del botón a la izquierda */\n"
"    font-size: 18px; /* Tamaño de fuente */\n"
"    margin-top:20px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(106, 106, 106); /* Gris claro al pasar el mouse */\n"
"    cursor: pointer; /* Cursor de mano al pasar sobre el botón */\n"
"}\n"
"\n"
"QToolButton {\n"
"    background-color: white; /* Fondo blanco */\n"
"    border: none; /* Sin borde ni decoración inicial */\n"
"    color:  rgb(50, 50, 50); /* Color del texto */\n"
"    border-radius: 15px; /* Bordes circulares */\n"
"    padding: 5px 10px; /* Espaciado interno para mejor apariencia */\n"
"    height: 40px; /* Altura del botón */\n"
"    text-align: left; /* Alinea el texto del botón a la izquierda */\n"
"    font-size: 18px; /* Tamaño de fuente */\n"
"    cursor: pointer;\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"    background-color: #f2f2f2; /* Gris claro al pasar el mouse */\n"
"    cursor: pointer;\n"
"}\n"
"QLineEdit {\n"
"    background-color: rgb(255, 255, 255); /* Fondo blanco */\n"
"    border: none; /* Sin bordes visibles */\n"
"    padding: 4px; /* Espaciado interno entre el texto y los bordes */\n"
"    margin-right: 5px; /* Espaciado externo solo a la derecha */\n"
"    border-radius: 10px; /* Bordes redondeados */\n"
"    color: black; /* Texto negro */\n"
"    text-align: left; /* Texto alineado a la izquierda */\n"
"    font-size: 18px; /* Tamaño del texto */\n"
"}\n"
"\n"
"/* Cuando el QLineEdit está enfocado (se está escribiendo) */\n"
"QLineEdit:focus {\n"
"    background-color: rgb(230, 230, 250); /* Color de fondo cuando el campo está activo */\n"
"    border: 1px solid rgb(0, 0, 0); /* Borde negro al estar activo */\n"
"}\n"
"\n"
"QLabel {\n"
"    font-size: 20px; /* Tamaño de fuente */\n"
"    color:  black; /* Color del texto */\n"
"    margin-right: 10px; /* Espaciado a la derecha */\n"
"    padding: 5px; /* Espaciado interno */\n"
"    text-align: left; /* Alineación del texto a la izquierda */\n"
"}\n"
"QTableWidget {\n"
"    border: none;\n"
"    background-color: #ffffff; /* Fondo blanco para la tabla */\n"
"    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Sombra suave alrededor de la tabla */\n"
"}\n"
"\n"
"QTableWidget::item {\n"
"    background-color: #f2f2f2; \n"
"    border: none; \n"
"    transition: background-color 0.3s ease; /* Suavizado de transición de color de fondo */\n"
"    pointer-events: none; /* Desactiva la interacción con las celdas (como editar) */\n"
"}\n"
"\n"
"QTableWidget::item:selected {\n"
"    background-color: #aad4ff; /* Color azul claro para celdas seleccionadas */\n"
"    color: black; /* Texto negro para celdas seleccionadas */\n"
"}\n"
"\n"
"QTableWidget::item:hover {\n"
"    background-color: #e6e6e6; /* Color de fondo al pasar el cursor sobre las celdas */\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    border: none; \n"
"    background-color: #f2f2f2; \n"
"    font-weight: normal; /* No negritas */\n"
"    text-align: center; /* Centrado del texto en los encabezados */\n"
"    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); /* Sombra suave para los encabezados */\n"
"}\n"
"\n"
"QHeaderView::section:focus {\n"
"    background-color: #f2f2f2; /* Sin color de fondo cuando está en foco */\n"
"    border: none; /* Sin borde cuando está en foco */\n"
"}\n"
"\n"
"QTableWidget::item:focus {\n"
"    border: none; /* Sin borde cuando las celdas tienen el foco */\n"
"    background-color: #f2f2f2; /* Mantener el fondo sin color azul */\n"
"}\n"
"\n"
"QTableCornerButton::section {\n"
"    background-color: #f2f2f2; \n"
"    border: none; \n"
"}\n"
"\n"
"QTableWidget::verticalHeader {\n"
"    background-color: #f2f2f2;\n"
"    border: none;\n"
"    font-weight: normal; /* No negritas */\n"
"}\n"
"\n"
"QTableWidget::item:hover {\n"
"    background-color: #e6e6e6; /* Color de fondo al pasar el cursor sobre las celdas */\n"
"}\n"
"\n"
"/* Personalización de la barra de desplazamiento */\n"
"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: #f7f7f7; /* Fondo de la barra */\n"
"    width: 8px; /* Barra más delgada */\n"
"    border-radius: 4px; /* Bordes más redondeados */\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: #bbb; /* Fondo del control deslizante */\n"
"    min-height: 20px; /* Control deslizante más delgado */\n"
"    border-radius: 4px; /* Bordes redondeados */\n"
"    transition: background-color 0.3s ease; /* Transición suave para el cambio de color */\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"    background: #888; /* Color más oscuro cuando el control deslizante está siendo desplazado */\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background: #f2f2f2; /* Fondo para los botones de la barra */\n"
"    height: 0px; /* Sin altura para los botones */\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: #f7f7f7; /* Fondo de la barra */\n"
"    height: 8px; /* Barra más delgada */\n"
"    border-radius: 4px; /* Bordes más redondeados */\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"    background: #bbb; /* Fondo del control deslizante */\n"
"    min-width: 20px; /* Control deslizante más delgado */\n"
"    border-radius: 4px; /* Bordes redondeados */\n"
"    transition: background-color 0.3s ease; /* Transición suave para el cambio de color */\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal:hover {\n"
"    background: #888; /* Color más oscuro cuando el control deslizante está siendo desplazado */\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: #f2f2f2; /* Fondo para los botones de la barra */\n"
"    width: 0px; /* Sin ancho para los botones */\n"
"}\n"
"\n"
"\n"
"")
        self.Contenedor.setObjectName("Contenedor")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.Contenedor)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Contenido = QtWidgets.QStackedWidget(self.Contenedor)
        self.Contenido.setStyleSheet("margin-left:10px;\n"
"border-radius:15px;\n"
"background-color: #f2f2f2; \n"
"")
        self.Contenido.setObjectName("Contenido")
        self.ContenidoPage1 = QtWidgets.QWidget()
        self.ContenidoPage1.setObjectName("ContenidoPage1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.ContenidoPage1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget = QtWidgets.QWidget(self.ContenidoPage1)
        self.widget.setStyleSheet("")
        self.widget.setObjectName("widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_2 = QtWidgets.QFrame(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QtCore.QSize(1200, 50))
        self.frame_2.setStyleSheet("")
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.LabelProductos = QtWidgets.QLabel(self.frame_2)
        self.LabelProductos.setStyleSheet("#LabelProductos {\n"
"    font-weight: bold; /* Negrita */\n"
"    font-size: 34px; /* Tamaño de fuente */\n"
"}\n"
"")
        self.LabelProductos.setObjectName("LabelProductos")
        self.gridLayout_3.addWidget(self.LabelProductos, 0, 0, 1, 1)
        self.verticalLayout_3.addWidget(self.frame_2, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.TablaPagoCredito = QtWidgets.QTableWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TablaPagoCredito.sizePolicy().hasHeightForWidth())
        self.TablaPagoCredito.setSizePolicy(sizePolicy)
        self.TablaPagoCredito.setMinimumSize(QtCore.QSize(950, 400))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.TablaPagoCredito.setFont(font)
        self.TablaPagoCredito.setStyleSheet("\n"
"QTableWidget {\n"
"    border: none;\n"
"    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Sombra suave alrededor de la tabla */\n"
"}\n"
"\n"
"QTableWidget::item {\n"
"    background-color: #f2f2f2; \n"
"    border: none; \n"
"    font-size: 18px; /* Tamaño de letra */\n"
"    transition: background-color 0.3s ease; /* Suavizado de transición de color de fondo */\n"
"    pointer-events: none; /* Desactiva la interacción con las celdas (como editar) */\n"
"}\n"
"\n"
"QTableWidget::item:selected {\n"
"    background-color: #aad4ff; /* Color azul claro para celdas seleccionadas */\n"
"    color: black; /* Texto negro para celdas seleccionadas */\n"
"}\n"
"\n"
"QTableWidget::item:hover {\n"
"    background-color: #e6e6e6; /* Color de fondo al pasar el cursor sobre las celdas */\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    border: none; \n"
"    background-color: #f2f2f2; \n"
"    font-size: 18px; /* Tamaño de letra */\n"
"    font-weight: normal; /* No negritas */\n"
"    text-align: center; /* Centrado del texto en los encabezados */\n"
"    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); /* Sombra suave para los encabezados */\n"
"}\n"
"\n"
"QHeaderView::section:focus {\n"
"    background-color: #f2f2f2; /* Sin color de fondo cuando está en foco */\n"
"    border: none; /* Sin borde cuando está en foco */\n"
"}\n"
"\n"
"QTableWidget::item:focus {\n"
"    border: none; /* Sin borde cuando las celdas tienen el foco */\n"
"    background-color: #f2f2f2; /* Mantener el fondo sin color azul */\n"
"}\n"
"\n"
"QTableCornerButton::section {\n"
"    background-color: #f2f2f2; \n"
"    border: none; \n"
"}\n"
"\n"
"QTableWidget::verticalHeader {\n"
"    background-color: #f2f2f2;\n"
"    font-size: 23px;\n"
"    border: none;\n"
"    font-weight: normal; /* No negritas */\n"
"}\n"
"\n"
"QTableWidget::item:hover {\n"
"    background-color: #e6e6e6; /* Color de fondo al pasar el cursor sobre las celdas */\n"
"}\n"
"/* Personalización de la barra de desplazamiento */\n"
"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: #f7f7f7; /* Fondo de la barra */\n"
"    width: 8px; /* Barra más delgada */\n"
"    border-radius: 4px; /* Bordes más redondeados */\n"
"    margin: 0px 2px 0px 0px; /* Un pequeño margen para el desplazamiento */\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: #bbb; /* Fondo del control deslizante */\n"
"    min-height: 20px; /* Control deslizante más delgado */\n"
"    border-radius: 4px; /* Bordes redondeados */\n"
"    transition: background-color 0.3s ease; /* Transición suave para el cambio de color */\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"    background: #888; /* Color más oscuro cuando el control deslizante está siendo desplazado */\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background: #f2f2f2; /* Fondo para los botones de la barra */\n"
"    height: 0px; /* Sin altura para los botones */\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: #f7f7f7; /* Fondo de la barra */\n"
"    height: 8px; /* Barra más delgada */\n"
"    border-radius: 4px; /* Bordes más redondeados */\n"
"    margin: 0px 0px 2px 0px; /* Un pequeño margen para el desplazamiento */\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"    background: #bbb; /* Fondo del control deslizante */\n"
"    min-width: 20px; /* Control deslizante más delgado */\n"
"    border-radius: 4px; /* Bordes redondeados */\n"
"    transition: background-color 0.3s ease; /* Transición suave para el cambio de color */\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal:hover {\n"
"    background: #888; /* Color más oscuro cuando el control deslizante está siendo desplazado */\n"
"}\n"
"")
        self.TablaPagoCredito.setObjectName("TablaPagoCredito")
        self.TablaPagoCredito.setColumnCount(7)
        self.TablaPagoCredito.setRowCount(26)
        item = QtWidgets.QTableWidgetItem()
        self.TablaPagoCredito.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaPagoCredito.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaPagoCredito.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaPagoCredito.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaPagoCredito.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaPagoCredito.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaPagoCredito.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaPagoCredito.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaPagoCredito.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaPagoCredito.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaPagoCredito.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaPagoCredito.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaPagoCredito.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaPagoCredito.setVerticalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaPagoCredito.setVerticalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaPagoCredito.setVerticalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaPagoCredito.setVerticalHeaderItem(16, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaPagoCredito.setVerticalHeaderItem(17, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaPagoCredito.setVerticalHeaderItem(18, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaPagoCredito.setVerticalHeaderItem(19, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaPagoCredito.setVerticalHeaderItem(20, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaPagoCredito.setVerticalHeaderItem(21, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaPagoCredito.setVerticalHeaderItem(22, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaPagoCredito.setVerticalHeaderItem(23, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaPagoCredito.setVerticalHeaderItem(24, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaPagoCredito.setVerticalHeaderItem(25, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setKerning(False)
        item.setFont(font)
        self.TablaPagoCredito.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.TablaPagoCredito.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.TablaPagoCredito.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.TablaPagoCredito.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.TablaPagoCredito.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.TablaPagoCredito.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.TablaPagoCredito.setHorizontalHeaderItem(6, item)
        self.verticalLayout_3.addWidget(self.TablaPagoCredito, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.verticalLayout_2.addWidget(self.widget)
        self.widget_3 = QtWidgets.QWidget(self.ContenidoPage1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.widget_3.setMinimumSize(QtCore.QSize(600, 0))
        self.widget_3.setStyleSheet("")
        self.widget_3.setObjectName("widget_3")
        self.gridLayout = QtWidgets.QGridLayout(self.widget_3)
        self.gridLayout.setObjectName("gridLayout")
        self.InputPago = QtWidgets.QLineEdit(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.InputPago.sizePolicy().hasHeightForWidth())
        self.InputPago.setSizePolicy(sizePolicy)
        self.InputPago.setMinimumSize(QtCore.QSize(250, 50))
        self.InputPago.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.InputPago.setObjectName("InputPago")
        self.gridLayout.addWidget(self.InputPago, 3, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1, QtCore.Qt.AlignLeft|QtCore.Qt.AlignBottom)
        self.label_2 = QtWidgets.QLabel(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.MetodoPagoBox = QtWidgets.QComboBox(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MetodoPagoBox.sizePolicy().hasHeightForWidth())
        self.MetodoPagoBox.setSizePolicy(sizePolicy)
        self.MetodoPagoBox.setMinimumSize(QtCore.QSize(250, 50))
        self.MetodoPagoBox.setStyleSheet("QComboBox {\n"
"    background-color: white; /* Fondo blanco */\n"
"    border: none; /* Sin borde */\n"
"    color: black; /* Color del texto */\n"
"    border-radius: 15px; /* Bordes redondeados */\n"
"    padding: 5px 10px; /* Espaciado interno */\n"
"    font-size: 18px; /* Tamaño de fuente */\n"
"    height: 40px; /* Altura del combo box */\n"
"    margin-top: 20px; /* Espaciado superior */\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    background-color: transparent; /* Fondo transparente */\n"
"    border: none; /* Sin borde */\n"
"    width: 20px; /* Tamaño del botón */\n"
"    /* No se define la flecha, por lo que se elimina */\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    cursor: pointer; /* Cursor de mano */\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: white; /* Fondo del menú desplegable */\n"
"    border: none; /* Sin borde */\n"
"    color: black; /* Color del texto en las opciones */\n"
"    selection-background-color: rgb(106, 106, 106); /* Fondo gris claro al seleccionar */\n"
"    selection-color: white; /* Texto blanco al seleccionar */\n"
"    border-radius: 10px; /* Bordes redondeados */\n"
"}")
        self.MetodoPagoBox.setObjectName("MetodoPagoBox")
        self.gridLayout.addWidget(self.MetodoPagoBox, 1, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.widget_3, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.widget_4 = QtWidgets.QWidget(self.ContenidoPage1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy)
        self.widget_4.setMinimumSize(QtCore.QSize(1000, 0))
        self.widget_4.setStyleSheet("")
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.BtnAbonar = QtWidgets.QPushButton(self.widget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BtnAbonar.sizePolicy().hasHeightForWidth())
        self.BtnAbonar.setSizePolicy(sizePolicy)
        self.BtnAbonar.setMinimumSize(QtCore.QSize(150, 0))
        self.BtnAbonar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BtnAbonar.setStyleSheet("\n"
"QPushButton {\n"
"    background-color: black; /* Fondo blanco */\n"
"    border: none; /* Sin borde ni decoración inicial */\n"
"    color:  white; /* Color del texto */\n"
"    border-radius: 15px; /* Bordes circulares */\n"
"    padding: 5px 10px; /* Espaciado interno para mejor apariencia */\n"
"    height: 40px; /* Altura del botón */\n"
"    text-align: center; /* Alinea el texto del botón a la izquierda */\n"
"    font-size: 18px; /* Tamaño de fuente */\n"
"    margin-top:20px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(106, 106, 106); /* Gris claro al pasar el mouse */\n"
"    cursor: pointer; /* Cursor de mano al pasar sobre el botón */\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("assets/iconos/signo_dinero.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BtnAbonar.setIcon(icon)
        self.BtnAbonar.setIconSize(QtCore.QSize(32, 32))
        self.BtnAbonar.setObjectName("BtnAbonar")
        self.horizontalLayout.addWidget(self.BtnAbonar, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignBottom)
        self.verticalLayout_2.addWidget(self.widget_4, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.Contenido.addWidget(self.ContenidoPage1)
        self.horizontalLayout_2.addWidget(self.Contenido)
        self.gridLayout_2.addWidget(self.Contenedor, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.LabelProductos.setText(_translate("Form", "Pago de Credito"))
        item = self.TablaPagoCredito.verticalHeaderItem(0)
        item.setText(_translate("Form", "1."))
        item = self.TablaPagoCredito.verticalHeaderItem(1)
        item.setText(_translate("Form", "Nueva fila"))
        item = self.TablaPagoCredito.verticalHeaderItem(2)
        item.setText(_translate("Form", "Nueva fila"))
        item = self.TablaPagoCredito.verticalHeaderItem(3)
        item.setText(_translate("Form", "Nueva fila"))
        item = self.TablaPagoCredito.verticalHeaderItem(4)
        item.setText(_translate("Form", "Nueva fila"))
        item = self.TablaPagoCredito.verticalHeaderItem(5)
        item.setText(_translate("Form", "Nueva fila"))
        item = self.TablaPagoCredito.verticalHeaderItem(6)
        item.setText(_translate("Form", "Nueva fila"))
        item = self.TablaPagoCredito.verticalHeaderItem(7)
        item.setText(_translate("Form", "Nueva fila"))
        item = self.TablaPagoCredito.verticalHeaderItem(8)
        item.setText(_translate("Form", "Nueva fila"))
        item = self.TablaPagoCredito.verticalHeaderItem(9)
        item.setText(_translate("Form", "Nueva fila"))
        item = self.TablaPagoCredito.verticalHeaderItem(10)
        item.setText(_translate("Form", "Nueva fila"))
        item = self.TablaPagoCredito.verticalHeaderItem(11)
        item.setText(_translate("Form", "Nueva fila"))
        item = self.TablaPagoCredito.verticalHeaderItem(12)
        item.setText(_translate("Form", "Nueva fila"))
        item = self.TablaPagoCredito.verticalHeaderItem(13)
        item.setText(_translate("Form", "New Row"))
        item = self.TablaPagoCredito.verticalHeaderItem(14)
        item.setText(_translate("Form", "New Row"))
        item = self.TablaPagoCredito.verticalHeaderItem(15)
        item.setText(_translate("Form", "New Row"))
        item = self.TablaPagoCredito.verticalHeaderItem(16)
        item.setText(_translate("Form", "New Row"))
        item = self.TablaPagoCredito.verticalHeaderItem(17)
        item.setText(_translate("Form", "New Row"))
        item = self.TablaPagoCredito.verticalHeaderItem(18)
        item.setText(_translate("Form", "New Row"))
        item = self.TablaPagoCredito.verticalHeaderItem(19)
        item.setText(_translate("Form", "New Row"))
        item = self.TablaPagoCredito.verticalHeaderItem(20)
        item.setText(_translate("Form", "New Row"))
        item = self.TablaPagoCredito.verticalHeaderItem(21)
        item.setText(_translate("Form", "New Row"))
        item = self.TablaPagoCredito.verticalHeaderItem(22)
        item.setText(_translate("Form", "New Row"))
        item = self.TablaPagoCredito.verticalHeaderItem(23)
        item.setText(_translate("Form", "New Row"))
        item = self.TablaPagoCredito.verticalHeaderItem(24)
        item.setText(_translate("Form", "New Row"))
        item = self.TablaPagoCredito.verticalHeaderItem(25)
        item.setText(_translate("Form", "New Row"))
        item = self.TablaPagoCredito.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Id"))
        item = self.TablaPagoCredito.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Nombre"))
        item = self.TablaPagoCredito.horizontalHeaderItem(2)
        item.setText(_translate("Form", "F.Registro"))
        item = self.TablaPagoCredito.horizontalHeaderItem(3)
        item.setText(_translate("Form", "F.Limite"))
        item = self.TablaPagoCredito.horizontalHeaderItem(4)
        item.setText(_translate("Form", "T.Deuda"))
        item = self.TablaPagoCredito.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Pendiente"))
        item = self.TablaPagoCredito.horizontalHeaderItem(6)
        item.setText(_translate("Form", "Estado"))
        self.label.setText(_translate("Form", "Metodo de Pago"))
        self.label_2.setText(_translate("Form", "Monto:"))
        self.BtnAbonar.setText(_translate("Form", " Abonar!"))
