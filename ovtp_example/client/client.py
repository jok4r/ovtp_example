from ovtp.client import OvtpClient
import json
import asyncio


class Client:
    def __init__(self, ip):
        self.oec = OvtpClient(ip, debug=True, verbose=True)
        self.loop = asyncio.new_event_loop()

    def run(self):
        while True:
            message = input("Input your message: ")
            # print(asyncio.run(self.action(message)))
            print(self.loop.run_until_complete(self.action(message)))

    async def action(self, message):
        result = await self.oec.send_message(json.dumps(message), timeout=2, retry=2)
        # await self.oec.close_connection()
        return f"Result is: {result}"
