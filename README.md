## Videos to Docx converter
 - spilts Video in frame compares the frames if there equal there got ignored
 - audio convertet with whisper to text 
 - adds both chronological in the Docx File

```bash
pip3 install -r requirements.txt
sudo apt install ffmpeg
mkdir Videos # folder for the input videos
python3 Video_to_Docx_converter.py_audio.py
#convert viedeo
for i in *.m4v; do ffmpeg -i "$i" "${i%.*}.mp4"; done

```