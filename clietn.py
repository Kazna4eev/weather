import socket

# Создаем клиентский сокет
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(('localhost', 8888))
    country = input("Enter country: ")
    city = input("Enter city: ")
    s.sendall(f"{country},{city}".encode('utf-8'))
    response = s.recv(1024).decode('utf-8')
    print(response)
