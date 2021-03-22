-- @Time    : 2021/3/16 12:07 下午
-- @Author  : taou.liu
-- @email   : liutao0705@live.com
-- @File    : 175
-- @Software: Pycharm

select
 a.FirstName
,a.LastName
,b.City
,b.State
from Person a
left join Address b
on a.PersonId = b.PersonId