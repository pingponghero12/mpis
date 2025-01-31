module Functions where

import Data.List (sort)
import Debug.Trace
import System.Random.Mersenne.Pure64 (PureMT, newPureMT, randomInt)

-- I love that gogle just shows System.Random.Mersenne(not PureMT) which was uploaded on 2011
-- Btw examples in docs there just dont work
-- Also it was pure heresy
step :: PureMT -> (Int, PureMT)
step mt =
  let (r, newMt) = randomInt mt
   in (if even r then -1 else 1, newMt)

-- Recursive Sn
sn :: PureMT -> Int -> (Int, PureMT)
sn mt 0 = step mt
sn mt n =
  let (tempSum, tempMt) = sn mt (n - 1)
      (tempAdd, newMt) = step tempMt
   in (tempSum + tempAdd, newMt)

genWalks :: PureMT -> Int -> Int -> ([Int], PureMT)
genWalks mt n 0 = ([], mt)
genWalks mt n k =
  let (walk, mt1) = sn mt n
      (remainingWalks, mt2) = genWalks mt1 n (k - 1)
   in (walk : remainingWalks, mt2)

-- Simulated CDF
simCDF :: [Int] -> Int -> [(Int, Int, Double)]
simCDF walks ns =
  let sorted = sort walks
      n = fromIntegral $ length walks
   in [(ns, x, fromIntegral (length $ filter (<= x) walks) / n) | x <- sorted]

example :: PureMT -> Int -> Int -> ([(Int, Int, Double)], PureMT)
example mt n k =
  let (walks, mt) = genWalks mt n k
   in (simCDF walks n, mt)
