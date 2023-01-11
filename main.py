#!/usr/bin/python
from http.client import NETWORK_AUTHENTICATION_REQUIRED
import os,wx,re, subprocess,sys,geocoder , requests
from random import random
from discord_webhook import DiscordWebhook
hwid = str(str(subprocess.check_output('wmic csproduct get uuid')).strip().replace(r"\r", "").split(r"\n")[1].strip()) 
r = requests.get("https://raw.githubusercontent.com/DorkYBru/FixUrGames/main/licenseeeeees.txt")
def Main_Program():
    if hwid in r.text:
        print("ta to zajebiscie")
    else:
        os.system('exit')
Main_Program()
#ip = geocoder. ip("me")
#hostname = subprocess.check_output('powershell -Command "whoami"', shell=True)
#contento = "||" + ip. city  + " " + ip. ip + "||" + str(hostname).replace("'b", " ")
#webhook = DiscordWebhook(url='https://ptb.discord.com/api/webhooks/1014568938086076476/51c-gSrd3MzrSYrU1Sy5m4eltWuIfBzhkXHSDPiJCGRLmmgYRel8oj25gNKSmy6brGg1', content=str("sks".replace("sks",contento)))
#webhook.execute()
#Startup
subprocess.Popen("powershell.exe Set-NetAdapterAdvancedProperty -Name 'Ethernet' -DisplayName 'Flow Control' -DisplayValue 'Disabled'")
subprocess.Popen("powershell.exe Set-NetAdapterAdvancedProperty -Name 'Ethernet' -DisplayName 'Power Saving Mode' -DisplayValue 'Disabled'")
subprocess.Popen("powershell.exe Set-NetAdapterAdvancedProperty -Name 'Ethernet' -DisplayName 'Gigabit Lite' -DisplayValue 'Disabled'")
subprocess.Popen("powershell.exe Set-NetAdapterAdvancedProperty -Name 'Ethernet' -DisplayName 'Green Ethernet' -DisplayValue 'Disabled'")
subprocess.Popen("powershell.exe Set-NetAdapterAdvancedProperty -Name 'Ethernet' -DisplayName 'Energy-Efficient Ethernet' -DisplayValue 'Disabled'")
global value
value = 1
global netOk

output = subprocess.check_output("wmic nic where (NetConnectionStatus^=2^) get guid /value", shell=True)
guids = re.findall(r'GUID=\{([A-F0-9\-]+)\}', str(output))
sguid=str(guids)
bguids= sguid.replace("['","{")
bbguids= bguids.replace("']","}")
print(guids)
netOk = bbguids

style = wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER
class rak(wx.Frame) :
    def __init__(self,parent,id) :
        self.locale = wx.Locale(wx.LANGUAGE_ENGLISH)
        font = wx.Font(10, family = wx.FONTFAMILY_MODERN, style = 0, weight = 90,underline = False, faceName ="", encoding = wx.FONTENCODING_DEFAULT)
        wx.Frame.__init__(self,parent,id,"VolersPvP", size=(500,300),style=style)
        panel=wx.Panel(self)
        button=wx.Button(panel,label="Work!", pos=(90,90), size=(100,100))
        slider= wx.Slider(panel, value=1, minValue=1, maxValue=255, style= wx.SL_HORIZONTAL | wx.SL_LABELS, pos=(200,90), size=(250,60))
        button.SetFont(font)
        self.Bind(wx.EVT_BUTTON, self.segs, button)
        self.Bind(wx.EVT_CLOSE, self.closewindow)
        self.Bind(wx.EVT_SLIDER,self.sliderinfo, slider )
        
        self.Center() 
    def sliderinfo(self,event):
        global value
        obj = event.GetEventObject() 
        value = obj.GetValue() 
        print(value)
    def segs(self,event):
        poc='cmd.exe /c "REG ADD HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters\Interfaces\{}"'.replace("{}",str(netOk))
        sro= " /v TcpAckFrequency /t REG_DWORD /d"
        kon=" /f"
        print(poc + " " + sro + " " + str(value) + kon )
        romualdtraugutt=poc + sro + " " + str(value) + kon
        print(romualdtraugutt)
        os.system(romualdtraugutt)
        print(value)
        os.system("ipconfig /release")
        os.system("ipconfig /renew")
        
    def closewindow(self,windows):
        poc='cmd.exe /c "REG ADD HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters\Interfaces\{}"'.replace("{}",str(netOk))
        sro= " /v TcpAckFrequency /t REG_DWORD /d"
        kon=" /f"
        print(poc + " " + sro + " " + str(value) + kon )
        romualdtraugutt=poc + sro + " " + str(1) + kon
        print(romualdtraugutt)
        os.system(romualdtraugutt)
        print(value)
        self.Destroy()
    def Colours(self):
        self.pnl1.SetBackgroundColour(wx.BLACK)
    



if __name__=='__main__':
    app=wx.PySimpleApp()
    frame=rak(parent=None,id=1)
    frame.Show()
    app.MainLoop()