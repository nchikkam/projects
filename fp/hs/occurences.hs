lst = [1, 2, 3, 4, 5, 6, 7, 5, 5, 8, 9,10]

occurs value [] = 0
occurs value (x:xs) = (if value == x then 1 else 0) + occurs value xs

main = print ( occurs 5 lst )