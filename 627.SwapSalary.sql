# https://leetcode.com/problems/swap-salary/submissions/
UPDATE salary
    SET sex  = (
        CASE WHEN sex = 'm' THEN  'f' 
        ELSE 'm' 
        END)
