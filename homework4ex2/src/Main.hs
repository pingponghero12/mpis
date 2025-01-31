module Main where

import Data.List (mapAccumL)
import Functions
import System.Random.Mersenne.Pure64 (PureMT, newPureMT, randomInt)

printToCSV :: [(Int, Int, Double)] -> IO ()
printToCSV results = do
  putStrLn "n,value,probability"
  mapM_
    ( \(n_val, val, prob) ->
        putStrLn $ show n_val ++ "," ++ show val ++ "," ++ show prob
    )
    results

main :: IO ()
main = do
  mt <- newPureMT
  let k = 100
  let ns = 5

  let (resultList, newMT) = example mt ns k

  printToCSV resultList
