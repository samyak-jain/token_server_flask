from flask import Flask
from flask import request
import time

from agora_token.RtcTokenBuilder import RtcTokenBuilder, Role_Publisher
from agora_token.RtmTokenBuilder import RtmTokenBuilder, Role_Rtm_User

app = Flask(__name__)

appID = "970CA35de60c44645bbae8a215061b33"
appCertificate = "5CFd2fd1755d40ecb72977518be15d3b"

@app.route('/rtc')
def rtc_token():
    channelName: str = request.args.get('channel', type=str)
    uid: int = request.args.get('uid', type=int)
    expireTimeInSeconds: int = request.args.get('expire', type=int)
    currentTimestamp = int(time.time())
    privilegeExpiredTs = currentTimestamp + expireTimeInSeconds
    tokenString: str = RtcTokenBuilder.buildTokenWithUid(appID, appCertificate, channelName, uid, Role_Publisher, privilegeExpiredTs)

    return tokenString


@app.route('/rtc_user_account')
def rtc_token_with_user_account():
    channelName: str = request.args.get('channel', type=str)
    userAccount:str = request.args.get('user_account', type=str)
    expireTimeInSeconds: int = request.args.get('expire', type=int)
    currentTimestamp = int(time.time())
    privilegeExpiredTs = currentTimestamp + expireTimeInSeconds
    tokenString: str = RtcTokenBuilder.buildTokenWithAccount(appID, appCertificate, channelName, userAccount, Role_Publisher, privilegeExpiredTs)

    return tokenString


@app.route('/rtm')
def rtm_token():
    user: str = request.args.get('user', type=str)
    tokenString = RtmTokenBuilder.buildToken(appID, appCertificate, user, Role_Rtm_User, privilegeExpiredTs)


