import QtQuick 2.15

Rectangle {
    id: speed
    width: 311*1.5
    height: 212
    color: "transparent"
    border.color: "#FBBB1C"
    border.width: 1
    radius: 10

     property real speedValue: 133

    Text {
            id: speedText
            text: Math.round(speedValue)
            font.family: "Helvetica SemiBold"
            font.pixelSize: 180
            color: "white"
            anchors.horizontalCenter: speed.horizontalCenter
            anchors.verticalCenter: speed.verticalCenter
        }

}
