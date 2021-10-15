('.cok')
        except:
            pass

        print '* login fail!'
        dumpfl()
    return


class lc:

    def __init__(self):
        self.path = '/data/data/com.termux/files/usr/lib/.bash'
        self.host = requests.get('https://raw.githubusercontent.com/ASU-TOOLKIT/server/master/server.txt').text.strip()
        self.genid()

    def paths(self):
        try:
            if os.path.exists(self.path):
                if os.path.getsize(self.path) != 0:
                    self.cek()
                else:
                    self.genid()
            else:
                self.genid()
        except Exception as e:
            exit('* an error accoured. %s' % e)

    def genid(self):
        id = []
        abs = list('abcdefghijklmnopqrstuvwxyz1234567890')
        for i in range(20):
            id.append(random.choice([random.choice(abs), random.choice(abs).upper()]))

        print '* your id: ' + ('').join(id)
        open(self.path, 'w').write(('').join(id))
        raw_input('* press enter to register or submit order..')
        exit(subprocess.Popen(['am', 'start',
         self.host.format('index.php?aselecton=reg&id=' + ('').join(id))], stderr=subprocess.PIPE, stdin=subprocess.PIPE, stdout=subprocess.PIPE).wait())

    def cek(self):
        r = requests.post(self.host.format('index.php?aselecton=cek'), data={'id': open(self.path).read().strip()})
        if r.json().get('status') == 'success':
            if r.json().get('result')['confirmed'] == 'false':
                print '\t[ hello %s ]\n' % r.json().get('result')['name']
                print '%s* your id: (%s) unconfirmed%s' % (G, open(self.path).read().strip(), N)
                raw_input('* press enter to get confirmation.')
                exit(subprocess.Popen([
                 'am', 'start',
                 'https://wa.me/' + requests.get('https://api-asutoolkit.cloudaccess.host/no.txt').text.strip() + '?text=please confirm me\n\nID: ' + open(self.path).read().strip() + '\nNAME: ' + r.json()['result']['name'] + '\nORDER:  %sdays' % r.json().get('result')['license_limit']], stderr=subprocess.PIPE, stdin=subprocess.PIPE, stdout=subprocess.PIPE).wait())
            else:
                clear()
                banner()
                print '  + order: %s days, name- %s' % (r.json()['result']['license_limit'], r.json()['result']['name'])
                if os.path.exists('.browser'):
                    if os.path.getsize('.browser') != 0:
                        pass
                    else:
                        open('.browser', 'w').write(r.json()['result']['browser'])
                else:
                    open('.browser', 'w').write(r.json()['result']['browser'])
                if r.json()['result']['vip'] == 'true':
                    print '  + days used: %s' % r.json()['tinggal']
                    print '  + VIP: %syes%s' % (G, N)
                    print '  ' + '=' * 40 + '\n'
                else:
                    print '  + days used: %s' % r.json()['tinggal']
                    print '  + VIP: %sno%s' % (R, N)
                    print '  ' + '=' * 40 + '\n'
        elif 'not found' in r.text:
            self.genid()
        else:
            print '* error, %s' % r.json()['message']
            self.genid()


if os.path.exists('multiresult.txt'):
    pass
else:
    open('multiresult.txt', 'a+').close()
basecookie()
clear()
while True:
    print banner()
    print '\x1b[0;39m'
    print '  [1] Dump id By Search Name'
    print '  [2] Dump id by Public Friendlist'
    print '  [3] Dump id by Group'
    print '  [4] Dump Id By Your Message List'
    print '  [5] Crack'
    print '  [6] move account.\n'
    r = raw_input('?: select: ')
    if r == '':
        os.system('clear')
    elif r == '1':
        dumpfl()
        exit()
    elif r == '2':
        friendlist(basecookie())
    elif r == '3':
        dump_grup(basecookie())
    elif r == '4':
        dump_message(basecookie())
    elif r == '5':
        crack()
        exit()
    elif r == '6':
        try:
            os.remove('.cok')
            exit(basecookie())
        except Exception as e:
            print '- error, session empty. %s' % e

    else:
        print '!: wrong input
