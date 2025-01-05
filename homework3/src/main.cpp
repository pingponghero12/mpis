#include <thread>

#include "max_load.hpp"
#include "insertion_sort.hpp"
#include "com_model.hpp"

int main(){
//    std::thread d1 = std::thread(max_load_thread_1);
//    std::thread d2 = std::thread(max_load_thread_2);
//    std::thread in = std::thread(insertion_sort_thread);
    std::thread cm = std::thread(com_model_thread);

//    d1.join();
//    d2.join();
//    in.join();
    cm.join();

    return 0;
}
