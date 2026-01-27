from utils import geometry

tracks = []
next_id = 0

def track(detections):

    (x1, y1, x2, y2) = detections["bbox"]
    cx, cy = geometry.get_center(x1, y1, x2, y2)


    

    
