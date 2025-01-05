#include "max_load.hpp"

void max_load_sim(mt19937::mt_state* state, std::ofstream* file, const int n, const int d) {
    std::vector<int> boxes(n, 0);
    int max_load = 0;

    for(int i=0; i<n; i++) {
        std::vector<int> box;
        for(int k=0; k<d; k++) box.push_back(mt19937::random_uint32(state) % n);

        int mn=n;
        int id;
        for(int k=0; k<d; k++) {
            if (boxes[box[k]] < mn) {
                mn = boxes[box[k]];
                id = box[k];
            }
        }
        boxes[id]++;
        if (boxes[id] > max_load) max_load = boxes[id];
    }

    *file << n << "," << max_load << "\n";
}

void max_load_thread_1() {
    mt19937::mt_state state;
    uint32_t seed = 19650218UL;
    mt19937::initialize_state(&state, seed);

    std::ofstream file("ex1_d1.csv");
    file << "n,max_load" << std::endl;

    for(int i = 10000; i <= 1000000; i+=10000) {
        for (int k = 0; k < 50; ++k) {
            max_load_sim(&state, &file, i, 1);
        }
    }
    file.close();
    std::cout << "max load thread 1" << std::endl;
}

void max_load_thread_2() {
    mt19937::mt_state state;
    uint32_t seed = 19650218UL;
    mt19937::initialize_state(&state, seed);

    std::ofstream file("ex1_d2.csv");
    file << "n,max_load" << std::endl;

    for(int i = 10000; i <= 1000000; i+=10000) {
        for (int k = 0; k < 50; ++k) {
            max_load_sim(&state, &file, i, 2);
        }
    }
    file.close();
    std::cout << "max load thread 2" << std::endl;
}
