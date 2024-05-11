# Simple Blog Project by [FastAPI and React]

### It is a simple blog appliation created by FastAPI for Backend and React for Frontend


#### Steps:

- Run porject on local machine:
  - clone the repository
  - create virtual environment [python version is 3.12]: `python -m venv env`
  - install requirements: `pip install src/requirements.txt`
  - start uvicorn server from src folder: `uvicorn main:app --relaod`
  - start react server from frontend folder: `npm start`
  - open API documentation from : `http://localhost:8000/docs`
  - open frontend from: `http://localhost:3000`
  
- Run project by using Docker:
  - clone the repository
  - run `docker-compose up --build`
  - open API documentation from : `http://localhost:8000/docs`
  - open frontend from: `http://localhost:3000`