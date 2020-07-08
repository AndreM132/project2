.~/. bashrc

docker-compose build
docker push andrem132/apps:app1
docker push andrem132/apps:app2
docker push andrem132/apps:app3
docker push andrem132/apps:app4
docker push andrem132/apps:nginx
docker stack deploy --compose-file docker-compose.yaml apps
