import QtQuick 2.15

Rectangle {
    id: warning
    width: 185*1.5
    height: 212
    color: "transparent"
    border.color: "red"
    border.width: 1
    radius: 10
    opacity: 0
    visible: true

    Rectangle {
        id: warningInner
        x: 10*1.5
        y: 10
        width: 165*1.5
        height: 192
        color: "red"
        radius: 10
        opacity: 0
    }

    Text {
        x: (warning.width - warningText.width) / 2
        y: (warning.height - warningText.height) / 2
        id: warningText
        text: "WARNING"
        font.family: "Helvetica SemiBold"
        font.bold: true
        font.pixelSize: 30
        color: "white"
        opacity: 0
    }

    Timer {
        interval: 500
        running: true
        repeat: true
        onTriggered: {

            warningInner.opacity = 1 - warningInner.opacity
            warningText.opacity = 1 - warningText.opacity
            warning.opacity = 1 - warning.opacity

        }
    }
}

