from database.DB_connect import DBConnect


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getAnni():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT YEAR(s.`datetime`) as year, count(*) as sum
FROM sighting s 
WHERE s.country = 'us' 
group by YEAR(s.`datetime`) 
order by YEAR(s.`datetime`)"""

        cursor.execute(query)

        for row in cursor:
            result.append((row["year"], row["sum"]))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getNodes(anno):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT DISTINCT s.state 
                    FROM sighting s 
                    WHERE s.country = 'us'
                    and YEAR(s.`datetime`)=%s
                    ORDER by s.state """

        cursor.execute(query,(anno,))

        for row in cursor:
            result.append(row["state"])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getData(anno,n):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT s.`datetime` as data
FROM sighting s 
WHERE s.state = %s
and YEAR (s.`datetime`) = %s
order by s.`datetime` ASC  """

        cursor.execute(query, (n,anno,))

        for row in cursor:
            result.append(row["data"])

        cursor.close()
        conn.close()
        return result