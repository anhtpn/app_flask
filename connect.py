from mongoengine import connect

def config():
    connect(
        db='project1',
        host='mongodb+srv://anhndvnist:ducanh99@cluster0.znpcr.mongodb.net'
        # host='mongodb://127.0.0.1:27017'
    )