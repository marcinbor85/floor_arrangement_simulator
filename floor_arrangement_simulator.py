import sys
import argparse

from collections import OrderedDict


AREA_FACTOR = 10000.0


class Surface:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    @property
    def area(self):
        return self.x * self.y


class Row:
    def __init__(self):
        self.panels = []
        self.lost_panels = []
        
    def add_panel(self, panel):
        self.panels.append(panel)
    
    def add_lost_panel(self, panel):
        self.lost_panels.append(panel)
    
    @property
    def length(self):
        return sum(map(lambda p: p.length, self.panels))
    
    @property
    def area(self):
        return sum(map(lambda p: p.area, self.panels))
    
    def __str__(self):
        s = ' '.join([str(p) for p in self.panels])
        if self.lost_panels:
            s += ' >>>>>>>>>> LOST: '
            s += ' '.join([str(p) for p in self.lost_panels])
        return s
    
    @property
    def width(self):
        return max(map(lambda p: p.width, self.panels), default=0)
    
    def cut(self, width):
        for p in self.panels:
            org_width = p.width
            p.cut_width(width)
            trash_panel = Panel.prepare(p, width=org_width - width)
            self.add_lost_panel(trash_panel)


class ArrangeException(Exception):
    pass


class Floor(Surface):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.rows = []
        
    def arrange(self, panel_pattern, min_length=20, start_length=0):
        self.rows = []
        current_area = 0
        while current_area < self.area:
            row = Row()
            if start_length > 0:
                start_panel = Panel.prepare(panel_pattern, length=start_length)
                row.add_panel(start_panel)
            
            while row.length < self.x:
                next_panel_length = panel_pattern.length
                if row.length + next_panel_length > self.x:
                    next_panel_length = self.x - row.length
                    start_length = panel_pattern.length - next_panel_length
                else:
                    start_length = 0
                
                if next_panel_length < min_length:
                    raise ArrangeException(f"next panel too short: {next_panel_length} < MIN_LENGTH")
                    
                if start_length < min_length and start_length > 0:
                    trash_panel = Panel.prepare(panel_pattern, length=start_length)
                    row.add_lost_panel(trash_panel)
                    start_length = 0
                
                next_panel = Panel.prepare(panel_pattern, length=next_panel_length)
                row.add_panel(next_panel)

            current_area += row.area
            self.rows.append(row)
        
        total_width = sum(map(lambda r: r.width, self.rows))
        last_row = self.rows[-1]
        correct_last_row_width = last_row.width - (total_width - self.y)
        last_row.cut(correct_last_row_width)
    
    @property
    def panels(self):
        ret = []
        for r in self.rows:
            ret.extend(r.panels)
        return ret
        
    @property
    def lost_panels(self):
        ret = []
        for r in self.rows:
            ret.extend(r.lost_panels)
        return ret
    
    @classmethod
    def count_panels(cls, panels):
        types = OrderedDict()
        for p in panels:
            count = types.get(str(p), 0)
            types.update({str(p): count + 1})
        types = OrderedDict(sorted(types.items(), key=lambda t: t[1], reverse=True))
        return types
            
    def summary(self):
        panels_count = sum(map(lambda r: len(r.panels), self.rows))
        lost_panels_count = len(self.lost_panels)
        lost_panels_area = sum(map(lambda p: p.area, self.lost_panels))/AREA_FACTOR
        print("-------------------------")
        print(f"TOTAL AREA ({self.x}x{self.y}): {self.area/AREA_FACTOR:.2f}")
        print(f"PANELS COUNT: {panels_count}")
        print(f"PANELS LOST COUNT: {lost_panels_count}, AREA: {lost_panels_area}")
        print("-------------------------")
        for i, r in enumerate(self.rows):
            print(f"ROW {i}: {r}")
        print("-------------------------")
        for p, n in Floor.count_panels(self.panels).items():
            print(f"PANEL {p}: {n}")
        print("-------------------------")
        for p, n in Floor.count_panels(self.lost_panels).items():
            print(f"PANEL LOST {p}: {n}")
        print("-------------------------")
        

class Panel(Surface):
    @property
    def length(self):
        return self.x
    
    @property
    def width(self):
        return self.y
    
    @length.setter
    def length(self, val):
        self.x = val
    
    @width.setter
    def width(self, val):
        self.y = val
    
    @classmethod
    def prepare(cls, panel_pattern, length=None, width=None):
        return Panel(
            length=length if length else panel_pattern.length,
            width=width if width else panel_pattern.width
        )
    
    def cut_width(self, width):
        self.width = width
    
    def __str__(self):
        x = f"{self.length:.1f}"
        if x[-1] == '0':
            x = int(self.length)
        y = f"{self.width:.1f}"
        if y[-1] == '0':
            y = int(self.width)
        
        return f"[{x}x{y}]"
    

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Floor arrangement simulator')
    parser.add_argument('-pl', dest='panel_length', type=float, default=108, help='panel length (default=108)')
    parser.add_argument('-pw', dest='panel_width', type=float, default=13, help='panel width (default=13)')
    parser.add_argument('-l', dest='floor_length', type=float, default=402, help='floor length (default=402)')
    parser.add_argument('-w', dest='floor_width', type=float, default=758, help='floor width (default=758)')
    parser.add_argument('-min', dest='min_panel_length', type=float, default=18, help='minimum panel length (default=18)')
    parser.add_argument('-s', dest='first_panel_length', type=float, default=0, help='first panel length (default=0)')
    
    args = parser.parse_args()
    
    origin_panel = Panel(length=args.panel_length, width=args.panel_width)
    floor = Floor(x=args.floor_length, y=args.floor_width)

    try:
        floor.arrange(origin_panel, min_length=args.min_panel_length, start_length=args.first_panel_length)
    except ArrangeException as e:
        print(str(e))
        sys.exit(-1)
        
    floor.summary()

