import QtQuick
import QtQuick 2.15
import QtQuick.Window 2.15
import "Components"

Window {
    width: 1280
    height: 400
    visible: true
    title: qsTr("Driver Display")
    color: "white"

    Rectangle {
        id: bottomBar1
        color: "white"
        border.color: "black"
        x: 60
        y: 40
        height: 82
        width: 242

        Text {
            anchors.centerIn: parent
            text: "INVERSOR"
        }
    }

    Rectangle {
        id: bottomBar2
        color: "white"
        border.color: "black"
        x: 60
        y: 160
        height: 82
        width: 242

        Text {
            //anchors.horizontalCenter: parent
            anchors.centerIn: parent
            text: "MOTOR"
        }
    }
    Rectangle {
        id: bottomBar3
        color: "white"
        border.color: "black"
        x: 60
        y: 280
        height: 82
        width: 242

        Text {
            anchors.centerIn: parent
            text: "BATERIA"
        }
    }

    Components {
        id: components
    }
}


