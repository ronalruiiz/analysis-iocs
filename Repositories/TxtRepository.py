import time
from progress.bar import Bar
from Services import IOCService

class TxtRepository:
    def output(self,query):
        f = open("result.txt", "a",encoding="utf-8")
        self.ouput_data(query,f.write)
        f.close()

    def ouput_data(self,query,write):
        count = open(query)
        print('\n')
        bar = Bar('Procesando', max=len(count.readlines()))
        count.close()
        for index,x in enumerate(open(query)):
            ioc = IOCService().getIOC(x,index)
            write("\n========================================\n")
            write('Indice: {0}\n'.format(str(ioc.item)))
            write('Value: {0}\n'.format(ioc.value.strip()))
            write('Nombre: {0} \n'.format(ioc.name)) 
            write('Tipo: {0}\n'.format(ioc.type))
            write("Reputación: {0}\n".format(ioc.reputation))    
            write("Detectado por: "+ioc.detection+"\n")
            write("Aplica: "+ioc.apply)
            write("\n========================================\n")
            time.sleep(0.1)
            bar.next()
        bar.finish()
        print('\n')