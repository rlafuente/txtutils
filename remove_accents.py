
def strip_accents(s):
    '''Returns the input string with portuguese accents and cedillas removed
    (replaced by unaccented characters).'''
    import unicodedata, re
    if not type(s) == unicode:
        new_s = str(s)
        new_s = new_s.decode('UTF-8')
        new_s = ''.join((c for c in unicodedata.normalize('NFD', new_s) if unicodedata.category(c) != 'Mn'))
        return new_s.encode('UTF-8')
    else:
        s = re.sub(re.compile(ur'\xe1|\xe0|\xe2|\xe3', re.UNICODE), 'a', s)
        s = re.sub(re.compile(ur'\xe9|\xe8|\xea',      re.UNICODE), 'e', s)
        s = re.sub(re.compile(ur'\xec|\xed',           re.UNICODE), 'i', s)
        s = re.sub(re.compile(ur'\xf3|\xf2|\xf4|\xf5', re.UNICODE), 'o', s)
        s = re.sub(re.compile(ur'\xfa|\xf9',           re.UNICODE), 'u', s)
        s = re.sub(re.compile(ur'\xe7',                re.UNICODE), 'c', s)
        s = re.sub(re.compile(ur'\xc1|\xc0|\xc2|\xc3', re.UNICODE), 'A', s)
        s = re.sub(re.compile(ur'\xc9|\xc8|\xca',      re.UNICODE), 'E', s)
        s = re.sub(re.compile(ur'\xcc|\xcd',           re.UNICODE), 'I', s)
        s = re.sub(re.compile(ur'\xd2|\xd3|\xd4|\xd5', re.UNICODE), 'O', s)
        s = re.sub(re.compile(ur'\xda|\xd9',           re.UNICODE), 'U', s)
        s = re.sub(re.compile(ur'\xc7',                re.UNICODE), 'C', s)
        return s
