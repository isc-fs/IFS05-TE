

/*
This is a UI file (.ui.qml) that is intended to be edited in Qt Design Studio only.
It is supposed to be strictly declarative and only uses a subset of QML. If you edit
this file manually, you might introduce QML code that is not supported by Qt Design Studio.
Check out https://doc.qt.io/qtcreator/creator-quick-ui-forms.html for details on .ui.qml files.
*/
import QtQuick 6.4
import QtQuick.Controls 6.4
import UntitledProject1

Rectangle {
    id: rectangle
    width: 1240
    height: Constants.height
    visible: true
    color: "#1c1c1c"

    Rectangle {
        id: rectangle1
        x: 465
        y: 103
        width: 311
        height: 212
        color: "#2f2f2f"
        radius: 10
        border.color: "#efe919"
        border.width: 5
    }

    Rectangle {
        id: rectangle2
        x: 776
        y: 0
        width: 270
        height: 315
        color: "#2f2f2f"
        radius: 10
        border.color: "#cb0085"
        border.width: 5

        Rectangle {
            id: rectangle7
            x: 12
            y: 160
            width: 246
            height: 138
            color: "#f3ff00"
            radius: 10
            border.width: 0
        }

        Rectangle {
            id: rectangle8
            x: 12
            y: 16
            width: 246
            height: 138
            color: "#60ff00"
            radius: 10
            border.width: 0
        }
    }

    Rectangle {
        id: rectangle4
        x: 465
        y: 0
        width: 311
        height: 103
        color: "#2f2f2f"
        radius: 10
        border.color: "#0ccb00"
        border.width: 5
    }

    Rectangle {
        id: rectangle5
        x: 195
        y: 315
        width: 851
        height: 85
        color: "#2f2f2f"
        radius: 10
        border.color: "#e1c300"
        border.width: 5
    }

    Rectangle {
        id: rectangle3
        x: 195
        y: 0
        width: 270
        height: 315
        color: "#2f2f2f"
        radius: 10
        border.color: "#cb0085"
        border.width: 5

        Text {
            id: text4
            x: 592
            y: 17
            width: 246
            height: 138
            color: "#fcfcfc"
            text: qsTr("58")
            font.pixelSize: 65
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignVCenter
            wrapMode: Text.NoWrap
            style: Text.Outline
            font.weight: Font.ExtraBold
            font.bold: false
            styleColor: "#000000"
        }

        Text {
            id: text3
            x: 592
            y: 161
            width: 246
            height: 138
            color: "#fcfcfc"
            text: qsTr("62")
            font.pixelSize: 65
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignVCenter
            wrapMode: Text.NoWrap
            style: Text.Outline
            font.weight: Font.ExtraBold
            font.bold: false
            styleColor: "#000000"
        }

        Text {
            id: text5
            x: 12
            y: 17
            width: 246
            height: 138
            color: "#fcfcfc"
            text: qsTr("46")
            font.pixelSize: 50
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignVCenter
            wrapMode: Text.NoWrap
            style: Text.Outline
            font.weight: Font.ExtraBold
            font.bold: false
            styleColor: "#000000"
        }
    }

    Rectangle {
        id: rectangle9
        x: 207
        y: 160
        width: 246
        height: 138
        color: "#ff6b00"
        radius: 10
        border.width: 0
    }

    Text {
        id: text7
        x: 207
        y: 160
        width: 246
        height: 138
        color: "#fcfcfc"
        text: qsTr("71")
        font.pixelSize: 65
        horizontalAlignment: Text.AlignHCenter
        verticalAlignment: Text.AlignVCenter
        wrapMode: Text.NoWrap
        style: Text.Outline
        font.weight: Font.ExtraBold
        font.bold: false
        styleColor: "#000000"
    }

    Rectangle {
        id: rectangle10
        x: 207
        y: 16
        width: 246
        height: 138
        color: "#ff0000"
        radius: 10
        border.width: 0
    }

    Text {
        id: text6
        x: 207
        y: 16
        width: 246
        height: 138
        color: "#fcfcfc"
        text: qsTr("87")
        font.pixelSize: 70
        horizontalAlignment: Text.AlignHCenter
        verticalAlignment: Text.AlignVCenter
        wrapMode: Text.NoWrap
        style: Text.Outline
        font.weight: Font.ExtraBold
        font.bold: false
        styleColor: "#000000"
    }

    Text {
        id: text1
        x: 465
        y: 0
        width: 311
        height: 103
        color: "#25e100"
        text: qsTr("-0.120")
        font.pixelSize: 60
        horizontalAlignment: Text.AlignHCenter
        verticalAlignment: Text.AlignVCenter
        style: Text.Outline
        styleColor: "#000000"
        font.weight: Font.Bold
    }

    Text {
        id: text2
        x: 465
        y: 103
        width: 311
        height: 212
        color: "#ffe32a"
        text: qsTr("100")
        font.pixelSize: 110
        horizontalAlignment: Text.AlignHCenter
        verticalAlignment: Text.AlignVCenter
        style: Text.Outline
        font.weight: Font.Bold
        styleColor: "#000000"
    }

    Text {
        id: text8
        x: 821
        y: 16
        width: 180
        height: 138
        color: "#ffffff"
        text: qsTr("FR TEMP")
        font.pixelSize: 15
        horizontalAlignment: Text.AlignHCenter
        verticalAlignment: Text.AlignBottom
        style: Text.Outline
        font.weight: Font.Bold
    }

    Text {
        id: text9
        x: 821
        y: 160
        width: 180
        height: 138
        color: "#ffffff"
        text: qsTr("RR TEMP")
        font.pixelSize: 15
        horizontalAlignment: Text.AlignHCenter
        verticalAlignment: Text.AlignBottom
        style: Text.Outline
        font.weight: Font.Bold
    }

    Text {
        id: text10
        x: 240
        y: 16
        width: 180
        height: 138
        color: "#ffffff"
        text: qsTr("FL TEMP")
        font.pixelSize: 15
        horizontalAlignment: Text.AlignHCenter
        verticalAlignment: Text.AlignBottom
        style: Text.Outline
        font.weight: Font.Bold
    }

    Text {
        id: text11
        x: 240
        y: 160
        width: 180
        height: 138
        color: "#ffffff"
        text: qsTr("RL TEMP")
        font.pixelSize: 15
        horizontalAlignment: Text.AlignHCenter
        verticalAlignment: Text.AlignBottom
        style: Text.Outline
        font.weight: Font.Bold
    }

    Text {
        id: text12
        x: 530
        y: 0
        width: 180
        height: 103
        color: "#ffffff"
        text: qsTr("DELTA")
        font.pixelSize: 15
        horizontalAlignment: Text.AlignHCenter
        verticalAlignment: Text.AlignBottom
        style: Text.Outline
        font.weight: Font.Bold
    }

    Text {
        id: text13
        x: 530
        y: 109
        width: 180
        height: 200
        color: "#ffffff"
        text: qsTr("SPEED")
        font.pixelSize: 15
        horizontalAlignment: Text.AlignHCenter
        verticalAlignment: Text.AlignBottom
        style: Text.Outline
        font.weight: Font.Bold
    }

    Rectangle {
        id: rectangle6
        x: 195
        y: 315
        width: 564
        height: 85
        color: "#e1c300"
        radius: 10
    }

    Text {
        id: text14
        x: 471
        y: 314
        width: 311
        height: 85
        color: "#ffffff"
        text: qsTr("64%")
        font.pixelSize: 70
        horizontalAlignment: Text.AlignHCenter
        verticalAlignment: Text.AlignVCenter
        style: Text.Outline
        font.weight: Font.Bold
        styleColor: "#000000"
    }

    Text {
        id: text15
        x: 438
        y: 233
        width: 180
        height: 138
        color: "#ffffff"
        text: qsTr("SoC")
        font.pixelSize: 15
        horizontalAlignment: Text.AlignHCenter
        verticalAlignment: Text.AlignBottom
        style: Text.Outline
        font.weight: Font.Bold
    }

    states: [
        State {
            name: "clicked"
            when: button.checked
        }
    ]
}
