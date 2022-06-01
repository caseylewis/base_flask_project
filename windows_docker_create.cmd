@echo off

@REM VARIABLES
set APP_NAME=base_flask_project
set PORT=5001

@REM STOP THE EXISTING CONTAINER
docker stop %APP_NAME%

@REM DELETE THE EXISTING CONTAINER
docker rm %APP_NAME%

@REM CREATE IMAGE AND RUN IT
docker image build -t %APP_NAME% .
docker run -p %PORT%:5000 --name %APP_NAME% -d %APP_NAME%

@REM DELETE ALL UNUSED IMAGES
@REM docker image prune