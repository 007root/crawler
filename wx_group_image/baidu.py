from aip import AipOcr


APP_ID = '1047'
API_KEY = 'UpVVnuSK4XbbpMgni'
SECRET_KEY = '2oO5G3HZUPoh8qdQ'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

def get_image_text(url):
    options = {
        "language_type": "CHN_ENG"
    }
    return client.basicGeneralUrl(url, options)
    
    

