from ovtp.server import OvtpServer
import json
import asyncio


class Server:
    def __init__(self):
        self.i = 0
        self.oes = OvtpServer(self.callback, debug=True, verbose=True)

    def run(self):
        asyncio.run(self.oes.run_server())

    def callback(self, status, response_json):
        try:
            response = json.loads(response_json)
        except json.JSONDecodeError:
            return False, f"Bad json: {response_json}"

        self.i += 1
        print(f'[{self.i}] {status=} {response=}')
        return status, response
