''''
sqlite> select student_id, score, test_type, date
   ...> from test, test_score
   ...> where test.id = test_score.test_id;
student_id  score       test_type   date
----------  ----------  ----------  ----------
1           15          1           2018-10-4
2           9           1           2018-10-4
3           12          1           2018-10-4
4           21          1           2018-10-4
5           6           1           2018-10-4
6           18          1           2018-10-4
7           5           1           2018-10-4
8           23          1           2018-10-4
9           5           1           2018-10-4
10          22          1           2018-10-4
1           2           2           2018-3-28
2           3           2           2018-3-28
3           4           2           2018-3-28
4           10          2           2018-3-28
5           20          2           2018-3-28
6           8           2           2018-3-28
7           6           2           2018-3-28
8           2           2           2018-3-28
9           18          2           2018-3-28
10          13          2           2018-3-28
1           22          2           2018-3-4
2           10          2           2018-3-4
3           7           2           2018-3-4
4           6           2           2018-3-4
5           1           2           2018-3-4
6           14          2           2018-3-4
7           19          2           2018-3-4
8           15          2           2018-3-4
9           9           2           2018-3-4
10          14          2           2018-3-4
1           17          2           2018-8-8
2           10          2           2018-8-8
3           11          2           2018-8-8
4           13          2           2018-8-8
5           17          2           2018-8-8
6           3           2           2018-8-8
7           3           2           2018-8-8
8           23          2           2018-8-8
9           17          2           2018-8-8
10          6           2           2018-8-8

sqlite> select f_name, l_name, score, test_type, date
   ...> from test, test_score, student
   ...> where test.id = test_score.test_id
   ...> and test_score.student_id = student.id;
f_name      l_name      score       test_type   date
----------  ----------  ----------  ----------  ----------
Ashley      Williams    15          1           2018-10-4
Matthew     Martin      9           1           2018-10-4
Daniel      Jackson     12          1           2018-10-4
Matthew     Martin      21          1           2018-10-4
Matthew     Garcia      6           1           2018-10-4
Ashley      Brown       18          1           2018-10-4
Jennifer    Thomas      5           1           2018-10-4
Samantha    Robinson    23          1           2018-10-4
Lauren      Smith       5           1           2018-10-4
Amanda      Williams    22          1           2018-10-4
Ashley      Williams    2           2           2018-3-28
Matthew     Martin      3           2           2018-3-28
Daniel      Jackson     4           2           2018-3-28
Matthew     Martin      10          2           2018-3-28
Matthew     Garcia      20          2           2018-3-28
Ashley      Brown       8           2           2018-3-28
Jennifer    Thomas      6           2           2018-3-28
Samantha    Robinson    2           2           2018-3-28
Lauren      Smith       18          2           2018-3-28
Amanda      Williams    13          2           2018-3-28
Ashley      Williams    22          2           2018-3-4
Matthew     Martin      10          2           2018-3-4
Daniel      Jackson     7           2           2018-3-4
Matthew     Martin      6           2           2018-3-4
Matthew     Garcia      1           2           2018-3-4
Ashley      Brown       14          2           2018-3-4
Jennifer    Thomas      19          2           2018-3-4
Samantha    Robinson    15          2           2018-3-4
Lauren      Smith       9           2           2018-3-4
Amanda      Williams    14          2           2018-3-4
Ashley      Williams    17          2           2018-8-8
Matthew     Martin      10          2           2018-8-8
Daniel      Jackson     11          2           2018-8-8
Matthew     Martin      13          2           2018-8-8
Matthew     Garcia      17          2           2018-8-8
Ashley      Brown       3           2           2018-8-8
Jennifer    Thomas      3           2           2018-8-8
Samantha    Robinson    23          2           2018-8-8
Lauren      Smith       17          2           2018-8-8
Amanda      Williams    6           2           2018-8-8

sqlite> select f_name || ' ' || l_name as Name,
   ...> count(absence.date) as Absences
   ...> from student, absence
   ...> where absence.student_id = student.id
   ...> group by id;
Name             Absences
---------------  ----------
Ashley Williams  21
Matthew Martin   16
Daniel Jackson   14
Matthew Martin   20
Matthew Garcia   20
Ashley Brown     15
Jennifer Thomas  15
Samantha Robins  23
Lauren Smith     23
Amanda Williams  13

sqlite> select f_name || ' ' || l_name as Name, score, test_id
   ...> from test_score join student
   ...> on student.id = test_score.student_id
   ...> order by(Name);
Name             score       test_id
---------------  ----------  ----------
Amanda Williams  22          1
Amanda Williams  13          2
Amanda Williams  14          3
Amanda Williams  6           4
Ashley Brown     18          1
Ashley Brown     8           2
Ashley Brown     14          3
Ashley Brown     3           4
Ashley Williams  15          1
Ashley Williams  2           2
Ashley Williams  22          3
Ashley Williams  17          4
Daniel Jackson   12          1
Daniel Jackson   4           2
Daniel Jackson   7           3
Daniel Jackson   11          4
Jennifer Thomas  5           1
Jennifer Thomas  6           2
Jennifer Thomas  19          3
Jennifer Thomas  3           4
Lauren Smith     5           1
Lauren Smith     18          2
Lauren Smith     9           3
Lauren Smith     17          4
Matthew Garcia   6           1
Matthew Garcia   20          2
Matthew Garcia   1           3
Matthew Garcia   17          4
Matthew Martin   9           1
Matthew Martin   21          1
Matthew Martin   3           2
Matthew Martin   10          2
Matthew Martin   10          3
Matthew Martin   6           3
Matthew Martin   10          4
Matthew Martin   13          4
Samantha Robins  23          1
Samantha Robins  2           2
Samantha Robins  15          3
Samantha Robins  23          4

sqlite> select f_name || ' ' || l_name as Name,
   ...> count(absence.date) as Absence
   ...> from student left join absence
   ...> on absence.student_id = student.id
   ...> group by id;
Name             Absence
---------------  ----------
Ashley Williams  21
Matthew Martin   16
Daniel Jackson   14
Matthew Martin   20
Matthew Garcia   20
Ashley Brown     15
Jennifer Thomas  15
Samantha Robins  23
Lauren Smith     23
Amanda Williams  13

sqlite> select f_name || ' ' || l_name as Name,
   ...> count(absence.date) as Absence
   ...> from student left join absence
   ...> on absence.student_id = student.id
   ...> group by id;
Name             Absence
---------------  ----------
Ashley Williams  21
Matthew Martin   16
Daniel Jackson   14
Matthew Martin   20
Matthew Garcia   20
Ashley Brown     15
Jennifer Thomas  15
Samantha Robins  23
Lauren Smith     23
Amanda Williams  13

sqlite> select score, test_id
   ...> from student natural join test_score
   ...> where student_id = id;
score       test_id
----------  ----------
15          1
9           1
12          1
21          1
6           1
18          1
5           1
23          1
5           1
22          1
2           2
3           2
4           2
10          2
20          2
8           2
6           2
2           2
18          2
13          2
22          3
10          3
7           3
6           3
1           3
14          3
19          3
15          3
9           3
14          3
17          4
10          4
11          4
13          4
17          4
3           4
3           4
23          4
17          4
6           4

sqlite> select (1+2) / (6/4) * 10;
(1+2) / (6/4) * 10
------------------
30

sqlite> select * from test_score
   ...> where score
   ...> between 15 and 20;
student_id  test_id     score
----------  ----------  ----------
1           1           15
6           1           18
5           2           20
9           2           18
7           3           19
8           3           15
1           4           17
5           4           17
9           4           17
'''