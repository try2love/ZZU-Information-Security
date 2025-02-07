--2.根据课程编号查询本课程的最高成绩、平均成绩、最低成绩
create procedure select2
@cno int=null
as
	if(@cno is null)
	begin
		print'请输入课程号以查询本课程的最高、最低和平均成绩。'
	end
	else if(
		(select cno from sc where cno=@cno)!=@cno)
	begin
		print '输入课程号有误。'
	end
	else
	begin
		select MAX(grade) 最高成绩,AVG(grade) 平均成绩,MIN(grade) 最低成绩
		from sc
		where sc.cno=@cno
	end
go