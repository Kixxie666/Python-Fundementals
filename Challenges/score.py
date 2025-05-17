student_scores = [123,123,345,456,34523,1243,24534,645,672,413,1]
##total_exam_score = sum(student_scores)
#print (total_exam_score)
#mid = 0
#for score in student_scores:
  #  mid += score
  #  print(mid)

max_score = 0
for score in student_scores:
    if score > max_score:
        max_score = score
        
print(max_score)