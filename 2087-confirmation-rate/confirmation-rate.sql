# Write your MySQL query statement below
Select s.user_id, 
    ROUND(IFNULL(AVG(action = 'confirmed'),0),2) confirmation_rate
FROM Signups s
LEFT JOIN Confirmations c
USING(user_id)
GROUP BY s.user_id
