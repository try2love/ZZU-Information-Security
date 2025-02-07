--5.按照课程编号分组统计选课人数、最高成绩、最低成绩、平均成绩、及格人数
create procedure select5
@cno int=null
as
	if(@cno is null)
	begin
		print'请输入课程编号用以统计该课程选课人数、最高成绩、最低成绩、平均成绩和及格人数'
	end
	else if((select cno from sc where cno=@cno)!=@cno)
	begin
		print'输入课程号错误！'
	end
	else
	begin
		select count(distinct sno) 选课人数,max(grade) 最高成绩,min(grade) 最低成绩,AVG(grade) 平均成绩,sum(case when grade>=60 then 1 else 0 end) 及格人数
		from sc
		where cno=@cno
	end
go