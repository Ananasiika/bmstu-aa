#pragma once
#include <iostream>
#include <fstream>
#include <string>
#include <queue>
#include <cstdlib>
#include <mutex>
#include <condition_variable>
#include <thread>
#include <functional>

class Conveyor
{
public:
    Conveyor(const std::string& filename);
    void start();
    void log_linear(int task_num, int stage_num, std::function<void(std::string&)> func, bool is_print);
    void log_conveyor(int task_num, int stage_num, std::function<void(std::string&)> func, bool is_print);
    void stage1_linear(int task_num, bool is_print);
    void stage2_linear(int task_num, bool is_print);
    void stage3_linear(int task_num, bool is_print);
    void parse_linear(bool is_print);
    void stage1_parallel(int task_num, bool is_print);
    void stage2_parallel(int task_num, bool is_print);
    void stage3_parallel(int task_num, bool is_print);
    void run();

private:
    std::string filename;
    std::vector<double> t1;
    std::vector<double> t2;
    std::vector<double> t3;
    std::mutex mtx; // мьютекс для синхронизации доступа к textQueue
    std::mutex m; // мьютекс для синхронизации доступа к lineQueue
    std::queue<std::string> textQueue; // очередь для хранения текстов
    std::queue<std::string> lineQueue; // очередь для хранения предложений
    std::condition_variable cv;
    double time_now;
};
