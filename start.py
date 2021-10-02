import os
import json
import traceback
import asyncio
import threading
from socket import getfqdn

URL = os.environ.get("SOCKET_URL")


def start():
	try:
		import websockets

		async def hello():

			await asyncio.sleep(15)

			ws = await websockets.connect(URL)

			data = {"op": "nodestart", "id": "MAIN"}

			await ws.send(json.dumps(data))

			await ws.close()

		asyncio.get_event_loop().run_until_complete(hello())

	except Exception:
		traceback.print_exc()


#if URL:
#	threading.Thread(target=start).start()

if not os.path.isfile("Lavalink.jar"):
	print("Baixando lavalink")
	url = "https://github.com/zRitsu/LL-binaries/releases/download/0.0.1/Lavalink.jar"
	os.system(f"wget -q --header='Accept:application/octet-stream' -O Lavalink.jar {url}")
	print("Download concluido")

#with open("application.conf") as f:
#	data = f.read()
#	data = data.replace("%PORT_HERE%", str(os.environ.get('PORT', '2333'))).replace("%PASSWORD_HERE%", os.environ.get("PASSWORD", '"youshallnotpass"'))
#with open("application.conf", "w") as fw:
#	fw.write(data)

print(f"Host = {getfqdn()}")

os.system('sed -i "s|PORT|$PORT|" application.yml')
password = os.environ.get("PASSWORD")
os.system(f'sed -i "s|PASSWORD|{"$PASSWORD" if password else "youshallnotpass"}|" application.yml')
options = os.environ.get("JAVA_OPTS", "")

# os.system(f'java {java_options} -jar Lavalink.jar')
# options = "-XX:CICompilerCount=2 -XX:ActiveProcessorCount=8 -Dfile.encoding=UTF-8 -Xmx450m -Xss512k"
os.system(f'java {options} -jar Lavalink.jar')
