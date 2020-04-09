import asyncio
from asyncio import transports
from typing import Optional


class ServerProtocol(asyncio.Protocol):
    login: str = None
    server: 'Server'
    transport: transports.Transport

    def __init__(self, server: 'Server'):
        self.server = server

    def data_received(self, data: bytes):
        decoded = data.decode('utf-8')
        if self.login is not None:
            self.send_message(decoded)
        else:
            if decoded.startswith("login:"):
                self.login = decoded.replace("login:", "").replace("\r\n", "").strip()
                for user in self.server.clients:
                    if self.login == user.login and user != self:
                        self.transport.write(f"This nickname is busy, choose another one\n".encode('utf-8'))
                        self.transport.close()
                self.transport.write(f"Hello, {self.login}!\n".encode('utf-8'))
                self.send_server_history()
            else:
                self.transport.write("Wrong login!\n".encode('utf-8'))

    def connection_made(self, transport: transports.BaseTransport):
        self.server.clients.append(self)
        self.transport = transport
        print("New client entered")

    def connection_lost(self, exc: Optional[Exception]):
        self.server.clients.remove(self)
        print("Client quitted")

    def send_message(self, content: str):
        message = f"{self.login}: {content}\n".replace("\r\n", "")
        self.write_server_history(message)
        for user in self.server.clients:
            user.transport.write(message.encode('utf-8'))

    def send_server_history(self):
        if len(self.server.history) > 0:
            self.transport.write(f"Chat's last 10 messages >>>\n{''.join(self.server.history)}".encode('utf-8'))

    def write_server_history(self, message: str):
        if len(self.server.history) < 10:
            self.server.history.append(message)
        else:
            self.server.history.append(message)
            self.server.history.pop(0)


class Server:
    clients: list
    history: list

    def __init__(self):
        self.clients = []
        self.history = []

    def build_protocol(self):
        return ServerProtocol(self)

    async def start(self):
        loop = asyncio.get_running_loop()

        coroutines = await loop.create_server(
            self.build_protocol,
            '127.0.0.1',
            8888
        )
        print("Server running")
        await coroutines.serve_forever()


process = Server()

try:
    asyncio.run(process.start())
except KeyboardInterrupt:
    print("Server stopped manually")
