class Word:
    def __init__(self, newword, str1, str2, answer) :
        self.newword = newword
        self.str1 = str1
        self.str2 = str2
        self.answer = answer
    
    def show_question(self):
        print(f"\"{self.newword}\"의 뜻은?" )
        print("1. " + self.str1)
        print("2. " + self.str2)
    
    def check_answer(self, user_input):
        if user_input == self.answer:
            print("정답입니다")
        else:
            print("틀렸습니다")

word = Word("얼죽아", "얼어 죽어도 아메리카노", "얼굴만은 죽어도 아기피부", 1)
word.show_question()
word.check_answer(int(input("=> ")))