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
}
