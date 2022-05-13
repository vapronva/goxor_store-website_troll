from pathlib import Path
import requests
from enum import Enum


class APIEndpoints(Enum):
    Text2Speech: str = "https://tts.api.cloud.yandex.net/speech/v1/tts:synthesize"
    IAM: str = "https://iam.api.cloud.yandex.net/iam/v1/tokens"


class YandexTTS:
    __voicesList = [
        {"name": "oksana", "language": "ru-RU", "gender": "female"},
        {"name": "jane", "language": "ru-RU", "gender": "female"},
        {"name": "omazh", "language": "ru-RU", "gender": "female"},
        {"name": "zahar", "language": "ru-RU", "gender": "male"},
        {"name": "ermil", "language": "ru-RU", "gender": "male"},
        {"name": "silaerkan", "language": "tr-TR", "gender": "female"},
        {"name": "erkanyavas", "language": "tr-TR", "gender": "male"},
        {"name": "alyss", "language": "en-US", "gender": "female"},
        {"name": "nick", "language": "en-US", "gender": "male"},
        {"name": "alena", "language": "ru-RU", "gender": "female"},
        {"name": "filipp", "language": "ru-RU", "gender": "male"}]

    def __init__(
            self, voice: str, speed: float, audioFormat: str, sampleRateHertz: int,
            folderId: str, maxCharachters: int = 5000) -> None:
        self._maxCharachters = maxCharachters
        """
        Initialize the YandexTTS class.

        Args:
            voice: Speaker string (standard: oksana/jane/omazh/zahar/ermil/silaerkan/erkanyavas/alyss/nick; premium: alena/filipp);
            speed: Speech tempo (from 0.1 to 3.0);
            format: Format of the synthesized audio;
            sampleRateHertz: Sampling rate of the synthesized audio (used if format==lpcm);
            folderId: Identifier of the folder in YandexCloud.
        """
        if voice not in map(lambda d: d["name"], self.__voicesList):
            raise TypeError(
                "Invalid speaker: no such a speaker was found in a list.")
        self._params = {
            "lang": next( # skipcq: PTC-W0063
                item for item in self.__voicesList if item["name"] == voice)["language"],
            "voice": voice,
            "speed": speed,
            "format": audioFormat,
            "sampleRateHertz": sampleRateHertz,
            "folderId": folderId}
        self.__data = None

    def IAMGen(self, ycAPIKey: str) -> None:
        """
        Generate an IAM token.

        Args:
            ycAPIKey (str): YandexCloud API key.
        """
        self._IAMToken = ycAPIKey

    def generate(self, text: str) -> None:
        """
        Generate an audio file.

        Args:
            text (str): Text to synthesize.
        """
        if len(text) >= self._maxCharachters:
            raise ValueError(
                f"Too many charchters: number of characters must be less than {self._maxCharachters}")
        params = self._params.copy()
        params["text"] = text
        self.__data = requests.post(
            APIEndpoints.Text2Speech.value,
            headers={
                "Authorization": f"Api-Key {self._IAMToken}"},
            data=params,
            stream=True).iter_content()

    def writeData(self, path: Path) -> None: # skipcq: PTC-W6004
        with open(path, "wb") as f:
            for data in self.__data:
                f.write(data)

    def getData(self) -> bytes:
        bytes_data = b""
        for data in self.__data:
            bytes_data += data
        return bytes_data
