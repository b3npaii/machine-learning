chain 1 = [1]
chain n
    | even n = n: chain (n `div` 2)
    | odd n = n:chain (n * 3 + 1)

firstChainLongerThan n = length (takeWhile (< n) [length(chainArr) | chainArr <- [chain i | i <- [1..]]]) + 1