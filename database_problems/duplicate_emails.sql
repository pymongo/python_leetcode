-- 我一开是的思路先用distinct email查一次，结果记为a，然后查所有email记为b
-- 通过MINUS operator得到b-a，最后SELECT DISTINCT email FROM b-a
-- 但是「MySQL不支持MINUS」求差集的操作

-- 按邮箱分组后用having语句查count(email)>1的
select Email from Person group by Email having count(Email) > 1;
