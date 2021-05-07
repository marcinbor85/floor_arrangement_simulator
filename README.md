# floor arrangement simulator
Extremely stupid app for planning the laying of the floor panels.

## Usage
```console
usage: floor_arrangement_simulator.py [-h] [-pl PANEL_LENGTH] [-pw PANEL_WIDTH] [-l FLOOR_LENGTH] [-w FLOOR_WIDTH] [-min MIN_PANEL_LENGTH] [-s FIRST_PANEL_LENGTH]

Floor arrangement simulator

optional arguments:
  -h, --help             show this help message and exit
  -pl PANEL_LENGTH       panel length (default=108)
  -pw PANEL_WIDTH        panel width (default=13)
  -l FLOOR_LENGTH        floor length (default=402)
  -w FLOOR_WIDTH         floor width (default=758)
  -min MIN_PANEL_LENGTH  minimum panel length (default=18)
  -s FIRST_PANEL_LENGTH  first panel length (default=0)
```

## Example output
```console
TOTAL AREA (402x758): 30.47
PANELS COUNT: 266
PANELS LOST COUNT: 19, AREA: 0.5802
ROW 0: [108x13] [108x13] [108x13] [78x13]
ROW 1: [30x13] [108x13] [108x13] [108x13] [48x13]
ROW 2: [60x13] [108x13] [108x13] [108x13] [18x13]
ROW 3: [90x13] [108x13] [108x13] [96x13] >>>>>>>>>> LOST: [12x13]
ROW 4: [108x13] [108x13] [108x13] [78x13]
ROW 5: [30x13] [108x13] [108x13] [108x13] [48x13]
ROW 6: [60x13] [108x13] [108x13] [108x13] [18x13]
ROW 7: [90x13] [108x13] [108x13] [96x13] >>>>>>>>>> LOST: [12x13]
ROW 8: [108x13] [108x13] [108x13] [78x13]
ROW 9: [30x13] [108x13] [108x13] [108x13] [48x13]
ROW 10: [60x13] [108x13] [108x13] [108x13] [18x13]
ROW 11: [90x13] [108x13] [108x13] [96x13] >>>>>>>>>> LOST: [12x13]
ROW 12: [108x13] [108x13] [108x13] [78x13]
ROW 13: [30x13] [108x13] [108x13] [108x13] [48x13]
ROW 14: [60x13] [108x13] [108x13] [108x13] [18x13]
ROW 15: [90x13] [108x13] [108x13] [96x13] >>>>>>>>>> LOST: [12x13]
ROW 16: [108x13] [108x13] [108x13] [78x13]
ROW 17: [30x13] [108x13] [108x13] [108x13] [48x13]
ROW 18: [60x13] [108x13] [108x13] [108x13] [18x13]
ROW 19: [90x13] [108x13] [108x13] [96x13] >>>>>>>>>> LOST: [12x13]
ROW 20: [108x13] [108x13] [108x13] [78x13]
ROW 21: [30x13] [108x13] [108x13] [108x13] [48x13]
ROW 22: [60x13] [108x13] [108x13] [108x13] [18x13]
ROW 23: [90x13] [108x13] [108x13] [96x13] >>>>>>>>>> LOST: [12x13]
ROW 24: [108x13] [108x13] [108x13] [78x13]
ROW 25: [30x13] [108x13] [108x13] [108x13] [48x13]
ROW 26: [60x13] [108x13] [108x13] [108x13] [18x13]
ROW 27: [90x13] [108x13] [108x13] [96x13] >>>>>>>>>> LOST: [12x13]
ROW 28: [108x13] [108x13] [108x13] [78x13]
ROW 29: [30x13] [108x13] [108x13] [108x13] [48x13]
ROW 30: [60x13] [108x13] [108x13] [108x13] [18x13]
ROW 31: [90x13] [108x13] [108x13] [96x13] >>>>>>>>>> LOST: [12x13]
ROW 32: [108x13] [108x13] [108x13] [78x13]
ROW 33: [30x13] [108x13] [108x13] [108x13] [48x13]
ROW 34: [60x13] [108x13] [108x13] [108x13] [18x13]
ROW 35: [90x13] [108x13] [108x13] [96x13] >>>>>>>>>> LOST: [12x13]
ROW 36: [108x13] [108x13] [108x13] [78x13]
ROW 37: [30x13] [108x13] [108x13] [108x13] [48x13]
ROW 38: [60x13] [108x13] [108x13] [108x13] [18x13]
ROW 39: [90x13] [108x13] [108x13] [96x13] >>>>>>>>>> LOST: [12x13]
ROW 40: [108x13] [108x13] [108x13] [78x13]
ROW 41: [30x13] [108x13] [108x13] [108x13] [48x13]
ROW 42: [60x13] [108x13] [108x13] [108x13] [18x13]
ROW 43: [90x13] [108x13] [108x13] [96x13] >>>>>>>>>> LOST: [12x13]
ROW 44: [108x13] [108x13] [108x13] [78x13]
ROW 45: [30x13] [108x13] [108x13] [108x13] [48x13]
ROW 46: [60x13] [108x13] [108x13] [108x13] [18x13]
ROW 47: [90x13] [108x13] [108x13] [96x13] >>>>>>>>>> LOST: [12x13]
ROW 48: [108x13] [108x13] [108x13] [78x13]
ROW 49: [30x13] [108x13] [108x13] [108x13] [48x13]
ROW 50: [60x13] [108x13] [108x13] [108x13] [18x13]
ROW 51: [90x13] [108x13] [108x13] [96x13] >>>>>>>>>> LOST: [12x13]
ROW 52: [108x13] [108x13] [108x13] [78x13]
ROW 53: [30x13] [108x13] [108x13] [108x13] [48x13]
ROW 54: [60x13] [108x13] [108x13] [108x13] [18x13]
ROW 55: [90x13] [108x13] [108x13] [96x13] >>>>>>>>>> LOST: [12x13]
ROW 56: [108x13] [108x13] [108x13] [78x13]
ROW 57: [30x13] [108x13] [108x13] [108x13] [48x13]
ROW 58: [60x4] [108x4] [108x4] [108x4] [18x4] >>>>>>>>>> LOST: [60x9] [108x9] [108x9] [108x9] [18x9]
PANEL [108x13]: 160
PANEL [78x13]: 15
PANEL [30x13]: 15
PANEL [48x13]: 15
PANEL [60x13]: 14
PANEL [18x13]: 14
PANEL [90x13]: 14
PANEL [96x13]: 14
PANEL [108x4]: 3
PANEL [60x4]: 1
PANEL [18x4]: 1
PANEL LOST [12x13]: 14
PANEL LOST [108x9]: 3
PANEL LOST [60x9]: 1
PANEL LOST [18x9]: 1
```

