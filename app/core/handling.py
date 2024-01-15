import pickle 


import nltk 
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')


# loading model
with open("./model/crf_model.pkl", "rb") as fp:
    crf_model = pickle.load(fp)


# function to extract feature from word
def word_to_features(sentence, i):
    word = sentence[i][0]
    features = {      
        # original word
        'word': word,
        'is_first': i == 0, 
        'is_last': i == len(sentence) - 1,  
        'is_capitalized': word[0].upper() == word[0],
        'is_all_caps': word.upper() == word,     
        'is_all_lower': word.lower() == word,      
        
        # prefix
        'prefix-1': word[0],   
        'prefix-2': word[:2],
        'prefix-3': word[:3],
        
        #suffix
        'suffix-1': word[-1],
        'suffix-2': word[-2:],
        'suffix-3': word[-3:],
        
        # previous word
        'prev_word': '' if i == 0 else sentence[i-1][0],

        # next word
        'next_word': '' if i == len(sentence)-1 else sentence[i+1][0],
        
        # special chars
        'has_hyphen': '-' in word,    
        'is_numeric': word.isdigit(),  
        'capitals_inside': word[1:].lower() != word[1:]       
    }
    return features


# function to extract feature from sentence
def sentence_to_features(sentence):
    return [word_to_features(sentence, i) for i in range(len(sentence))]


# function to get entities 
def get_entity(sentence):
    entities = {}

    tokens = sentence.split(" ")
    res = nltk.pos_tag(nltk.word_tokenize(sentence)) 
    x_sample = [sentence_to_features(res)] 
    y_sample = crf_model.predict(x_sample)[0] 
    
    for entity_ind in range(len(y_sample)):
        if(y_sample[entity_ind].upper() != 'O'):
            tag = y_sample[entity_ind].split('-')[1]
            entities[tokens[entity_ind]] = tag

    return entities 