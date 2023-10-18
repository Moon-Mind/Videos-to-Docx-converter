## Videos to Docx data extractor
Uses Videos and spilts the frames in /Temp/data then it compares the frames to the next if equal to a degree it dont saves it. Next it uses the audio of the Video to put in whisper and extract the spoken text and adds botch chronological in the Docx File

```bash
pip install -r requirements.txt
python extract_from_audio.py test.mp4
```


- [x] Fixing time frame
