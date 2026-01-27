from utils import geometry
from utils import config
import math
import numpy as np

features = []
time = 1 / config.FPS

def calc_speed(history, speeds):
    for i in range(len(history)-2):
        x1 = history[i][0]
        y1 = history[i][1]
        x2 = history[i+1][0]
        y2 = history[i+1][1]

        dist = geometry.get_distance(x1, y1, x2, y2)
            
        speed = dist/time
        speeds.append(speed)

    avg_speed = sum(speeds) / len(speeds)
    max_speed = max(speeds)
   
    return avg_speed, max_speed

def calc_acc(speeds, accelerations):
    for i in range(len(speeds)-2):
            acceleration = (speeds[i+1] - speeds[i]) / time
            accelerations.append(acceleration)

    abs_acc = [abs(x) for x in accelerations]
    max_acc = max(abs_acc)

    return max_acc

def detect_oscillation(delta_theta):
    # remove small changes
    significant_changes = delta_theta[np.abs(delta_theta) > 0.05]
    
    if len(significant_changes) < 2:  
        return False
    
    # sign changes
    sign_changes = np.sum(np.diff(np.sign(significant_changes)) != 0)
    oscillation_rate = sign_changes / len(significant_changes)
    
    # variance
    variance = np.std(significant_changes)
    
    # combined score
    oscillation_score = oscillation_rate * variance
    
    return oscillation_score > 0.15

def calc_dir_change(history):
    theta = []
    del_theta = []

    for i in range(len(history)-2): 
        x1 = history[i][0]
        y1 = history[i][1]
        x2 = history[i+1][0]
        y2 = history[i+1][1]
        dx = x2 - x1
        dy = y2 - y1
        angle = math.atan2(dy, dx)  
        theta.append(angle)
    
    for i in range(len(theta)): 
        delta = theta[i] - theta[i-1]
        delta = (delta + math.pi) % (2 * math.pi) - math.pi
        del_theta.append(delta)
    
    change = detect_oscillation(np.array(del_theta)) 
    return change



def calc_path_length(history):
    path_length = 0

    for i in range(len(history)-2):
        x1 = history[i][0]
        y1 = history[i][1]
        x2 = history[i+1][0]
        y2 = history[i+1][1]

        dist = geometry.get_distance(x1, y1, x2, y2)
        path_length += dist

    return path_length

def extract_features(tracks):
    for track in tracks:
        history = track["history"]
        speeds = []
        accelerations = []
        direction_change = False
        path_length = 0
        
        # skip if the history has less that two data of speed
        if len(history)< 3:
            continue

        avg_speed, max_speed = calc_speed(history, speeds)
        max_acc = calc_acc(speeds, accelerations)
        path_length = calc_path_length(history)
        direction_change = calc_dir_change(history)

        features.append({
            "id": track["id"],
            "avg_speed": avg_speed,
            "max_speed": max_speed,
            "acceleration": max_acc,
            "direction_change": direction_change,
            "path_length": path_length,
        })
            

