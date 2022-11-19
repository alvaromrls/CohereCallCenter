import requests
import whisper
import cohere
import json
from cohere.classify import Example

newConversation = """Press:
- S to start a new conversation
- L to reload data from server
- Any other key to skip
 """


class client:
    def __init__(self):
        self.filename = "temporal.wav"
        self.transcription = ""
        f = open("user/config.json")
        config = json.load(f)
        key = config["cohereKey"]
        self.co = cohere.Client(key)
        self.load_data()
        print("A new client has started")

    def load_data(self):
        self.data = requests.get("http://localhost:5000/metadata").json()
        self.set_examples()

    def set_examples(self):
        self.examples = []
        for key in self.data:
            for value in self.data[key]:
                self.examples.append(Example(value, key))

    def conversate(self):
        print(self.transcription)

    def record_audio(self, time):
        import pyaudio
        import wave

        chunk = 1024  # Record in chunks of 1024 samples
        sample_format = pyaudio.paInt16  # 16 bits per sample
        channels = 1
        fs = 44100  # Record at 44100 samples per second
        seconds = time

        p = pyaudio.PyAudio()  # Create an interface to PortAudio

        print(f"Recording for {time} seconds")

        stream = p.open(
            format=sample_format,
            channels=channels,
            rate=fs,
            frames_per_buffer=chunk,
            input=True,
        )

        frames = []  # Initialize array to store frames

        # Store data in chunks for 3 seconds
        for i in range(0, int(fs / chunk * seconds)):
            data = stream.read(chunk)
            frames.append(data)

        # Stop and close the stream
        stream.stop_stream()
        stream.close()
        # Terminate the PortAudio interface
        p.terminate()

        print("Finished recording")
        wf = wave.open(self.filename, "wb")
        wf.setnchannels(channels)
        wf.setsampwidth(p.get_sample_size(sample_format))
        wf.setframerate(fs)
        wf.writeframes(b"".join(frames))
        wf.close()

    def transcript(self):
        model = whisper.load_model("base.en")
        result = model.transcribe(self.filename)
        self.transcription = result["text"]

    def call_cohere(self):
        response = self.co.classify(
            inputs=[self.transcription],
            examples=self.examples,
        )
        print(response)

    def loop(self):
        while True:
            k = input(newConversation)
            if k.strip() in ["S", "s"]:
                self.record_audio(5)
                self.transcript()
                self.conversate()
                self.call_cohere()
            elif k.strip() in ["L", "l"]:
                self.load_data()
                print("Data loaded!")
            else:
                print("Good bye!")
                break
