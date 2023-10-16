def intersect(line1_x1:int, line1_y1:int, line1_x2:int, line1_y2:int, 
  line2_x1:int, line2_y1:int, line2_x2:int, line2_y2:int)->bool:

  u1t = (line2_x2 - line2_x1) * (line1_y1 - line2_y1) \
    - (line2_y2 - line2_y1) * (line1_x1 - line2_x1)
  u2t = (line1_x2 - line1_x1) * (line1_y1 - line2_y1) \
    - (line1_y2 - line1_y1) * (line1_x1 - line2_x1)
  u2 = (line2_y2 - line2_y1) * (line1_x2 - line1_x1) \
    - (line2_x2 - line2_x1) * (line1_y2 - line1_y1)

  if u2 != 0:
    u1 = u1t / u2;
    u02 = u2t / u2;

    if (0 <= u1):
      if (u1 <= 1):
        if (0 <= u02):
          if (u02 <= 1):
            return True
    return False
  else:
    if u1t == 0:
      return True
    if u2t == 0:
      return True
    return False