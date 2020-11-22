import os

lavalink_url = "https://github.com/Frederikam/Lavalink/releases/download/3.2.2/Lavalink.jar"

if not os.path.isfile("Lavalink.jar"):
	print("Baixando lavalink")
	os.system(f'wget -q -N {lavalink_url}')

os.system('sed -i "s|PORT|$PORT|" application.yml')

password = os.environ.get("PASSWORD")

os.system(f'sed -i "s|PASSWORD|{"$PASSWORD" if password else "youshallnotpass"}|" application.yml')

java_options = os.environ.get("JAVA_OPTIONS")

os.system(f'java -jar Lavalink.jar {java_options}')