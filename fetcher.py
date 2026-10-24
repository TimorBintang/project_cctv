import requests

def check_cctv_url(url):
    http_status,size,indikasi = 0,0,"TIMEOUT/OFFLINE"

    try:
        resp = requests.get(url,timeout=5)
        http_status,size = resp.status_code, len(resp.content)

        if http_status != 200:
            indikasi = "ERROR SERVER"
        elif size <= 500:
            indikasi = "ANOMALI/BURIK"
        else:
            indikasi = "NORMAL"

    except requests.RequestException:
        pass

    return http_status,size,indikasi