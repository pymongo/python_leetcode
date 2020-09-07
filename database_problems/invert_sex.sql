update users
set sex = if(sex = 'male', 'female', 'male');

-- 方法2，使用case when语句
UPDATE orders
SET
    ask_or_bid = CASE ask_or_bid
        WHEN 'ask' THEN 'bid'
        ELSE 'ask'
    END;
