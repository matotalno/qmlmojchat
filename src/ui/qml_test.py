import sys
import os
import asyncio
import logging
from pathlib import Path
from PySide6.QtWidgets import QApplication
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtCore import QUrl
from PySide6.QtQuickControls2 import QQuickStyle
import qasync

# Dodajemo root direktorijum u PYTHONPATH
root_dir = str(Path(__file__).parent.parent.parent)
sys.path.append(root_dir)

from src.ui.chat_bridge import QMLBridge

# Postavljanje logginga
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def main():
    try:
        # Inicijalizacija aplikacije
        app = QApplication(sys.argv)
        QQuickStyle.setStyle("Basic")
        
        # Event loop setup
        loop = qasync.QEventLoop(app)
        asyncio.set_event_loop(loop)
        
        # Dodaj exception handler za event loop
        def handle_exception(loop, context):
            logger.error("Exception in event loop!")
            logger.error(f"Context: {context}")
            if 'exception' in context:
                logger.error(f"Exception details:", exc_info=context['exception'])
        
        loop.set_exception_handler(handle_exception)
        
        # QML Engine setup
        engine = QQmlApplicationEngine()
        bridge = QMLBridge(loop)
        
        # Postavljanje context properties
        engine.rootContext().setContextProperty("chatBridge", bridge)
        engine.rootContext().setContextProperty("chatModel", bridge.chat_model)
        engine.rootContext().setContextProperty("sessionModel", bridge.session_model)

        # Učitavanje QML fajla
        qml_file = os.path.join(os.path.dirname(__file__), "qml", "ChatView.qml")
        engine.load(QUrl.fromLocalFile(qml_file))
        
        # Proveri da li je QML učitan
        if not engine.rootObjects():
            logger.error("Failed to load QML!")
            return -1
            
        logger.debug("QML loaded successfully")
        logger.debug(f"Event loop status: {loop.is_running()}")

        # Pokretanje event loop-a
        with loop:
            loop.run_forever()
            
        return 0

    except Exception as e:
        logger.error(f"Greška u main funkciji: {e}", exc_info=True)
        return 1

if __name__ == "__main__":
    sys.exit(main())
