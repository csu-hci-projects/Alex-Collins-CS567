#!/usr/bin/env python3

import csv 
import copy 
import datetime
from dateutil import parser

class Analysis: 
    
    def __init__(self):
        self.data = None
        self.bin_data = None
        self.l_1 = None
        self.l_2 = None

    def __check_answer(data, correct_answer):
        if data == correct_answer:
            return True
        return False 

    def __open_file(self, f_path):
        data = []
        with open(f_path, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                data.append(row)
        self.data = data

    def __check_answer(self, row_iter,  q_index, c_ans):
        if self.data[row_iter][q_index] == c_ans:
            self.bin_data[row_iter][q_index] = 1
        else:
            self.bin_data[row_iter][q_index] = 0

    def __analyse_question(self, row_iter): 
        self.__check_answer(row_iter, 4, 'Stereopsis')
        self.__check_answer(row_iter, 5, 'Stereoscope')
        self.__check_answer(row_iter, 6, 'Ivan Sutherland')
        self.__check_answer(row_iter, 7, 'Glove')
        self.__check_answer(row_iter, 8, 'Virtual Interface Environment Workstation')
        self.__check_answer(row_iter, 9, 'Yes')
        self.__check_answer(row_iter, 10, 'Palmer Luckey')
        self.__check_answer(row_iter, 11, 'Emory University')
        self.__check_answer(row_iter, 12, '1838')
        self.__check_answer(row_iter, 13, 'VPL Research')
    
    def __print_datasets(self):
        for row_iter in range(len(self.bin_data)):
            print (self.bin_data[row_iter])

        for row_iter in range(len(self.data)):
            print (self.data[row_iter])
    
    def __gender_analysis(self):
        m_cnt = 0
        m_cor = 0
        f_cnt = 0
        f_cor = 0

        m_o_cnt = 0
        m_t_cnt = 0
        f_o_cnt = 0
        f_t_cnt = 0

        m_o_cor = 0
        m_t_cor = 0
        f_o_cor = 0
        f_t_cor = 0

        for row in self.bin_data:
            if row[14] == 'Male':
                m_cor += (sum([ int(x) for x in row[4:14] ]))
                m_cnt += 1
                if row[16] == "one":
                    m_o_cnt +=1
                    m_o_cor += (sum([ int(x) for x in row[4:14] ]))
                elif  row[16] == "two":
                    m_t_cnt +=1
                    m_t_cor += (sum([ int(x) for x in row[4:14] ]))
            elif row[14] == 'Female':
                f_cor += (sum([ int(x) for x in row[4:14] ]))
                f_cnt += 1
                if row[16] == "one":
                    f_o_cnt +=1
                    f_o_cor += (sum([ int(x) for x in row[4:14] ]))
                elif  row[16] == "two":
                    f_t_cnt +=1
                    f_t_cor += (sum([ int(x) for x in row[4:14] ]))
        
        t_cnt = m_cnt + f_cnt

        print("Gender analysis:")
        print("  Number Male Tested: {0:.2f}".format(m_cnt))
        print("  Percent Male Tested: {0:.2f}".format((m_cnt*100/t_cnt)))
        print("  Number Male Tested Lecture One: {0:.2f}".format(m_o_cnt))
        print("  Number Male Correct Answers Lecture One: {0:.2f}".format(m_o_cor))
        print("  Percent Male Correct Answers Lecture One: {0:.2f}".format(m_o_cor*100/(m_o_cnt*10)))
        print("  Number Male Tested Lecture Two: {0:.2f}".format(m_t_cnt))
        print("  Number Male Correct Answers Lecture Two: {0:.2f}".format(m_t_cor))
        print("  Percent Male Correct Answers Lecture Two: {0:.2f}".format(m_t_cor*100/(m_t_cnt*10)))
        print("  Number Male Correct Answers: {0:.2f}".format(m_cor))
        print("  Percent Male Correct Answers: {0:.2f}".format((m_cor*100/(m_cnt * 10))))
        print()
        print("  Number Female Tested: {0:.2f}".format(f_cnt))
        print("  Percent Female Tested: {0:.2f}".format((f_cnt*100/t_cnt)))
        print("  Number Female Tested Lecture One: {0:.2f}".format(f_o_cnt))
        print("  Number Female Correct Answers Lecture One: {0:.2f}".format(f_o_cor))
        print("  Percent Female Correct Answers Lecture One: {0:.2f}".format(f_o_cor*100/(f_o_cnt*10)))
        print("  Number Female Tested Lecture Two: {0:.2f}".format(f_t_cnt))
        print("  Number Female Correct Answers Lecture Two: {0:.2f}".format(f_t_cor))
        print("  Percent Female Correct Answers Lecture Two: {0:.2f}".format(f_t_cor*100/(f_t_cnt*10)))
        print("  Number Female Correct Answers: {0:.2f}".format(f_cor))
        print("  Percent Female Correct Answers: {0:.2f}".format((f_cor*100/(f_cnt * 10))))
        print('\n')

    def __lecture_analysis(self):
        o_cor = 0
        t_cor = 0
        for row in self.bin_data:
            if row[16] == 'one':
                o_cor += (sum([ int(x) for x in row[4:14] ]))
            elif row[16] == 'two':
                t_cor += (sum([ int(x) for x in row[4:14] ]))
        
        print("Lecture analysis:")
        print("  Number One Correct Answers: {0:.2f}".format(o_cor))
        print("  Percent One Correct Answers: {0:.2f}".format(o_cor))
        print()
        print("  Number Two Correct Answers: {0:.2f}".format(t_cor))
        print("  Percent Two Correct Answers: {0:.2f}".format(t_cor))
        print('\n')
    
    def __get_question_index(self, q_text):
        for i in range(len(self.bin_data[0])):
            if self.bin_data[0][i].strip() == q_text:
                return i
        return None
    
    def __per_question_analysis(self,q_txt):
        q_idx = self.__get_question_index(q_txt)
        q_o_cor_count = 0
        q_t_cor_count = 0
        for row in self.bin_data:
            if row[16] == 'one':
                if row[q_idx] == 1:
                    q_o_cor_count+=1
            elif row[16] == 'two':
                if row[q_idx] == 1:
                    q_t_cor_count+=1

        return q_o_cor_count*100/10, q_t_cor_count*100/10

    def __question_analysis(self):
        print("Percent each student got correct answers across leactures(one,two):")
        print (*self.__per_question_analysis("In what year was the first stereoscope created?"))
        print (*self.__per_question_analysis("What is the process of tricking the mind to show depth by showing a different image to each eye?"))
        print (*self.__per_question_analysis("What is the view master?"))
        print (*self.__per_question_analysis("What was the name of the creator of The Sword of Damocles?"))
        print (*self.__per_question_analysis("What was the company founded in 1985 that specialized in VR products?"))
        print (*self.__per_question_analysis("What was the device that was paired with the EyePhone?"))
        print (*self.__per_question_analysis("What did NASA's VIEW acronym mean?"))
        print (*self.__per_question_analysis("What medical school partnered with Georgia Tech to use VR as a treatment for PTSD?"))
        print (*self.__per_question_analysis("Does Google Earth support VR?"))
        print (*self.__per_question_analysis("Who founded the company Oculus VR?"))
    

    def __age_analysis(self):
        o_ave_age = []
        t_ave_age = []
        all_ave_age = []
        for row in self.bin_data:
            if row[15] != 'What is your date of birth?':
                parsed_date = parser.parse(row[15])
                all_ave_age.append(parsed_date.date())
                if row[16] == 'one':
                    parsed_date = parser.parse(row[15])
                    o_ave_age.append(parsed_date.date())
                elif row[16] == 'two':
                    parsed_date = parser.parse(row[15])
                    t_ave_age.append(parsed_date.date())

        today = datetime.date.today()
        all_average_age = sum(map(lambda x: today-x, all_ave_age), datetime.timedelta(0))/len(all_ave_age)
        one_average_age = sum(map(lambda x: today-x, o_ave_age), datetime.timedelta(0))/len(o_ave_age)
        two_average_age = sum(map(lambda x: today-x, t_ave_age), datetime.timedelta(0))/len(t_ave_age)

        print()
        print("Age Analysis:")
        print("  Total average age: {0:.2f}".format(all_average_age.days/365.25))
        print("  Total one average age: {0:.2f}".format(one_average_age.days/365.25))
        print("  Total two average age: {0:.2f}".format(two_average_age.days/365.25))

    def analyse(self, file_path):
        self.__open_file("./res.csv")
        self.bin_data = copy.deepcopy(self.data)
        
        for row_iter in range(len(self.data)):
            if self.data[row_iter][0] != 'Timestamp':
                self.__analyse_question(row_iter)

        self.__gender_analysis()
        self.__lecture_analysis()
        self.__question_analysis()
        self.__age_analysis()

        # self.__print_datasets()

def main():
    
    a = Analysis()
    a.analyse('./res.csv')

if __name__== '__main__': 
    main()

    