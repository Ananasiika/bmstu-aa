#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include "building.h"

#define PARALLEL 1
#define NO_PARALLEL 2

QT_BEGIN_NAMESPACE
namespace Ui { class MainWindow; }
QT_END_NAMESPACE

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    MainWindow(QWidget *parent = nullptr);
    ~MainWindow();

private slots:
    void on_exec_clicked();

    void read_parallel();

    void on_time_mes_btn_clicked();

    void on_time_mes_btn_r_clicked();

private:
    int type_parallel = 0;
    Ui::MainWindow *ui;
};
#endif // MAINWINDOW_H
