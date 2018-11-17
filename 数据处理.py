import win32clipboard as w
import win32con
import os
import win32api

def setText(aString):  # 写入剪切板  
    w.OpenClipboard()
    w.EmptyClipboard()
    w.SetClipboardData(win32con.CF_TEXT, aString.encode('gbk'))
    w.CloseClipboard()


colors={}

colors["说"]="ffffff"
colors["喊"]="ff4040"
colors["队伍"]="82cdfc"
colors["公会"]="40ff40"
colors["系统"]="ffff00"
colors["世界"]="ffbaba"
colors["团队"]="ff7f00"
colors["团队警告"]=""
colors["密语"]="ff80ff"
colors["团长"]="ff4809"
colors["官员"]="40c040"
colors["拾取"]="00aa00"


colors["垃圾"]="9d9d9d"
colors["普通"]="ffffff"
colors["稀有"]="1eff00"
colors["精良"]="0070dd"
colors["史诗"]="a335ee"
colors["传说"]=""
colors["艾泽拉斯之心"]="e6cc80"
colors["传家宝"]="00ccff"


colors["DH"]="a330c9"
colors["DK"]="c41f3b"
colors["LR"]="abd473"
colors["XD"]="ff7d0a"
colors["FS"]="69ccf0"
colors["WS"]="00ff96"
colors["QS"]="f58cba"
colors["MS"]="ffffff"
colors["DZ"]="fff569"
colors["SM"]="0070de"
colors["SS"]="9482c9"
colors["ZS"]="c79c6e"






def getdata(line):
    x=list(line.split("###"))
    length=len(x)
    y='DEFAULT_CHAT_FRAME:AddMessage(("'   
    z='"):format('
    for i in range(length):
        if(i%2==0):
            y=y+'\\124cff'+colors[x[i]]+'%s\\124r'
        else:
            z=z+'"'+x[i].rstrip("\n")+'",'
    z=z.rstrip(",")
    return (y+z+'))')


if __name__=="__main__":
    try:
        File=open("剧本.txt")
        k=[]
        while 1:
            line = File.readline()
            if not line or line=="\n":
                break
            k.append(getdata(line))
        f="\n".join(k)
        setText(f)
        File.close()
    except:
        win32api.MessageBox(0,"剪切板数据错误,\n请重新复制","数据错误",win32con.MB_ICONWARNING)
    else:    
        win32api.MessageBox(0, "处理完成，\n请直接粘贴", "处理完成",win32con.MB_OK)

