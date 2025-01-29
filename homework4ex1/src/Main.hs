module Main where

import Functions

main :: IO ()
main = do
  let ns = [100, 1000, 10000]
      p = 0.5

  putStrLn "a)"
  mapM_
    ( \n -> do
        let ex = calculateEX n p
            thresholdA = 1.15 * ex
            markovVal = markovBound n p thresholdA
            chebVal = chebyshevBound n p thresholdA
            exactValA = exactProbA n p 1.15

        putStrLn $ "n = " ++ show n
        putStrLn $ "Markov Bound: " ++ show markovVal
        putStrLn $ "Chebyshev Bound: " ++ show chebVal
        putStrLn $ "Exact Value: " ++ show exactValA
        putStrLn ""
    )
    ns

  putStrLn "b)"
  mapM_
    ( \n -> do
        let ex = calculateEX n p
            thresholdB = 0.1 * ex
            markovVal = markovBound n p thresholdB
            chebVal = chebyshevBound n p thresholdB
            exactValB = exactProbB n p 0.1

        putStrLn $ "n = " ++ show n
        putStrLn $ "Markov Bound: " ++ show markovVal
        putStrLn $ "Chebyshev Bound: " ++ show chebVal
        putStrLn $ "Exact Value: " ++ show exactValB
    )
    ns
