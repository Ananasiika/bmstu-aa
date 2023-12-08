#include "mainwindow.h"

#include <QApplication>


int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    MainWindow w;
    w.setWindowTitle("Построение деревьев синтаксических зависимостей текстов");
    w.show();

    return a.exec();
}
