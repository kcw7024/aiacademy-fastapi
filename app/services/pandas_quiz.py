# from app.models.pandas_quiz import PandasQuiz
from dataclasses import replace
from icecream import ic
import pandas as pd
import random 
import string


class PandasQuiz(object):
    def __init__(self) -> None:
        pass
      
    '''
    Q1. 다음 결과 출력
       a  b  c
    1  1  3  5
    2  2  4  6
    ic| df1:       a  b  c
                1  1  3  5
                2  2  4  6  
    '''
    

    
    def quiz1(self) -> None:
        df = pd.DataFrame.from_dict(
            {'1':[ 1,  3,  5],'2':[ 2,  4,  6]},
            orient='index',
            columns=['a','b','c']
            )
        ic(df)
        
    '''
    A   B   C
    1   1   2   3
    2   4   5   6
    3   7   8   9
    4  10  11  12
    ic| df2:     A   B   C
                1   1   2   3
                2   4   5   6
                3   7   8   9
                4  10  11  12

    '''

        
    def quiz2(self) -> None:
        df2 = pd.DataFrame.from_dict(
            {'1':[1, 2, 3],'2':[4, 5, 6],'3':[7, 8, 9],'4':[10, 11, 12]},
            orient='index',
            columns=['A','B','C']
            )
        ic(df2)
    
        
    '''
    ic| df3:         0   1   2
                 0  95  25  74
                 1  44  24  97    
    '''
    
    
    
    def quiz3(self) -> None:
        num = random.sample(range(0,100), 6)
        
        df3 = pd.DataFrame.from_dict(
            {'0':[num[0], num[1],num[2]],
             '1':[num[3], num[4],num[5]],},
            orient='index',
            columns=['0','1','2']
        )
        ic(df3)
        
        
    '''
    Q4 국어, 영어, 수학, 사회 4과목을 시험치른 10명의 학생들의 성적표 작성. 
    단 점수 0 ~ 100이고 학생은 랜덤 알파벳 5자리 ID 로 표기
    ic| self.id(): 'HKKHc'
    ic| self.score(): 22
    ic| df4:        국어  영어  수학  사회
                    lDZid  57  90  55  24
                    Rnvtg  12  66  43  11
                    ljfJt  80  33  89  10
                    ZJaje  31  28  37  34
                    OnhcI  15  28  89  19
                    claDN  69  41  66  74
                    LYawb  65  16  13  20
                    QDBCw  44  32   8  29
                    PZOTP  94  78  79  96
                    GOJKU  62  17  75  49
            
    '''
                    
    def ran_id(self):
        ran_id = ''
        for i in range(5) :  #랜덤이름 대소문자 5글자
            ran_id += str(random.choice(string.ascii_letters)) #string으로 랜덤한문자뽑아냄 
        return ran_id
    
        
    def ran_score(self):
        return random.sample(range(0,100), 4)
               
                    
    def quiz4(self) :
        ic(self.ran_id())
        ic(self.ran_score())
        
        df4 = pd.DataFrame.from_dict({self.ran_id():self.ran_score()},
                                     orient='index', columns=['국어', '영어', '수학', '사회'])
        for i in range(9):
            df4 = pd.concat([df4,pd.DataFrame.from_dict({self.ran_id():self.ran_score()}, 
                                                        orient='index', columns=['국어', '영어', '수학', '사회'])],axis=0)
        ic(df4)

'''    
    def get_id(self)
    
    
    
'''