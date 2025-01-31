module Main where

import Data.List (foldl')
import Functions
import System.Random.Mersenne.Pure64 (PureMT, newPureMT, randomInt)

printToCSV :: [(Int, Int, Double)] -> IO ()
printToCSV results = do
  putStrLn "n,k,pn"
  mapM_
    ( \(n_val, val, prob) ->
        putStrLn $ show n_val ++ "," ++ show val ++ "," ++ show prob
    )
    results

agg :: PureMT -> Int -> Int -> ([(Int, Int, Double)], PureMT)
agg mt n 0 =
  let (pnVal, mt1) = pn mt n
   in ([(n, 0, pnVal)], mt1)
agg mt n k =
  let (result, mt1) = agg mt n (k - 1)
      (pnVal, mt2) = pn mt1 n
   in (result ++ [(n, k, pnVal)], mt2)

main :: IO ()
main = do
  mt <- newPureMT
  let k = 5000
  let ns = [100, 1000, 10000]

  let (results, _) =
        foldl'
          ( \(acc, mt1) n ->
              let (dupa, mt2) = agg mt1 n k
               in (acc ++ dupa, mt2)
          )
          ([], mt)
          ns
  let formatted = results

  printToCSV formatted
