import QtQuick
import QtQuick 2.15
import QtQuick.Window 2.15

Window {
    width: 1280
    height: 400
    visible: true
    title: qsTr("Driver Display")
    color: "black"

    Rectangle {
        id: inversor
        color: "transparent"
        border.color: "purple"
        border.width: 2
        radius: 8
        x: 40
        y: 91
        height: 123
        width: 123

        Text {
            anchors.centerIn: parent
            text: "INVERSOR"
            color: "white"
        }
    }

    Rectangle {
        id: baterias
        color: "transparent"
        border.color: "purple"
        border.width: 2
        radius: 8
        x: 165
        y: 91
        height: 123
        width: 123

        Text {
            anchors.centerIn: parent
            text: "BATERIAS"
            color: "white"
        }
    }

    Rectangle {
        id: motor
        color: "transparent"
        border.color: "purple"
        border.width: 2
        radius: 8
        x: 100
        y: 216
        height: 123
        width: 123

        Text {
            anchors.centerIn: parent
            text: "MOTOR"
            color: "white"
        }
    }

    Rectangle {
        id: velocidad
        color: "transparent"
        border.color: "white"
        border.width: 2
        radius: 8
        x: 500
        y: 50
        height: 250
        width: 250

        Text {
            anchors.centerIn: parent
            text: "VELOCIDAD"
            color: "white"
        }
    }

    Rectangle {
        id: fl
        color: "transparent"
        border.color: "red"
        border.width: 2
        radius: 8
        x: 372
        y: 50
        height: 123
        width: 123

        Text {
            anchors.centerIn: parent
            text: "FL"
            color: "white"
        }
    }

    Rectangle {
        id: rl
        color: "transparent"
        border.color: "orange"
        border.width: 2
        radius: 8
        x: 372
        y: 176
        height: 123
        width: 123

        Text {
            anchors.centerIn: parent
            text: "RL"
            color: "white"
        }
    }

    Rectangle {
        id: fr
        color: "transparent"
        border.color: "green"
        border.width: 2
        radius: 8
        x: 754
        y: 50
        height: 123
        width: 123

        Text {
            anchors.centerIn: parent
            text: "FR"
            color: "white"
        }
    }

    Rectangle {
        id: rr
        color: "transparent"
        border.color: "yellow"
        border.width: 2
        radius: 8
        x: 754
        y: 176
        height: 123
        width: 123

        Text {
            anchors.centerIn: parent
            text: "RR"
            color: "white"
        }
    }

    Rectangle {
        id: databar
        color: "transparent"
        border.color: "blue"
        border.width: 2
        radius: 8
        x: 373
        y: 315
        height: 70
        width: 505

        Text {
            anchors.centerIn: parent
            text: "DATA"
            color: "white"
        }
    }

    Rectangle {
        id: acelerador
        color: "transparent"
        border.color: "green"
        border.width: 2
        radius: 8
        x: 1000
        y: 50
        height: 320
        width: 70

        Text {
            anchors.centerIn: parent
            text: "ACELERADOR %"
            color: "white"
        }
    }

    Rectangle {
        id: freno
        color: "transparent"
        border.color: "red"
        border.width: 2
        radius: 8
        x: 1130
        y: 50
        height: 320
        width: 70

        Text {
            anchors.centerIn: parent
            text: "FRENO %"
            color: "white"
        }
    }

    /*Image {
        id: carRender
        x: 200
        y: 200
        height: 30
        width: 30
        fillMode: Image.PreserveAspectFit
        source: "qrc:/DisplayV5/ISCRacingTeam.png"
    }*/
}


