import QtQuick 2.15

Rectangle {
    id: leftScreen
    anchors {
        top: parent.top
        bottom: bottombar.top
        right: rightscreen.left
        left: parent.left
    }

    color: "white"

    Image {
        id: carRender
        anchors.centerIn: parent
        width: parent.width * .9
        fillMode: Image.PreserveAspectFit
        source: "qrc:/ui/assets/carRender.png"
    }

}

