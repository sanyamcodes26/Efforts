'''
sqlite> select test.date as Date,
   ...> min(test_score.score) as Worst,
   ...> max(test_score.score) as Best
   ...> from test_score, test
   ...> where test_score.test_id = test.id
   ...> group by test.date;
Date        Worst       Best
----------  ----------  ----------
2018-10-4   5           23
2018-3-28   2           20
2018-3-4    1           22
2018-8-8    3           23

sqlite> select test.date as Date,
   ...> avg(test_score.score) as Avg_Score
   ...> from test_score, test
   ...> where test_score.test_id = test.id
   ...> group by test.date;
Date        Avg_Score
----------  ----------
2018-10-4   13.6
2018-3-28   8.6
2018-3-4    11.7
2018-8-8    12.0

sqlite> select f_name || ' ' || l_name as Name,
   ...> test_score.score as Score
   ...> from test_score, student
   ...> where test_score.score > 20
   ...> and test_score.student_id = student.id
   ...> group by Name;
Name             Score
---------------  ----------
Amanda Williams  22
Ashley Williams  22
Matthew Martin   21
Samantha Robins  23



'''