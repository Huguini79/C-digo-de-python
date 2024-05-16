import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
import time
import webbrowser
import socket
import random

root = tk.Tk()
root.geometry('660x550')
root.title('Fondos en Python')
def primer_botón():
    root.configure(bg='yellow')
def segundo_botón():
    root.configure(bg='blue')
def tercer_botón():
    root.configure(bg='green')
def cuarto_botón():
    root.configure(bg='pink')
def quinto_botón():
    root.configure(bg='black')
def sexto_botón():
    root.configure(bg='white')
def séptimo_botón():
    root.configure(bg='brown')
def octavo_botón():
    root.configure(bg='red')
def noveno_botón():
    root.configure(bg='orange')
def enviar():
    texto2 = texto.get('1.0', 'end-1c')
    if texto2 == 'amarillo':
        root.configure(bg='yellow')
    elif texto2 == 'azul':
        root.configure(bg='blue')
    elif texto2 == 'rosa':
        root.configure(bg='pink')
    elif texto2 == 'rojo':
        root.configure(bg='red')
    elif texto2 == 'negro':
        root.configure(bg='black')
    elif texto2 == 'white':
        root.configure(bg='white')
    elif texto2 == 'naranja':
        root.configure(bg='orange')
    elif texto2 == 'verde':
        root.configure(bg='green')
    elif texto2 == 'marrón':
        root.configure(bg='brown')
    else:
        messagebox.showwarning('Error', 'No te he entendido')
def calculadora():
    pregunta = simpledialog.askfloat('Mensaje', 'Dime un número para la calculadora.')
    operador = simpledialog.askstring('Mensaje', 'Dime el operador para la calculadora.')
    pregunta2 = simpledialog.askfloat('Mensaje', 'Dime un último número para la calculadora.')
    suma = pregunta + pregunta2
    resta = pregunta - pregunta2
    multiplicación = pregunta * pregunta2
    división = pregunta / pregunta2
    if operador == '+':
        messagebox.showinfo('Mensaje', 'El resultado de la suma es: '+ str(suma))
    elif operador == '-':
        messagebox.showinfo('Mensaje', 'El resultado de la resta es: '+ str(resta))
    elif operador == '*':
        messagebox.showinfo('Mensaje', 'El resultado de la multiplicación es: '+ str(multiplicación))
    elif operador == '/':
        messagebox.showinfo('Mensaje', 'El resultado de la división es: '+ str(división))
    else:
        messagebox.showwarning('Error', 'No te he entendido.')
def cronómetro():
    texto4 = texto3.get('1.0', 'end-1c')
    texto5 = int(texto4)
    for i in range(texto5 + 1):
        print('Contador: ', i)
        time.sleep(1)
        if i == texto5:
            messagebox.showinfo('Mensaje', 'Operación exitosa.')
def palabras():
    for i in range(500):
        print('Hola')
    for i in range(500):
        print('Hugo')
def navegador():
    página = simpledialog.askstring('Mensaje', 'Dime la url de el sitio web que quieres ir.')
    webbrowser.open(página)
def youtube():
    webbrowser.open('https://www.youtube.com')
def ip():
    pregunta = messagebox.askquestion('Mensaje importante', 'Esta parte del programa se ha hecho para fines educativos y éticos, si vas a esta parte del programa, vas a poder ver las direcciones ip de hosts/servidores y no se debe usar para hacer el mal...¿Quieres ejecutarlo?')
    if pregunta == 'yes':
      root2 = tk.Tk()
      root2.configure(bg='yellow')
      root2.geometry('660x550')
      texto6 = tk.Text(root2, height='2', width='10')
      label = tk.Label(root2, text='Busca direcciones ip por nombres.')
      label.grid(row=0, column=0, padx=10, pady=10)
      texto6.grid(row=0, column=1, padx=10, pady=10)
      def solicitud():
        try:
          texto7 = texto6.get('1.0', 'end-1c')
          ip = socket.gethostbyname(texto7)
          messagebox.showinfo('Mensaje', 'La dirección ip del host es: '+ ip)
        except:
          messagebox.showwarning('Error', 'No se ha podido encontrar la dirección ip del host.')
      def cerrar_ventana():
          root2.destroy()
      botón16 = tk.Button(root2, text='Enviar', height='2', width='10', bg='yellow', fg='red', command=solicitud)
      botón17 = tk.Button(root2, text='Cerrar Ventana', height='2', width='10', bg='lightblue', fg='white', command=cerrar_ventana)
      botón16.grid(row=0, column=2, padx=10, pady=10)
      botón17.grid(row=2, column=0, padx=10, pady=10)
      root2.mainloop()
    else:
        exit
