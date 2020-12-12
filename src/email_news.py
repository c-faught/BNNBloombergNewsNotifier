import yagmail
import keyring

yag = yagmail.SMTP('BNNBloombergNotifier')
contents = ["this is another","test"]
yag.send('jimmy123@zippymail.info', 'test', contents)
