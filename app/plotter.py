import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class Plotter:
    def __init__(self, data_handler):
        self.data_handler = data_handler
        self.data = []  # Lista para armazenar dados recebidos

    def update_plot(self, frame):
        """Atualiza o gráfico em tempo real."""
        new_data = self.data_handler.get_data()
        if new_data is not None:
            self.data.append(new_data)
            if len(self.data) > 100:  # Mantém apenas os últimos 100 pontos
                self.data.pop(0)

        plt.cla()
        plt.plot(self.data, label="Sensor Data")
        plt.xlabel("Time")
        plt.ylabel("Value")
        plt.title("Real-Time Sensor Data")
        plt.legend()

    def start_plot(self):
        """Inicia o gráfico em tempo real."""
        print("Starting real-time plot...")
        animation = FuncAnimation(plt.gcf(), self.update_plot, interval=1000)
        plt.show()
