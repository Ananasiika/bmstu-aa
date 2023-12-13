#include "building.h"
#include <QProcess>
#include <QDebug>
#include <QtConcurrent/QtConcurrent>
#include <QFile>
#include <QTextStream>
#include <iostream>
#include <fstream>
#include <string>
#include <vector>

void exec_no_parallel(QString size)
{
    std::ifstream inputFile("data/input_" + size.toStdString() + "kb.txt");

    std::string text;
    std::string line;
    while (std::getline(inputFile, line)) {
        text += line + " ";
    }

    std::vector<std::string> sentences;
    std::string delimiter = ".!?";

    size_t pos = 0;
    std::string token;
    while (true) {
        pos = text.find_first_of(delimiter);
        if (pos == std::string::npos) {
            break;
        }
        token = text.substr(0, pos+1);
        sentences.push_back(token);
        text.erase(0, pos+1);
    }

    if (!text.empty()) {
        sentences.push_back(text);
    }

    std::string filename_prep = "./data/prep/no_" + size.toStdString() + ".txt";
    std::ofstream outputFile(filename_prep);
    if (!outputFile.is_open()) {
        std::cout << "Failed to open output file" <<  std::endl;
        return;
    }

    for (const auto& sentence : sentences) {
        outputFile << sentence << std::endl;
    }
    outputFile.close();

    std::string command = "python3 main.py " + filename_prep + " ./result/no_" + size.toStdString() + "output.txt";
    system(command.c_str());
}

void execute_one_thread(std::string filename_prep, std::string file_output) {
    std::string command = "python3 main.py " + filename_prep + " " + file_output;
    system(command.c_str());
}

void exec_parallel(QString size, int threads_count)
{
    std::ifstream inputFile("data/input_" + size.toStdString() + "kb.txt");

    std::string line;
    std::string text;
    while (std::getline(inputFile, line)) {
        text += line + " ";
    }

    std::vector<std::string> sentences;
    std::string delimiter = ".!?";

    size_t pos = 0;
    std::string token;
    while (true) {
        pos = text.find_first_of(delimiter);
        if (pos == std::string::npos) {
            break;
        }
        token = text.substr(0, pos+1);
        sentences.push_back(token);
        text.erase(0, pos+1);
    }

    if (!text.empty()) {
        sentences.push_back(text);
    }

    int sentences_count = sentences.size();
    int part_count = sentences_count / threads_count;

    for (int i = 0; i < threads_count; ++i) {
        std::string filename_prep = "./data/prep/" + size.toStdString() + "_" + QString::number(i).toStdString() + ".txt";
        std::ofstream outputFile(filename_prep);
        if (!outputFile.is_open()) {
            std::cout << "Failed to open output file" <<  std::endl;
            return;
        }
        for (int j = 0; j < part_count; ++j)
            outputFile << sentences[i * part_count + j] << std::endl;
        outputFile.close();
    }

    std::vector<std::thread> threads;

    for (int i = 0; i < threads_count; ++i) {
        std::string file_output = "./result/" + size.toStdString() + "output.txt";
        std::string filename_prep = "./data/prep/" + size.toStdString() + "_" + QString::number(i).toStdString() + ".txt";
        threads.push_back(std::thread(execute_one_thread, filename_prep, file_output));
    }

    for (std::thread& t : threads) {
        t.join();
    }
}

double time_mes_no_parallel(QString size)
{
    std::chrono::time_point<std::chrono::system_clock> time_start, time_end;
    double res_time = 0;

    for (int i = 0; i < ITERATIONS; i++)
    {
        time_start = std::chrono::system_clock::now();
        exec_no_parallel(size);
        time_end = std::chrono::system_clock::now();

        res_time += (std::chrono::duration_cast<std::chrono::nanoseconds>
        (time_end - time_start).count());
    }

    res_time /= ITERATIONS;

    return res_time / 1e9;
}


double time_mes_parallel(QString size, int threads)
{
    std::chrono::time_point<std::chrono::system_clock> time_start, time_end;
    double res_time = 0;

    for (int i = 0; i < ITERATIONS; i++)
    {
        time_start = std::chrono::system_clock::now();
        exec_parallel(size, threads);
        time_end = std::chrono::system_clock::now();

        res_time += (std::chrono::duration_cast<std::chrono::nanoseconds>
            (time_end - time_start).count());
    }

    res_time /= ITERATIONS;

    return res_time / 1e9;
}
