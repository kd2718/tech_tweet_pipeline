docker-compose up -d --force-recreate 

sleep 8;
docker-compose ps;
echo "if things are working than you should go here: \n http://localhost:8123/play?user=default#c2VsZWN0ICogZnJvbSBUV0lUVEVSLnR3ZWV0cw=="

python main.py