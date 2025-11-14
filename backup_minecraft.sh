#!/bin/bash
while :;do
	echo "> cd minecraft-server; cp /var/minecraft /tmp/; tar cavf game_$(date +%s)_$(date +%Y%m%d_%H%M%S).tar"
	cd ~/minecraft-server && \
	docker compose exec -it minecraft-rcon mcrcon list save-all && \
	docker run --rm -it \
		-v minecraft-server_minecraft-core:/var/minecraft:ro \
		-v ~/minecraft-server:/mnt/host \
		-w /var/minecraft alpine sh \
		-c "cp -r /var/minecraft /tmp/ && cd /tmp/minecraft && tar cavf /mnt/host/mods/game_$(date +%s)_$(date +%Y%m%d_%H%M%S).tar --exclude .fabric --exclude libraries --exclude versions ./" && \
	for i in ~/minecraft-server/mods/*.tar
	do
		echo "> xz ${i}"
		xz "${i}"
	done
	echo "> mv *xz ~/Downloads/"
	mv ~/minecraft-server/mods/*xz ~/Downloads/

	echo "> mv ~/Downloads/*xz ~/gdrive"
	mountpoint -q ~/gdrive && mv ~/Downloads/*xz ~/gdrive/Chrome\ から保存/

	echo "> wait 3hour"
	countdown 10800 #3hours
done

