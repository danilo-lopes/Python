# Criar um Script que monitore a cada 15 minutos os logs dos processos Linux e sejam
# gravados em um arquivo (dica: comando "ps")


def write(getTopMem, getTopCPU, currentTime):

    with open('/var/log/monitor_process.log', 'a') as log:
        log.write('{}\n'.format(currentTime))
        log.write('\n\nMemória:\n\n{}\n\n CPU:\n\n{}\n\n'.format(getTopMem, getTopCPU))
