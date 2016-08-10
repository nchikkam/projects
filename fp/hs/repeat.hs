rep :: a -> [a]  
rep x = x:rep x

main = print ( rep [1, 2, 3] )