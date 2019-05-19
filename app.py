import argparse
import os
from functools import reduce
from morse_txt import txt2morse, morse2txt
from morse_audio import morse2audio, audio2morse

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description='Conversor audio <-> morse <-> texto')
  parser.add_argument('filename', type=str, help='file .wav, .txt ou .morse')
  args = parser.parse_args()
  filename, file_extension = os.path.splitext(args.filename)

  if file_extension == '.wav':
    morse = audio2morse(args.filename)
    with open(f'{filename}.morse', 'w') as morse_file:
      morse_file.write(morse)
    txt = morse2txt(morse)
    with open(f'{filename}.txt', 'w') as txt_file:
      txt_file.write(txt)    

  elif file_extension == '.txt':
    with open(args.filename, 'r') as txt_file:
      txt = reduce((lambda x, y: x + y), txt_file.readlines())
      morse = txt2morse(txt)
      with open(f'{filename}.morse', 'w') as morse_file:
        morse_file.write(morse)
      morse2audio(morse, f'{filename}.wav')

  elif file_extension == '.morse':
    with open(args.filename, 'r') as morse_file:
      morse = reduce((lambda x, y: x + y), morse_file.readlines())
      txt = morse2txt(morse)
      with open(f'{filename}.txt', 'w') as txt_file:
        txt_file.write(txt)
      morse2audio(morse, f'{filename}.wav')

  else:
    print("Extensão inválida")
    