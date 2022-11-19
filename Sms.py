import requests

key = "qqYaIprq4RZ25q9JENdRqQbKZ"
sender = "Xen"


def sendMsg(_msg, _to):
    url = f"https://apps.mnotify.net/smsapi?key={key}&to={_to}&msg={_msg}&sender_id={sender}"

    # Sending message
    try:
        requests.post(url)
        return "Message Sent"

    except:
        return "Network Connection lost"
