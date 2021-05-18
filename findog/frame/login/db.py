from frame.login.value import  Member
from frame.login.connect import Db
from frame.login.sql import Sql

class MemberDb(Db) :
    def insert(self, member_id, member_pwd, member_name, member_home, member_cellphone):
        try :
            conn = super().getConnection();
            print(conn)
            cursor = conn.cursor();
            cursor.execute(Sql.userinsert % (member_id, member_pwd, member_name, member_home, member_cellphone));
            conn.commit();
        except Exception as e :
            conn.rollback();
            print('예외발생', e);
            raise Exception;
        finally:
            super().close(conn, cursor);

    def selectid(self, member_id):
        conn = super().getConnection();
        cursor = conn.cursor()
        cursor.execute(Sql.selectid % member_id);
        m = cursor.fetchone();
        member = Member(m[0], m[1], m[2], m[3], m[4]);
        super().close(conn, cursor);
        return member;


