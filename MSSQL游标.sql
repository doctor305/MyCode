---1.声明游标

declare orderNum_01_cursor cursor scroll

for select 单位编码 from 测试表 order by 单位编码

--2.打开游标

open orderNum_01_cursor

--3.声明变量

declare @ID int

declare @count int

declare @temp varchar(15)

set @count = 1

set @temp = ''


fetch First from orderNum_01_cursor into @ID
 
while @@fetch_status=0   
 
  begin
   
   if @ID=@temp
	
    begin
		
     set @count = @count + 1

    end

   else

    begin

     print @temp + '编码有记录条数：'

     print @count

     set @count = 1

     set @temp = @ID

    end

  fetch next from orderNum_01_cursor into @ID  --移动游标

 end
close orderNum_01_cursor --关闭游标

deallocate orderNum_01_cursor --删除游标