## Videos to Docx data extractor
Uses Videos and spilts the frames in /Temp/data then it compares the frames to the next if equal to a degree it dont saves it. Next it uses the audio of the Video to put in whisper and extract the spoken text and adds botch chronological in the Docx File

```bash
pip install -r requirements.txt
sudo apt install ffmpeg
mkdir Videos # folder for the input videos
python extract_from_audio.py
```


- [x] Fixing time frame
