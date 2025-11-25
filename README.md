# Calculadora con PyQt5

![Calculadora](assets/calculator-icon.png)  <!-- Si tienes un ícono, puedes agregarlo -->

Una calculadora funcional desarrollada con PyQt5 y diseñada con QTDesigner. Permite realizar operaciones matemáticas básicas y muestra los resultados con formato de 2 decimales.

## Características

- Interfaz gráfica intuitiva
- Operaciones básicas: suma (+), resta (-), multiplicación (*) y división (/)
- Manejo de decimales
- Botón de porcentaje (%)
- Diseño responsivo

## Requisitos Previos

- Python 3.7 o superior
- pip (gestor de paquetes de Python)

## Instalación


1. Clona el repositorio:
   ```bash
   git clone https://github.com/jdgonzalez03/simple-calculator.git
   cd simple-calculator
   ```

2. Crea y activa el entorno virtual:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # En Windows: .venv\Scripts\activate
   ```

3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

4. Ejecuta la calculadora:
   ```bash
   python main.py
   ```

## Estructura del Proyecto

calculadora-qt/
├── assets/           # Recursos gráficos
│   └── gui.py        # Código generado por QTDesigner
├── main.py           # Lógica principal de la aplicación
├── requirements.txt  # Dependencias del proyecto
└── README.md         # Este archivo
