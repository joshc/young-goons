# Helper functions for user module

import flask


def get_user_data(user_id):
    with flask.g.pymysql_db.cursor() as cursor:
        sql = 'SELECT user_id, username, email, profile_picture_path ' \
              'FROM tbl_user NATURAL JOIN' \
              '(SELECT * FROM tbl_user_info WHERE user_id = %s) tbl_user_info_id'
        cursor.execute(sql, (user_id, ))
        query_result = cursor.fetchall()

        if len(query_result) != 1:
            return None
            # return make_response(
            #     jsonify({'msg': 'Error fetching user info data'}), 400)

        user = {
            'userId': query_result[0][0],
            'username': query_result[0][1],
            'email': query_result[0][2],
            'profile_picture_path': query_result[0][3]
        }

        return user