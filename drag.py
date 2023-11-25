def mousePressEvent(self, event):
    self.dragPos = event.globalPosition().toPoint()


def mouseMoveEvent(self, event):
    self.move(self.pos() + event.globalPosition().toPoint() - self.dragPos)
    self.dragPos = event.globalPosition().toPoint()
    event.accept()
