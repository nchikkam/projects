lst = [1, 2, 3, 4, 5, 6, 7, 8, 9,10]

positives lst = [ x | x <- lst, x <5 ]

main = print ( positives lst )