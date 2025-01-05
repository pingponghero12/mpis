#include "com_model.hpp"

// Random procent
double rp(mt19937::mt_state* state) {
    double x = (static_cast<double>(mt19937::random_uint32(state)) / static_cast<double>(UINT32_MAX));
    return x;
}

void insertion_sort_sim(mt19937::mt_state* state, std::ofstream* file, const int n, const double p) {
    // This algorithm can be easily faster howerver repeating rp() for dead will ensure we keep distribution.
    std::vector<bool> recived(n, false);
    int recived_count = 0;
    int tn = 0;

    while (recived_count != n) {
        for (int i = 0; i < n; i++) {
            double temp = rp(state);
            if (temp < p) {
                if (!recived[i]) recived_count++;
                recived[i] = true;
            }
        }
        tn++;
    }
    *file << n << "," << p << "," << tn << "\n";
}

void com_model_thread() {
    mt19937::mt_state state;
    uint32_t seed = 19650218UL;
    mt19937::initialize_state(&state, seed);

    std::ofstream file("ex3_01.csv");
    file << "n,p,tn" << std::endl;

    for(int i = 10000; i <= 1000000; i+=10000) {
        for (int k = 0; k < 50; ++k) {
            insertion_sort_sim(&state, &file, i, 0.1);
        }
    }
    file.close();
    std::cout << "com_model end" << std::endl;
}
