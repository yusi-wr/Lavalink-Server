import os

password = os.environ.get("PASSWORD")

with open('application.conf') as f:
	d = f.read()
	d = d.replace("DYNAMICPASSWORD", password if password else "youshallnotpass").replace('DYNAMICPORT', os.environ.get('PORT'))

with open('application.conf', 'w') as f:
	f.write(d)

java_options = os.environ.get("JAVA_TOOL_OPTIONS")

os.system(f'java -jar Andesite.jar {java_options}')