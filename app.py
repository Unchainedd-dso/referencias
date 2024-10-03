import os
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

class ImageApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Visualizador de Imagens")

        self.label = Label(root, text="Digite o nome da imagem:")
        self.label.pack(pady=10)

        self.entry = Entry(root)
        self.entry.pack(pady=10)

        self.button = Button(root, text="Carregar Imagem", command=self.carregar_imagem)
        self.button.pack(pady=10)

        self.canvas = Canvas(root, width=400, height=400)
        self.canvas.pack(pady=10)

    def carregar_imagem(self):
        nome_imagem = self.entry.get()
        nome_imagem = nome_imagem + ".jpeg"
        caminho_imagem = os.path.join('images', nome_imagem)

        if os.path.exists(caminho_imagem):
            self.mostrar_imagem(caminho_imagem)
        else:
            messagebox.showerror("Erro", "Imagem não encontrada!")

    def mostrar_imagem(self, caminho_imagem):
        img = Image.open(caminho_imagem)
        img = img.resize((400, 400), Image.LANCZOS)  # Redimensiona a imagem
        self.img_tk = ImageTk.PhotoImage(img)
        self.canvas.create_image(0, 0, anchor=NW, image=self.img_tk)

if __name__ == '__main__':
    root = Tk()
    app = ImageApp(root)
    root.mainloop()
