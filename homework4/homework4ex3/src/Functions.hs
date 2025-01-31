module Functions where

import Data.List (group, sort)
import Debug.Trace (trace)
import System.Random.Mersenne.Pure64 (PureMT, newPureMT, randomInt)
import Prelude

step :: PureMT -> (Int, PureMT)
step mt =
  let (r, newMt) = randomInt mt
   in (if even r then -1 else 1, newMt)

-- Recursive Sn
-- If I add : here it is faster, but not quite as fast
sn :: PureMT -> Int -> ([Int], PureMT)
sn mt 1 =
  let (result, mt1) = step mt
   in ([result], mt1)
sn mt n =
  let (tempArr, tempMt) = sn mt (n - 1)
      (tempAdd, newMt) = step tempMt
   in (tempArr ++ [tempAdd + last tempArr], newMt)

superHelper :: Int -> Int
superHelper (-1) = 0
superHelper 1 = 1

-- Optimized sn function using tail recursion (O(n) time complexity):
-- (newSum : acc) is time constant, compared to O(n) of
snOptimized :: PureMT -> Int -> ([Int], PureMT)
snOptimized mt n =
  let go :: Int -> PureMT -> Int -> [Int] -> ([Int], PureMT)
      go 0 mt' _ acc = (reverse acc, mt')
      go k mt' current acc =
        let (val, newMt) = step mt'
            newSum = current + val
         in go (k - 1) newMt newSum (newSum : acc)
   in go n mt 0 [0] -- Start with an initial "0" to accumulate sums

dn :: Maybe Int -> Int -> Int
dn Nothing n
  | n > 0 = 1
  | otherwise = 0
dn (Just n1) n2
  | n1 > 0 = 1
  | n2 > 0 = 1
  | otherwise = 0

ln :: [Int] -> Int
ln [n] = dn Nothing n
ln (x : s : xs) = dn (Just x) s + ln (s : xs)

pn :: PureMT -> Int -> (Double, PureMT)
pn mt n =
  let (snArr, mt1) = snOptimized mt n
      val = fromIntegral $ ln snArr
   in (val / fromIntegral n, mt1)
