#!/usr/bin/env python3
import os
import time
msg='❗️ВОт так делать точно не стоит!'
title='❗️❗️✴️✴️✴️ U IS PWNED ❗️❗️'
for i in range(60):
    os.system('notify-send "'+title+'" "'+msg+'"')
    time.sleep(1)
