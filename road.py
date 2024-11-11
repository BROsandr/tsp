from enum import Enum
from dataclasses import dataclass
from typing import Any
from matplotlib import Axes

class Block_type(Enum):
  LEFT = 0
  UP = 1
  RIGTH = 2
  DOWN = 3

@dataclass(order=True)
class Point:
  x: int
  y: int

@dataclass(order=True)
class Road_block:
  dir: Block_type
  lenth: int

def plot(ax: Axes, cities, roads):
  for i, (city_x, city_y) in enumerate(cities):
      ax.scatter(city_x, city_y, s=1200, zorder=2)
      ax.annotate(i, (city_x, city_y), fontsize=40, ha='center', va='center', zorder=3)

      # Connect cities with opaque lines
      for j, (other_x, other_y) in enumerate(cities):
          if i != j:
              ax.plot([city_x, other_x], [city_y, other_y], color='gray', linestyle='-', linewidth=1, alpha=0.1)
