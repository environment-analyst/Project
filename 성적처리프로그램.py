#!/usr/bin/env python
# coding: utf-8

# In[1]:



import copy

a_name = ["Students","Name","Miderm","Final","Average","Grade"]



# 전체 학생 정보 출력
def show_function(a):
    a.sort(key = lambda e : e[4],reverse = True)
    a_name = ["Students","Name","Miderm","Final","Average","Grade"]
    print(f"{a_name[0]:<15} {a_name[1]:>15} {a_name[2]:^8} {a_name[3]:^8} {a_name[4]:^8} {a_name[5]:^8}")
    print("-"*60)
    for l,n,m,o,p,q in a: # a[i][0]-> 형태로 출력인 안되서 언팩킹함
        print(f"{l:<15} {n:>15} {m:^8} {o:^8} {p:^8.1f} {q:^8}")
        
    
# 특정 학생 검색
def search_function():
    a = input("Student ID:")
    for i in range(len(stu_list)):
        if a in stu_list[i][0]:
            print(f"{a_name[0]:<15} {a_name[1]:>15} {a_name[2]:^8} {a_name[3]:^8} {a_name[4]:^8} {a_name[5]:^8}")
            print("-"*60)
            print(f"{stu_list[i][0]:<15} {stu_list[i][1]:>15} {stu_list[i][2]:^8} {stu_list[i][3]:^8} {stu_list[i][4]:^8} {stu_list[i][5]:^8}")
            return
    print("NO SUCH PERSON")



# In[2]:



# 점수 수정
def changescore_function():
    name_list = []
    for i in range(len(stu_list)):
        name_list.append(stu_list[i][0])

    a = input("Student ID:")

    if a not in name_list:
        print("NO SUCH PERSON")

    k=0
    for i in range(len(stu_list)):
        if a in stu_list[i][0]:
            b = input("Mid/Final?")
            if b == "mid":
                score = int(input("Input new score:"))
                if  score>= 0 and score <= 100:
                    ex_score = copy.copy(stu_list[i][2])
                    stu_list[i][2] = score
                    avg = (stu_list[i][2]+stu_list[i][3])/2
                    if avg >= 90:
                        grade = "A"
                    elif avg >=80:
                        grade = "B"
                    elif avg>=70:
                        grade = "C"
                    elif avg>=60:
                        grade = "D"
                    else:
                        grade = "F"
                    ex_avg = copy.copy(stu_list[i][4])
                    ex_grade = copy.copy(stu_list[i][5])
                    stu_list[i][4] = avg
                    stu_list[i][5] = grade
                    # stu_list를 변화시킨 다는 것에 유의한다.
                    #변화시키고자 하는 값이 무엇인지, 변화시킨 값을 넣었는지 확인한다.
                    print(f"{a_name[0]:<15} {a_name[1]:>15} {a_name[2]:^8} {a_name[3]:^8} {a_name[4]:^8} {a_name[5]:^8}")
                    print("-"*60)
                    print(f"{stu_list[i][0]:<15} {stu_list[i][1]:>15} {ex_score:^8} {stu_list[i][3]:^8} {ex_avg:^8} {ex_grade:^8}")
                    print("Score changed.")
                    print(f"{stu_list[i][0]:<15} {stu_list[i][1]:>15} {stu_list[i][2]:^8} {stu_list[i][3]:^8} {stu_list[i][4]:^8} {stu_list[i][5]:^8}")
                    return


            elif b == "final":
                score = int(input("Input new score:"))
                if  score>= 0 and score <= 100:
                    ex_score = copy.copy(stu_list[i][3])
                    stu_list[i][3] = score
                    avg = (stu_list[i][2]+stu_list[i][3])/2
                    if avg >= 90:
                        grade = "A"
                    elif avg >=80:
                        grade = "B"
                    elif avg>=70:
                        grade = "C"
                    elif avg>=60:
                        grade = "D"
                    else:
                        grade = "F"
                    ex_avg = copy.copy(stu_list[i][4])
                    ex_grade = copy.copy(stu_list[i][5])
                    stu_list[i][4] = avg
                    stu_list[i][5] = grade
                    print(f"{a_name[0]:<15} {a_name[1]:>15} {a_name[2]:^8} {a_name[3]:^8} {a_name[4]:^8} {a_name[5]:^8}")
                    print("-"*60)
                    print(f"{stu_list[i][0]:<15} {stu_list[i][1]:>15} {stu_list[i][2]:^8} {ex_score:^8} {ex_avg:^8} {ex_grade:^8}")
                    print("Score changed.")
                    print(f"{stu_list[i][0]:<15} {stu_list[i][1]:>15} {stu_list[i][2]:^8} {stu_list[i][3]:^8} {stu_list[i][4]:^8} {stu_list[i][5]:^8}")
                    return


    


