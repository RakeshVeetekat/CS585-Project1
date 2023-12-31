import datetime
import os
import time
import random
from random import randrange
from datetime import timedelta
from datetime import datetime

class LogsGeneration:
    def __init__(self, size, csv_path):
        self.size = size
        self.dataset_path = csv_path
        self.possible_people_ids = []
        self.possible_page_ids = []
        self.output_path = os.getcwd() + "access_logs.csv"
        self.access_types = [
            "note", "added a friend", "just viewed", "requested to follow",
            "accepted follow request", "shared a post", "blocked the profile",
            "viewed mutual followers", "sent a message"
        ]

    def read_first_csv(self): # will return tuple of person ID 
        possible_ids = []
        with open(self.dataset_path, "r") as f:
            lines = f.readlines()
            for x in range(0, len(lines)):
                if x == 0:
                    continue
                id_val = lines[x].split(",")[0]
                possible_ids.append(id_val)
                print(id_val)

        return possible_ids
    
    def create_output_csv(self):
        with open(self.output_path, "w") as f:
            f.write("AccessId, ByWho, WhatPage, TypeOfAccess, AccessTime\n")
        f.close()

    def write_to_csv(self, entry):
        with open(self.output_path, "a+") as f:
            f.write(entry + "\n")
        f.close()

    def format_entry(self, log_entry):
        final_entry = ""
        for x in range(0, len(log_entry)):
            final_entry += str(log_entry[x]) + ","
        
        return final_entry[:-1]

    def random_date(self, start, end):
        delta = end - start
        int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
        random_second = randrange(int_delta)
        return start + timedelta(seconds=random_second)


    def create_entry(self, ids):
        access_id_lower = 1
        access_id_upper = 10000000 
        by_who = ids[random.randint(0, len(ids) - 1)]
        what_page = ids[random.randint(0, len(ids) - 1)]
        access_id = random.randint(access_id_lower, access_id_upper)
        idx = random.randint(0, len(self.access_types) - 1)
        access_type = self.access_types[idx]
        start_date = datetime.strptime('6/1/2023 1:30 PM', '%m/%d/%Y %I:%M %p')
        end_date = datetime.strptime('9/21/2023 1:30 PM', '%m/%d/%Y %I:%M %p')
        access_date = self.random_date(start_date, end_date)

        entry = [access_id, by_who, what_page, access_type, access_date]
        final_entry = self.format_entry(entry)

        self.write_to_csv(final_entry)


    def generate_data(self):
        self.create_output_csv()
        ids = self.read_first_csv()
        for x in range(0, self.size):
            self.create_entry(ids)

