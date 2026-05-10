from app import create_app, socketio

app = create_app()

if __name__ == '__main__':
    # SocketIO vaprun app run kara (Real-time features sathi)
    socketio.run(app, debug=True)