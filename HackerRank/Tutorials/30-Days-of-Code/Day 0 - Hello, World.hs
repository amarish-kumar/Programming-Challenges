main = do
    -- Get a line of input from stdin and save it to our variable
    inputString <- getLine
    -- Your first line of output goes here
    putStrLn ("Hello, World.")
    -- Write the second line of output
    putStrLn (inputString)
