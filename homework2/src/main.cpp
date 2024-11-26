#include <iostream>
#include <mt19937.hpp>
#include <cmath>
#include <vector>
#include <functional>
#include <fstream>

double mp(mt19937::mt_state* state, int n, double M, 
        double a, 
        double b, 
        const std::function<bool(double, double)>& condition) {

    int C = 0;

    for(int i = 0; i < n; i++){
        double x = a + (static_cast<double>(mt19937::random_uint32(state)) / static_cast<double>(UINT32_MAX)) * (b-a);
        double y = (static_cast<double>(mt19937::random_uint32(state)) / static_cast<double>(UINT32_MAX)) * M;

        if (condition(x, y)) C++;
    }

    return (static_cast<double>(C) / static_cast<double>(n)) * (b-a) * M;
}

void print_example(mt19937::mt_state* state, std::string file_name, double M, double a, double b, 
        const std::function<bool(double, double)>& ex){
    std::ofstream file(file_name + "-5.csv");
    file << "n,int" << std::endl;
    
    for(int i = 50; i <= 5000; i+=50){
        for(int kappa = 0; kappa < 5; kappa++){
            file << i << "," << mp(state, i, M, a, b, ex) << std::endl;
        }
    }

    file.close();

    std::ofstream file1(file_name + "-50.csv");
    file1 << "n,int" << std::endl;

    for(int i = 50; i <= 5000; i+=50){
        for(int kappa = 0; kappa < 50; kappa++){
            file1 << i << "," << mp(state, i, M, a, b, ex) << std::endl;
        }
    }
    file1.close();
}

void simulation(mt19937::mt_state* state, std::ofstream* file, int n) {
    std::vector<int> boxes(n, 0);
    int full_box_count = 0;

    int bn = -1;
    int un;
    int cn = -1;
    int cn_help = 0;
    int dn;
    int diff;

    int counter = 1;
    while(full_box_count != n) {
        int box = mt19937::random_uint32(state) % n;
        boxes[box]++;

        if (boxes[box] == 2) full_box_count++;

        // bn
        if (bn == -1 && boxes[box] == 2) bn = counter;

        // un
        if (boxes[box] == 1) cn_help++;
        if (counter == n) un = cn_help;

        // cn
        if (cn == -1 && cn_help == n) cn = counter;

        counter++;
    }

    dn = counter-1;
    diff = dn - cn;

    *file << n << "," << bn << "," << un << "," << cn << "," << dn << "," << diff << std::endl;
}
    

int main(){
    mt19937::mt_state state;
    uint32_t seed = 19650218UL;
    mt19937::initialize_state(&state, seed);

    std::ofstream file("data.csv");
    file << "n,bn,un,cn,dn,diff" << std::endl;

    for(int i = 1000; i <= 100000; i+=1000) {
        for (int k = 0; k < 50; ++k) {
            simulation(&state, &file, i);
        }
    }

    return 0;
}
