# piano-tiles-bot

Script Python que detecta píxeles oscuros en columnas de la pantalla y hace clic usando PyAutoGUI. Las coordenadas dependen de la posición del juego y la resolución de la pantalla.

## Estructura

- [piano-tiles.py](piano-tiles.py)

## Preparación y uso

Instala `pyautogui` y `keyboard` en un entorno Python local. Ejecuta `python piano-tiles.py --columns 100 200 300 400 --y 475`, sustituyendo los números por las cuatro columnas reales del juego. Mantén pulsada `s` para terminar. El script original referenciaba `x4` sin definir; ahora exige cuatro coordenadas explícitas antes de iniciar.

## Pruebas

```sh
python -m unittest discover -p test_piano_tiles.py
```

Las cuatro pruebas usan dobles de pantalla y teclado: verifican la cuarta columna, la detención, los límites de pantalla y los argumentos incompletos sin hacer clic ni capturar el escritorio.

## Validación y estado

Esta guía se contrastó con el árbol de archivos y los manifiestos del repositorio. No se ha validado una ejecución completa contra servicios externos, bases de datos o hardware. Las versiones y los scripts mostrados describen el código actual; no implican que sus dependencias antiguas sigan siendo compatibles.
