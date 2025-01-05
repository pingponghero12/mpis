#include "insertion_sort.hpp"

std::vector<int> random_permutation(mt19937::mt_state* state, int n) {
    std::vector<int> perm(n, 0);
    for(int i = 1; i<=n; i++) {
        int box = mt19937::random_uint32(state) % n;

        while (perm[box] != 0) box = mt19937::random_uint32(state) % n;

        perm[box] = i;
    }
    return perm;
}

void insertion_sort_sim(mt19937::mt_state* state, std::ofstream* file, const int n) {
    std::vector<int> A = random_permutation(state, n);
    int cmp = 0;
    int s = 0;

    for (int j = 1; j<n; j++) {
        int key = A[j];
        int i = j-1;

        while (i > 0 && A[i] > key) {
            s++;
            cmp++;
            A[i+1] = A[i];
            i--;
        }
        cmp++;
        A[i+1] = key;
    }

    *file << n << "," << cmp << "," << s << "\n";
}

void insertion_sort_thread() {
    mt19937::mt_state state;
    uint32_t seed = 19650218UL;
    mt19937::initialize_state(&state, seed);

    std::ofstream file("ex2.csv");
    file << "n,cmp,s" << std::endl;

    for(int i = 100; i <= 10000; i+=100) {
        for (int k = 0; k < 50; ++k) {
            insertion_sort_sim(&state, &file, i);
        }
    }
    file.close();
    std::cout << "insert sort" << std::endl;
}
