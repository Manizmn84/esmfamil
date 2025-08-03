valid_words = {}

def normalize_word(word: str) -> str :
   return "".split(word.split())

def ready_up():
    global valid_words

    try:
        with open("esm_famil_data.csv","r",encoding="utf-8") as f :
            header = f.readline().strip().split(",")

            for category in header :
                valid_words[category] = set()
            
            for line in f :
                parts = line.strip().split(",")

                for i, word in enumerate(parts):
                    category = header[i]
                    normalize = normalize_word(word)
                    if normalize:
                        valid_words[category].add(normalize)
    except:
      print('Error: esm_famil_data.csv not found.')