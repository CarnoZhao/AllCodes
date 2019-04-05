def change(data):
    ret = data[:]
    if data[1] != data[2] and data[2] <= '12':
        ret[1], ret[2] = data[2], data[1]
    else:
        ret = None
    return ret
    
def check_dates(records):
    ret = [0, 0, 0]
    for rcd in records:
        pre = rcd[0].split('-')
        predata = [pre, change(pre)] if change(pre) != None else [pre]
        post = rcd[1].split('-')
        postdata = [post, change(post)] if change(post) != None else [post]
        orivalid = 1 if ''.join(pre) < ''.join(post) else 0
        valid = 0
        for pre in predata:
            pre = ''.join(pre)
            for post in postdata:
                post = ''.join(post)
                if pre <= post:
                    valid += 1
        if valid == 1 and orivalid == 1:
            ret[0] += 1
        elif valid == 1 and orivalid == 0:
            ret[1] += 1
        elif valid > 1:
            ret[2] += 1
    return ret

records = [
    ["2015-04-04", "2015-05-13"],  # correct
    ["2013-06-18", "2013-08-05"],  # correct
    ["2001-02-07", "2001-03-01"],  # correct
    ["2011-10-08", "2011-08-14"],  # recoverable
    ["2009-08-21", "2009-04-12"],  # recoverable
    ["1996-01-24", "1996-03-09"],  # uncertain
    ["2000-10-09", "2000-11-20"],  # uncertain
    ["2002-02-07", "2002-12-10"]]  # uncertain

print(check_dates(records))