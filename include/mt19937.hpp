// This was taken from wikipedia and then rewriten so I could use it later.
// Namespace so I dont mix it later with some other random generators.

#ifndef MT19937_HPP
#define MT19937_HPP

#include <cstdint>

namespace mt19937 {
const int n = 624;
const int m = 397;
const int W = 32;
const int R = 31;
const uint32_t UMASK = 0xffffffffUL << R;
const uint32_t LMASK = 0xffffffffUL >> (W-R);
const uint32_t a = 0x9908b0dfUL;
const int u = 11;
const int s = 7;
const int t = 15;
const int l = 18;
const uint32_t b = 0x9d2c5680UL;
const uint32_t c = 0xefc60000UL;
const uint32_t f = 1812433253UL;


struct mt_state{
    uint32_t state_array[n];
    int state_index;
};

void initialize_state(mt_state* state, uint32_t seed);
uint32_t random_uint32(mt_state* state);

} // namespace mt19937

#endif // MT19937_HPP
