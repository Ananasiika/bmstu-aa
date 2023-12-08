#ifndef BUILDING_H
#define BUILDING_H

#include <ui_mainwindow.h>
#include <math.h>

#include <thread>
#include <mutex>
#include <vector>
#include <chrono>
#include <ctime>

#include <iostream>

#define ITERATIONS 5
#define MAX_THREADS 4

void exec_no_parallel(QString size);
void exec_parallel(QString size, int threads);
double time_mes_no_parallel(QString size);
double time_mes_parallel(QString size, int threads);

#endif
