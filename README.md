# Mini-Banco
Programa que utiliza conocimientos básico en el leguaje de programación Python, como un mini proyecto para reforzar la lógica de programación en este entorno.

# 🏧 Simulador de Cajero Automático en Python

Un programa de consola sencillo desarrollado en Python que simula las operaciones básicas de un cajero automático y lleva un registro de la actividad mediante un historial.

## ✨ Características Principales

* **1. Registrar Usuario:** Permite dar de alta nuevos usuarios con validación para evitar nombres duplicados.
* **2. Consulta de Saldo:** Muestra el balance actual de la cuenta.
* **3. Depositar / Retirar:** Permite ingresar o extraer dinero (funcionalidad en expansión según la lógica de tu código).
* **4. Historial:** Registra los pasos, ingresos al menú, errores y acciones de los usuarios en tiempo real.
* **5. Salir:** Cierra la sesión o el programa de forma segura.

## 🚀 Requisitos

* **Python 3.x** instalado en tu sistema.

## 💻 Cómo ejecutar el código

1. Clona este repositorio o descarga el archivo principal de Python (por ejemplo, `cajero.py`).
2. Abre tu terminal o consola.
3. Ejecuta el script con el siguiente comando:

```bash
python cajero.py
```

## 🗺️ Menú de Navegación

Al iniciar el programa verás el siguiente menú en consola:

```text
----**MENU DE CAJERO**----
1. Registrar Usuario
2. Consulta de Saldo
3. Depositar / Retirar
4. Historial
5. Salir
```

## 📌 Manejo de Sesión y Errores

* Para cancelar el registro de un usuario en cualquier momento, puedes escribir la letra **`s`**.
* Si el nombre de usuario ya existe en el sistema, el programa te pedirá ingresar un nombre alternativo.
* Las opciones inválidas son detectadas automáticamente y se almacenan en el **historial**.

## 🛠️ Mejoras Pendientes

* [ ] Implementar el cálculo exacto de depósitos y retiros por usuario.
* [ ] Agregar persistencia de datos (guardar usuarios en un archivo JSON o base de datos).
* [ ] Mejorar la interfaz visual en consola.
