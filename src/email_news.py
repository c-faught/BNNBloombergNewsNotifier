import yagmail
import keyring

#keyring.set_password('yagmail', 'BNNBloombergNotifier', 'tr0llface')


yag = yagmail.SMTP('BNNBloombergNotifier', 'test')
contents = ["this is another","test"]
yag.send('faught.colin@gmail.com', 'test', contents)
