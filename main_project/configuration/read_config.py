import config
cfg = config.Config('configuration/jira.cfg')

def read_config():
    print('=== READ CONFIG ===')
    print(cfg.__dict__)
    if "username" not in cfg:
        print('ERROR: No username in config file')
        return None
    else:
        print('Username: ' + cfg['username'])
    if "url" not in cfg:
        print('ERROR: No url in config file')
        return
    else:
        print('URL: ' + cfg['url'])
    if "token" not in cfg:
        print('ERROR: No token in config file')
        return
    else:  
        print('Token: ' + cfg['token'])

    username = cfg['username']
    url = cfg['url']
    token = cfg['token']
    # port?
    return {
        'username': username,
        'url': url,
        'token': token
    }

if __name__ == '__main__':
    read_config()