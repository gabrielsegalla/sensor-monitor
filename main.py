from app.tcp_server import TCPServer
from app.tcp_client_simulator import TCPSensorSimulator
from app.data_handler import DataHandler
from app.plotter import Plotter
from app.api import start_api
import threading

def start_client():
    """Inicia o cliente simulador em uma thread separada."""
    simulator = TCPSensorSimulator()
    simulator.send_data()

def start_server(data_handler):
    """Inicia o servidor TCP para receber dados."""
    server = TCPServer(data_handler)
    for data in server.start_server():
        print(f"Server received: {data}")
        data_handler.add_to_queue(data)

if __name__ == "__main__":
    # Inicializa o gerenciador de dados
    data_handler = DataHandler()

    # Inicia o cliente simulador em uma thread separada
    client_thread = threading.Thread(target=start_client, daemon=True)
    client_thread.start()

    # Inicia o servidor TCP em uma thread separada
    server_thread = threading.Thread(target=start_server, args=(data_handler,), daemon=True)
    server_thread.start()

    # Inicia a API Flask em uma thread separada
    api_thread = threading.Thread(target=start_api, args=(data_handler,), daemon=True)
    api_thread.start()

    # Inicia o plotador em tempo real
    plotter = Plotter(data_handler)
    plotter.start_plot()
