docker-compose stop;
docker-compose rm ;

yes Y | docker volume rm -f $(docker volume ls -q)
