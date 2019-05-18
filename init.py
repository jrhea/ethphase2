import logging
import threading
import time
import sys
from shard import Shard
from pydispatch import dispatcher
from beacon import Beacon
import matplotlib.pyplot as plt
from viz import VizController
from config import system_config

SHARD_COUNT = None

if __name__ == "__main__":
    shard_count = int(sys.argv[1])

    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    threads = []
    shard_signals = []
    viz = []
    for i in range(shard_count):
        logging.info(f"Main    : creating thread {i}")
        shard_signals.append(f"SHARD_{i}")
        # viz.append(VizController(i))
        #threads.append(threading.Thread(target=viz, args=(i,)))
        shard = Shard(i)
        threads.append(threading.Thread(target=shard.run))

    logging.info(f"Main    : shard signals {shard_signals}")

    for i, thread in enumerate(threads):
        logging.info(f"Main    : starting thread {i}")
        thread.start()

    logging.info("Main    : creating beacon chain")
    beacon_chain = Beacon(shard_count)

    logging.info("Main    : starting beacon chain")
    beacon_thread = threading.Thread(target=beacon_chain.run).start()


    logging.info("Main    : all initialized...")
    
    # figs=[]
    # while True:
    #     for i in range(shard_count):
    #         figs.append(plt.figure(i))
    #         viz[i].render()
    #     plt.show()
    
    
    
    
    #     plt.clf()
    # plt.imshow(frames[k],cmap=plt.cm.gray)
    # fig.canvas.draw()
    # time.sleep(1e-6)