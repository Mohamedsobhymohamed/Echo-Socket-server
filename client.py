import socket

def communicate_with_server(msg, server_ip='127.0.0.1', server_port=12345):
    """Establishes a connection with the server, sends a message, and receives a response."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_conn:
        client_conn.connect((server_ip, server_port))
        client_conn.sendall(msg.encode())
        server_reply = client_conn.recv(1024).decode()
        print(f"Server Response: {server_reply}")

if __name__ == "__main__":
    sample_inputs = ["Ahello", "Cworld", "Dpython", "Xinvalid"]
    for item in sample_inputs:
        communicate_with_server(item)
