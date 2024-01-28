from PyQt5.QtCore import * # ? Подключили основу 
from PyQt5.QtWidgets import * # ? Подключили виджеты

from random import randint

app = QApplication([]) # ? Создали приложение
window = QWidget() # ? Создали окно приложения
window.resize(1280, 720)

main_layout = QVBoxLayout() # ? Вертикальный лейаут

# ! Создали, НО НЕ ОТОБРАЗИЛИ ВИДЖЕТЫ
lbl_info = QLabel("Генератор случайных чисел")
lbl_number = QLabel("?")

btn_generate = QPushButton("Сгенерировать")

# ! Помещаем виджеты в main_layout чтобы отобразить их
main_layout.addWidget(lbl_info)
main_layout.addWidget(lbl_number)
main_layout.addWidget(btn_generate)

# ! Создаем событие для кнопки
def generate():
    lbl_number.setText(str(randint(1, 100)))
    
btn_generate.clicked.connect(generate) # ? Привязали к кнопке btn_generate событие clicked, и при нажатии она будет выполнять функцию generate

window.setLayout(main_layout) # ? Интерфейс окна такой, как описано в main_layout

window.show() # ? Отобразили окно приложения
app.exec() # ? Запустили приложение