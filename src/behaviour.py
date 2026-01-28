from utils import config

def compute_thresholds(features):
    speeds = []
    accelerations = []
    
    for feature in features:
        speeds.append(feature["avg_speed"])
        accelerations.append(feature["acceleration"])

    speeds.sort()
    accelerations.sort()

    speed_idx = int(config.SPEED_HIGH * len(speeds))
    acc_idx = int(config.ACCEL_HIGH * len(accelerations))

    speed_high = speeds[speed_idx]
    acc_high = accelerations[acc_idx]

    thresholds = []
    thresholds.append({speed_high, acc_high})

    return thresholds

def detect_behaviours(features, thresholds):
    flags = []

    for feature in features:
        avg_speed = feature["avg_speed"]
        acceleration = feature["acceleration"]
        direction_change_count = feature["direction_change_count"]
        path_length = feature["path_length"]
        displacement = feature["displacement"]
        
        path_ratio = path_length / displacement

        speed_high = False
        acc_high = False
        erratic = False

        if avg_speed > thresholds[0]:
            speed_high = True
        
        if acceleration > thresholds[1]:
            acc_high = True

        if path_ratio > config.PATH_RATIO_HIGH:
            if direction_change_count <= 3:
                erratic = False
            elif direction_change_count >= 6:
                erratic = True
        
        flags.append({
            "speeding": speed_high,
            "aggressive_acc": acc_high,
            "erratic": erratic
        })

    return flags

            
        