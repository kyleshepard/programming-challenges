class Solution {
    public double angleClock(int hour, int minutes) {
        double angleDiff = Math.abs((hour % 12)*30 + ((double) minutes)/2 - (6 * minutes));
        return Math.min(angleDiff, 360.0 - angleDiff);
    }
}