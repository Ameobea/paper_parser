rm out/*
rm split/*
python process.py
echo 'launching webserver on port 5000'
python web/server.py
