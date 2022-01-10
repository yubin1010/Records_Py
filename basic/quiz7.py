'''
당신으ㅣ 회사에서는 매주 1회 작성해야하는 보고서
보고서는 항상 아래와같은 형태로 출력

- X 주차 주간보고 - 
부서 : 
이름 : 
업무 요약 : 

1주차 부터 50주차까지의 보서 파일을 만드는 프로그램 작성
조건: 파일명은 '1주차.txt, '2주차.txt ...'''

#for i in range(1,51):
 #   with open(str(i)+"주차.txt", "w", encoding="utf-8") as bogo_file:
  #      bogo_file.write("- ",str(i)," 주차 주간 보고")
   #     bogo_file.write("부서 : 안녕")
    #    bogo_file.write("이름 : 김유빈")
     #   bogo_file.write("업무 요약 : 어쩌구 저쩌구")

for i in range(1,51):
    with open(str(i)+"주차.txt","w",encoding="utf-8") as report_file:
        report_file.write("- {0} 주차 주간 보고".format(i))
        report_file.write("\n부서 : 안녕")
        report_file.write("\n이름 : 김유빈")
        report_file.write("\n업무 요약 : 어쩌구 저쩌구")