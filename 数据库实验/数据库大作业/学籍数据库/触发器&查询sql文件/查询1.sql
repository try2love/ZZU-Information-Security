--1.	根据学生编号、课程编号等查询成绩信息
CREATE PROCEDURE select1
@sno int=NULL,
@cno int=NULL
AS
	IF(@sno is null or @cno is null)
	begin
		print '请输入学号与课程号用以查询成绩!'
	end
	else if(
		(select sno from sc where sno=@sno)!=@sno
		or (select cno from sc where cno=@cno)!=@cno
		)
	begin
		print '输入学号或课程号错误！'
	end
	else
	begin
		select sc.sno 学号,student.sname 姓名,sc.cno 课程号,grade 成绩
		from student,sc
		where student.sno=sc.sno and cno=@cno and sc.sno=@sno
	end
go