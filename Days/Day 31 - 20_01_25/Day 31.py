

from tkinter import *
from tkinter import ttk
import logging

scriptname: str = __file__

# Logger Paramteres
filename: str = "C:/Users/simon/Git_Repos/100_project_in_100_days/Days/Day 31 - 20_01_25/log.log"
LOG_FORMAT = "|-- %(asctime)s --- %(levelname)s --- %(message)s --------|"

# Define logger
logging.basicConfig(filename = filename, 
    level = logging.DEBUG,
    format = LOG_FORMAT)
logger = logging.getLogger(__name__)


def start()-> None: # move to header file
    print(f'|---------------------------------------------------|')
    print(f'|================= PROGRAM STARTED =================|')
    print(f'|---------------------------------------------------|')
    print(f'\n')
    logger.info(f'***** File Run ***** {scriptname}')

def end()-> None:# move to header file
    print(f'\n')

    print(f'|---------------------------------------------------|')
    print(f'|================== PROGRAM ENDED ==================|')
    print(f'|---------------------------------------------------|')

def debug(message:str)-> None:
    logger.debug(f'{message}')
   
def info(message):

    root = Tk()
    frm = ttk.Frame(root, padding = 100)
    frm.grid()
    ttk.Label(frm, text=f"INFO: {message}").grid(column=0, row=0)
    ttk.Button(frm, text="CLEAR", command=root.destroy).grid(column=0, row=1)
    root.mainloop()
    logger.info(f'Some infomation {message}')


def main():

    info_message_1:str = "Information 1"
    info_message_2:str = "Information 2"
    info_message_3:str = "Information 3"
    info_message_4:str = "Information 4"

    start()
    info(info_message_1)
    debug('this')
    debug('that')
    debug('somthing')
    debug('new')
    debug('new')
    debug('new')
    debug('new')
    debug('new')
    info(info_message_2)

    end()
    

if __name__ == '__main__':
    main()