def pantalla():
       root3 = tk.Tk()
       root3.configure(bg='black')
       root3.attributes('-fullscreen', True)
       label = tk.Label(root3, text='Error 002', bg='black', fg='white', height='2', width='25')
       label2 = tk.Label(root3, text='Un error ha ocurrido, intenta apagar tu equipo, si no se soluciona el problema, contacta con la cuenta técnica elgranhuguini.', bg='black', fg='white', height='2', width='100')
       label.grid(row=1, column=0, padx=10, pady=10)
       label2.grid(row=3, column=0, padx=10, pady=10)
       root3.after(10000, root3.destroy)
       root3.mainloop()
def ajustes():
    root4 = tk.Tk()
    root4.configure(bg='green')
    root4.geometry('660x550')
    def pantalla_ajustes():
        pregunta = messagebox.askquestion('Mensaje', '¿Quieres que esté la pantalla completa del todo?')
        if pregunta == 'yes':
            root4.attributes('-fullscreen', True)
            root.attributes('-fullscreen', True)
        else:
            pregunta2 = messagebox.askquestion('Mensaje', '¿Quieres que la pantalla la puedas ajustar tú?')
            if pregunta2 == 'yes':
                root4.attributes('-fullscreen', False)
                root.attributes('-fullscreen', False)
            else:
                exit
    def pantalla_cerrar():
        root4.destroy()
    botón18 = tk.Button(root4, text='Pantalla', height='2', width='10', bg='yellow', fg='green', command=pantalla_ajustes)
    botón19 = tk.Button(root4, text='Cerrar Ventana', height='2', width='10', bg='yellow', fg='green', command=pantalla_cerrar)
    botón18.grid(row=0, column=0, padx=10, pady=10)
    botón19.grid(row=2, column=0, padx=10, pady=10)
def google():
    webbrowser.open('https://www.google.com')
def gmail():
    webbrowser.open('https://www.gmail.com')
def google_maps():
    webbrowser.open('https://www.googlemaps.com')
def número_aleatorio():
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    aleatorio = random.choice(lista)
    messagebox.showinfo('Mensaje', 'El número aleatorio es: '+ str(aleatorio))
def restaurante():
    root5 = tk.Tk()
    root5.configure(bg='yellow')
    root5.geometry('660x550')
    def menú():
        global precio, precio2, precio3, suma, prr
        root6 = tk.Tk()
        root6.configure(bg='yellow')
        root6.geometry('660x550')
        def cerrar_ventana2():
            root6.destroy()
        def enviar2():
            precio, precio2, precio3 = 0, 0, 0
            texto11 = texto8.get('1.0', 'end-1c')
            texto12 = texto9.get('1.0', 'end-1c')
            texto13 = texto10.get('1.0', 'end-1c')
            lista = ['', 'Hamburguesa', 'Agua', 'Papas fritas']
            if texto11 == lista[1]:
                precio += 5
            elif texto11 == lista[2]:
                precio2 += 0.45
            elif texto11 == lista[3]:
                precio3 += 3.75
            elif texto11 == lista[0]:
                prr = 0
            if texto12 == lista[1]:
                precio += 5
            elif texto12 == lista[2]:
                precio2 += 0.45
            elif texto12 == lista[3]:
                precio3 += 3.75
            elif texto12 == lista[0]:
                prr = 0
            if texto13 == lista[1]:
                precio += 5
            elif texto13 == lista[2]:
                precio2 += 0.45
            elif texto13 == lista[3]:
                precio3 += 3.75
            elif texto13 == lista[0]:
                prr = 0.45
            suma = precio + precio2 + precio3
            messagebox.showinfo('Mensaje', 'El pedido sale: '+ str(suma))
        def borrar():
            global precio, precio2, precio3
            precio, precio2, precio3 = 0, 0, 0
            texto8.delete('1.0', 'end')
            texto9.delete('1.0', 'end')
            texto10.delete('1.0', 'end')
        label = tk.Label(root6, text='Menú: Hamburguesa, Agua, Papas fritas', height='2', width='100', bg='blue', fg='green')
        label.grid(row=0, column=0, padx=10, pady=10)
        root6.attributes('-fullscreen', True)
        texto8 = tk.Text(root6, height='2', width='10', bg='yellow', fg='green')
        texto9 = tk.Text(root6, height='2', width='10', bg='yellow', fg='green')
        texto10 = tk.Text(root6, height='2', width='10', bg='yellow', fg='green')
        botón25 = tk.Button(root6, text='Enviar', height='2', width='10', bg='yellow', fg='green', command=enviar2)
        botón24 = tk.Button(root6, text='Cerrar Ventana', height='2', width='10', bg='yellow', fg='green', command=cerrar_ventana2)
        botón26 = tk.Button(root6, text='Borrar', height='2', width='10', bg='yellow', fg='red', command=borrar)
        texto8.grid(row=2, column=0, padx=10, pady=10)
        texto9.grid(row=3, column=0, padx=10, pady=10)
        texto10.grid(row=4, column=0, padx=10, pady=10)
        botón25.grid(row=5, column=0, padx=10, pady=10)
        botón24.grid(row=1, column=0, padx=10, pady=10)
        botón26.grid(row=6, column=0, padx=10, pady=10)
        root6.mainloop()
    botón23 = tk.Button(root5, text='Menú', height='2', width='10', bg='yellow', fg='blue', command=menú)
    botón23.grid(row=0, column=0, padx=10, pady=10)
    root5.mainloop()
