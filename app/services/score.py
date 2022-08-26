from app.models.score import Score

class ScoreService(object):
    def __init__(self) -> None:
        self.credit = 0 
        
    def set_socre(self, name, kor, eng, math):
        score = Score(name, kor, eng, math)
        score.set_avg()
        avg = score.get_avg()
       
        if avg >= 90 :
            self.credit = 'A'
        elif avg >= 80 :
            self.credit = 'B'
        elif avg >= 70 :
            self.credit = 'C'
        elif avg >= 60 :
            self.credit = 'D'
        elif avg >= 50 :
            self.credit = 'E'
        else : 
            self.credit = 'F'
    
    def get_score(self, name, kor, eng, math):
        self.set_socre(name, kor, eng, math) 
        return self.credit    