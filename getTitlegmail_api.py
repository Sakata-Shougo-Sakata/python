from __future__ import print_function

import auth
from client import ApiClient
import util

# （認証）If modifying these scopes, delete the file token.pickle. 
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']
# Number of emails retrieved　（メールの最大取得件数）
MAIL_COUNTS = 5
# Search criteria　（検索条件）
SEARCH_CRITERIA = {
    'from': "",
    'to': "受信者メールアドレス",
    'subject': "メールの件名"
}
BASE_DIR = 'mail_box'


def build_search_criteria(query_dict):
    query_string = ''
    for key, value in query_dict.items():
        if value:
            query_string += key + ':' + value + ' '

    return query_string


#creds・・資格情報の管理
def main():
    creds = auth.authenticate(SCOPES)
    
    #検索条件
    query = build_search_criteria(SEARCH_CRITERIA)

    client = ApiClient(creds)
    messages = client.get_mail_list(MAIL_COUNTS, query)

    for message in messages:
        message_id = message['id']

    # get subject and message
    result = client.get_subject_message(message_id)

    # save file
    util.save_file(BASE_DIR, result)


if __name__ == '__main__':
    main()