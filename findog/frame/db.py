from frame.connect import Db
from frame.sql import Sql
from frame.value import lostdoglist


class lostdoglistDb(Db) :
    def selectall(self) :
        conn = super().getConnection();
        cursor = conn.cursor();
        cursor.execute(Sql.selectall)
        result = cursor.fetchall();
        all = [];
        for i in result :
            item = lostdoglist(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10])
            all.append(item);
        super().close(conn, cursor);
        return all;

    def selectbyid(self, i_dogid) :
        conn = super().getConnection();
        cursor = conn.cursor();
        cursor.execute(Sql.selectbyid % i_dogid);
        i = cursor.fetchone()
        item = lostdoglist(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10])
        super().close(conn, cursor);
        return item;



