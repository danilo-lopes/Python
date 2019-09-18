# Criar um Script que monitore a cada 15 minutos os logs dos processos Linux e sejam
# gravados em um arquivo (dica: comando "ps")
# Crie um arquivo chamado: "monitor_process.log" em /var/log/

import subprocess
from write_log import write
import time


currentTime = time.ctime()
getTopMem = subprocess.getoutput('ps -eo pid,ppid,cmd,%cpu,%mem --sort=-%mem | head')
getTopCPU = subprocess.getoutput('ps -eo pid,ppid,cmd,%cpu,%mem --sort=-%cpu | head')

write(getTopMem, getTopCPU, currentTime)
