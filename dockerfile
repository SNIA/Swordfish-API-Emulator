FROM python:3-slim

# For healthcheck
RUN apt-get update && apk upgrade && \ 
	apk add --no-cache bash pip python git openssh curl 

RUN git clone https://github.com/DMTF/Redfish-Interface-Emulator

COPY Redfish-Interface-Emulator/requirements.txt /tmp/
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r /tmp/requirements.txt

RUN git clone https://github/SNIA/Swordfish-API-Emulator

cd Redfish-Interface-Emulator
rm -rf api_emulator/redfish/static
cp -r -f ../Swordfish_API_Emulator/api_emulator .
cp -r -f ../Swordfish_API_Emulator/Resources .
cp -r -f ../Swordfish_API_Emulator/emulator-config.json .
cp -r -f ../Swordfish_API_Emulator/emulator.py .

# Copy server files
COPY . /usr/src/app/.

# Env settings
EXPOSE 5000
HEALTHCHECK CMD curl --fail http://127.0.0.1:5000/redfish/v1/ || exit 1
WORKDIR /usr/src/app
ENTRYPOINT ["python", "emulator.py"]
