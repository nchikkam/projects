isSquare :: Integer -> Bool
isSquare n = foldr (\x r-> x*x==n || x*x<n && r ) False [1..]

main = print ( isSquare 91 )