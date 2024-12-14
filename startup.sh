echo "Starting up the server..."
sudo docker-compose up -d
echo "WAIT FOR THE MODEL TO BE PULLED IF RUNNING FOR THE FIRST TIME"
python3 main.py
