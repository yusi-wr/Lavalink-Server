import os
import json
import traceback
import asyncio
import threading

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
	token = 'c081c0771b1908ece26aae2df6ffdc8f0e276fd6'
	author_id = "zRitsu"
	repo_name = "LL-binaries"
	a = os.popen(f'curl -s -H "Authorization: token {token}" https://api.github.com/repos/{author_id}/{repo_name}/releases/latest').read().strip()
	a = json.loads(a)
	print(a)
	asset_id = (a['assets'][0]['id'])
	url = f"https://api.github.com/repos/{author_id}/{repo_name}/releases/assets/{asset_id}?access_token={token}"
	os.system(f"wget -q --header='Accept:application/octet-stream' -O Lavalink.jar {url}")
	print("Download concluido")

#with open("application.conf") as f:
#	data = f.read()
#	data = data.replace("%PORT_HERE%", str(os.environ.get('PORT', '2333'))).replace("%PASSWORD_HERE%", os.environ.get("PASSWORD", '"youshallnotpass"'))
#with open("application.conf", "w") as fw:
#	fw.write(data)

os.system('sed -i "s|PORT|$PORT|" application.yml')
password = os.environ.get("PASSWORD")
os.system(f'sed -i "s|PASSWORD|{"$PASSWORD" if password else "youshallnotpass"}|" application.yml')
options = os.environ.get("JAVA_TOOL_OPTIONS", "")

# os.system(f'java {java_options} -jar Lavalink.jar')
# options = "-XX:CICompilerCount=2 -XX:ActiveProcessorCount=8 -Dfile.encoding=UTF-8 -Xmx450m -Xss512k"
os.system(f'java {options} -jar Lavalink.jar')
