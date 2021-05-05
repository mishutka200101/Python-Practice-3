llst = ['а','б','в','г','д','е','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я']
blst = ['А','Б','В','Г','Д','Е','Ж','З','И','Й','К','Л','М','Н','О','П','Р','С','Т','У','Ф','Х','Ц','Ч','Ш','Щ','Ъ','Ы','Ь','Э','Ю','Я']
 
 
def encrypt_caesar(msg, shift=3):
    ret = ""
    for x in msg:
        if x in llst:
            ind = llst.index(x)
            ret += llst[ind+shift]
        elif x in blst:
            ind = blst.index(x)
            ret += blst[ind+shift]
        else:
            ret += x
    return ret
 
def decrypt_caesar(msg, shift=3):
    ret = ""
    for x in msg:
        if x in llst:
            ind = llst.index(x)
            ret += llst[ind-shift]
        elif x in blst:
            ind = blst.index(x)
            ret += blst[ind-shift]
        else:
            ret += x
    return ret
