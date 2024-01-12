import logging

logging.basicConfig(filename='LoggerDemo.log',level=10,filemode='w',format='%(asctime)s:%(levelname)s : %(message)s',
                    datefmt='%Y:%m:%d %I:%M:%S %p')# Default file_Mode=Append
""" logger Format== level:logger:message"""
logging.critical("Critical Massage...") # Level=50
logging.error("Error Massage...") # Level=40
logging.warning("Warning Massage..") # Level=30
logging.info("Info Massage..") # Level=20
logging.debug("Debug Massage..")# Level=10