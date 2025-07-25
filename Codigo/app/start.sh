docker build -t fastapi-app .
docker run -d -p 8001:8001 --name proyecto fastapi-app