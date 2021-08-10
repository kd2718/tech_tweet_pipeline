docker-compose up -d --force-recreate 

sleep 8;
docker-compose ps;

python main.py