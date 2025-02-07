--3.查询选修了某位老师所教课程的学生的姓名
create procedure select3
@teacher char(16)=null
as
	if(@teacher is null)
	begin
		print'请输入老师姓名以查询该老师所教课程的学生的姓名'
	end
	else if((select teacher from course where teacher=@teacher)!=@teacher)
	begin
		print'输入的老师姓名有误！'
	end
	else
	begin
		select sname 学生姓名
		from sc,course,student
		where sc.cno=course.cno and student.sno=sc.sno and teacher=@teacher
	end
go