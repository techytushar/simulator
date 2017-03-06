"""
@package p2psp-simulator
peer_core module
"""
from queue import Queue

class Peer_core():
    def __init__(self):
        self.socket = Queue()
        self.alive = True
        print("DBS initialized")
        
    def process_message(self, message, sender):
        raise NotImplementedError

    def process_next_message(self):
        content = self.socket.get()
        return process_message(content[1], content[0])

    def buffer_data(self):
        #TO-DO: buffering

    def keep_the_buffer_full(self):
        last_received_chunk = process_next_message()
        while (las_received_chunk < 0):
            last_received_chunk = process_next_message()

        play_next_chunks(last_received_chunk)

    def play_next_chunks(self, last_received_chunk):
        for i in range(last_received_chunk-prev_received_chunk):
            play_chunk(played_chunk)
        
    def play_chunk(self, chunk_number):
        raise NotImplementedError

    def run(self):
        while(alive):
            keep_the_buffer_full()