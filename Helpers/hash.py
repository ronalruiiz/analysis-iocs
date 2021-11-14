def detect_hash(hash):    
    algorithms={
        'MD5':'ae11fd697ec92c7c98de3fac23aba525',
        'SHA-256':'2c740d20dab7f14ec30510a11f8fd78b82bc3a711abe8a993acdb323e78e6d5e',
        'SHA-1':'4a1d4dbc1e193ec3ab2e9213876ceb8f4db72333'
    }

    for key in algorithms:
        if len(hash)==len(algorithms[key]) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
            return key

    return ""
