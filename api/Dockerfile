FROM python:3.10-alpine

WORKDIR /usr/src/app

COPY . .

RUN apk add --no-cache ffmpeg=~4.4.1-r2

RUN apk add --no-cache gst-libav=1.20.2-r0

RUN pip3 install pydantic==1.9.0 requests==2.27.1 fastapi==0.75.1 pymongo==4.1.0 uvicorn==0.17.6 pydub==0.25.1 pycountry==22.3.5

CMD ["python3", "-m", "uvicorn", "main:app", "--port", "8000", "--host", "0.0.0.0", "--proxy-headers"]
