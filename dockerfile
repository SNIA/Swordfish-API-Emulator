FROM ubuntu:latest AS SetupFiles

# For healthcheck
RUN apt-get update && apt-get install bash git openssl -y

RUN git clone https://github.com/DMTF/Redfish-Interface-Emulator && git clone https://github.com/SNIA/Swordfish-API-Emulator

RUN /bin/bash -c 'rm -rf Redfish-Interface-Emulator/api_emulator/redfish/static'
RUN /bin/bash -c 'rm -rf Redfish-Interface-Emulator/api_emulator/redfish/templates'
RUN /bin/bash -c 'rm -rf Redfish-Interface-Emulator/api_emulator/redfish/*.py'

RUN /bin/bash -c 'cp -r -f Swordfish-API-Emulator/api_emulator Redfish-Interface-Emulator/'
RUN /bin/bash -c 'cp -r -f Swordfish-API-Emulator/Resources Redfish-Interface-Emulator/'
RUN /bin/bash -c 'cp -r -f Swordfish-API-Emulator/emulator-config.json Redfish-Interface-Emulator/'
RUN /bin/bash -c 'cp -r -f Swordfish-API-Emulator/emulator.py Redfish-Interface-Emulator/'
RUN /bin/bash -c 'cp -r -f Swordfish-API-Emulator/g.py Redfish-Interface-Emulator/'
RUN /bin/bash -c 'cp -r -f Swordfish-API-Emulator/certificate_config.cnf Redfish-Interface-Emulator/'
RUN /bin/bash -c 'cp -r -f Swordfish-API-Emulator/v3.ext Redfish-Interface-Emulator/'
RUN /bin/bash -c 'cp -r -f Swordfish-API-Emulator/requirements.txt Redfish-Interface-Emulator/'

RUN /bin/bash -c 'openssl genrsa -out Redfish-Interface-Emulator/server.key 2048'

RUN /bin/bash -c 'openssl rsa -in Redfish-Interface-Emulator/server.key -pubout -out Redfish-Interface-Emulator/server_public.key'

RUN /bin/bash -c 'openssl req -new -key Redfish-Interface-Emulator/server.key -out Redfish-Interface-Emulator/server.csr -config Redfish-Interface-Emulator/certificate_config.cnf'

RUN /bin/bash -c 'openssl x509 -in Redfish-Interface-Emulator/server.csr -out Redfish-Interface-Emulator/server.crt -req -signkey Redfish-Interface-Emulator/server.key -days 365 -extfile Redfish-Interface-Emulator/v3.ext'

FROM python:3-slim

# For healthcheck
RUN apt-get update && apt-get install curl -y

# Copy server files
COPY --from=SetupFiles /Redfish-Interface-Emulator /usr/src/app/.

# Install python requirements
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r /usr/src/app/requirements.txt

# Env settings
EXPOSE 5000
HEALTHCHECK CMD curl --fail http://127.0.0.1:5000/redfish/v1/ || exit 1
WORKDIR /usr/src/app
ENTRYPOINT ["python", "emulator.py"]
