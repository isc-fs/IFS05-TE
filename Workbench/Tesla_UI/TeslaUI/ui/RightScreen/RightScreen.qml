import QtQuick 2.15
//import QtPositioning 5.15
//import QtLocation 5.15

Rectangle {
    id: rightScreen
    anchors {
        top: parent.top
        bottom: bottombar.top
        right: parent.right
    }

   // Plugin {
       // id: mapPlugin
       // name: "mapboxgl" // "mapboxgl", "esri", ...
        // specify plugin parameters if necessary
        // PluginParameter {
        //     name:
        //     value:
        // }

    Image {
        id: lockIcon
        anchors{
            left: parent.left
            top: parent.top
            margins: 20
        }

        width: parent.width / 40
        fillMode: Image.PreserveAspectFit
        source: ( systemHandler.carLocked ? "qrc:/ui/assets/lock.png" : "qrc:/ui/assets/unlock.png")

        MouseArea {
            anchors.fill: parent
            onClicked: systemHandler.setcarLocked(!systemHandler.carLocked)

        }


    }

    Text {
        id: dateTimeDisplay
        anchors {
            left: lockIcon.right
            leftMargin: 30
            bottom: lockIcon.bottom
        }

        font.pixelSize: 15
        font.bold: true
        color: "black"
        text: systemHandler.currentTime
    }

    Text {
        id: outdoorTemperatureDisplay
        anchors {
            left: dateTimeDisplay.right
            leftMargin: 30
            bottom: lockIcon.bottom
        }

        font.pixelSize: 15
        font.bold: true
        color: "black"
        text: systemHandler.outdoorTemp + "°C"
    }

    Text {
        id: userDislay
        anchors {
            left: outdoorTemperatureDisplay.right
            leftMargin: 30
            bottom: lockIcon.bottom
        }

        font.pixelSize: 15
        font.bold: true
        color: "black"
        text: systemHandler.userName
    }

    width: parent.width * 2/3
}
