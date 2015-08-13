# -*- coding: utf-8 -*-
'''
Created on 2015. 8. 13.
@attention: About Exception
@author: Sangyun
'''

'''
 발생 에러 종류 - 파이썬 내장에러 목록 
 FileNotFoundError - 파일을 찾지 못했을 때 발생 - (Python 2.7ver에서는 IOError 로 발생)
 ZeroDivisionError - 0으로 나누었을 때 발생 
 IndexError - 인덱싱을 잘못했을 때 발생 // List[0~4]까지 인덱싱 할 수 있을 때 List[5]를 해버리는 경우 
 NotImplementedError - 구현 되지 않았을 때 발생 // 상속관계에서 함수 오버라이드가 안되었을 때 
'''

def FileNotFound_Error():
    try :
        File = open ("뻬에에에에엨", 'r')
    
#     except종류 
#     except :                          # try블럭에서 에러발생시 실행됨 
#     except 발생에러 :                   # try블럭에서 [발생에러]발생시 실행됨 
#     except 발생에러 as 에러메세지 변수 :    # 위와 같은데 에러 메세지 변수가 딸려온다 
    except FileNotFoundError as ErrorMessage:
        print (ErrorMessage)            # [Errno 2] No such file or directory: '뻬에에에에엨'
        
    finally:        # finally블록은 try블록에서 에러가 발생하든말든 실행 된다 // except블록 다음에 실행된다 ㅇ 
        print ("End")   # 보통 사용한 리소스를 다시 클로즈 할 때 사용한다 
    
def ZeroDivision_Error():
    try : 
        A = 5
        B = 0
        C = A / B
        
    except ZeroDivisionError:
        print ("ZeroDivision")          # ZeroDivision
    
    # 중요 : if-else와 인터프리터가 햇갈릴 수도 있으므로, else블럭앞에 반드시 except블럭이 존재하여야한다    
    else :      # else블럭은 try블럭에서 에러가 발생하지 않았을 때 실행된다
        print ("C : " + str(C))
        print ("Success")                                               
    
def Except_Error():
    try :
        Raise_Error()
        
    except NotImplementedError:
        print("미구현된 함수가 실행되었습니다")
    
def Raise_Error():
    # raise로 에러를 발생시켰다 
    raise NotImplementedError    # 파이썬 내장에러 


def Main() : 
    FileNotFound_Error()
    ZeroDivision_Error()
    Except_Error()
    

if __name__ == "__main__" :
    Main()
    
    

    
    
