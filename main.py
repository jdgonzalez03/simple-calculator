from assets.gui import *



# Definimos la clase MainWindow, que hereda de QMainWindow (para la funcionalidad de la ventana)
# y Ui_MainWindow (para la interfaz de usuario diseñada).
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    # Constructor de la clase MainWindow
    def __init__(self, *args, **kwargs):
        # Inicializamos la clase base QMainWindow con cualquier argumento adicional proporcionado.
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        # Llamamos a setupUi para configurar la interfaz de usuario en esta ventana principal.
        self.setupUi(self)

        self.current_operation = ""
        self.stored_value = ''
        self.current_value = ''

        # Link function to press number buttons
        self.btn_0.clicked.connect(lambda: self.press_number(0))
        self.btn_1.clicked.connect(lambda: self.press_number(1))
        self.btn_2.clicked.connect(lambda: self.press_number(2))
        self.btn_3.clicked.connect(lambda: self.press_number(3))
        self.btn_4.clicked.connect(lambda: self.press_number(4))
        self.btn_5.clicked.connect(lambda: self.press_number(5))
        self.btn_6.clicked.connect(lambda: self.press_number(6))
        self.btn_7.clicked.connect(lambda: self.press_number(7))
        self.btn_8.clicked.connect(lambda: self.press_number(8))
        self.btn_9.clicked.connect(lambda: self.press_number(9))

        # Link function to press operator buttons
        self.btn_plus.clicked.connect(lambda: self.press_operator('+'))
        self.btn_subs.clicked.connect(lambda: self.press_operator('-'))
        self.btn_mult.clicked.connect(lambda: self.press_operator('*'))
        self.btn_division.clicked.connect(lambda: self.press_operator('/'))
        self.btn_equals.clicked.connect(self.calculate)

        # Link clear button
        self.btn_clear_all.clicked.connect(self.clear_all)
        self.btn_remove.clicked.connect(self.clear_entry)

        # Toggle positive/negative
        self.comodin.clicked.connect(self.toggle_sign)

        # Add comma button
        self.btn_comma.clicked.connect(self.add_comma)

        # Add percentage button
        self.btn_percent.clicked.connect(self.add_percentage)
    
    def add_percentage(self):
        if self.current_value and self.current_value != 'Error':
            try:
                value = float(self.current_value)
                result = value / 100
                if isinstance(result, float) and result.is_integer():
                    result = int(result)
                self.current_value = str(result)
                self.display_value()
            except:
                self.current_value = "Error"
                self.display_value("Error")
    
    def press_number(self, number):
        print(f"Adding number: {number}")
        if self.current_value == '0':
            self.current_value = str(number)
        else:
            self.current_value += str(number)
        
        self.display_value()
    
    def display_value(self, msg=None):
        if not msg:
            self.output.setText(f"{self.stored_value} {self.current_operation} {self.current_value}")
        else:
            self.output.setText(str(msg))
    
    def press_operator(self, operator):
        print(f"Operator pressed: {operator}")
        
        if self.current_operation and self.stored_value and self.current_value:
            self.calculate()
            self._operator(operator)
        else:
            self._operator(operator)
    
    def _operator(self, operator):
        self.current_operation = operator
        self.stored_value = self.current_value
        self.current_value = ''
        self.display_value()
    
    def calculate(self):
        print("Calculating...")
        if self.current_operation and self.stored_value:
            try:
                result = eval(f"{self.stored_value}{self.current_operation}{self.current_value}")
                if isinstance(result, float):
                    result = round(result, 10)
                    if result.is_integer():
                        result = int(result)
                    else:
                        # Keep as float but remove trailing zeros
                        result = "{:.2f}".format(result)
                self.current_value = str(result)
                self.display_value(result)
                self.current_operation = ""
                self.stored_value = ""
            except:
                self.current_value = "Error"
                self.display_value("Error")
    
    def clear_all(self):
        self.current_value = '0'
        self.stored_value = ''
        self.current_operation = ''
        self.display_value()
    
    def clear_entry(self):
        self.current_value = '0'
        self.display_value()

    def toggle_sign(self):
        if self.current_value != '0' and self.current_value != 'Error':
            if self.current_value.startswith('-'):
                self.current_value = self.current_value[1:]
            else:
                self.current_value = '-' + self.current_value
            self.display_value()
    
    def add_comma(self):
        if self.current_value and self.current_value != 'Error' and '.' not in self.current_value:
            self.current_value += '.'
            self.display_value()

# Este bloque se ejecuta si el script es el programa principal y no un módulo importado.
if __name__ == "__main__":
    # Creamos una instancia de QApplication, necesaria para cualquier aplicación GUI de PyQt.
    app = QtWidgets.QApplication([])
    # Creamos una instancia de nuestra clase MainWindow.
    window = MainWindow()
    # Mostramos la ventana principal.
    window.show()
    # Ejecutamos el bucle principal de la aplicación, esperando eventos como clics o teclas.
    app.exec_()