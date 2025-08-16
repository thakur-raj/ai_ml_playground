import logging

logging.basicConfig(force=True,filename="test.log",filemode="w",
level=logging.DEBUG, format='%(asctime)s - %(name)s %(levelname)s - %(message)s')
