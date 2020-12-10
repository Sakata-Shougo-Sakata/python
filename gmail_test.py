import httplib2, os
from apiclient import discovery
import gmail_auth # 先ほど作成したプログラム
class GmailAPI:
	# Gmailのサービスを取得
	def gmail_get_service(self):
		# ユーザー認証の取得
		credentials = gmail_auth.gmail_user_auth()
		http = credentials.authorize(httplib2.Http())
		# GmailのAPIを利用する
		service = discovery.build('gmail', 'v1', http=http)
		return service
	# メッセージの一覧を取得		
	def GetMessageList(self,DateFrom,DateTo):
		#APIに接続
		service = self.gmail_get_service()
		MessageList = []
		query = ''
		# 検索用クエリを指定する
		if DateFrom != None and DateFrom !="":
			query += 'after:' + DateFrom + ' '
		if DateTo != None  and DateTo !="":
			query += 'before:' + DateTo + ' '
		# if MessageFrom != None and MessageFrom !="":
		# 	query += 'From:' + MessageFrom + ' '
		# メールIDの一覧を取得する(最大100件)テストで10件
		messageIDlist = service.users().messages().list(userId='me',maxResults=10,q=query).execute()
		#該当するメールが存在しない場合は、処理中断
		if messageIDlist['resultSizeEstimate'] == 0: 
			print("Message is not found")
			return MessageList
		#メッセージIDを元に、メールの詳細情報を取得
		for message in messageIDlist['messages']:
			row = {}
			row['ID'] = message['id']
			MessageDetail = service.users().messages().get(userId='me',id=message['id']).execute()
			for header in MessageDetail['payload']['headers']:
				#日付、送信元、件名を取得する
				if header['name'] == 'Date':
					row['Date'] = header['value'] 
				elif header['name'] == 'From':
					row['From'] = header['value']
				elif header['name'] == 'Subject':
					row['Subject'] = header['value']
			MessageList.append(row)
		return MessageList



 # メッセージの取得を実行
if __name__ == '__main__':
	test = GmailAPI()
	#パラメータは、任意の値を指定する
	messages = test.GetMessageList(DateFrom='2020-12-01',DateTo='2020-12-02')
	#結果を出力
	for message in messages:
		print(message)
		print(type(message))
	print(type(messages))


    for messages in Messagelist['from']== Messagelist['ID']:  #繰り返して、取得した件名を持ってくる。
    　　　if 'cct案件' in messages          #その中の上で取得したメッセージ（MessageList）のなかに入っている件名の中から、'CCT案件'と書いてあるものを取得してくる
            MessageNameList.append(row)   # idと案件名を取得してどこかに保持する
    return  MessageNameList #MessageListを返す

    #上記の『MessageNameList』のなかに入っている『id』と一致する案件情報を取得
    for  MessageIDList    
    
    if MessageIDList


    #メッセージの中身を取得し、特定の文字列が入っているものを取得する。