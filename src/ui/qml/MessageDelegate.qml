import QtQuick 2.15
import QtQuick.Controls 2.15

Rectangle {
    id: messageRoot
    width: ListView.view ? ListView.view.width : implicitWidth
    height: contentColumn.height
    color: model.isUser ? "#ffffff" : "#f7f7f8"

    Column {
        id: contentColumn
        width: parent.width
        spacing: 8
        topPadding: 16
        bottomPadding: 16

        Rectangle {
            width: parent.width
            height: messageContent.height
            color: "transparent"
            
            Item {
                id: messageContent
                width: parent.width - 48  // 24px padding sa obe strane
                height: messageColumn.height + 8
                anchors.horizontalCenter: parent.horizontalCenter

                Rectangle {
                    id: avatar
                    width: 30
                    height: 30
                    radius: 15
                    color: model.isUser ? "#007AFF" : "#19c37d"
                    anchors {
                        left: model.isUser ? undefined : parent.left
                        right: model.isUser ? parent.right : undefined
                        top: parent.top
                    }

                    Text {
                        anchors.centerIn: parent
                        text: model.isUser ? "Vi" : "AI"
                        color: "white"
                        font.pixelSize: 12
                    }
                }

                Column {
                    id: messageColumn
                    width: parent.width - 46
                    spacing: 4
                    anchors {
                        left: model.isUser ? undefined : avatar.right
                        right: model.isUser ? avatar.left : undefined
                        leftMargin: model.isUser ? 0 : 16
                        rightMargin: model.isUser ? 16 : 0
                        top: parent.top
                    }

                    Text {
                        width: parent.width
                        text: model.message
                        wrapMode: Text.Wrap
                        color: "#374151"
                        font.pixelSize: 16
                        lineHeight: 1.5
                    }

                    Text {
                        visible: model.isUser
                        text: model.timestamp
                        color: "#6B7280"
                        font.pixelSize: 12
                    }
                }
            }
        }
    }

    // Uklanjamo hover akcije za sada dok ne dodamo ikonice
    /*HoverHandler {
        id: messageHovered
    }*/
}
