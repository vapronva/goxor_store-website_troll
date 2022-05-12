from SpeechKit import YandexTTS
from IPInfoAPI import IPInfoAPI
from ipaddress import IPv4Address, AddressValueError
from pathlib import Path
import os
import pydub
import fastapi
from fastapi.responses import StreamingResponse
import io


app = fastapi.FastAPI(
    title="goxor.store API",
    version="0.1.0",
    docs_url="/docs",
    debug=True,
    redoc_format="json",
    redoc_config={
        "title": "goxor.store API"})

__ipinfo = IPInfoAPI(os.environ["IPINFO_TOKEN"])

__ttsMale = YandexTTS(
    voice="nick",
    speed=1.0,
    format="oggopus",
    sampleRateHertz=48000,
    folderId=os.environ["YANDEXCLOUD_FOLDERID"])
__ttsFemale = YandexTTS(
    voice="alyss",
    speed=1.0,
    format="oggopus",
    sampleRateHertz=48000,
    folderId=os.environ["YANDEXCLOUD_FOLDERID"])
__ttsMale.IAMGen(os.environ["YANDEXCLOUD_APITOKEN"])
__ttsFemale.IAMGen(os.environ["YANDEXCLOUD_APITOKEN"])


@app.get("/")
def main_root():
    return {"action": "GET_ROOT_URL", "result": {
        "message": "Welcome to goxor.store API! :)"}, "error": None}


@app.get("/leaks/zenith_v11.mp3")
def leaks_zenithv11(request: fastapi.Request):
    try:
        try:
            userIP = IPv4Address(request.headers["x-vprw-internal-realip"])
            print(request.headers["x-vprw-internal-realip"])
            print(f"Found IP {userIP} using x-vprw-internal-realip")
        except AddressValueError:
            try:
                userIP = IPv4Address(request.headers["X-Forwarded-For"])
                print(request.headers["X-Forwarded-For"])
                print(f"Found IP {userIP} using X-Forwarded-For")
            except AddressValueError:
                userIP = IPv4Address(request.client.host)
                print(request.client.host)
                print(f"Found IP {userIP} using client.host")
        filenames = {
            0: Path("music/geoxor-zenith-cutted-reverb.mp3"),
            1: Path(f"user-audios/parts/audio-user-{userIP.__str__().split('.')[0]}_{userIP.__str__().split('.')[1]}_{userIP.__str__().split('.')[2]}_{userIP.__str__().split('.')[3]}-part_1.ogg"),
            2: Path(f"user-audios/parts/audio-user-{userIP.__str__().split('.')[0]}_{userIP.__str__().split('.')[1]}_{userIP.__str__().split('.')[2]}_{userIP.__str__().split('.')[3]}-part_2.ogg"),
            3: Path("music/assets/audio-user-part_3.ogg"),
            4: Path(f"user-audios/parts/audio-user-{userIP.__str__().split('.')[0]}_{userIP.__str__().split('.')[1]}_{userIP.__str__().split('.')[2]}_{userIP.__str__().split('.')[3]}-part_4.ogg"),
            5: Path("music/assets/audio-user-part_5.ogg"),
            6: Path("music/rickroll-with-memes.mp3"),
            "final": Path(f"user-audios/{userIP.__str__().split('.')[0]}_{userIP.__str__().split('.')[1]}_{userIP.__str__().split('.')[2]}_{userIP.__str__().split('.')[3]}.mp3")}
        if not filenames["final"].exists():
            ipinfoInfomation = __ipinfo.getInfo(userIP)
            usPartOne = f"ha-ha! get trolled: you live in {ipinfoInfomation.city}"
            usPartTwo = f"(which is a nice city in {ipinfoInfomation.country}, by the way)."
            usPartThree = "your ip-address got leaked! it's pronounced like this, just so you know:"
            usPartFour = f"{userIP.__str__().split('.')[0]} point {userIP.__str__().split('.')[1]} point {userIP.__str__().split('.')[2]} point {userIP.__str__().split('.')[3]}."
            usPartFive = f"and that's all for now, folks."
            if not filenames[1].exists():
                __ttsFemale.generate(usPartOne)
                __ttsFemale.writeData(filenames.get(1))
            if not filenames[2].exists():
                __ttsMale.generate(usPartTwo)
                __ttsMale.writeData(filenames.get(2))
            if not filenames[4].exists():
                __ttsMale.generate(usPartFour)
                __ttsMale.writeData(filenames.get(4))
            audioPartZero = pydub.AudioSegment.from_file(filenames.get(0))
            audioPartOne = pydub.AudioSegment.from_file(filenames.get(1))
            audioPartTwo = pydub.AudioSegment.from_file(filenames.get(2))
            audioPartThree = pydub.AudioSegment.from_file(filenames.get(3))
            audioPartFour = pydub.AudioSegment.from_file(filenames.get(4))
            audioPartFive = pydub.AudioSegment.from_file(filenames.get(5))
            audioPartSix = pydub.AudioSegment.from_file(filenames.get(6))
            allSpokenParts = audioPartOne + audioPartTwo
            outputAudio = audioPartZero.overlay(allSpokenParts, position=4750)
            outputAudio += audioPartThree + audioPartFour + audioPartFive + audioPartSix
            outputAudio.set_frame_rate(48000)
            outputAudio.export(
                f"user-audios/{userIP.__str__().split('.')[0]}_{userIP.__str__().split('.')[1]}_{userIP.__str__().split('.')[2]}_{userIP.__str__().split('.')[3]}.mp3",
                format="mp3",
                bitrate="192k",
                tags={
                    "artist": "Geoxor",
                    "title": "Zenith (v11) [LEAK]",
                    "album": f"haha, your ip is {userIP.__str__()}!"})
        stream = io.BytesIO()
        stream.write(open(filenames.get("final"), "rb").read())
        response = StreamingResponse(
            iter([stream.getvalue()]),
            media_type="audio/mpeg")
        return response
    except Exception as e:
        print(e)
        stream = io.BytesIO()
        stream.write(open("music/rickroll-with-memes.mp3", "rb").read())
        response = StreamingResponse(
            iter([stream.getvalue()]),
            media_type="audio/mpeg")
        return response
