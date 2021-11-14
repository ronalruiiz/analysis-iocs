import pandas as pd
from pandas import ExcelWriter
import time
from styleframe import StyleFrame, Styler, utils
from progress.bar import Bar
from Services import IOCService

class XlsRepository:
    
    def __init__(self):
        self.iocs = []

    def output(self,query):
        excel_writer = ExcelWriter('result.xlsx')
        self.ouput_data(query)
        df = pd.DataFrame([t.__dict__ for t in self.iocs])
        sf=StyleFrame(df)
        sf.apply_column_style(cols_to_style=df.columns,width=15,styler_obj=Styler(bg_color=utils.colors.white, bold=False, font=utils.fonts.calibri,font_size=10),style_header=True)
        sf.set_column_width(columns=['item'],width=10)
        sf.set_column_width(columns=['value'],width=68)
        sf.set_column_width(columns=['detection'],width=48)
        sf.to_excel(excel_writer,'IOCs',row_to_add_filters=0,index=False)
        excel_writer.save()

    def ouput_data(self,query):
        count = open(query)
        print('\n')
        bar = Bar('Procesando', max=len(count.readlines()))
        count.close()
        
        for index,x in enumerate(open(query)):
            self.iocs.append(IOCService().getIOC(x,index))
            time.sleep(0.1)
            bar.next()
        bar.finish()
        print('\n')