module Functions where

import Statistics.Distribution
import Statistics.Distribution.Binomial

calculateEX :: Integer -> Double -> Double
calculateEX n p = (fromIntegral n) * p

calculateVar :: Integer -> Double -> Double
calculateVar n p = (fromIntegral n) * p * (1 - p)

markovBound :: Integer -> Double -> Double -> Double
markovBound n p a = (calculateEX n p) / a

chebyshevBound :: Integer -> Double -> Double -> Double
chebyshevBound n p a = (calculateVar n p) / (a * a)

-- Exact distibutions
createBin :: Integer -> Double -> BinomialDistribution
createBin n p = binomial (fromIntegral n) p

probGreaterEq :: BinomialDistribution -> Double -> Double
probGreaterEq ds k = 1 - cumulative ds (k - 1) -- cumulative is <=

exactProbA :: Integer -> Double -> Double -> Double
exactProbA n p a =
  let ds = createBin n p
      ex = calculateEX n p
      mx = a * ex
   in probGreaterEq ds mx

exactProbB :: Integer -> Double -> Double -> Double
exactProbB n p a =
  let ds = createBin n p
      ex = calculateEX n p
   in 2 * probGreaterEq ds (ex + 0.1 * ex)
