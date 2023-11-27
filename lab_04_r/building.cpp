#include "building.h"
#include <QProcess>
#include <QDebug>
#include <QtConcurrent/QtConcurrent>
#include <QFile>
#include <QTextStream>

void exec_no_parallel(QString size)
{
    QString command = "python3 ./main.py data/input_" + size + "kb.txt ./result/no_" + size + "output.txt"; // Команда для выполнения скрипта

    system(command.toLatin1().constData());
}

void executeCommand(const QString& command) {
    system(command.toLatin1().constData());
}

void exec_parallel(QString size, int threads_count)
{
    QString filename = "data/input_" + size + "kb.txt";
    QFile file(filename);

    if (!file.open(QIODevice::ReadOnly | QIODevice::Text)) {
        qDebug() << "Failed to open input file:" << filename;
        return;
    }

    QTextStream in(&file);
    QString text = in.readAll();
    file.close();
    int textLength = text.length();
    int partLength = textLength / threads_count;

    for (int i = 0; i < threads_count; ++i) {
        QString part = text.mid(i * partLength, partLength);
        QString partFile = "data/parts/part_" + size + "kb_" + QString::number(i) + ".txt";
        QFile partFileObj(partFile);

        if (!partFileObj.open(QIODevice::WriteOnly | QIODevice::Text)) {
            qDebug() << "Failed to open part file:" << partFile;
            continue;
        }

        QTextStream out(&partFileObj);
        out << part;
        partFileObj.close();
    }

    std::vector<std::thread> threads;

    for (int i = 0; i < threads_count; ++i) {
        QString command = "python3 ./main.py data/parts/part_" + size + "kb_" + QString::number(i) + ".txt ./result/" + size + "output.txt";
        threads.push_back(std::thread(executeCommand, command));
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
