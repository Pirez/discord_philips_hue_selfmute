
build:
	docker build -t dicsord-mute_philips-hue .

run:
	docker run -d --restart always dicsord-mute_philips-hue