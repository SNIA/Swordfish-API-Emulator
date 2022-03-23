FROM python:3-slim

# For healthcheck
RUN apt-get update && apt-get install bash pip python git curl -y

RUN git clone https://github.com/DMTF/Redfish-Interface-Emulator && git clone https://github.com/SNIA/Swordfish-API-Emulator

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r Redfish-Interface-Emulator/requirements.txt

RUN /bin/bash -c 'rm -rf Redfish-Interface-Emulator/api_emulator/redfish/static'

RUN /bin/bash -c 'cp -r -f Swordfish-API-Emulator/api_emulator Redfish-Interface_Emulator/'
RUN /bin/bash -c 'cp -r -f Swordfish-API-Emulator/Resources Redfish-Interface_Emulator/'
RUN /bin/bash -c 'cp -r -f Swordfish-API-Emulator/emulator-config.json Redfish-Interface_Emulator/'
RUN /bin/bash -c 'cp -r -f Swordfish-API-Emulator/emulator.py Redfish-Interface_Emulator/'

# Copy server files
COPY . /usr/src/app/.

# Env settings
EXPOSE 5000
HEALTHCHECK CMD curl --fail http://127.0.0.1:5000/redfish/v1/ || exit 1
WORKDIR /usr/src/app
ENTRYPOINT ["python", "emulator.py"]
