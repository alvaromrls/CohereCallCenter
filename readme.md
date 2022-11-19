# Cohere Hackaton: Call Center

This the source code repository for cohere Hackaton. This solution detect voice and take a decision based on it.

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
