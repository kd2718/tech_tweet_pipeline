docker-compose stop;
docker-compose rm ;

docker volume rm -f $(docker volume ls -q)
