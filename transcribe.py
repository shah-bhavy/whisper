import whisper
model = whisper.load_model("base")
result = model.transcribe("Tut12 Audio.MP3", language="hi", task="transcribe")
print(result["text"])
