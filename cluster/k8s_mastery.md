



docker run --publish 5000:5000 --detach --name sa-logic sentiment-analysis-logic:1.0
docker run --publish 80:80 --detach --name sa-frontend sentiment-analysis-frontend:1.0


## Frontend

### Build
npm run build
