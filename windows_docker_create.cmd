@echo off

@REM VARIABLES - MAKE SURE THIS MATCHES THE APP_NAME IN 'app.py'
set APP_NAME=base_flask_project
set TEMP_DIR=C:\Users\Casey\Desktop
set COPY_DATA=1

@REM COPY DATA DIRECTORY FROM DOCKER TO DESKTOP
if %COPY_DATA%==1 (
 echo Copying data from container to host...
 docker cp %APP_NAME%:"\data_%APP_NAME%" "%TEMP_DIR%"
 echo "new" > %TEMP_DIR%\data_%APP_NAME%\test.txt
) else (
 echo Not copying data.
)

@REM STOP THE EXISTING CONTAINER
docker stop %APP_NAME%

@REM DELETE THE EXISTING CONTAINER
docker rm %APP_NAME%

@REM CREATE IMAGE AND RUN IT
docker image build -t %APP_NAME% .
docker-compose up -d

@REM COPY DATA FROM DESKTOP TO DOCKER

if %COPY_DATA%==1 (
 echo Copying data from host to container...
 docker cp "%TEMP_DIR%\data_%APP_NAME%" %APP_NAME%:"/"
 rmdir /s "\data_%APP_NAME%"
) else (
 echo Not copying data.
)

@REM DELETE ALL UNUSED IMAGES
@REM docker image prune