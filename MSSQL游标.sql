---1.�����α�

declare orderNum_01_cursor cursor scroll

for select ��λ���� from ���Ա� order by ��λ����

--2.���α�

open orderNum_01_cursor

--3.��������

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

     print @temp + '�����м�¼������'

     print @count

     set @count = 1

     set @temp = @ID

    end

  fetch next from orderNum_01_cursor into @ID  --�ƶ��α�

 end
close orderNum_01_cursor --�ر��α�

deallocate orderNum_01_cursor --ɾ���α