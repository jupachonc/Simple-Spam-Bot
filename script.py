import pyautogui as p

msg = input("¿Qué Mensaje desea enviar?\n")

n = int(input("¿Cuántas copias del mensaje quiere enviar?\n"))

for x in range(n):
    p.write(msg)
    p.press("enter")
