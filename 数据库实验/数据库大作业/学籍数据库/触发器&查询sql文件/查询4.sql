--4.根据学生编号查询该生的所有课程的总成绩和总学分情况
create procedure select4
@sno int=null
as
	if(@sno is null)
	begin
		print'请输入学生学号用以查询该生的所有课程的总成绩和总学分'
	end
	else if((select sno from sc where sno=@sno)!=@sno)
	begin
		print'输入的学号有误！'
	end
	else
	begin
		select sum(grade) 总成绩,sum(credit) 总学分
		from sc
		where sno=@sno
	end
go