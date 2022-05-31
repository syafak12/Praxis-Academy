import tornado
import motor

async def get_server_info():

    # replace this with your MongoDB connection string
    conn_str = "<your MongoDB Atlas connection string>"

    # set a 5-second connection timeout
    client = motor.motor_tornado.MotorClient(conn_str, serverSelectionTimeoutMS=5000)

    try:
        print(await client.server_info())
    except Exception:
        print("Unable to connect to the server.")

tornado.ioloop.IOLoop.current().run_sync(get_server_info)