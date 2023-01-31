// main.cpp
#include <QApplication>
#include <QWidget>
#include <QVBoxLayout>
#include <QLabel>
#include <QPushButton>
#include <QTextEdit>
#include <QTimer>

class display : public QWidget {
    Q_OBJECT
  private:
    int velocidad;
    int potencia;
    int SoC;
    int FL_temp;
    int FR_temp;
    int RL_temp;
    int RR_temp;
    QLabel *velocidad_label;
    QLabel *potencia_label;
    QLabel *SoC_label;
    QLabel *FL_temp_label;
    QLabel *FR_temp_label;
    QLabel *RL_temp_label;
    QLabel *RR_temp_label;
    QTimer *timer;
    
  public:
    display() {
        velocidad = 0;
        potencia = 0;
        SoC = 100;
        FL_temp = 0;
        FR_temp = 0;
        RL_temp = 0;
        RR_temp = 0;
        velocidad_label = new QLabel("Velocidad: " + QString::number(velocidad) + " KM/H");
        potencia_label = new QLabel("Potencia: " + QString::number(potencia) + "KW");
        SoC_label = new QLabel("SoC: " + QString::number(SoC) + "%");
        FL_temp_label = new QLabel("FL_temp: " + QString::number(FL_temp));
        FR_temp_label = new QLabel("FR_temp: " + QString::number(FR_temp));
        RL_temp_label = new QLabel("RL_temp: " + QString::number(RL_temp));
        RR_temp_label = new QLabel("RR_temp: " + QString::number(RR_temp));

        QVBoxLayout *main_layout = new QVBoxLayout;
        main_layout->addWidget(velocidad_label);
        main_layout->addWidget(potencia_label);
        main_layout->addWidget(SoC_label);
        main_layout->addWidget(FL_temp_label);
        main_layout->addWidget(FR_temp_label);
        main_layout->addWidget(RL_temp_label);
        main_layout->addWidget(RR_temp_label);

        setLayout(main_layout);

        timer = new QTimer(this);
        connect(timer, &QTimer::timeout, this, &display::periodicUpdate);
        timer->start(10);
    }

    void updateVelocidad(int valor) {
        velocidad = valor;
        velocidad_label->setText("Velocidad: " + QString::number(velocidad) + " KM/H");
    }

    void updatePotencia(int valor) {
        potencia = valor;
        potencia_label->setText("Potencia: " + QString::number(potencia) + " KW");
    }

    void updateSoC(int valor) {
        SoC = valor;
        SoC_label->setText("SoC: " + QString::number(SoC) + "%");
    }

    void updateFL_temp(int valor) {
        FL_temp = valor;
        FL_temp_label->setText("FL_temp: " + QString::number(FL_temp));
    }

    void updateFR_temp(int valor) {
        FR_temp = valor;
        FR_temp_label->setText("FR_temp: " + QString::number(FR_temp));
    }

    void updateRL_temp(int valor) {
        RL_temp = valor;
        RL_temp_label->setText("RL_temp: " + QString::number(RL_temp));
    }

    void updateRR_temp(int valor) {
        RR_temp = valor;
        RR_temp_label->setText("RR_temp: " + QString::number(RR_temp));
    }

  public slots:
    void periodicUpdate() {
    // Aquí se coloca el código para actualizar los valores de los atributos
    // Puede ser una llamada a una API, una lectura de un sensor, etc.
        updateVelocidad(velocidad + 1);
        updatePotencia(potencia + 2);
        updateSoC(SoC - 1);
        updateFL_temp(FL_temp + 1);
        updateFR_temp(FR_temp + 2);
        updateRL_temp(RL_temp + 3);
        updateRR_temp(RR_temp + 4);
    }
};
