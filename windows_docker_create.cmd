@echo off

@REM VARIABLES
set APP_NAME=base_flask_project

@REM STOP THE EXISTING CONTAINER
docker stop %APP_NAME%

@REM DELETE THE EXISTING CONTAINER
docker rm %APP_NAME%

@REM CREATE IMAGE AND RUN IT
docker image build -t %APP_NAME% .
docker-compose up -d

@REM DELETE ALL UNUSED IMAGES
@REM docker image prune