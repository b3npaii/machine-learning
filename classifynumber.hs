classifyNumber(x) = if x < 0
    then return "negative number"
    else return "nonnegative number"

--crossproduct x y = return [x!!1 * y!!2 - x!!2 * y!!1, x!!0 * y!!2 - x!!2 * y!!0, x!!0 * y!!1 - x!! 1 * ]
