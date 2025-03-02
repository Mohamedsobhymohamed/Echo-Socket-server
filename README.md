# TCP Echo Server & Client

This project implements a simple **TCP Echo Server and Client** using Python's `socket` module. The server listens for incoming client connections and processes messages based on predefined commands. The client connects to the server, sends requests, and receives responses.

## Features

- The server sorts or modifies input strings based on a command prefix.
- The client sends test messages to the server and displays responses.
- Communication is established using **TCP sockets**.
- Wireshark can be used to monitor and analyze network traffic.

## Server Logic

The server processes incoming messages based on the **first character**:

- `A` → Sorts the rest of the string **in descending order**.
- `C` → Sorts the rest of the string **in ascending order**.
- `D` → Converts all letters to **uppercase**.
- Any other prefix → **Returns the message unchanged**.

## Files

- `server.py` → Runs the TCP **Echo Server**.
- `client.py` → Runs the TCP **Client** to send messages to the server.
- `README.md` → Documentation for setup and usage.

## Installation & Setup

### Prerequisites

- Python 3.x installed.
- Wireshark (optional for network analysis).

### Steps to Run

1. **Start the Server:**

   ```sh
   python server.py
   ```

   The server will start listening on **127.0.0.1:12345**.

2. **Run the Client:**

   ```sh
   python client.py
   ```

   The client will send test messages to the server and display responses.

## Testing with Wireshark

1. **Open Wireshark** and start capturing packets.
2. Apply the filter:
   ```
   tcp.port == 12345
   ```
3. Run the server and client, then analyze **TCP communication packets**.
4. Stop and save the Wireshark capture for reference.

## Expected Output

### Example Client Input:

```
Ahello
Cworld
Dpython
Xinvalid
```

### Corresponding Server Response:

```
ollhe
dlorw
PYTHON
Xinvalid
```

## Troubleshooting

- **Connection Refused Error**: Ensure the server is running before starting the client.
- **No Response from Server**: Check if the correct IP and port are used.
- **Packets Not Captured in Wireshark**: Select the correct network interface (Loopback Adapter for localhost).

## License

This project is open-source and available for modification and use.

## Author

Developed by **Mohamed Sobhy**.

