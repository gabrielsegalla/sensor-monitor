import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from app.data_handler import DataHandler

class SensorApp:
    def __init__(self, root, data_handler):
        self.root = root
        self.data_handler = data_handler

        self.figure = Figure(figsize=(5, 4), dpi=100)
        self.ax = self.figure.add_subplot(111)

        # Cria o canvas para embutir o gráfico no Tkinter
        self.canvas = FigureCanvasTkAgg(self.figure, master=root)
        self.canvas.get_tk_widget().pack()

        # Inicia a atualização do gráfico
        self.update_plot()

    def setup_ui(self):
        # Frame principal
        self.main_frame = ttk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Último dado
        self.latest_label = ttk.Label(self.main_frame, text="Último dado: --", font=("Arial", 14))
        self.latest_label.pack(pady=10)

        # Canvas para o gráfico
        self.figure, self.ax = plt.subplots(figsize=(5, 4))
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.main_frame)
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.pack(pady=10)

        # Botão para atualizar o gráfico
        self.update_button = ttk.Button(self.main_frame, text="Atualizar Gráfico", command=self.update_plot)
        self.update_button.pack(pady=5)

    def update_latest_data(self):
        """Atualiza o dado mais recente na interface."""
        latest_data = self.data_handler.get_data()
        if latest_data is not None:
            self.latest_label.config(text=f"Último dado: {latest_data}")
        self.root.after(1000, self.update_latest_data)  # Atualiza a cada 1 segundo

    def update_plot(self):
        """Atualiza o gráfico com os dados do DataHandler."""
        # Obtenha os dados para plotar
        data = self.data_handler.get_all_data()

        # Limpe o gráfico atual
        self.ax.clear()

        # Crie o novo gráfico
        if data:
            x = list(range(len(data)))
            y = data
            self.ax.plot(x, y, label="Dados do Sensor")
            self.ax.set_title("Dados em Tempo Real")
            self.ax.set_xlabel("Tempo")
            self.ax.set_ylabel("Valor")
            self.ax.legend()
        else:
            self.ax.text(0.5, 0.5, "Sem Dados", fontsize=14, ha='center', va='center', transform=self.ax.transAxes)

        # Atualize o canvas
        self.canvas.draw()        