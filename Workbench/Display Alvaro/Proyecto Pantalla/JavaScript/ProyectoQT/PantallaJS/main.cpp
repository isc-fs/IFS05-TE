#include "display.h"
#include <QApplication>
#include <QLocale>
#include <QTranslator>

int main(int argc, char *argv[]) {
    QApplication a(argc, argv);
    Display display;
    display.show();
    return a.exec();
}
