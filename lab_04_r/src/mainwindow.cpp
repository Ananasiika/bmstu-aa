#include "mainwindow.h"
#include "ui_mainwindow.h"

#include <QMessageBox>
#include <QFile>
#include <QTextStream>

MainWindow::MainWindow(QWidget *parent):
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::read_parallel()
{
    if (ui->no_parallel->isChecked())
    {
        type_parallel = NO_PARALLEL;
    }
    else if (ui->parallel->isChecked())
    {
        type_parallel = PARALLEL;
    }
}

void MainWindow::on_exec_clicked()
{
    read_parallel();

    if (ui->spinBox->text().toInt() % 100 != 0)
    {
        QMessageBox::critical(this, "Ошибка", "Не верно выбран размер файла");
        return;
    }
    if (type_parallel == 0)
    {
        QMessageBox::critical(this, "Ошибка", "Не выбран режим");
        return;
    }
    if (type_parallel == PARALLEL && ui->threads_entry->text() == "0")
    {
        QMessageBox::critical(this, "Ошибка", "Не выбрано количество потоков");
        return;
    }

    if (type_parallel == NO_PARALLEL)
        exec_no_parallel(ui->spinBox->text());
    else if (type_parallel == PARALLEL)
        exec_parallel(ui->spinBox->text(), ui->threads_entry->text().toInt());

}


void MainWindow::on_time_mes_btn_clicked()
{
    std::cout << "Размер   Время" << std::endl;
    for (int i = 100; i <= 1000; i += 100)
    {
        double res_time = time_mes_no_parallel(QString::number(i));
        std::cout << i << "   " << res_time << std::endl;
    }
}


void MainWindow::on_time_mes_btn_r_clicked()
{
//    if (ui->spinBox->text().toInt() % 100 != 0)
//    {
//        QMessageBox::critical(this, "Ошибка", "Не верно выбран размер файла");
//        return;
//    }
    for (int i = 800; i <= 1000; i += 100)
    {
        std::cout << "Размер файла = " << i << std::endl;
        std::cout << "Кол-во потоков   Время" << std::endl;
        for (int threads = 1; threads <= 8 * MAX_THREADS; threads *= 2)
        {
            double res_time = time_mes_parallel(QString::number(i), threads);
            std::cout << threads << "   " << res_time << std::endl;
        }
    }
//    for (int i = 100; i <= 1000; i += 100)
//    {
//        double res_time = time_mes_parallel(QString::number(i), 2);
//        std::cout << res_time << ", " << std::endl;
//    }

}
