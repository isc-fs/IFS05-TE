import QtQuick 2.15

Rectangle{
    id: dashboard
    anchors.fill: parent
    color: "#191a1e"

    Item {
        id: components

        Warning{
           x: 40*1.5
           y: 103
        }

        Inverter{
            x: 265*1.5
            y: 7
        }

        Accumulator{
            x: 465*1.5
            y: 7
        }

        Engine{
            x: 781*1.5
            y: 7

        }

        LeftTires{
            x: 265*1.5
            y: 103
        }

        Speed{
            x: 465*1.5
            y: 103
        }

        RightTires{
            x: 781*1.5
            y: 105
        }

        Soc{
            x: 265*1.5
            y: 325

        }

        Brake{
            x: 1050*1.5
            y: 40
        }

        Throttle{
            x: 1150*1.5
            y: 40
        }


    }

}

