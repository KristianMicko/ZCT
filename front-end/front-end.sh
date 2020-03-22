docker build -t myapp .
docker run --rm httpd:2.4 cat /usr/local/apache2/conf/httpd.conf > my-httpd.conf
docker rmi myapp
docker build -t myapp .
docker run -p 8080:80 --name aplikacia --network zadanie -itd myapp 
