from queue import Queue

class DataHandler:
    def __init__(self, file_name="sensor_data.csv"):
        self.file_name = file_name
        self.data_queue = Queue()  # Fila para dados recebidos

    def save_data(self, value):
        """Salva o valor em um arquivo CSV."""
        with open(self.file_name, 'a') as file:
            file.write(f"{value}\n")
        print(f"Data saved: {value}")

    def add_to_queue(self, value):
        """Adiciona o dado à fila e salva no arquivo."""
        self.data_queue.put(float(value))
        self.save_data(value)

    def get_data(self):
        """Obtém o dado mais recente da fila."""
        if not self.data_queue.empty():
            return self.data_queue.get()
        return None
