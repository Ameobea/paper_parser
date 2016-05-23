rm out/*
rm split/*
python process.py
rm web/data/raw/*
cp out/* web/data/raw/
cp split/* web/data/pdf/
echo 'launching webserver on port 5000'
cd web
python server.py
