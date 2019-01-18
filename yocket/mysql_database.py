import mysql.connector
from mysql.connector import Error
import xlsxwriter
def insert_profile(term,gre_date,work_experience_months,ug_score,ug_score_pattern,en_exam_pattern,en_exam_score,
                   gre_score,status,course_name,university_name,gre_verbal_score,gre_quant_score,
                   gre_awa_score,en_exam_writing_score,en_exam_listening_score,
                   en_exam_reading_score,en_exam_speaking_score,nickname):
    term = str(term)
    gre_date = str(gre_date)
    work_experience_months = float(work_experience_months)
    ug_score = float(ug_score)
    ug_score_pattern = str(ug_score_pattern)
    en_exam_pattern = str(en_exam_pattern)
    en_exam_score = float(en_exam_score)
    gre_score = int(gre_score)
    status = str(status)
    course_name = str(course_name)
    university_name = str(university_name)
    gre_verbal_score = int(gre_verbal_score)
    gre_quant_score = int(gre_quant_score)
    gre_awa_score = float(gre_awa_score)
    en_exam_writing_score = int(en_exam_writing_score)
    en_exam_listening_score = int(en_exam_listening_score)
    en_exam_reading_score = int(en_exam_reading_score)
    en_exam_speaking_score = int(en_exam_speaking_score)
    nickname = str(nickname)
    emp_data= dict(term=term, gre_date=gre_date, work_experience_months=work_experience_months, ug_score=ug_score,
                   ug_score_pattern=ug_score_pattern, en_exam_pattern=en_exam_pattern, en_exam_score=en_exam_score,
                   gre_score=gre_score, status=status, course_name=course_name, university_name=university_name,
                   gre_verbal_score=gre_verbal_score, gre_quant_score=gre_quant_score, gre_awa_score=gre_awa_score,
                   en_exam_writing_score=en_exam_writing_score, en_exam_listening_score=en_exam_listening_score,
                   en_exam_reading_score=en_exam_reading_score, en_exam_speaking_score=en_exam_speaking_score,
                   nickname=nickname)
    print emp_data

    # try:
    #     pass
    #
    #     conn = mysql.connector.connect(host='localhost',
    #                                    database='yocket_db',
    #                                    user='root',
    #                                    password='root')
    #     cursor = conn.cursor()
    #
    #     cursor.execute('INSERT INTO yocket_db.profiles VALUES("%s","%s",%d,%d,"%s","%s",%d,%d,"%s","%s","%s",%d,%d,%d,%d,%d,%d,%d,%s)'%
    #                    (term,
    #                     gre_date,
    #                     work_experience_months,
    #                     ug_score,ug_score_pattern,en_exam_pattern,
    #                     en_exam_score,gre_score,status,course_name,university_name,gre_verbal_score,gre_quant_score,gre_awa_score,en_exam_writing_score,en_exam_listening_score,en_exam_reading_score,en_exam_speaking_score,nickname))
    #     conn.commit()
    # except Error as error:
    #     print(error)