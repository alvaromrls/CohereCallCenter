# Cohere Hackaton: Call Center

## Introduction

This the source code repository for cohere Hackaton. This solution detect voice and take a decision based on it.
It's divided in 3 parts:

- Server: Storages the labeled data and fails from the clasification (logs). Implemented with Flask (Python) and saves into a JSON file.
- User: With a command line interface, you can start "a conversation", detects a voice a dispatch an action.
- Admin: With a command line interface, you can manage logs from the server (deleting or labaling it).

## Server API

- **/metadata** [GET] get all the labeled data
- **/logs** [GET] get all logs [POST] create a new log (data={log:"new log"})
- **/admin/{ID}** [DEL] delete the log with in the ID position [PATCH] assign a log to a correspondant category (data={category:"category"})

## Instation

- Set up the python libraries

> python3 -m venv myenv
>
> .\myenv\Scripts\Activate.ps1
>
> pip install -r requirements.txt

- To install whisper:

> pip install git+https://github.com/openai/whisper.git

- To install ffmpeg (in a windows computer):
  https://phoenixnap.com/kb/ffmpeg-windows

- Create a .env file in src/cli with the API key from codere

## Execution

Be sure you are using the python environment!

1. Server: in a terminal

   > cd src
   >
   > python server/app.py

2. User: in a terminal

   > cd src
   >
   > python cli/user

3. Admin: in a terminal
   > cd src
   >
   > python cli/admin

## References

- Pyaudio reference:
  https://people.csail.mit.edu/hubert/pyaudio/docs/

- Whisper:
  https://github.com/openai/whisper
