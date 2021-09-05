#!/usr/bin/python3
# -*- coding: utf-8 -*-
# pylint: disable=R,C0330,C0301,C0303
import argparse
import sys
import time
import os
from Repositories import TxtRepository
from Repositories import XlsRepository
from Repositories import CmdRepository
import logging
from dotenv import load_dotenv

load_dotenv()

def verify_type(query,type):
    controllers_output = None
    ouput = {
        "xls": lambda value: XlsRepository().output(value),
        "txt":lambda value: TxtRepository().output(value),
        "cmd": lambda value: CmdRepository().output(value),
    }
    ouput.get(type)(query)

def main():
    parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,description='''\
        ___                ___                     ________  _______      
       /   |  ____  ____ _/ (_)___  ____ ______   /  _/ __ \/ ____( )_____
      / /| | / __ \/ __ `/ / /_  / / __ `/ ___/   / // / / / /    |// ___/
     / ___ |/ / / / /_/ / / / / /_/ /_/ / /     _/ // /_/ / /___   (__  ) 
    /_/  |_/_/ /_/\__,_/_/_/ /___/\__,_/_/     /___/\____/\____/  /____/  by:@ronalruiiz
                                                                          
    ''',conflict_handler="resolve")
    parser.add_argument("-h",'--help' ,action="help", help="Menú de ayuda.")
    parser.add_argument(
        "-o",
        "--output",
        required=True,
        type=str,
        dest="ouput",
        metavar="",
        help="Salida en archivo [txt,xls y cmd]"
    );

    parser.add_argument(
        "-f",
        "--file",
        required=True,
        type=str,
        dest="file",
        metavar="",
        help="Archivo con IOC´s"
     );

    args = parser.parse_args()
    
    if args.file:
        file = args.file
        if(len(file)>1):
            if args.ouput:
                try:
                    verify_type(file,args.ouput)
                except Exception as e:
                    logging.critical(e)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("User Interrupted..")
        sys.exit(0)