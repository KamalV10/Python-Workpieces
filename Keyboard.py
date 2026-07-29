import keyboard as k # можно заменить k на что угодно или удалить as k
def test(): # набор функций
  k.press("b") # нажимает и удерживает b
  k.release("b") # отпускает "b" если он нажат
  k.press_and_release("a") # нажимает и сразу отпускает "a"
  k.write("launch") # пишет launch
  k.is_pressed("c") # выдает True если нажат "c"
  k.send("shift+alt") # одновременно нажимает shift и alt
k.add_hotkey("alt+z", test) # выполняет функцию test при нажатии alt и z
