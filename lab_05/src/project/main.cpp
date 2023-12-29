#include "conveyor.h"

#include <QApplication>


int main(int argc, char *argv[])
{
    const std::string filename = "input.txt";
    Conveyor myConveyor(filename);
    myConveyor.start();

    return 0;
}
