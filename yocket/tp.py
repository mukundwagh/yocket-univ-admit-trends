data = ['term','gre_date','work_experience_months','ug_score','ug_score_pattern','en_exam_pattern','en_exam_score','gre_score','status','course_name','university_name','gre_verbal_score','gre_quant_score','gre_awa_score','en_exam_writing_score','en_exam_listening_score','en_exam_reading_score','en_exam_speaking_score','nickname']
for d in data :
    print d

import base64

pas = base64.b64encode('%s:%s' % ("mukundwagh@gmail.com", "mukund@123"))
print pas