def hugo():
    messagebox.showinfo('Mensaje', 'Hugo')
def videojuego():
    class Application(tk.Frame):
        def __init__(self, master=None):
            super().__init__(master)
            self.master = master
            self.master.title("Juego de la Serpiente")
            self.grid()
            self.create_widgets()
            self.snake = [(20, 20), (20, 40), (20, 60)]
            self.apple = self.create_apple()
            self.direction = "Right"
            self.score = 0
            self.running = True
            self.after(100, self.perform_actions)

        def create_widgets(self):
            self.canvas = tk.Canvas(self, width=600, height=400, background="black")
            self.canvas.grid(row=0, column=0, columnspan=3)
            self.score_label = tk.Label(self, text="Puntos: 0", font=("TkDefaultFont", 16))
            self.score_label.grid(row=1, column=0)
            self.restart_button = tk.Button(self, text="Reiniciar Juego", command=self.restart_game)
            self.restart_button.grid(row=1, column=2)
            self.bind_all("<Key>", self.on_key_press)

        def create_apple(self):
            return random.randint(0, 29) * 20, random.randint(0, 19) * 20

        def on_key_press(self, e):
            new_direction = e.keysym
            all_directions = ("Up", "Down", "Left", "Right")
            opposites = ({"Up", "Down"}, {"Left", "Right"})
            if (new_direction in all_directions and
                    not {new_direction, self.direction} in opposites):
                self.direction = new_direction

        def perform_actions(self):
            if self.running:
                self.move_snake()
                self.check_collisions()
                self.after(100, self.perform_actions)

        def move_snake(self):
            head_x, head_y = self.snake[0]
            if self.direction == "Left":
                head_x -= 20
            elif self.direction == "Right":
                head_x += 20
            elif self.direction == "Up":
                head_y -= 20
            elif self.direction == "Down":
                head_y += 20
            new_head = (head_x, head_y)

            # Check if snake has eaten an apple
            if new_head == self.apple:
                self.apple = self.create_apple()
                self.snake = [new_head] + self.snake
                self.score += 1
                self.update_score_display()
            else:
                self.snake.pop()
                self.snake = [new_head] + self.snake
            self.redraw()

        def check_collisions(self):
            head_x, head_y = self.snake[0]
            if (head_x < 0 or head_x >= self.canvas.winfo_width() or
                    head_y < 0 or head_y >= self.canvas.winfo_height() or
                    (head_x, head_y) in self.snake[1:]):
                self.running = False

        def update_score_display(self):
            self.score_label.config(text=f"Puntos: {self.score}")

        def redraw(self):
            self.canvas.delete("snake")
            self.canvas.delete("apple")
            self.canvas.create_rectangle(self.apple[0], self.apple[1], self.apple[0]+20, self.apple[1]+20, fill="red", tags="apple")
            for x, y in self.snake:
                self.canvas.create_rectangle(x, y, x+20, y+20, fill="green", tags="snake")

        def restart_game(self):
            self.snake = [(20, 20), (20, 40), (20, 60)]
            self.apple = self.create_apple()
            self.direction = "Right"
            self.score = 0
            self.update_score_display()
            self.running = True
            self.redraw()

    # Crear una nueva ventana para el juego
    game_window = tk.Toplevel(root)
    app = Application(master=game_window)
    app.pack()

