import QtQuick 2.15
import QtQuick.Window 2.15
import "ui/BottomBar"
import "ui/RightScreen"
import "ui/LeftScreen"

Window {
    width: 1920
    height: 480
    visible: true
    title: qsTr("Tesla Model 3 UI")


    BottomBar {
        id: bottombar

    }

    RightScreen {
        id: rightscreen

    }

    LeftScreen {
        id: leftscreen
    }
}
