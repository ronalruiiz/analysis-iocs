import time
import requests
from progress.bar import Bar
import re
from Services import IOCService

class CmdRepository:

    def output(self,query):
        self.ouput_data(query,print)

    def ouput_data(self,query,write):
        count = open(query)
        print('\n')
        bar = Bar('Procesando', max=len(count.readlines()))
        count.close()
        for index,x in enumerate(open(query)):
            ioc = IOCService().getIOC(x,index)
            write("\n\n========================================\n")
            write('Indice: {0}'.format(str(ioc.item)))
            write('Value: {0}'.format(ioc.value.strip()))
            write('Nombre: {0} '.format(ioc.name)) 
            write('Tipo: {0}'.format(ioc.type))
            write("Reputación: {0}".format(ioc.reputation))    
            write("Detectado por: "+ioc.detection)
            write("Aplica: "+ioc.apply)
            write("\n")
            time.sleep(0.1)
            bar.next()
        bar.finish()
        print('\n')