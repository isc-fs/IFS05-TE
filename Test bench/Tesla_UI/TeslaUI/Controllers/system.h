#ifndef SYSTEM_H
#define SYSTEM_H

#include <QObject>
#include <QTimer>

class System : public QObject
{
    Q_OBJECT
    Q_PROPERTY(bool carLocked READ carLocked WRITE setcarLocked NOTIFY carLockedChanged)
    Q_PROPERTY(int outdoorTemp READ outdoorTemp WRITE setoutdoorTemp NOTIFY outdoorTempChanged)
    Q_PROPERTY(QString userName READ userName WRITE setuserName NOTIFY userNameChanged)
    Q_PROPERTY(QString currentTime READ currentTime WRITE setcurrentTime NOTIFY currentTimeChanged)


public:
    explicit System(QObject *parent = nullptr);

    bool carLocked() const;


    int outdoorTemp() const;


    QString userName() const;



    QString currentTime() const;


public slots: //setters y cualquier func que modifique un estado
        void setcarLocked(bool newCarLocked);
        void setoutdoorTemp(int newOutdoorTemp);
        void setuserName(const QString &newUserName);
        void setcurrentTime(const QString &newCurrentTime);
        void currentTimeTimerTimeout();

signals:

    void carLockedChanged();
    void outdoorTempChanged();

    void userNameChanged();

    void currentTimeChanged();

private:
    bool m_carLocked;
    int m_outdoorTemp;
    QString m_userName;
    QString m_currentTime;
    QTimer * m_currentTimeTimer;

};

#endif // SYSTEM_H
