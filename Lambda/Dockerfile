# Define global args
ARG FUNCTION_DIR="/slim-ds/"
ARG RUNTIME_VERSION="3.7"

############## Stage 1 ##############

# Start with a slim python image & use args
FROM python:${RUNTIME_VERSION}-slim AS python-slim-build
ARG FUNCTION_DIR
ARG RUNTIME_VERSION

# Create function directory
RUN mkdir -p ${FUNCTION_DIR}

# Copy app.py
COPY app/* ${FUNCTION_DIR}

# Prepare to install depenendencies
ADD https://automation.deepsecurity.trendmicro.com/sdk/20_0/v1/dsm-py-sdk.zip ${FUNCTION_DIR}sdk-temp/
RUN apt update && apt install -y unzip
RUN unzip ${FUNCTION_DIR}sdk-temp/dsm-py-sdk.zip -d ${FUNCTION_DIR}sdk-temp

# Install dependencies, including runtime interface client for Python
RUN python${RUNTIME_VERSION} -m pip install ${FUNCTION_DIR}sdk-temp/ --target ${FUNCTION_DIR}
RUN python${RUNTIME_VERSION} -m pip install boto3 --target ${FUNCTION_DIR}
RUN python${RUNTIME_VERSION} -m pip install awslambdaric --target ${FUNCTION_DIR}

# Minor cleanup
RUN rm -rf ${FUNCTION_DIR}sdk-temp/*


############## Stage 2 ##############
# Restart with a fresh slim python image & basic setup
FROM python:${RUNTIME_VERSION}-slim
ARG FUNCTION_DIR
WORKDIR ${FUNCTION_DIR}

# Copy everything from build image
COPY --from=python-slim-build ${FUNCTION_DIR} ${FUNCTION_DIR}

# Setup Runtime emulator (optional)
ADD https://github.com/aws/aws-lambda-runtime-interface-emulator/releases/latest/download/aws-lambda-rie /usr/bin/aws-lambda-rie
COPY entry.sh /
RUN chmod 755 /usr/bin/aws-lambda-rie /entry.sh

#Configure entrypoint and handler
ENTRYPOINT [ "/entry.sh" ]
CMD [ "app.lambda_handler" ]
