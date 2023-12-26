import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import string

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
class YesNoAI:
    def __init__(self):
        self.knowledge_base = {}

    def process_question(self, question):
        transformed_question = self.transform_question(question)
        for stored_question, answer in self.knowledge_base.items():
            stored_transformed_question = self.transform_question(stored_question)
            if transformed_question == stored_transformed_question:
                return answer
        return "Я не знаю."

    def remember_question(self, question, answer):
        self.knowledge_base[question] = answer

    def transform_question(self, question):
       
        question_lower = question.lower()
       
        tokens = word_tokenize(question_lower)
       
        table = str.maketrans('', '', string.punctuation)
        stripped = [w.translate(table) for w in tokens]
      
        stop_words = set(stopwords.words('russian'))
        words = [w for w in stripped if not w in stop_words]
       
        lemmatizer = WordNetLemmatizer()
        lemmatized_words = [lemmatizer.lemmatize(w) for w in words]
        return set(lemmatized_words)

def main():
    ai = YesNoAI()
    while True:
        question = input("Ваш вопрос: ")
        if question.lower() == "выход":
            break
        else:
            answer = ai.process_question(question)
            if answer != "Я не знаю.":
                print(answer)
            else:
                remember = input("Я не знаю ответа на этот вопрос. Пожалуйста, введите ответ (да или нет): ")
                ai.remember_question(question, remember.lower())

if __name__ == "__main__":
    main()
