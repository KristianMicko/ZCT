cd databazy
./databazy.sh
cd ..

cd flask
docker build -t flask-run .
docker run -p 3500:5000 --name restdostup --network zadanie -itd flask-run

cd ..
cd front-end
./front-end.sh
