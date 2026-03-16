# Calculadora con PyQt5

Una calculadora funcional desarrollada con PyQt5 y diseñada con QTDesigner. Permite realizar operaciones matemáticas básicas y muestra los resultados con formato de 2 decimales.
<img width="315" height="576" alt="Screenshot 2026-03-16 at 4 56 04 PM" src="https://github.com/user-attachments/assets/1f38ddf8-71fe-4dd3-a567-ea2cbe191384" />


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

```bash
calculadora-qt/
├── assets/           # Recursos gráficos
│   └── gui.py        # Código generado por QTDesigner
├── main.py           # Lógica principal de la aplicación
├── requirements.txt  # Dependencias del proyecto
└── README.md         # Este archivo
```
