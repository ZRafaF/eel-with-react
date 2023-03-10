# Copyright 2023 rafae
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import eel
import random
import json
import time


@eel.expose
def get_one():
    return 1


@eel.expose
def start_time():
    global start 
    start = time.time()

@eel.expose
def end_time():
    end = time.time()
    print("Elapsed time: ", (end - start))

@eel.expose
def get_random_data_points(dataSize):
    returnArray = []
    for i in range(dataSize):
        point = {"x": random.randint(0, 100), "y": i}
        returnArray.append(point)

    start_time()
    return returnArray


class dataPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y


@eel.expose
def get_random_data_points_JSON(dataSize):
    returnArray = []
    for i in range(dataSize):
        returnArray.append((dataPoint(x=random.randint(0, 100), y=i).__dict__))

    json_dump = json.dumps(returnArray)
    start_time()
    return json_dump
