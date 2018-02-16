from pyspatialite import dbapi2 as db

class SqliteDB(object):

    __conn = db.Connection

    def __init__(self):
        pass

    @staticmethod
    def connect(self, file_name):
        try:
            self.__conn = db.connect(file_name)
        except:
            return 1
        else:
            return 0


if __name__ == "__main__":
    myConnection = SqliteDB
    myConnection.connect("~/code")