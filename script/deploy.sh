. ~/.bashrc 

ssh andre_m132@swarm-master << EOF
cd /home/andre_m132/project2
docker stack deploy --compose-file docker-compose.yaml apps

EOF
