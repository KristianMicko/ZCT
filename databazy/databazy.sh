docker network create zadanie
docker run -p 3306:3306 --network zadanie --name mysql -e MYSQL_ALLOW_EMPTY_PASSWORD=yes -d mysql
#docker exec -i mysql mysql < prikazy.sql
./naplnenie.sh

