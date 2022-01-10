#import pickle

#file을 열어서 profile_file에 저장 -> 자동으로 종료
#with open("profile.pickle","rb") as profile_file:
 #   print(pickle.load(profile_file))

#with open("study.txt","w",encoding="utf-8") as study_file:
 #   study_file.write("파이썬을 열심이 공부하고 있어요")

with open("study.txt", "r", encoding="utf-8") as study_file:
    print(study_file.read())