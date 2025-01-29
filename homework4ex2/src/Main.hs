module Main where

import Functions
import System.Random.Mersenne.Pure64 (PureMT, newPureMT, randomInt)

main :: IO ()
main = do
  mt <- newPureMT
  let k = 10000
  let n = [5, 10 .. 30]
