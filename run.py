from app import create_app, socketio

app = create_app()

if __name__ == '__main__':
    # wth the help of socketio run app 
    socketio.run(app, debug=True)
