import keyboard as k #можно заменить k на что угодно или удалить as k
def test(): # набор функций
  k.press("b") # нажимает и удерживает b
  k.release("b") # отпускает "b" если он нажат
  k.press_and_release("a") # нажимает и отпускает "a"
  k.write("launch") # пишет launch