# In[3]:




# 학생 추가
def add_function():
    a = input("Student ID:")
    name_list=list()
    
    for i in range(len(stu_list)):
        name_list.append(stu_list[i][0])
    
    if a in name_list:
        print("ALREADY EXITS")
    else:
        b = []
        b.append(a)
        b.append(input('Name:'))
        b_m = int(input('Midterm Score:'))
        b_f = int(input('Final Score:'))
        b.append(b_m)
        b.append(b_f)
        b_a = (b_m + b_f)/2
        if b_a>=0 and b_a<=100:
            b.append(b_a)

        if b_a >= 90:
            b.append("A")
        elif b_a >=80:
            b.append("B")
        elif b_a>=70:
            b.append("C")
        elif b_a>=60:
            b.append("D")
        else:
            b.append("F")

        stu_list.append(b)        
        print("Student added.")




# In[4]:


# grade 검색
def searchgrade_function():
    a = input("Grade to Search:")
    k = 0
    if a not in ['A','B','C','D','F']:
        pass
    else:         
        for i in range(len(stu_list)):
            if a in stu_list[i][5]:
                print(f"{stu_list[i][0]:<15} {stu_list[i][1]:>15} {stu_list[i][2]:^8} {stu_list[i][3]:^8} {stu_list[i][4]:^8} {stu_list[i][5]:^8}")
            else:
                k += 1
                if k == len(stu_list):
                    print("NO RESULTS")


# In[6]:


# 특정 학생 삭제
def remove_function():
    


    name_list=list()
    
    for i in range(len(stu_list)):
        name_list.append(stu_list[i][0])

    k = 0
    if name_list == []:
        print("List is empty")
    else:
        a = input("Student ID:")
        if a not in name_list:
            print("NO SUCH PERSON")
        else:
            i=name_list.index(a)
            del stu_list[i]
            print("Student removed.")



# In[7]:


# 종료
def quit_function():
    a = input("Save data?[yes/no]")
    if a == "yes":
        b=input("File name:")
        fw = open(b,"w")
        stu_list.sort(key = lambda e : e[4],reverse = True)
        for j in range(len(stu_list)):
            for k in range(len(stu_list[j])):
                stu_list[j][k] = str(stu_list[j][k])
        for i in stu_list:
            a = "\t".join(i)
            fw.write(a+'\n')
            
        fw.close()
        
            
                
    


# In[8]:



fname = input("파일명의 입력:")

if fname == "":
    fname = "students.txt"

fr = open(fname,"r")
fr_c = fr.readlines()
fr.close()


# In[9]:


score = []
stu_list = []
# stu_list.append(["Student", "Name", "Midterm", "Final", "Average", "Grade"])


for l in fr_c:
    l = l.strip()
    score = l.split("\t")
    score[2] = int(score[2])
    score[3] = int(score[3])
#     print(score[2],score[3])
    avg = (int(score[2])+int(score[3]))/2
#     print(avg)
#     print(type(score[3]))
    score.append(avg)
    
    if avg >= 90:
        score.append("A")
    elif avg >=80:
        score.append("B")
    elif avg>=70:
        score.append("C")
    elif avg>=60:
        score.append("D")
    else:
        score.append("F")

    stu_list.append(score)



# In[ ]:


while True:
    command = input("#" )
    command.lower()
    
    if command.lower() == "show":
        show_function(stu_list)
        print()
        
    elif command.lower() =="search":
        command.lower()
        search_function()
        print()
        
    elif command.lower() == "changescore":
        
        changescore_function()
        print()
        
    elif command.lower() == 'grade':
        searchgrade_function()
        print()
        
    elif command.lower() == "add":
        add_function()
        print()
    elif command.lower() == "searchgrade":
        searchgrade_function()
        print()
    
    elif command.lower() == "remove":
        remove_function()
        print()
        
    elif command.lower() == "quit":
        quit_function()
        break
    else:
        print("wrong input!")


# In[ ]:




