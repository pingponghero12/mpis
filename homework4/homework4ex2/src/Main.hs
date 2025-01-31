module Main where

import Data.List (foldl')
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
  let k = 10000
  let ns = [100]

  let (results, _) =
        foldl'
          ( \(acc, mt1) n ->
              let (dupa, mt2) = example mt1 n k
               in (acc ++ dupa, mt2)
          )
          ([], mt)
          ns
  let formatted = results

  printToCSV formatted
