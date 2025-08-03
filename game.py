valid_words = {}
participants_data = {}
def normalize_word(word: str) -> str :
   return "".join(word.split())

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

def add_participant(participant: str, answers: dict) :
    global participants_data
    participants_data[participant] = answers


def calculate_all() -> dict:
    if not participants_data:
        return {}

    # Initialize scores for all participants to zero.
    final_scores = {participant: 0 for participant in participants_data}
    
    # Get the list of categories from the loaded data.
    categories = valid_words.keys()

    for category in categories :
        category_answer = {}
        has_blank_answer = False
        for participant , participant_answer in participants_data.items() :
            answer = participant_answer.get(category,"").strip()
            normalize = normalize_word(answer)
            category_answer[participant] = normalize

            if not normalize :
                has_blank_answer = True
        
        if has_blank_answer:
            unique_points = 15
            duplicate_points = 10
        else:
            unique_points = 10
            duplicate_points = 5
        
        valid_answer_list = []

        for norms_ans in category_answer.values() :
            if norms_ans and norms_ans in valid_words.get(category,set()) :
                valid_answer_list.append(norms_ans)

        word_count = {}

        for word in valid_answer_list :
            word_count[word] = word_count.get(word,0) + 1
        
        for participant , normalized_answer in category_answer.items() :
            if normalized_answer in word_count :
                if word_count[normalized_answer] > 1 :
                    final_scores[participant] += duplicate_points
                else :
                    final_scores[participant] += unique_points
    
    return final_scores