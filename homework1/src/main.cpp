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

int main(){
    mt19937::mt_state state;
    uint32_t seed = 19650218UL;
    mt19937::initialize_state(&state, seed);

    auto ex1 = [](double x, double y) {
        return y <= pow(x, 1.0/3.0);
    };

    print_example(&state, "ex1", 2, 0, 8, ex1);
    
    auto ex2 = [](double x, double y) {
        return y <= sin(x);
    };

    print_example(&state, "ex2", 1, 0, M_PI, ex2);

    auto ex3 = [](double x, double y) {
        return y <= 4*x*pow(1 - x, 3);
    };

    print_example(&state, "ex3", 0.421875, 0, 1, ex3);

    auto ex4 = [](double x, double y) {
        return y*y <= 1 - x*x;
    };

    print_example(&state, "ex4", 1, 0, 1, ex4);

    return 0;
}
