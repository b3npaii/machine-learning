clothing tempc 
    | tempf >= 80 = "wear a short sleeve shirt"
    | tempf >= 65 = "wearing a long sleeve shirt"
    | tempf >= 50 = "wear a sweater"
    | otherwise = "wear a jacket"
    where tempf = tempc* 1.8 + 32