texto = tk.Text(root, width='10', height='2')
botón = tk.Button(root, text='Enviar', height='2', width='10', bg='yellow', fg='white', command=enviar)
botón1 = tk.Button(root, text='Amarillo', height='2', width='10', bg='yellow', fg='white', command=primer_botón)
botón2 = tk.Button(root, text='Azul', height='2', width='10', bg='blue', fg='white', command=segundo_botón)
botón3 = tk.Button(root, text='Verde', height='2', width='10', bg='green', fg='white', command=tercer_botón)
botón4 = tk.Button(root, text='Rosa', height='2', width='10', bg='pink', fg='white', command=cuarto_botón)
botón5 = tk.Button(root, text='Negro', height='2', width='10', bg='black', fg='white', command=quinto_botón)
botón6 = tk.Button(root, text='Blanco', height='2', width='10', bg='white', fg='white', command=sexto_botón)
botón7 = tk.Button(root, text='Marrón', height='2', width='10', bg='brown', fg='white', command=séptimo_botón)
botón8 = tk.Button(root, text='Rojo', height='2', width='10', bg='red', fg='white', command=octavo_botón)
botón9 = tk.Button(root, text='Naranja', height='2', width='10', bg='orange', fg='white', command=noveno_botón)
botón10 = tk.Button(root, text='Calculadora', bg='green', fg='yellow', height='2', width='10', command=calculadora)
botón12 = tk.Button(root, bg='yellow', fg='blue', text='1000 palabras Hola y Hugo', command=palabras)
texto3 = tk.Text(root, height='2', width='10')
botón11 = tk.Button(root, text='Enviar para cronómetro', height='2', width='10', bg='orange', fg='white', command=cronómetro)
botón13 = tk.Button(root, text='Navegador', bg='yellow', fg='orange', height='2', width='10', command=navegador)
botón14 = tk.Button(root, text='Youtube', bg='red', fg='white', height='2', width='10', command=youtube)
botón15 = tk.Button(root, text='Buscador de ips', bg='red', fg='white', height='2', width='10', command=ip)
botón16 = tk.Button(root, text='Hackeo', height='2', width='10', bg='yellow', fg='blue', command=pantalla)
botón17 = tk.Button(root, text='Ajustes', height='2', width='10', bg='yellow', fg='blue', command=ajustes)
botón18 = tk.Button(root, text='Google', height='2', width='10', bg='yellow', fg='blue', command=google)
botón19 = tk.Button(root, text='Gmail', height='2', width='10', bg='yellow', fg='blue', command=gmail)
botón20 = tk.Button(root, text='Google maps', height='2', width='10', bg='yellow', fg='blue', command=google_maps)
botón21 = tk.Button(root, text='Número aleatorio hasta el 10', height='2', width='10', bg='yellow', fg='blue', command=número_aleatorio)
botón22 = tk.Button(root, text='Restaurante', height='2', width='10', bg='yellow', fg='blue', command=restaurante)
botón23 = tk.Button(root, text='Hugo', height='2', width='10', bg='yellow', fg='pink', command=hugo)
botón24 = tk.Button(root, text='Videojuego por Copilot', height='2', width='25', bg='yellow', fg='blue', command=videojuego)
texto6 = tk.Text(root, height='2', width='10')
texto.grid(row=0, column=0, padx=10, pady=10)
botón.grid(row=0, column=1, padx=10, pady=10)
botón1.grid(row=0, column=2, padx=10, pady=10)
botón2.grid(row=0, column=3, padx=10, pady=10)
botón3.grid(row=0, column=4, padx=10, pady=10)
botón4.grid(row=0, column=5, padx=10, pady=10)
botón5.grid(row=0, column=6, padx=10, pady=10)
botón6.grid(row=0, column=7, padx=10, pady=10)
botón7.grid(row=0, column=8, padx=10, pady=10)
botón8.grid(row=0, column=9, padx=10, pady=10)
botón9.grid(row=0, column=10, padx=10, pady=10)
botón10.grid(row=0, column=11, padx=10, pady=10)
texto3.grid(row=1, column=0, padx=10, pady=10)
botón11.grid(row=1, column=1, padx=10, pady=10)
botón12.grid(row=1, column=2, padx=10, pady=10)
botón13.grid(row=1, column=3, padx=10, pady=10)
botón14.grid(row=1, column=4, padx=10, pady=10)
botón15.grid(row=1, column=5, padx=10, pady=10)
botón16.grid(row=5, column=0, padx=10, pady=10)
botón17.grid(row=1, column=6, padx=10, pady=10)
botón18.grid(row=1, column=7, padx=10, pady=10)
botón19.grid(row=1, column=8, padx=10, pady=10)
botón20.grid(row=1, column=9, padx=10, pady=10)
botón21.grid(row=1, column=10, padx=10, pady=10)
botón22.grid(row=1, column=11, padx=10, pady=10)
botón23.grid(row=1, column=12, padx=10, pady=10)
botón24.grid(row=2, column=0, padx=10, pady=10)
root.mainloop()