rooms = {
  'hall':{
    'desc':'Eski bir salon. Kuzeyde bir kapı, doğuda bir çalışma odası. Bir anahtar var.',
    'exits':{'north':'kitchen','east':'study'},
    'items':['key']
  },
  'kitchen':{
    'desc':'Karanlık bir mutfak. Batı duvarında kilitli bir kutu.',
    'exits':{'south':'hall'},
    'items':['box']
  },
  'study':{
    'desc':'Tozlu kitaplar ve bir mektup. Mektubu okuyabilirsin.',
    'exits':{'west':'hall'},
    'items':['letter']
  }
}
state={'room':'hall','inv':[],'box_open':False}
def look():
    r=rooms[state['room']]
    print(r['desc'])
    if r['items']:
        print('Etrafta:', ', '.join(r['items']))
def go(dir):
    r=rooms[state['room']]
    if dir in r['exits']:
        state['room']=r['exits'][dir]
        look()
    else:
        print('O tarafa gidemezsin.')
def take(item):
    r=rooms[state['room']]
    if item in r['items']:
        r['items'].remove(item)
        state['inv'].append(item)
        print(item, 'aldın.')
    else:
        print('Burada yok.')
def use(item):
    if item=='letter' and item in state['inv']:
        print('Mektup: "Kutu anahtarı salonda..."')
    elif item=='key' and state['room']=='kitchen' and 'box' in rooms['kitchen']['items']:
        rooms['kitchen']['items'].remove('box')
        state['box_open']=True
        print('Kutu açıldı! İçinden bir taş çıktı.')
        state['inv'].append('gem')
    else:
        print('Bir şey olmadı.')
def main():
    print('=== CAYTEN Text Adventure ===')
    look()
    while True:
        cmd=input('> ').strip().split()
        if not cmd: continue
        if cmd[0]=='look': look()
        elif cmd[0]=='go' and len(cmd)>1: go(cmd[1])
        elif cmd[0]=='take' and len(cmd)>1: take(cmd[1])
        elif cmd[0]=='use' and len(cmd)>1: use(cmd[1])
        elif cmd[0] in ('inv','bag'):
            print('Envanter:', ', '.join(state['inv']) or 'boş')
        elif cmd[0] in ('quit','exit'): break
        else: print('Komut: look | go <dir> | take <item> | use <item> | inv | quit')
if __name__=='__main__':
    main()
