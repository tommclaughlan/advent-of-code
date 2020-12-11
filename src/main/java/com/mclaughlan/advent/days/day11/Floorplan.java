package com.mclaughlan.advent.days.day11;

import java.util.ArrayList;
import java.util.List;

public class Floorplan {
    private List<List<Character>> floorplan;

    public Floorplan(List<List<Character>> floorplan) {
        this.floorplan = floorplan;
    }

    public boolean tick(boolean lineOfSight, int occupiedLimit) {
        var hasChanged = false;
        var next = new ArrayList<List<Character>>();

        for (var i = 0; i < floorplan.size(); i++) {
            next.add(new ArrayList<>());
            for (var j = 0; j < floorplan.get(i).size(); j++) {
                var tile = floorplan.get(i).get(j);
                next.get(i).add(tile);

                switch (tile) {
                    case '.':
                        break;
                    case 'L':
                        if (getAdjacentCount(j, i, lineOfSight) == 0) {
                            next.get(i).set(j, '#');
                            hasChanged = true;
                        }
                        break;
                    case '#':
                        if (getAdjacentCount(j, i, lineOfSight) >= occupiedLimit) {
                            next.get(i).set(j, 'L');
                            hasChanged = true;
                        }
                        break;
                }
            }
        }
        floorplan = next;

        return hasChanged;
    }

    public int getOccupied() {
        var count = 0;
        for (List<Character> characters : floorplan) {
            for (Character tile : characters) {
                if (tile.equals('#')) {
                    count++;
                }
            }
        }
        return count;
    }

    private int getAdjacentCount(int x, int y, boolean lineOfSight) {
        var count = 0;
        int distance = Math.max(floorplan.size(), floorplan.get(0).size());
        if (!lineOfSight) {
            distance = 1;
        }

        for (var xd = -1; xd <=1; xd++) {
            for (var xy = -1; xy <=1; xy++) {
                if (xd == 0 && xy == 0) continue;
                if (testDirection(x, y, xd, xy, distance)) {
                    count++;
                }
            }
        }
        return count;
    }

    private Character getAdjacentTile(int x, int y, int xd, int yd) {
        try {
            return floorplan.get(y + yd).get(x + xd);
        } catch (IndexOutOfBoundsException e) {
            return 'E'; // this is the edge
        }
    }

    private boolean testDirection(int x, int y, int xd, int yd, int distance) {
        for (var d = 1; d <= distance; d++) {
            var tile = getAdjacentTile(x, y, xd*d, yd*d);
            if (!tile.equals('.')) {
                return tile.equals('#');
            }
        }
        return false;
    }
}
