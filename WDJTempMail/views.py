from django.shortcuts import render,HttpResponse
from WDJApp.models import WDJTempMailContent,WDJTempMail
from Modules.utils import data,startMailServer,get_client_ip
from django.views.decorators.csrf import csrf_exempt
from json import dumps,loads



def saveMailContent(message):
    try:
        email = message['to'][0]['address']
        if (message['hasAttachments'] == True):
            attach = dumps(message['attachments'])
        else:
            attach = {}

        mail_id = WDJTempMail.objects.get(email=email)

        app = WDJTempMailContent(
            temp_mail_id = str(mail_id.mail_id),
            created_at = str(message['createdAt']),
            msgDownUrl = str(message['downloadUrl']),
            message_id = str(message['msgid']),
            mail_text = str(message['text']),
            mail_subject = str(message['subject']),
            mail_html = str(message['html']),
            from_side = dumps(message['from']),
            attachments = attach,
            cc_mails = dumps(message['cc']),
            bcc_mails = dumps(message['bcc']),
        )
        app.save()

    except Exception as e:
        print("Error: ",str(e))    
    
def temp_mail(req):
    try:
        data['title'] = "TempMail Home"
        mail_data = startMailServer(saveMailContent)
        add_mail = WDJTempMail(email=mail_data['email_id'],password=mail_data['password'],domain=mail_data['domain'],ip_addr=get_client_ip(req))
        add_mail.save()
        data['email'] = mail_data['email_id']   

    except Exception as e:
        print("Error in TM: ",str(e))
        data['error'] = "Mail Not Generated, refresh the page"

    return render(req,'temp_mail.html',context=data)

@csrf_exempt
def getIncomingMails(req):
    try:
        if (req.method == "POST"):
            jsonData = dict(loads(req.body))
            mail_id = WDJTempMail.objects.get(email=jsonData['email'])
            resultset = WDJTempMailContent.objects.filter(temp_mail=mail_id.mail_id).all()
            mail_content = []
            for mail in list(resultset):
                msg_id = str(mail.msgDownUrl).split("/")
                mail_content.append(
                    {
                        "mail_id":msg_id[2],
                        "subject":mail.mail_subject,
                    }
                )

            resJson = {
                "Status":"OK",
                "Message":"Data Fetched Successfully",
                "Data": mail_content
            }


    except Exception as e:
        resJson = {"Status":"ERROR","Message":"There is Something Wrong"}
        print(e)
        # data['showMsg'] = e

    return HttpResponse(dumps(resJson))


def getMailMessage(req,slug):
    msg_id = "/messages/{}/download".format(slug)
    rs = WDJTempMailContent.objects.get(msgDownUrl = msg_id)

    data['title'] = "Mail"
    data['subject'] = rs.mail_subject
    data['text'] = rs.mail_text
    data['html'] = str(rs.mail_html).replace("\\n","").replace("\\r","")

    return render(req,'tempmail_message.html',context=data)
    
