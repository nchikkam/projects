range :: Int -> Int -> [Int]
range start end
 | start > end = []
 | start == end = [end]
 | otherwise = start: (range (start+1) end)

main = print (range 1 20)
