import socket

def handle_client_input(client_message: str) -> str:
    """Processes the client's message based on predefined commands."""
    if not client_message:
        return ""

    cmd, content = client_message[0], client_message[1:]

    if cmd == 'A':
        return "".join(sorted(content, reverse=True))
    elif cmd == 'C':
        return "".join(sorted(content))
    elif cmd == 'D':
        return content.upper()
    return client_message

def launch_server(ip_address='127.0.0.1', port_num=12345):
    """Initializes and runs a TCP server that listens for client connections."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as srv_socket:
        srv_socket.bind((ip_address, port_num))
        srv_socket.listen(5)
        print(f"Server is active on {ip_address}:{port_num}")

        while True:
            conn, client_address = srv_socket.accept()
            with conn:
                print(f"New connection from {client_address}")
                while True:
                    received_data = conn.recv(1024).decode().strip()
                    if not received_data:
                        break
                    print(f"Incoming: {received_data}")
                    server_reply = handle_client_input(received_data)
                    print(f"Replying: {server_reply}")
                    conn.sendall(server_reply.encode())

if __name__ == "__main__":
    launch_server()
