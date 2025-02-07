CREATE TRIGGER dynamic_yueshu
--在成绩表上修改成绩时，自动修改学生的学分和总学分
ON sc
AFTER UPDATE,insert,delete
AS
BEGIN
	declare @sno int,@cno int,@grade int
	select @sno=sno,@cno=cno,@grade=grade
		from inserted
	if @grade>=90 and @grade<=100
		update sc
		set credit=course.ccredit
		from course inner join sc
		on sc.cno=course.cno
		where sno=@sno and @cno=sc.cno
	else if @grade>=80 and @grade<90
		update sc
		set credit=course.ccredit*0.7
		from course inner join sc
		on sc.cno=course.cno
		where sno=@sno and @cno=sc.cno
	else if @grade>=70 and @grade<80
		update sc
		set credit=course.ccredit*0.5
		from course inner join sc
		on sc.cno=course.cno
		where sno=@sno and @cno=sc.cno
	else if @grade>=60 and @grade<70
		update sc
		set credit=course.ccredit*0.3
		from course inner join sc
		on sc.cno=course.cno
		where sno=@sno and @cno=sc.cno
	else
		update sc
		set credit=0
		from course inner join sc
		on sc.cno=course.cno
		where sno=@sno and @cno=sc.cno
	update student
	set scredit=tem.total
	from(select sum(credit) as total from sc where sno=@sno) as tem
	where sno=@sno
end