import sys

from PySide6.QtWidgets import QApplication, QPushButton


app = QApplication(sys.argv)

botao = QPushButton("Clique aqui 01")
botao.setStyleSheet("font-size: 40px; color: red;")  # Adiciona estilo ao botão (CSS)
botao.show()  # Adicionar o widget na hierarquia e exibe a janela

# executa o loop da aplicação
app.exec()
