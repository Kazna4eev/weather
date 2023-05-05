import socket
import threading

weather_data = {
    ('Ukraine', 'Kiev'): 'cloudy',
    ('Ukraine', 'Lvov'): 'rainy',
    ('USA', 'New York'): 'sunny',
    ('USA', 'Los Angeles'): 'windy',
    ('China', 'Beijing'): 'smoggy',
}

def handle_client(conn, addr):
    print(f"Connected by {addr}")
    data = conn.recv(1024).decode('utf-8')
    country, city = data.split(',')
    weather = get_weather(country, city)
    conn.sendall(weather.encode('utf-8'))
    conn.close()

def get_weather(country, city):
    if (country, city) in weather_data:
        return weather_data[(country, city)]
    else:
        return "Weather data not found."

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('localhost', 8888))
        s.listen()
        print("Server started. Listening for clients...")
        while True:
            conn, addr = s.accept()
            threading.Thread(target=handle_client, args=(conn, addr)).start()

if __name__ == '__main__':
    start_server()
