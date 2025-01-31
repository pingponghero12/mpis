module Functions where

import Data.List (group, sort)
import Debug.Trace (trace)
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
sn mt 1 = step mt
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

-- simCDF :: [Int] -> Int -> [(Int, Int, Double)]
-- simCDF walks ns =
--  let sorted = sort walks
--      n = fromIntegral $ length walks
--   in [(ns, x, fromIntegral (length $ filter (<= x) walks) / n) | x <- sorted]

-- Simulated CDF
-- This is O(n log n) O1 generated this, coz my algo was O(n^2) which was super slow
simCDF :: [Int] -> Int -> [(Int, Int, Double)]
simCDF walks ns =
  let sortedWalks = sort walks
      total = fromIntegral (length sortedWalks)
      grouped = group sortedWalks
      cumulativeCounts = scanl1 (+) (map length grouped)
      distinctValues = map head grouped
   in zipWith
        (\x countSoFar -> (ns, x, fromIntegral countSoFar / total))
        distinctValues
        cumulativeCounts

example :: PureMT -> Int -> Int -> ([(Int, Int, Double)], PureMT)
example mt n k =
  -- I've spend like 2h here since I had let(walks, mt) before and the name confilict
  -- Funnly enough ghc did not notice it and I would only get h4: <<loop>>
  let (walks, mt1) = genWalks mt n k
   in (simCDF walks n, mt1)
