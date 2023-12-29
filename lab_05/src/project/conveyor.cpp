#include "conveyor.h"

Conveyor::Conveyor(const std::string& filename) : filename(filename){ }

void Conveyor::start()
{
    std::thread reader(&Conveyor::parse_linear, this, true);

    reader.join();
}

void Conveyor::log_linear(int task_num, int stage_num, std::function<void(std::string&)> func, bool is_print)
{
    std::chrono::time_point<std::chrono::system_clock> time_start, time_end;
    double start_res_time = time_now, res_time = 0;

    time_start = std::chrono::system_clock::now();
    std::string line;
    func(line);
    time_end = std::chrono::system_clock::now();

    res_time = (std::chrono::duration_cast<std::chrono::nanoseconds>(time_end - time_start).count()) / 1e9;

    time_now = start_res_time + res_time;

    if (is_print)
        printf("Task: %3d, Tape: %3d, Start: %.6f, End: %.6f\n",
                    task_num, stage_num, start_res_time, start_res_time + res_time);
}

void Conveyor::log_conveyor(int task_num, int stage_num, std::function<void(std::string&)> func, bool is_print)
{
    std::chrono::time_point<std::chrono::system_clock> time_start, time_end;
    double res_time = 0;
    double start_res_time = time_now;

    time_start = std::chrono::system_clock::now();
    std::string line;
    func(line);
    time_end = std::chrono::system_clock::now();

    res_time = (std::chrono::duration_cast<std::chrono::nanoseconds>(time_end - time_start).count()) / 1e9;

    time_now = start_res_time + res_time;

    if (stage_num == 1)
    {
        start_res_time = t1[task_num - 1];
        t1[task_num] = start_res_time + res_time;
        t2[task_num - 1] = t1[task_num];
    }
    else if (stage_num == 2)
    {
        start_res_time = t2[task_num - 1];
        t2[task_num] = start_res_time + res_time;
        t3[task_num - 1] = t2[task_num];
    }
    else if (stage_num == 3)
    {
        start_res_time = t3[task_num - 1];
    }

    if (is_print)
        printf("Task: %3d, Tape: %3d, Start: %.6f, End: %.6f\n",
                    task_num, stage_num, start_res_time, start_res_time + res_time);
}

void Conveyor::stage1_linear(int task_num, bool is_print)
{
    log_linear(task_num, 1, [this](std::string& filename) {
        std::ifstream inputFile(filename);
        std::string text((std::istreambuf_iterator<char>(inputFile)),
                         std::istreambuf_iterator<char>());

        std::unique_lock<std::mutex> lock(mtx);
        textQueue.push(text);
        lock.unlock();
        cv.notify_one(); // Уведомить о появлении новых данных в очереди
    }, is_print);
}

void Conveyor::stage2_linear(int task_num, bool is_print)
{
    log_linear(task_num, 2, [this](std::string& line) {
        m.lock();
        bool is_q2empty = textQueue.empty();  // Проверяем исходную очередь textQueue, а не lineQueue
        m.unlock();

        if (!is_q2empty)
        {
            m.lock();
            std::string text = textQueue.front();  // Получаем текст из очереди textQueue
            textQueue.pop();
            m.unlock();

            // Разделение текста на предложения и запись их в lineQueue
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

            // Записываем предложения в lineQueue
            for (const auto& sentence : sentences) {
                m.lock();
                lineQueue.push(sentence);
                m.unlock();
            }
        } }, is_print);
}


void callPythonScript(const std::string& filename_prep)
{
    std::string command = "python3 main.py " + filename_prep + " output.txt";
    std::system(command.c_str());
}

void Conveyor::stage3_linear(int task_num, bool is_print)
{
    log_linear(task_num, 3, [this](std::string& line) {
        std::ofstream outputFile("prep.txt", std::ios::out);

        while (!lineQueue.empty())
        {
            m.lock();
            std::string line = lineQueue.front();
            lineQueue.pop();
            m.unlock();
            outputFile << line << std::endl;
        }

        outputFile.close();
        callPythonScript("prep.txt"); }, is_print);
}

void Conveyor::parse_linear(bool is_print)
{
    std::cout << "Количество: 9" << std::endl;
    time_now = 0;
    for (int i = 0; i < 9; i++)
    {
        std::string line;
        stage1_linear(i + 1, is_print);
        stage2_linear(i + 1, is_print);
        stage3_linear(i + 1, is_print);
    }
}

void Conveyor::stage1_parallel(int task_num, bool is_print) {
    log_conveyor(task_num, 1, [this](std::string& filename) {
        std::ifstream inputFile(filename);
        std::string text((std::istreambuf_iterator<char>(inputFile)),
                         std::istreambuf_iterator<char>());

        std::unique_lock<std::mutex> lock(mtx);
        textQueue.push(text);
        lock.unlock();
        cv.notify_one(); // Уведомить о появлении новых данных в очереди
    }, is_print);
}

void Conveyor::stage2_parallel(int task_num, bool is_print) {
    log_conveyor(task_num, 2, [this](std::string& line) {
        m.lock();
        bool is_q2empty = textQueue.empty();  // Проверяем исходную очередь textQueue, а не lineQueue
        m.unlock();

        if (!is_q2empty)
        {
            m.lock();
            std::string text = textQueue.front();  // Получаем текст из очереди textQueue
            textQueue.pop();
            m.unlock();

            // Разделение текста на предложения и запись их в lineQueue
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

            // Записываем предложения в lineQueue
            for (const auto& sentence : sentences) {
                m.lock();
                lineQueue.push(sentence);
                m.unlock();
            }
        } }, is_print);
}

void Conveyor::stage3_parallel(int task_num, bool is_print) {
    log_conveyor(task_num, 3, [this](std::string& line) {
        std::ofstream outputFile("prep.txt", std::ios::out);

        while (!lineQueue.empty())
        {
            m.lock();
            std::string line = lineQueue.front();
            lineQueue.pop();
            m.unlock();
            outputFile << line << std::endl;
        }

        outputFile.close();
        callPythonScript("prep.txt"); }, is_print);
}

void Conveyor::run() {
    std::thread reader(&Conveyor::stage1_parallel, this, 1, true);
    std::thread splitter(&Conveyor::stage2_parallel, this, 1, true);
    std::thread scriptRunner(&Conveyor::stage3_parallel, this, 1, true);

    reader.join();
    splitter.join();
    scriptRunner.join();
}
