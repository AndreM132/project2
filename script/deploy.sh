. ~/.bashrc 

ssh jenkins@swarm-master << EOF
cd /home/andre_m132/project2
. /home/andre_m132/.bashrc
docker stack deploy --compose-file docker-compose.yaml stackapp

EOF
