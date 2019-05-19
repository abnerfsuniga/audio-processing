ALPHA_MORSE_DICT = {
  'A':'10111', 'B':'111010101', 
  'C':'111011101', 'D':'1110101', 'E':'1', 
  'F':'101011101', 'G':'111011101', 'H':'1010101', 
  'I':'101', 'J':'1011101110111', 'K':'111010111', 
  'L':'101110101', 'M':'1110111', 'N':'11101', 
  'O':'11101110111', 'P':'10111011101', 'Q':'1110111010111', 
  'R':'1011101', 'S':'10101', 'T':'111', 
  'U':'1010111', 'V':'101010111', 'W':'101110111', 
  'X':'11101010111', 'Y':'1110101110111', 'Z':'11101110101', 
  '1':'10111011101110111', '2':'101011101110111', '3':'1010101110111', 
  '4':'10101010111', '5':'101010101', '6':'11101010101', 
  '7':'1110111010101', '8':'111011101110101', '9':'11101110111011101', 
  '0':'1110111011101110111'
} 

MORSE_ALPHA_DICT = {v: k for k, v in ALPHA_MORSE_DICT.items()}

def txt2morse(string):
  string = string.upper()
  words = string.split()
  morsewords = []
  for word in words:
    morseletters = [ALPHA_MORSE_DICT[letter] for letter in word]
    morseword = '000'.join(morseletters)
    morsewords.append(morseword)
  return '0000000'.join(morsewords)

def morse2txt(morse):
  morsewords = morse.split('0000000')
  words = []
  for morseword in morsewords:
    letters = [MORSE_ALPHA_DICT[morseletter] for morseletter in morseword.split('000')]
    word = ''.join(letters)
    words.append(word)
  return ' '.join(words)
