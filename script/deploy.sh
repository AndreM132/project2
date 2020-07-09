. ~/.bashrc 

ssh jenkins@swarm-master << EOF
cd /home/andre_m132/project2
. /home/andre_m132/.bashrc
env OUTFIT_DB_URI="${OUTFIT_DB_URI}" env NEW_SECRET_KEY="${NEW_SECRET_KEY}" docker stack deploy --compose-file docker-compose.yaml stackapp

EOF
